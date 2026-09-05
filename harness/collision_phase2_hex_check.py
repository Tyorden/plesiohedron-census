#!/usr/bin/env python
"""collision_phase2_hex_check.py — PHASE-2 batch 2 (hexagonal family) collision
screen at Schmitt's printed points, confirmed by RECOMPUTATION for the top-10
survivors of TRIAGE_PHASE2_HEX_RESULT.md, mirroring collision_phase2_check.py.

Two parts:
  1. STORE-SIDE SCREEN (all menu-sighted hexagonal types; recomputed here from
     the store independently of the triage script): per (type, sighted group)
     the type survives iff its f-vector is printed in no row of that group, or
     every printed row with that (group, f-vector) reproduced in pass P2 as a
     DIFFERENT stored type; SAME anywhere = collision (reframe); a printed row
     that did not reproduce = UNRESOLVED for that pair. Counts must equal the
     triage's verdict counts (asserted).
  2. RECOMPUTATION for the top-10 survivors' worklist pairs
     (triage_phase2_hex_shortlist.json): Schmitt's printed (group, b, point)
     is run through the accepted batch-2 exact chain
     (sweep_phase2_hexagonal.evaluate: orbit -> Gram(b) -> float proposal ->
     exact clip with the 4*rho^2 <= D^2 certificate asserted on cell 0 and a
     second orbit cell, Euler, orbit congruence) with the G2c-confirmed
     conversion H1 (second enantiomorphs: verbatim, then z -> -z), the printed
     f-vector must reproduce (else FVEC-MISMATCH), and the canonical code is
     compared with the survivor's stored code and with the stored P2 cell's
     code (must agree with the store). Verdicts: SAME TYPE / DIFFERENT TYPE /
     FVEC-MISMATCH / CHAIN-QUARANTINE / TIMEOUT-DEFERRED (600 s per pair).

Read-only: the store is sha256-verified before and after; nothing is added.

LANGUAGE (G5, once): DIFFERENT does not establish novelty — Schmitt's tables
print ONE representative point per (group, f-vector) from a grid sampling;
every survivor stays "not matched against the records checked as of
2026-09-04".

Run (from harness/):
  python3 collision_phase2_hex_check.py
Writes: COLLISION_PHASE2_HEX_RESULTS.md, collision_phase2_hex_results.json.
Exit 0 iff every pair produced a verdict and the screen counts match the triage.
"""
import hashlib
import json
import os
import signal
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sweep_phase2_hexagonal as SH                   # noqa: E402

STORE = os.path.join(HERE, "phase2_hexagonal_types.json")
SHA_FILE = os.path.join(HERE, "phase2_hexagonal_types.SHA256SUMS")
TABLES = os.path.join(HERE, "schmitt_hexagonal_tables.json")
SHORTLIST = os.path.join(HERE, "triage_phase2_hex_shortlist.json")
OUT_MD = os.path.join(HERE, "COLLISION_PHASE2_HEX_RESULTS.md")
OUT_JSON = os.path.join(HERE, "collision_phase2_hex_results.json")
TIMEOUT_S = 600
SNAPSHOT = "2026-09-04"
MENU_PASSES = {"P1", "P3", "P4", "P5"}


class PairTimeout(Exception):
    pass


def _alarm(signum, frame):
    raise PairTimeout()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def code_id(code_str):
    return hashlib.sha1(code_str.encode("ascii")).hexdigest()[:16]


def fk(strs):
    return tuple(F(s) for s in strs)


def pt_str(p):
    return "(" + ", ".join(SH.frac_str(x) for x in p) + ")"


def main():
    t_all = time.time()
    sha0 = sha256_file(STORE)
    expected = open(SHA_FILE).read().split()[2]
    assert sha0 == expected, "store sha256 mismatch"
    store = json.load(open(STORE))
    types = store["types"]
    code2type = {t["canon_code"]: tid for tid, t in types.items()}
    sl = json.load(open(SHORTLIST))
    assert sl["store_sha256"] == sha0, "triage ran on a different store"
    tables = json.load(open(TABLES))
    rows = []
    for key, blk in tables.items():
        if key == "_meta":
            continue
        for r in blk["rows"]:
            rows.append({"groups": list(blk["groups"]), "f": tuple(r["f"]), "b": r["b"],
                         "pt": list(r["pt"]), "pdf": r["pdf_page"]})
    by_group_f = defaultdict(set)
    rows_by_gf = defaultdict(list)
    for r in rows:
        for g in r["groups"]:
            by_group_f[g].add(r["f"])
            rows_by_gf[(g, r["f"])].append(r)

    # ---- 1. store-side screen, recomputed
    p2_map = {}
    for tid, t in types.items():
        for s in t["sightings"]:
            if s["pass"] == "P2":
                p2_map[(s["group"], fk(s["printed_point_Bpp"]), F(s["b"]))] = tid
    menu = [tid for tid, t in types.items() if t["first_sighting_system"] == SH.SYSTEM
            and any(s["pass"] in MENU_PASSES for s in t["sightings"])]
    verdict = {}
    for tid in sorted(menu):
        t = types[tid]
        fv = tuple(t["f_vector"])
        groups = sorted({s["group"] for s in t["sightings"]})
        scell = any(s["pass"] == "P2" for s in t["sightings"])
        same = unres = False
        for g in groups:
            if fv not in by_group_f.get(g, set()):
                continue
            for r in rows_by_gf[(g, fv)]:
                hit = p2_map.get((g, fk(r["pt"]), F(r["b"])))
                if hit is None:
                    unres = True
                elif hit == tid:
                    same = True
        verdict[tid] = "COLLISION" if (same or scell) else ("UNRESOLVED" if unres else "SURVIVOR")
    vc = Counter(verdict.values())
    counts_match = dict(vc) == {k: v for k, v in sl["verdict_counts"].items()}
    survivors_here = [tid for tid in sl["survivors_ranked"] if verdict.get(tid) == "SURVIVOR"]
    ranked_match = survivors_here == sl["survivors_ranked"]

    # ---- 2. recomputation for the top-10 survivors' pairs
    signal.signal(signal.SIGALRM, _alarm)
    results = []
    for pr in sl["worklist"]:
        t0 = time.time()
        num, b = pr["group"], F(pr["b"])
        x = fk(pr["point_Bpp"])
        tgt = types[pr["target"]]
        convs = [("H1", SH.h1(x))]
        if num in SH.ENANTIO_SECOND:
            convs.append(("H1+zflip", SH.h1(SH.zflip(x))))
        res = dict(pr, secs=None)
        signal.alarm(TIMEOUT_S)
        try:
            got = None
            attempts = []
            for lab, p in convs:
                try:
                    r = SH.evaluate(num, p, b, "collision")
                except SH.ChainError as exc:
                    attempts.append((lab, f"quarantine {exc.reason}"))
                    continue
                attempts.append((lab, tuple(r["fvec"])))
                if tuple(r["fvec"]) == tuple(pr["fvec"]):
                    got = (lab, p, r)
                    break
            signal.alarm(0)
            res["attempts"] = attempts
            if got is None:
                if all(isinstance(a[1], str) for a in attempts):
                    res.update(verdict="CHAIN-QUARANTINE", detail=str(attempts))
                else:
                    res.update(verdict="FVEC-MISMATCH", detail=f"printed {pr['fvec']}, attempts {attempts}")
            else:
                lab, p, r = got
                code = r["code_str"]
                res.update(conversion=lab, point_ITA=pt_str(p), got_fvec=tuple(r["fvec"]),
                           got_pvec=SH.pvec_compact(r["pvec"]), got_aut=r["aut"],
                           orbit_n=r["orbit_conventional"], stab=r["stabilizer_order"], period=r["period"],
                           cutoff_D2=r["cutoff_D2"], congruence_checked=r["congruence_checked"],
                           store_hit=code2type.get(code), store_hit_id_of_code=code_id(code))
                res["verdict"] = "SAME TYPE" if code == tgt["canon_code"] else "DIFFERENT TYPE"
                res["store_consistent"] = (pr["p2_id"] is None) or (code2type.get(code) == pr["p2_id"])
        except PairTimeout:
            res.update(verdict="TIMEOUT-DEFERRED", detail=f"> {TIMEOUT_S} s")
        finally:
            signal.alarm(0)
        res["secs"] = round(time.time() - t0, 1)
        results.append(res)
        print(f"{pr['rank']:2d} {pr['target']} IT({num}) f={tuple(pr['fvec'])} b={pr['b']} -> {res['verdict']} "
              f"[{res.get('conversion')}; store_hit {res.get('store_hit')}; consistent {res.get('store_consistent')}] "
              f"{res['secs']}s", flush=True)

    sha1 = sha256_file(STORE)
    per_target = defaultdict(list)
    for r in results:
        per_target[r["target"]].append(r["verdict"])
    post = {}
    for s in sl["top10_survivors"]:
        vs = per_target.get(s["id"], [])
        if not vs:
            post[s["id"]] = "SURVIVES (f-vector absent from every sighted group's printed table; nothing to recompute)"
        elif all(v == "DIFFERENT TYPE" for v in vs):
            post[s["id"]] = f"SURVIVES (all {len(vs)} printed pair(s) DIFFERENT by recomputation)"
        elif any(v == "SAME TYPE" for v in vs):
            post[s["id"]] = "COLLISION (SAME TYPE at a printed point) -> reframe"
        else:
            post[s["id"]] = "INCOMPLETE (" + ", ".join(sorted(set(vs))) + ")"
    all_ok = (counts_match and ranked_match and sha0 == sha1
              and all(r["verdict"] in ("SAME TYPE", "DIFFERENT TYPE") for r in results)
              and all(r.get("store_consistent", True) for r in results))

    L = [f"# COLLISION screen — Phase-2 batch 2 (hexagonal family) at Schmitt's printed points ({SNAPSHOT})", "",
         "Script: `collision_phase2_hex_check.py` (model `collision_phase2_check.py`). Store: "
         f"`phase2_hexagonal_types.json` sha256 {sha0} (verified before and after: "
         f"{'unchanged' if sha0 == sha1 else 'CHANGED'}). Rows: `schmitt_hexagonal_tables.json`. Shortlist/worklist: "
         "`triage_phase2_hex_shortlist.json`. Chain: `sweep_phase2_hexagonal.evaluate` (accepted Gram modules; "
         "certificate asserted on two orbit cells; Euler; congruence). Conversion: H1 (ANCHORS G2c); second "
         "enantiomorphs verbatim then z -> -z.", "",
         f"**LANGUAGE (G5): DIFFERENT TYPE does not establish novelty; every survivor is \"not matched against the "
         f"records checked as of {SNAPSHOT}\" (Schmitt's tables print one representative per (group, f-vector) from a "
         "sampling).**", "",
         "## 1. Store-side screen (all menu-sighted hexagonal types), recomputed here", "",
         f"- Verdicts: SURVIVOR {vc['SURVIVOR']}, COLLISION {vc['COLLISION']}, UNRESOLVED {vc['UNRESOLVED']} of "
         f"{len(menu)} menu-sighted types — {'MATCH' if counts_match else 'MISMATCH'} with the triage's counts "
         f"{sl['verdict_counts']}; survivor ranking {'identical' if ranked_match else 'DIFFERS'}.",
         "- Definition: SURVIVOR = in every sighted group the f-vector is absent from the printed table or every printed "
         "row with that (group, f) reproduced (P2) as a different stored type; COLLISION = the type reproduces one of "
         "his printed cells (S-cell / SAME); UNRESOLVED = a printed row with that (group, f) was quarantined "
         "(schmitt_fvec_mismatch after both conversions), so no type-level statement is possible for that pair.", "",
         "## 2. Recomputation at the printed points — top-10 survivors", "",
         "| # | survivor | IT | printed f | printed b | printed point (B'') | PDF | conversion | point (ITA) | exact f | p | aut | stab | orbit | store hit | verdict | store-consistent | s |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in results:
        L.append(f"| {r['rank']} | `{r['target']}` | {r['group']} | {tuple(r['fvec'])} | {r['b']} | "
                 f"({', '.join(r['point_Bpp'])}) | {r['pdf']} | {r.get('conversion', '-')} | {r.get('point_ITA', '-')} | "
                 f"{r.get('got_fvec', '-')} | {r.get('got_pvec', '-')} | {r.get('got_aut', '-')} | {r.get('stab', '-')} | "
                 f"{r.get('orbit_n', '-')} | {r.get('store_hit') or 'not stored'} | **{r['verdict']}** | "
                 f"{r.get('store_consistent', '-')} | {r['secs']} |")
    L += ["", "## Post-screen verdict, top-10 survivors", ""]
    for s in sl["top10_survivors"]:
        L.append(f"- #{s['rank']} `{s['id']}` IT({s['group']}) f={tuple(s['f'])} aut {s['aut']} b={s['b']} O/W label "
                 f"{s['ow']}: {post[s['id']]}")
    L += ["", "## Honest limits", "",
          "- Type-level only at Schmitt's printed representatives; every other Schmitt flag stays f-vector-level.",
          "- UNRESOLVED pairs (printed rows that failed to reproduce after both documented conversions) are listed in "
          "the sweep's quarantines; no verdict is claimed for them.",
          "- No perturbation certificates and no G4 (roundness / geometric symmetry / Burnside / Engel / Bernhard) here.",
          "- The digitization is a text-layer parse with a 153-row visual cross-read, not an independent re-key.",
          f"", f"Wall {time.time() - t_all:.0f} s, single process. Deterministic except the timing columns."]
    open(OUT_MD, "w").write("\n".join(L) + "\n")
    json.dump({"store_sha256_before": sha0, "store_sha256_after": sha1, "screen_counts": dict(vc),
               "counts_match_triage": counts_match, "ranking_match_triage": ranked_match,
               "results": results, "post": post}, open(OUT_JSON, "w"), indent=1, default=str)
    print(f"screen: {dict(vc)} match={counts_match} ranked_match={ranked_match}; pairs {len(results)}; "
          f"store unchanged={sha0 == sha1}; all_ok={all_ok}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
