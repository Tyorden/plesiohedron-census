#!/usr/bin/env python
"""phase2_schmitt_origin_check.py — POST-RUN diligence on the P2 Schmitt
screen mismatches of sweep_phase2_tetragonal.py (reads phase2_types.json).

Observed in the run: schmitt_fvec_mismatch quarantines are concentrated in
(a) the ITA TWO-ORIGIN-CHOICE tetragonal groups (85, 86, 88, 125, 126, 129,
    130, 133, 134, 137, 138, 141, 142) — the frozen spacegroups.json uses
    ORIGIN CHOICE 1 (setting_convention field), so if Schmitt's coordinates
    are in origin choice 2 his printed points must be SHIFTED before they
    mean the same orbit in our setting; and
(b) the SECOND member of an enantiomorphic pair (95 = P4_322, 96 =
    P4_32_12) where the sweep ran the pair's printed point unchanged — the
    printed point belongs to the first-listed group's coordinate system and
    the enantiomorph is its mirror image (z -> -z), so an unchanged point is
    not expected to reproduce.

This script tests those two hypotheses EXACTLY and reports; it does not
edit the store. For each two-origin group: brute-force the origin shift s
over (1/8)Z^3 mod 1 (512 candidates) on ONE mismatched row, keep the shifts
whose exact f-vector equals the printed one, then verify every survivor on
ALL printed rows of the group (matched and mismatched). For 95/96: test the
16 signed-axis transforms (±x, ±y, ±z) and (±y, ±x, ±z) on all rows. Any
residual mismatch is reported as such (unexplained).

Run (after the sweep, from harness/):
  nice -n 10 python3 \
      phase2_schmitt_origin_check.py
Writes: PHASE2_SCHMITT_ORIGIN_CHECK.md, phase2_schmitt_origin_check.json.
"""
import itertools
import json
import multiprocessing as mp
import os
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sweep_phase2_tetragonal as S2                 # noqa: E402

TWO_ORIGIN = {85, 86, 88, 125, 126, 129, 130, 133, 134, 137, 138, 141, 142}
ENANTIO_SECOND = {78: 76, 95: 91, 96: 92}
WORKERS = int(os.environ.get("PHASE2_WORKERS", 12))


def fvec_of(num, p, b):
    try:
        r = S2.evaluate(num, p, b, "schmitt_printed")
        return list(r["fvec"])
    except Exception as exc:                     # ChainError or crash
        return f"ERR:{type(exc).__name__}"


def job(task):
    kind, num, pstr, bstr, label = task
    p = tuple(F(s) for s in pstr)
    return task, fvec_of(num, p, F(bstr))


def shifted(p, s):
    return tuple(F(x) + F(y) for x, y in zip(p, s))


def transformed(p, t):
    sx, sy, sz, swap = t
    x, y, z = p
    if swap:
        x, y = y, x
    return (sx * x, sy * y, sz * z)


def main():
    t0 = time.time()
    store = json.load(open(S2.OUT_JSON))
    rows = json.load(open(S2.OUT_ROWS))["rows"]
    mism = [q for q in store["quarantines"] if q["reason"] == "schmitt_fvec_mismatch"]
    by_group = defaultdict(list)
    for q in mism:
        by_group[q["group"]].append(q)
    rows_by_group = defaultdict(list)
    for r in rows:
        for g in r["groups"]:
            rows_by_group[g].append(r)
    L = ["# Phase 2 — Schmitt screen mismatch diligence (post-run, 2026-09-03)", "",
         f"Input: phase2_types.json ({len(mism)} schmitt_fvec_mismatch quarantines "
         f"over groups {sorted(by_group)}), schmitt_tetragonal_rows_harvested.json. "
         "Frozen setting: origin choice 1 (spacegroups.json setting_convention). "
         "Exact chain: sweep_phase2_tetragonal.evaluate (float proposal -> exact "
         "clip with certificate -> f-vector).", ""]
    out = {"mismatch_groups": {g: len(v) for g, v in sorted(by_group.items())},
           "two_origin": {}, "enantiomorph_second": {}, "residual": {}}
    ctx = mp.get_context("fork")
    pool = ctx.Pool(WORKERS)

    # ---- (a) two-origin groups: shift search on one row, verify on all rows
    L += ["## (a) Two-origin-choice groups: origin shift search", "",
          "| group | symbol | mismatched rows | rows total | shifts surviving row-1 "
          "screen | shifts reproducing ALL rows | residual rows under best shift |",
          "|---|---|---|---|---|---|---|"]
    shifts = [tuple(F(k, 8) for k in ks) for ks in itertools.product(range(8), repeat=3)]
    for g in sorted(by_group):
        if g not in TWO_ORIGIN:
            continue
        q0 = min(by_group[g], key=lambda q: max(F(x).denominator for x in q["point"]))
        p0 = tuple(F(x) for x in q0["point"])
        want0 = None
        for r in rows_by_group[g]:
            if r["point"] == q0["point"] and r["b_ratio"] == q0["b"]:
                want0 = r["f_vector"]
        tasks = [("shift", g, [str(x) for x in shifted(p0, s)], q0["b"], s) for s in shifts]
        surv = [t[4] for t, fv in pool.imap(job, tasks, chunksize=8) if fv == want0]
        # verify survivors on all rows
        best, best_res, per_shift = None, None, {}
        for s in surv:
            tasks = [("verify", g, [str(x) for x in shifted(tuple(F(x) for x in r["point"]), s)],
                      r["b_ratio"], (s, tuple(r["f_vector"]))) for r in rows_by_group[g]]
            res = [(t, fv) for t, fv in pool.imap(job, tasks, chunksize=4)]
            bad = [(t[2], t[3], t[4][1], fv) for t, fv in res if fv != list(t[4][1])]
            per_shift[str(tuple(S2.frac_str(x) for x in s))] = len(bad)
            if best_res is None or len(bad) < len(best_res):
                best, best_res = s, bad
        full = [k for k, v in per_shift.items() if v == 0]
        out["two_origin"][g] = {"mismatched": len(by_group[g]), "rows": len(rows_by_group[g]),
                                "survivors_row1": [tuple(S2.frac_str(x) for x in s) for s in surv],
                                "shifts_all_rows": full,
                                "best_shift": tuple(S2.frac_str(x) for x in best) if best else None,
                                "best_residual": [(p, b, list(w), fv) for p, b, w, fv in (best_res or [])]}
        L.append(f"| {g} | {S2.GROUPS[g]['international_short']} | {len(by_group[g])} | "
                 f"{len(rows_by_group[g])} | {len(surv)} | {full if full else 'NONE'} | "
                 f"{len(best_res) if best_res is not None else 'n/a'} |")
        print(f"#{g}: {len(surv)} survivors, all-rows shifts {full}, best residual "
              f"{len(best_res) if best_res is not None else 'n/a'}  [{time.time()-t0:.0f}s]", flush=True)

    # ---- (b) enantiomorph second members: signed-axis transforms
    L += ["", "## (b) Second members of enantiomorphic pairs: signed-axis transforms of "
          "the printed point (printed for the first member)", "",
          "| group | symbol | mismatched rows | rows total | transforms reproducing ALL "
          "rows (sx,sy,sz,swap) | best residual |", "|---|---|---|---|---|---|"]
    transforms = [(sx, sy, sz, sw) for sx in (1, -1) for sy in (1, -1)
                  for sz in (1, -1) for sw in (False, True)]
    for g in sorted(by_group):
        if g not in ENANTIO_SECOND:
            continue
        per_t, best, best_res = {}, None, None
        for t in transforms:
            tasks = [("enant", g, [str(x) for x in transformed(tuple(F(x) for x in r["point"]), t)],
                      r["b_ratio"], (t, tuple(r["f_vector"]))) for r in rows_by_group[g]]
            res = [(tk, fv) for tk, fv in pool.imap(job, tasks, chunksize=4)]
            bad = [(tk[2], tk[3], list(tk[4][1]), fv) for tk, fv in res if fv != list(tk[4][1])]
            per_t[str(t)] = len(bad)
            if best_res is None or len(bad) < len(best_res):
                best, best_res = t, bad
        full = [k for k, v in per_t.items() if v == 0]
        out["enantiomorph_second"][g] = {"mismatched": len(by_group[g]),
                                         "rows": len(rows_by_group[g]),
                                         "transforms_all_rows": full, "best": str(best),
                                         "best_residual": best_res}
        L.append(f"| {g} | {S2.GROUPS[g]['international_short']} | {len(by_group[g])} | "
                 f"{len(rows_by_group[g])} | {full if full else 'NONE'} | {len(best_res)} |")
        print(f"#{g}: transforms all rows {full}, best residual {len(best_res)}", flush=True)

    # ---- (c) residual groups (neither class): list details + try both searches on the row
    L += ["", "## (c) Mismatches outside both classes", ""]
    for g in sorted(by_group):
        if g in TWO_ORIGIN or g in ENANTIO_SECOND:
            continue
        for q in by_group[g]:
            p = tuple(F(x) for x in q["point"])
            want = None
            for r in rows_by_group[g]:
                if r["point"] == q["point"] and r["b_ratio"] == q["b"]:
                    want = r["f_vector"]
            tasks = [("shift", g, [str(x) for x in shifted(p, s)], q["b"], s) for s in shifts]
            surv = [tuple(S2.frac_str(x) for x in t[4])
                    for t, fv in pool.imap(job, tasks, chunksize=8) if fv == want]
            tasks = [("enant", g, [str(x) for x in transformed(p, t)], q["b"], t) for t in transforms]
            surv_t = [str(t[4]) for t, fv in pool.imap(job, tasks) if fv == want]
            out["residual"][f"{g}:{','.join(q['point'])}@{q['b']}"] = {
                "detail": q["detail"], "shifts_reproducing": surv, "transforms_reproducing": surv_t}
            L.append(f"- group {g} {S2.GROUPS[g]['international_short']} point "
                     f"({', '.join(q['point'])}) b={q['b']}: {q['detail']}; shifts in (1/8)Z^3 "
                     f"reproducing the printed f-vector: {surv if surv else 'none'}; signed-axis "
                     f"transforms reproducing: {surv_t if surv_t else 'none'}")
    pool.terminate()
    pool.join()
    L += ["", f"Wall {time.time()-t0:.0f} s, {WORKERS} workers. This check explains "
          "mismatches as coordinate-convention effects where a single shift/transform "
          "reproduces ALL printed rows of a group; anything else stays an open "
          "mismatch (recorded, not explained away)."]
    open(os.path.join(HERE, "PHASE2_SCHMITT_ORIGIN_CHECK.md"), "w").write("\n".join(L) + "\n")
    json.dump(out, open(os.path.join(HERE, "phase2_schmitt_origin_check.json"), "w"), indent=1)
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
