#!/usr/bin/env python
"""schmitt_collision_check.py — pre-G4 collision screen for the TOP-10 shortlist.

Generalizes the schmitt_220_check.py pattern: for every (group, f-vector) pair
where a TOP-10 shortlist type (TRIAGE_RESULT.md, 2026-08-30) has a sighting AND
Schmitt's printed per-group table (Schmitt 2016 dissertation, Sec. 2.2.5,
printed pp. 119-150) contains that f-vector, orbit Schmitt's printed generating
grid point under the frozen group ops (spacegroups.json, G1-verified), scale
exactly, run float sweep (W=2) -> exact clip (4*rho^2 <= D^2 certificate
asserted) -> canonical code, and compare against OUR stored type's canonical
code from phase1_types.json.

Verdicts per pair:
  SAME TYPE      — Schmitt's cell at his printed point IS our candidate's
                   combinatorial type (collision: reframe per kill criteria).
  DIFFERENT TYPE — same f-vector, different combinatorial type; the candidate
                   survives THIS screen. NOTE (stated once, applies to every
                   DIFFERENT verdict): this does NOT establish novelty — his
                   table prints ONE representative point per f-vector from a
                   grid SAMPLING; the type may exist in his unprinted ~14TB
                   data. All language stays "not matched against the catalog
                   snapshot of 2026-08-28".
  TIMEOUT-DEFERRED — the pair exceeded the per-pair wall clock (600 s);
                   recorded, not silently capped.
  FVEC-MISMATCH  — our exact cell at his printed point has a different
                   f-vector than his printed row (would indicate a coordinate
                   convention problem; recorded, never forced).

All 21 printed points below were transcribed from visual reads of the archived
PDF (references/Schmitt_2016_dissertation.pdf, printed page = PDF page - 5) on
2026-08-30 and cross-checked against the pdftotext text layer; every needed
f-vector was found exactly where the triage digitization flagged it (no
discrepancies). Enantiomorph note: IT(212)/IT(213) share one printed table
(header "IT(212) = P4_3 32, IT(213) = P4_1 32"); canonical_code identifies
mirror images, so the comparison run under the frozen IT(212) ops covers both.

ORIGIN CONVENTION (two-origin groups): Schmitt's data use IT origin choice 2;
our frozen spacegroups.json uses origin choice 1 (both facts machine-verified
in SCHMITT_OPS_XCHECK_2026-08-28.md / xcheck_schmitt_ops.py, which recovered
the exact affine map x_his = x_ours + v per group). For the five affected
pairs (IT 201, 203, 224, 227, 228) the printed point is converted to our
setting as x_ours = x_his - v (mod 1) before orbiting; v is recorded below.
A global origin shift translates the whole orbit, so the cell's combinatorial
type is unchanged — this is a coordinate conversion, not a perturbation.


Run: python3 \
        schmitt_collision_check.py [--pair P01 [P02 ...]]
Writes: SCHMITT_COLLISION_RESULTS.md. Exit 0 iff every requested pair ran
clean (any verdict); nonzero on internal inconsistency.
"""
import argparse
import json
import os
import signal
import sys
import time
from fractions import Fraction as F

import orbit
from sweep_voronoi import sweep
from exact_cell import clip_cell
from canon_code import canonical_code

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.join(HERE, "phase1_types.json")
OUT = os.path.join(HERE, "SCHMITT_COLLISION_RESULTS.md")
TIMEOUT_S = 600

# Every (group, f-vector) pair for the TOP-10 shortlist with a P flag.
# point = Schmitt's printed generating grid point, VERBATIM rationals from the
# visual page read; page = printed page number (PDF page = printed + 5).
PAIRS = [
    dict(pair="P01", rank=1, target="ceb70631e274e727", group=212,
         fvec=(37, 57, 22), point=("-511/2124", "-29/236", "1/72"),
         page=135, freq="1027"),
    dict(pair="P02", rank=2, target="359beee832567a71", group=230,
         fvec=(40, 61, 23), point=("-263/2328", "-149/2328", "787/3492"),
         page=150, freq="132168"),
    dict(pair="P03", rank=3, target="fd96e7fc36481986", group=199,
         fvec=(36, 54, 20), point=("379/3492", "379/3492", "379/3492"),
         page=123, freq="758"),
    dict(pair="P04", rank=4, target="998994bcf8df722b", group=206,
         fvec=(30, 45, 17), point=("1/8", "1/8", "1/8"),
         page=128, freq="873"),
    dict(pair="P05", rank=4, target="998994bcf8df722b", group=220,
         fvec=(30, 45, 17), point=("1/8", "1/8", "1/8"),
         page=142, freq="291"),
    dict(pair="P06", rank=4, target="998994bcf8df722b", group=230,
         fvec=(30, 45, 17), point=("1/8", "1/8", "1/8"),
         page=150, freq="582"),
    dict(pair="P07", rank=5, target="8c69db9e84095469", group=199,
         fvec=(30, 45, 17), point=("1/8", "1/8", "1/8"),
         page=123, freq="115"),
    dict(pair="P08", rank=5, target="8c69db9e84095469", group=212,
         fvec=(30, 45, 17), point=("-3/8", "-1/8", "1/8"),
         page=134, freq="179"),
    dict(pair="P09", rank=5, target="8c69db9e84095469", group=214,
         fvec=(30, 45, 17), point=("1/8", "1/8", "1/8"),
         page=136, freq="1"),
    dict(pair="P10", rank=6, target="2001fe7ea92fd0ad", group=203,
         fvec=(16, 30, 16), point=("1/8", "1/8", "1/8"),
         page=125, freq="1"),
    dict(pair="P11", rank=6, target="2001fe7ea92fd0ad", group=210,
         fvec=(16, 30, 16), point=("0", "0", "0"),
         page=132, freq="1"),
    dict(pair="P12", rank=6, target="2001fe7ea92fd0ad", group=212,
         fvec=(16, 30, 16), point=("0", "0", "0"),
         page=134, freq="1"),
    dict(pair="P13", rank=6, target="2001fe7ea92fd0ad", group=227,
         fvec=(16, 30, 16), point=("1/8", "1/8", "1/8"),
         page=147, freq="1"),
    dict(pair="P14", rank=7, target="afeb1ae44c1a3443", group=198,
         fvec=(32, 48, 18), point=("1/8", "1/8", "1/8"),
         page=122, freq="207"),
    dict(pair="P15", rank=7, target="afeb1ae44c1a3443", group=212,
         fvec=(32, 48, 18), point=("1/8", "1/8", "1/8"),
         page=134, freq="1"),
    dict(pair="P16", rank=8, target="c314dedd38208a2e", group=212,
         fvec=(30, 46, 18), point=("-55/708", "-239/2124", "-329/4248"),
         page=134, freq="7322558"),
    dict(pair="P17", rank=9, target="aa6b0077c3234d24", group=214,
         fvec=(30, 47, 19), point=("-455/6984", "-73/776", "545/3492"),
         page=136, freq="48889552"),
    dict(pair="P18", rank=10, target="ea1baec328356a32", group=201,
         fvec=(25, 39, 16), point=("1817/7264", "1817/7264", "1815/7264"),
         page=124, freq="5445"),
    dict(pair="P19", rank=10, target="ea1baec328356a32", group=208,
         fvec=(25, 39, 16), point=("1815/7264", "1815/7264", "1815/7264"),
         page=130, freq="1815"),
    dict(pair="P20", rank=10, target="ea1baec328356a32", group=224,
         fvec=(25, 39, 16), point=("1817/7264", "1817/7264", "1815/7264"),
         page=145, freq="5445"),
    dict(pair="P21", rank=10, target="ea1baec328356a32", group=228,
         fvec=(25, 39, 16), point=("180/1441", "180/1441", "180/1441"),
         page=147, freq="4320"),
]


# x_his = x_ours + v (xcheck_schmitt_ops.py, CONJUGATE-VERIFIED, M=I);
# convert his printed coordinates to our origin-1 setting: x_ours = x_his - v.
ORIGIN_V = {
    201: ("3/4", "3/4", "3/4"),
    203: ("7/8", "7/8", "7/8"),
    224: ("3/4", "3/4", "3/4"),
    227: ("7/8", "7/8", "7/8"),
    228: ("1/8", "1/8", "5/8"),
}


class PairTimeout(Exception):
    pass


def _alarm(signum, frame):
    raise PairTimeout()


def run_pair(pr, groups, store, code2type):
    """Run one (group, f-vector) pair; return a result dict."""
    t0 = time.time()
    entry = groups[pr["group"]]
    X = tuple(F(s) for s in pr["point"])
    v = ORIGIN_V.get(pr["group"])
    if v is not None:
        X = tuple((x - F(s)) % 1 for x, s in zip(X, v))
    orb = orbit.orbit(entry, X)
    spts, sP = orbit.scale_orbit(orb["points"])

    cells_f = sweep(spts, sP, W=2)
    cells_e = [clip_cell(c, spts, sP) for c in spts]
    for e, f in zip(cells_e, cells_f):
        assert e["facet_count"] == f["facet_count"], \
            f"{pr['pair']}: float/exact facet count disagree"
        assert e["p_vector"] == f["p_vector"], \
            f"{pr['pair']}: float/exact p-vector disagree"
        assert 4 * e["rho2"] <= e["cutoff_D"] ** 2, \
            f"{pr['pair']}: provable cutoff violated"
    codes = [canonical_code(e["facet_cycles"]) for e in cells_e]
    cset = set(codes)
    assert len(cset) == 1, f"{pr['pair']}: orbit produced >1 canonical code"
    code_b, aut = codes[0]
    code = code_b.decode("ascii")

    e0 = cells_e[0]
    n_edges = sum(len(c) for c in e0["facet_cycles"]) // 2
    got_f = (e0["n_vertices"], n_edges, e0["facet_count"])
    pvec = e0["p_vector"]

    tgt = store[pr["target"]]
    same = (code == tgt["canon_code"])
    hit = code2type.get(code)

    if got_f != pr["fvec"]:
        verdict = "FVEC-MISMATCH"
    elif same:
        verdict = "SAME TYPE"
    else:
        verdict = "DIFFERENT TYPE"
    # Is his printed point (converted to our setting) literally one of our
    # stored sighting points for the target type in this group? If so the
    # collision was foregone: our sweep grid sampled his exact representative.
    sight_pts = {tuple(F(x) % 1 for x in s["point"])
                 for s in tgt["sightings"] if s["group"] == pr["group"]}
    coincide = tuple(x % 1 for x in X) in sight_pts

    return dict(pr, verdict=verdict, got_fvec=got_f, got_pvec=pvec,
                got_aut=aut, code=code, store_hit=hit, coincide=coincide,
                orbit_n=orb["n_conventional"],
                stab=orb["stabilizer_order"], period=sP,
                secs=round(time.time() - t0, 1))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--pair", nargs="*", default=None,
                    help="pair ids to run (default: all)")
    args = ap.parse_args(argv)
    todo = [p for p in PAIRS if args.pair is None or p["pair"] in args.pair]

    groups = orbit.load_groups()
    raw = json.load(open(STORE))
    store = raw["types"]
    for p in PAIRS:
        assert p["target"] in store, f"target {p['target']} not in store"
        assert tuple(store[p["target"]]["f_vector"]) == p["fvec"], \
            f"{p['pair']}: shortlist f-vector != store f-vector"
    code2type = {v["canon_code"]: k for k, v in store.items()}
    assert len(code2type) == len(store), "store canon codes not unique"

    results = []
    old = signal.signal(signal.SIGALRM, _alarm)
    try:
        for pr in todo:
            signal.alarm(TIMEOUT_S)
            try:
                r = run_pair(pr, groups, store, code2type)
            except PairTimeout:
                r = dict(pr, verdict="TIMEOUT-DEFERRED", got_fvec=None,
                         got_pvec=None, got_aut=None, code=None,
                         store_hit=None, coincide=False, orbit_n=None,
                         stab=None, period=None, secs=TIMEOUT_S)
            finally:
                signal.alarm(0)
            print(f"{r['pair']} rank{r['rank']:>2} IT({r['group']}) "
                  f"f={r['fvec']} -> {r['verdict']}"
                  f" [{r['secs']}s, orbit={r['orbit_n']}, stab={r['stab']},"
                  f" period={r['period']}]")
            results.append(r)
    finally:
        signal.signal(signal.SIGALRM, old)

    write_md(results)
    # exit 0 iff all requested pairs produced a verdict (asserts abort earlier)
    return 0


def write_md(results):
    L = []
    A = L.append
    A("# Schmitt printed-point collision screen — TOP-10 shortlist "
      "(pre-G4, 2026-08-30)")
    A("")
    A("Script: `schmitt_collision_check.py` (this run: %d pair(s)). Pattern: "
      "`schmitt_220_check.py`. Sources: Schmitt 2016 dissertation "
      "(`../references/Schmitt_2016_dissertation.pdf`), Sec. 2.2.5 per-group "
      "tables, printed pp. 119-150 (PDF page = printed + 5); frozen "
      "`spacegroups.json` (G1); `phase1_types.json` (Phase-1 ACCEPTED "
      "2026-08-29); shortlist per `TRIAGE_RESULT.md` (2026-08-30)."
      % len(results))
    A("")
    A("**LANGUAGE (G5, stated once for every verdict below): a DIFFERENT-TYPE "
      "verdict does NOT establish novelty.** Schmitt's tables print ONE "
      "representative generating point per (group, f-vector) from a grid "
      "SAMPLING; a type absent at his printed point may still occur in his "
      "unprinted data. Every surviving candidate remains only \"not matched "
      "against the catalog snapshot of 2026-08-28\". A SAME-TYPE verdict IS "
      "decisive: our candidate's combinatorial type appears in Schmitt 2016 "
      "at his printed point (collision; reframe per kill criteria).")
    A("")
    A("## Transcription record (visual page reads, 2026-08-30)")
    A("")
    A("All 21 generating points transcribed from visual reads of the archived "
      "PDF pages and cross-checked against the pdftotext text layer; both "
      "agree verbatim on all 21 rows. Every (group, f-vector) pair flagged P "
      "by the triage digitization was found on re-read — NO discrepancies vs "
      "`triage_phase1.py`. IT(212)/IT(213) share one printed table (printed "
      "pp. 133-135); runs use the frozen IT(212) ops — `canon_code` "
      "identifies mirror images, so the verdict covers both enantiomorphs.")
    A("")
    A("Two-origin groups (IT 201, 203, 224, 227, 228): Schmitt's data are "
      "origin choice 2, the G1 freeze is origin choice 1 "
      "(`SCHMITT_OPS_XCHECK_2026-08-28.md`, machine-verified x_his = x_ours "
      "+ v, M = I); the printed point is converted as x_ours = x_his - v "
      "(mod 1) before orbiting (global translation — type-invariant). The v "
      "used is shown in the last column.")
    A("")
    A("| pair | IT | printed f-vector | printed generating point | freq | "
      "printed p. | origin-2 -> origin-1 shift v |")
    A("|---|---|---|---|---|---|---|")
    for r in results:
        v = ORIGIN_V.get(r["group"])
        A("| %s | %d | %s | (%s) | %s | %d | %s |"
          % (r["pair"], r["group"], str(r["fvec"]),
             ", ".join(r["point"]), r["freq"], r["page"],
             "(%s)" % ", ".join(v) if v else "—"))
    A("")
    A("## Per-pair verdicts")
    A("")
    A("| pair | rank | target type | IT | f-vector | orbit | stab | PERIOD | "
      "Schmitt cell p-vector | aut | verdict | secs |")
    A("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in results:
        pv = ("`" + " ".join(f"{k}^{r['got_pvec'].count(k)}"
                             for k in sorted(set(r["got_pvec"]))) + "`"
              ) if r["got_pvec"] else "—"
        note = ""
        if r["verdict"] == "DIFFERENT TYPE":
            note = (" (= stored type `%s`)" % r["store_hit"]
                    if r["store_hit"] else " (not any stored type)")
        if r["verdict"] == "FVEC-MISMATCH":
            note = " (computed f=%s)" % (r["got_fvec"],)
        if r["coincide"]:
            note += " [point = stored sighting point: collision foregone]"
        A("| %s | %d | `%s` | %d | %s | %s | %s | %s | %s | %s | **%s**%s | %s |"
          % (r["pair"], r["rank"], r["target"], r["group"], str(r["fvec"]),
             r["orbit_n"], r["stab"], r["period"], pv,
             r["got_aut"] if r["got_aut"] else "—", r["verdict"], note,
             r["secs"]))
    A("")
    A("## Summary (this run)")
    A("")
    by_rank = {}
    for r in results:
        by_rank.setdefault((r["rank"], r["target"]), []).append(r["verdict"])
    for (rk, tid), vs in sorted(by_rank.items()):
        if any(v == "SAME TYPE" for v in vs):
            s = ("COLLISION — the type is Schmitt's printed cell in %d/%d "
                 "checked group(s); reframe per kill criteria (not a new "
                 "sighting-class candidate)."
                 % (sum(v == "SAME TYPE" for v in vs), len(vs)))
        elif all(v == "DIFFERENT TYPE" for v in vs):
            s = ("survives this screen (all %d pair(s) DIFFERENT); proceeds "
                 "to G4 under snapshot language only." % len(vs))
        else:
            s = "mixed/incomplete: " + ", ".join(vs)
        A("- rank %d `%s`: %s" % (rk, tid, s))
    A("")
    A("## Notes")
    A("")
    A("- Special positions (stab > 1) handled by `orbit.py` normally; the "
      "orbit/stab columns record them.")
    A("- \"[point = stored sighting point]\" marks pairs where Schmitt's "
      "printed representative point, converted to our setting, is EXACTLY a "
      "point our Phase-1 sweep already sampled for the target type — the "
      "SAME verdict there is a deterministic recomputation, recorded for "
      "completeness.")
    A("- Where a DIFFERENT verdict names a stored type, that means Schmitt's "
      "printed representative for the f-vector is itself a type our sweep "
      "also found — the two types share an f-vector in that group (same "
      "class of micro-fact as the Josehedron / Schmitt-220 result, "
      "`SCHMITT_220_CHECK_RESULT.md`).")
    A("- Per-pair wall-clock cap %d s -> TIMEOUT-DEFERRED (recorded, never "
      "silent)." % TIMEOUT_S)
    A("- Certificate asserted per cell: float/exact facet-count and p-vector "
      "agreement, and 4*rho^2 <= D^2 exact cutoff; one canonical code across "
      "the whole orbit.")
    A("")
    with open(OUT, "w") as fh:
        fh.write("\n".join(L))
    print("wrote", OUT)


if __name__ == "__main__":
    sys.exit(main())
