#!/usr/bin/env python
"""schmitt_crossgroup_check.py — G5 cross-group collision batch (batch 2 of the
schmitt_collision_check.py pattern) for the 11 G4-certified candidates.

WHY (G5_DILIGENCE_2026-08-30.md, cross-group scan): the triage ABSENT-all flag
was scoped to SIGHTED groups. 10 of the 11 candidate f-vectors appear in
Schmitt's printed tables for OTHER groups; a same-type coincidence across
groups was not excluded by the accepted batch-1 screen (sighted-group pairs
only). This batch runs the identical exact chain at Schmitt's printed
representative point for EVERY (candidate f-vector) x (other group whose
printed table shows it) pair — 55 pairs total, enumerated programmatically
from the accepted digitization (triage_phase1.SCHMITT_FVECTORS), reproducing
the G5 doc's scan table exactly. Candidate #3 `8cf50403cf88c455` (16,25,11)
has ZERO cross-group rows (f-vector absent from the entire printed cubic
survey) and is reported with an empty pair set.

Verdicts per pair (identical semantics to batch 1 — run_pair is IMPORTED from
the accepted schmitt_collision_check.py, not reimplemented):
  SAME TYPE        — Schmitt's cell at his printed point IS the candidate's
                     combinatorial type (cross-group collision; reframe per
                     kill criteria).
  DIFFERENT TYPE   — different combinatorial type; the note records whether it
                     equals some OTHER stored type or is new-to-store.
  FVEC-MISMATCH    — our exact cell at his printed point does not reproduce
                     his printed f-vector (coordinate-convention STOP for the
                     pair; recorded, never forced).
  TIMEOUT-DEFERRED — per-pair wall clock > 600 s; recorded, not silent.

LANGUAGE (stated once): a DIFFERENT-TYPE verdict does NOT establish novelty.
Schmitt's tables print ONE representative generating point per
(group, f-vector) from a grid SAMPLING; surviving every printed representative
leaves the type possible in his unprinted ~14TB data. All wording stays
"not matched against the catalog snapshot of 2026-08-30".

TRANSCRIPTION of the 55 printed points (this session, 2026-08-30): primary
extraction = pdftotext -layout text layer of the archived PDF
(references/Schmitt_2016_dissertation.pdf, PDF page = printed page + 5),
parsed programmatically with per-page tracking. The parser was validated four
ways before any point was trusted: (a) parsed f-vector sequences of ALL 36
cubic tables identical to the accepted triage digitization (881 rows);
(b) parsed f-vectors AND frequencies identical to the accepted independent
re-key (rekey_tables.json) on all 386 rows of the six re-keyed groups;
(c) the parser reproduces all 21 batch-1 points/frequencies/page numbers that
were transcribed by VISUAL page reads (accepted screen) verbatim; (d) every
one of the 55 rows below was additionally verified against a fresh VISUAL
read of its rendered PDF page in this session (point, frequency, page).

ORIGIN CONVENTION (two-origin groups in this batch: IT 203, 222, 227, 228):
Schmitt's data use IT origin choice 2; the frozen spacegroups.json uses origin
choice 1 (machine-verified, SCHMITT_OPS_XCHECK_2026-08-28.md). Conversion
x_ours = x_his - v (mod 1) via the accepted ORIGIN_V of batch 1, EXTENDED here
by IT(222): v = (3/4, 3/4, 3/4) (x_his = x_ours - 1/4 per coordinate),
machine-recovered from Schmitt's own 2016 ops via the accepted
xcheck_schmitt_ops machinery. verify_origin_shifts() re-derives v for ALL
two-origin groups used in this batch at runtime and asserts agreement before
any pair runs; additionally every pair must reproduce the printed f-vector
(FVEC-MISMATCH otherwise), the same functional check that provably caught a
missing shift for IT(203) in batch 1.

Run: python3 \
        schmitt_crossgroup_check.py [--pair X01 [X02 ...]]
Writes: CROSS_GROUP_RESULTS.md. Exit 0 iff every requested pair produced a
verdict (internal inconsistencies abort via assert).
"""
import argparse
import json
import os
import signal
import sys
import time
from fractions import Fraction as F

import orbit
import schmitt_collision_check as base
from schmitt_collision_check import run_pair, PairTimeout, _alarm

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.join(HERE, "phase1_types.json")
OUT = os.path.join(HERE, "CROSS_GROUP_RESULTS.md")
TIMEOUT_S = 600

# Candidate ids in G5-doc numbering (candidate #3 has no cross-group rows).
CANDIDATES = {
    1: "ceb70631e274e727", 2: "359beee832567a71", 3: "8cf50403cf88c455",
    4: "c314dedd38208a2e", 5: "aa6b0077c3234d24", 6: "f3d0f39a0b9676b9",
    7: "2de0a21129cabe90", 8: "c4ea3f32fdd6dc51", 9: "9b69eefb8bd8437c",
    10: "d2d935e5499e6e11", 11: "f98a3ee5675fc121",
}
SIGHTED = {1: 212, 2: 230, 3: 220, 4: 212, 5: 214, 6: 214, 7: 201, 8: 224,
           9: 224, 10: 224, 11: 224}

# Every (other group, candidate f-vector) pair with a printed row in Schmitt's
# cubic tables. point = printed generating grid point VERBATIM (rationals);
# page = printed page (PDF page = printed + 5); freq = printed frequency.
PAIRS = [
    dict(pair="X01", cand=1, target="ceb70631e274e727", group=199,
         fvec=(37, 57, 22), point=("1/12", "35/388", "77/388"),
         page=123, freq="7"),
    dict(pair="X02", cand=1, target="ceb70631e274e727", group=214,
         fvec=(37, 57, 22), point=("75/776", "7/72", "407/2328"),
         page=137, freq="101"),
    dict(pair="X03", cand=1, target="ceb70631e274e727", group=230,
         fvec=(37, 57, 22), point=("499/6984", "83/6984", "821/3492"),
         page=150, freq="1"),
    dict(pair="X04", cand=2, target="359beee832567a71", group=206,
         fvec=(40, 61, 23), point=("1/8", "125/2328", "499/2328"),
         page=129, freq="22842322"),
    dict(pair="X05", cand=2, target="359beee832567a71", group=212,
         fvec=(40, 61, 23), point=("-217/1062", "-115/1062", "23/4248"),
         page=135, freq="2574890"),
    dict(pair="X06", cand=2, target="359beee832567a71", group=214,
         fvec=(40, 61, 23), point=("10/97", "361/3492", "1123/6984"),
         page=137, freq="1660625"),
    dict(pair="X07", cand=2, target="359beee832567a71", group=220,
         fvec=(40, 61, 23), point=("1/8", "365/6984", "373/1746"),
         page=143, freq="12841602"),
    dict(pair="X08", cand=4, target="c314dedd38208a2e", group=198,
         fvec=(30, 46, 18), point=("1/8", "1/24", "5/24"),
         page=122, freq="843"),
    dict(pair="X09", cand=4, target="c314dedd38208a2e", group=206,
         fvec=(30, 46, 18), point=("785/6984", "787/6984", "425/3492"),
         page=128, freq="30035545"),
    dict(pair="X10", cand=4, target="c314dedd38208a2e", group=214,
         fvec=(30, 46, 18), point=("31/1746", "109/873", "1309/6984"),
         page=136, freq="19665278"),
    dict(pair="X11", cand=4, target="c314dedd38208a2e", group=220,
         fvec=(30, 46, 18), point=("88/873", "353/3492", "127/1164"),
         page=142, freq="96509074"),
    dict(pair="X12", cand=4, target="c314dedd38208a2e", group=230,
         fvec=(30, 46, 18), point=("-455/6984", "-73/776", "545/3492"),
         page=150, freq="53229871"),
    dict(pair="X13", cand=5, target="aa6b0077c3234d24", group=199,
         fvec=(30, 47, 19), point=("439/6984", "49/776", "527/2328"),
         page=123, freq="168"),
    dict(pair="X14", cand=5, target="aa6b0077c3234d24", group=206,
         fvec=(30, 47, 19), point=("-461/6984", "-473/6984", "545/3492"),
         page=128, freq="8842620"),
    dict(pair="X15", cand=5, target="aa6b0077c3234d24", group=212,
         fvec=(30, 47, 19), point=("-151/2124", "-179/2124", "-65/2124"),
         page=134, freq="52233655"),
    dict(pair="X16", cand=5, target="aa6b0077c3234d24", group=230,
         fvec=(30, 47, 19), point=("-659/6984", "-869/6984", "545/3492"),
         page=150, freq="5218967"),
    dict(pair="X17", cand=6, target="f3d0f39a0b9676b9", group=197,
         fvec=(10, 17, 9), point=("909/3632", "909/3632", "453/1816"),
         page=120, freq="453"),
    dict(pair="X18", cand=6, target="f3d0f39a0b9676b9", group=199,
         fvec=(10, 17, 9), point=("0", "0", "1/2328"),
         page=122, freq="436"),
    dict(pair="X19", cand=6, target="f3d0f39a0b9676b9", group=211,
         fvec=(10, 17, 9), point=("121/454", "967/3632", "789/3632"),
         page=132, freq="179872"),
    dict(pair="X20", cand=6, target="f3d0f39a0b9676b9", group=212,
         fvec=(10, 17, 9), point=("-1/4", "-353/4248", "89/1062"),
         page=133, freq="177"),
    dict(pair="X21", cand=6, target="f3d0f39a0b9676b9", group=217,
         fvec=(10, 17, 9), point=("909/3632", "909/3632", "453/1816"),
         page=139, freq="453"),
    dict(pair="X22", cand=6, target="f3d0f39a0b9676b9", group=218,
         fvec=(10, 17, 9), point=("909/3632", "909/3632", "453/1816"),
         page=140, freq="453"),
    dict(pair="X23", cand=6, target="f3d0f39a0b9676b9", group=230,
         fvec=(10, 17, 9), point=("-1/6984", "-1/6984", "1745/6984"),
         page=149, freq="70"),
    dict(pair="X24", cand=7, target="2de0a21129cabe90", group=197,
         fvec=(20, 33, 15), point=("3285/7264", "3283/7264", "229/7264"),
         page=121, freq="20486921"),
    dict(pair="X25", cand=7, target="2de0a21129cabe90", group=206,
         fvec=(20, 33, 15), point=("-457/6984", "-211/2328", "545/3492"),
         page=128, freq="36467"),
    dict(pair="X26", cand=7, target="2de0a21129cabe90", group=208,
         fvec=(20, 33, 15), point=("1937/7264", "1935/7264", "1577/7264"),
         page=130, freq="111858167"),
    dict(pair="X27", cand=7, target="2de0a21129cabe90", group=210,
         fvec=(20, 33, 15), point=("219/11528", "201/11528", "185/11528"),
         page=132, freq="110275905"),
    dict(pair="X28", cand=7, target="2de0a21129cabe90", group=212,
         fvec=(20, 33, 15), point=("-355/4248", "-179/2124", "-44/531"),
         page=134, freq="22087236"),
    dict(pair="X29", cand=7, target="2de0a21129cabe90", group=214,
         fvec=(20, 33, 15), point=("-73/776", "-659/6984", "121/776"),
         page=136, freq="983215"),
    dict(pair="X30", cand=7, target="2de0a21129cabe90", group=218,
         fvec=(20, 33, 15), point=("3285/7264", "3283/7264", "229/7264"),
         page=140, freq="23274317"),
    dict(pair="X31", cand=7, target="2de0a21129cabe90", group=220,
         fvec=(20, 33, 15), point=("0", "9/388", "105/776"),
         page=142, freq="1"),
    dict(pair="X32", cand=7, target="2de0a21129cabe90", group=230,
         fvec=(20, 33, 15), point=("-53/1164", "-43/582", "119/1164"),
         page=149, freq="11"),
    dict(pair="X33", cand=8, target="c4ea3f32fdd6dc51", group=197,
         fvec=(14, 23, 11), point=("1817/7264", "1817/7264", "1813/7264"),
         page=121, freq="491821"),
    dict(pair="X34", cand=8, target="c4ea3f32fdd6dc51", group=208,
         fvec=(14, 23, 11), point=("121/454", "967/3632", "789/3632"),
         page=130, freq="1027254"),
    dict(pair="X35", cand=8, target="c4ea3f32fdd6dc51", group=212,
         fvec=(14, 23, 11), point=("-103/1416", "-103/1416", "103/1416"),
         page=133, freq="353"),
    dict(pair="X36", cand=8, target="c4ea3f32fdd6dc51", group=217,
         fvec=(14, 23, 11), point=("1817/7264", "1817/7264", "1813/7264"),
         page=139, freq="491821"),
    dict(pair="X37", cand=8, target="c4ea3f32fdd6dc51", group=218,
         fvec=(14, 23, 11), point=("1817/7264", "1817/7264", "1813/7264"),
         page=140, freq="491821"),
    dict(pair="X38", cand=8, target="c4ea3f32fdd6dc51", group=222,
         fvec=(14, 23, 11), point=("15/227", "45/3632", "7/3632"),
         page=144, freq="846570215"),
    dict(pair="X39", cand=8, target="c4ea3f32fdd6dc51", group=230,
         fvec=(14, 23, 11), point=("281/6984", "289/2328", "1453/6984"),
         page=149, freq="118"),
    dict(pair="X40", cand=9, target="9b69eefb8bd8437c", group=208,
         fvec=(11, 18, 9), point=("909/3632", "909/3632", "453/1816"),
         page=130, freq="453"),
    dict(pair="X41", cand=10, target="d2d935e5499e6e11", group=195,
         fvec=(6, 11, 7), point=("1815/3632", "907/1816", "0"),
         page=119, freq="1646205"),
    dict(pair="X42", cand=10, target="d2d935e5499e6e11", group=200,
         fvec=(6, 11, 7), point=("1815/3632", "907/1816", "0"),
         page=124, freq="1646205"),
    dict(pair="X43", cand=10, target="d2d935e5499e6e11", group=202,
         fvec=(6, 11, 7), point=("247/7264", "13/1816", "7/3632"),
         page=125, freq="609531852"),
    dict(pair="X44", cand=10, target="d2d935e5499e6e11", group=204,
         fvec=(6, 11, 7), point=("179/3632", "125/3632", "67/3632"),
         page=126, freq="1475"),
    dict(pair="X45", cand=10, target="d2d935e5499e6e11", group=208,
         fvec=(6, 11, 7), point=("1817/7264", "1817/7264", "1815/7264"),
         page=130, freq="3630"),
    dict(pair="X46", cand=10, target="d2d935e5499e6e11", group=228,
         fvec=(6, 11, 7), point=("721/5764", "180/1441", "-180/1441"),
         page=147, freq="4320"),
    dict(pair="X47", cand=11, target="f98a3ee5675fc121", group=203,
         fvec=(10, 15, 7), point=("180/1441", "180/1441", "180/1441"),
         page=125, freq="2880"),
    dict(pair="X48", cand=11, target="f98a3ee5675fc121", group=204,
         fvec=(10, 15, 7), point=("1815/7264", "1815/7264", "1815/7264"),
         page=126, freq="1815"),
    dict(pair="X49", cand=11, target="f98a3ee5675fc121", group=210,
         fvec=(10, 15, 7), point=("180/1441", "180/1441", "180/1441"),
         page=131, freq="1440"),
    dict(pair="X50", cand=11, target="f98a3ee5675fc121", group=211,
         fvec=(10, 15, 7), point=("1815/7264", "1815/7264", "1815/7264"),
         page=132, freq="1815"),
    dict(pair="X51", cand=11, target="f98a3ee5675fc121", group=217,
         fvec=(10, 15, 7), point=("1819/7264", "1817/7264", "1695/7264"),
         page=139, freq="148432727"),
    dict(pair="X52", cand=11, target="f98a3ee5675fc121", group=222,
         fvec=(10, 15, 7), point=("1817/7264", "1817/7264", "1815/7264"),
         page=143, freq="5445"),
    dict(pair="X53", cand=11, target="f98a3ee5675fc121", group=223,
         fvec=(10, 15, 7), point=("1815/7264", "1815/7264", "1815/7264"),
         page=144, freq="1815"),
    dict(pair="X54", cand=11, target="f98a3ee5675fc121", group=227,
         fvec=(10, 15, 7), point=("180/1441", "180/1441", "180/1441"),
         page=147, freq="2880"),
    dict(pair="X55", cand=11, target="f98a3ee5675fc121", group=229,
         fvec=(10, 15, 7), point=("1815/7264", "1815/7264", "1815/7264"),
         page=148, freq="1815"),
]

# Extend the accepted batch-1 origin-shift table by IT(222) (not needed in
# batch 1). run_pair reads base.ORIGIN_V, so the conversion executes through
# the accepted code path.
assert 222 not in base.ORIGIN_V, "base ORIGIN_V changed; re-audit"
base.ORIGIN_V[222] = ("3/4", "3/4", "3/4")


def enumerate_expected_pairs():
    """Re-derive the pair set from the accepted digitization; the hardcoded
    PAIRS above must match it exactly (guards transcription of the QUEUE, not
    of the points)."""
    from triage_phase1 import SCHMITT_FVECTORS
    want = set()
    for num, cid in CANDIDATES.items():
        fv = FVECS[num]
        for g in sorted(k for k in SCHMITT_FVECTORS if k != 213):
            if g != SIGHTED[num] and tuple(fv) in [tuple(r) for r in
                                                   SCHMITT_FVECTORS[g]]:
                want.add((cid, g, tuple(fv)))
    got = {(p["target"], p["group"], tuple(p["fvec"])) for p in PAIRS}
    assert want == got, ("pair-set mismatch vs digitization",
                         want ^ got)


FVECS = {1: (37, 57, 22), 2: (40, 61, 23), 3: (16, 25, 11), 4: (30, 46, 18),
         5: (30, 47, 19), 6: (10, 17, 9), 7: (20, 33, 15), 8: (14, 23, 11),
         9: (11, 18, 9), 10: (6, 11, 7), 11: (10, 15, 7)}


def verify_origin_shifts():
    """Re-derive x_his = x_ours + v from Schmitt's recovered 2016 ops for
    every two-origin group used in this batch and assert agreement with the
    ORIGIN_V actually applied. Exact arithmetic (accepted xcheck machinery)."""
    import xcheck_schmitt_ops as X
    frozen, _, _ = X.load_frozen()
    splitters_all = X.parse_splitters()
    used = sorted({p["group"] for p in PAIRS} & set(base.ORIGIN_V))
    for n in used:
        his_ops = X.parse_schmitt_group(n)
        hs = splitters_all[n]
        ours = frozen[n]
        our_cosets = sorted(X.coset_set(ours["ops"], ours["cent"]))
        his_cosets = X.coset_set(his_ops, hs)
        v = X.try_basis(X.IDENT, our_cosets, ours["cent"], his_cosets, hs,
                        len({X.mod1(s) for s in hs}), ours["mult"],
                        check_lattice=True)
        assert v is not None, f"IT({n}): no pure-shift map recovered"
        got = tuple(F(x) % 1 for x in v)
        usedv = tuple(F(s) % 1 for s in base.ORIGIN_V[n])
        assert got == usedv, f"IT({n}): recovered v {got} != applied {usedv}"
    return used


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--pair", nargs="*", default=None,
                    help="pair ids to run (default: all 55)")
    args = ap.parse_args(argv)
    todo = [p for p in PAIRS if args.pair is None or p["pair"] in args.pair]

    enumerate_expected_pairs()
    shifted = verify_origin_shifts()
    print("origin shifts re-derived and verified for IT groups:", shifted)

    groups = orbit.load_groups()
    raw = json.load(open(STORE))
    store = raw["types"]
    for p in PAIRS:
        assert p["target"] in store, f"target {p['target']} not in store"
        assert tuple(store[p["target"]]["f_vector"]) == p["fvec"], \
            f"{p['pair']}: candidate f-vector != store f-vector"
        assert p["group"] != SIGHTED[p["cand"]], \
            f"{p['pair']}: sighted-group pair leaked into cross-group batch"
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
            print(f"{r['pair']} cand#{r['cand']:>2} IT({r['group']}) "
                  f"f={r['fvec']} -> {r['verdict']}"
                  f" [{r['secs']}s, orbit={r['orbit_n']}, stab={r['stab']},"
                  f" period={r['period']}]")
            results.append(r)
    finally:
        signal.signal(signal.SIGALRM, old)

    write_md(results)
    return 0


def write_md(results):
    L = []
    A = L.append
    A("# Schmitt printed-point collision screen, batch 2 — CROSS-GROUP pairs "
      "for the 11 G4-certified candidates (G5, 2026-08-30)")
    A("")
    A("Script: `schmitt_crossgroup_check.py` (this run: %d of 55 pair(s)); "
      "verdict machinery = `run_pair` IMPORTED from the accepted batch-1 "
      "`schmitt_collision_check.py`. Sources: Schmitt 2016 dissertation "
      "(`../references/Schmitt_2016_dissertation.pdf`), Sec. 2.2.5 per-group "
      "tables, printed pp. 119-150 (PDF page = printed + 5); frozen "
      "`spacegroups.json` (G1); `phase1_types.json` (Phase-1 ACCEPTED "
      "2026-08-29); queue per the cross-group scan in "
      "`../G5_DILIGENCE_2026-08-30.md` (re-derived at runtime from the "
      "accepted digitization and asserted equal)." % len(results))
    A("")
    A("**LANGUAGE (stated once for every verdict below): a DIFFERENT-TYPE "
      "verdict does NOT establish novelty, and surviving ALL printed "
      "representatives still does not.** Schmitt's tables print ONE "
      "representative generating point per (group, f-vector) from a grid "
      "SAMPLING; a candidate type absent at every printed point may still "
      "occur in his unprinted ~14TB data. Every surviving candidate remains "
      "only \"not matched against the catalog snapshot of 2026-08-30\". A "
      "SAME-TYPE verdict IS decisive: the candidate's combinatorial type "
      "appears in Schmitt 2016 at his printed point for another group "
      "(collision; reframe per kill criteria).")
    A("")
    A("## Transcription record (2026-08-30)")
    A("")
    A("All 55 printed generating points extracted from the archived PDF's "
      "text layer (`pdftotext -layout`, per-page tracked) and verified four "
      "ways before use: (a) parsed f-vector sequences of all 36 cubic tables "
      "identical to the accepted triage digitization (881 rows); (b) parsed "
      "f-vectors AND frequencies identical to the accepted independent "
      "re-key (`rekey_tables.json`, 386 rows, six groups); (c) parser "
      "reproduces all 21 batch-1 visually-transcribed rows (point, "
      "frequency, page) verbatim; (d) each of the 55 rows below verified "
      "against a fresh visual read of its rendered PDF page this session. "
      "IT(212)/IT(213) share one printed table; runs use the frozen IT(212) "
      "ops — `canon_code` identifies mirror images, so verdicts cover both "
      "enantiomorphs.")
    A("")
    A("Two-origin groups in this batch (IT 203, 222, 227, 228): printed "
      "points are origin choice 2, converted as x_ours = x_his - v (mod 1). "
      "v for 203/227/228 = the accepted batch-1 values; v for IT(222) = "
      "(3/4, 3/4, 3/4), NEW in this batch, machine-recovered from Schmitt's "
      "own 2016 ops (accepted `xcheck_schmitt_ops` machinery). "
      "`verify_origin_shifts()` re-derives ALL applied shifts at runtime and "
      "asserts agreement before any pair runs; independently, every pair "
      "must reproduce the printed f-vector (else FVEC-MISMATCH, the "
      "conversion-failure STOP).")
    A("")
    A("| pair | cand | IT | printed f-vector | printed generating point | "
      "freq | printed p. | shift v |")
    A("|---|---|---|---|---|---|---|---|")
    for r in results:
        v = base.ORIGIN_V.get(r["group"])
        A("| %s | #%d | %d | %s | (%s) | %s | %d | %s |"
          % (r["pair"], r["cand"], r["group"], str(r["fvec"]),
             ", ".join(r["point"]), r["freq"], r["page"],
             "(%s)" % ", ".join(v) if v else "—"))
    A("")
    A("## Per-pair verdicts")
    A("")
    A("| pair | cand | target type | IT | f-vector | orbit | stab | PERIOD | "
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
            note += " [point = stored sighting point]"
        A("| %s | #%d | `%s` | %d | %s | %s | %s | %s | %s | %s | **%s**%s "
          "| %s |"
          % (r["pair"], r["cand"], r["target"], r["group"], str(r["fvec"]),
             r["orbit_n"], r["stab"], r["period"], pv,
             r["got_aut"] if r["got_aut"] else "—", r["verdict"], note,
             r["secs"]))
    A("")
    A("## Per-candidate cross-group summary (this run)")
    A("")
    by_cand = {}
    for r in results:
        by_cand.setdefault(r["cand"], []).append(r)
    for num in sorted(CANDIDATES):
        cid = CANDIDATES[num]
        rs = by_cand.get(num)
        if num == 3:
            A("- #3 `%s` (IT(220), (16,25,11)): ZERO cross-group pairs — the "
              "f-vector is absent from the ENTIRE printed cubic survey "
              "(G5 doc); nothing to run. Cross-group status: SURVIVES-ALL "
              "vacuously (strongest Schmitt-side candidate; sampling caveat "
              "stands)." % cid)
            continue
        if rs is None:
            A("- #%d `%s`: not run in this invocation." % (num, cid))
            continue
        vs = [r["verdict"] for r in rs]
        if any(v == "SAME TYPE" for v in vs):
            hit = sorted(r["group"] for r in rs if r["verdict"] == "SAME TYPE")
            A("- #%d `%s`: **COLLIDED-AT IT%s** — the candidate's type IS "
              "Schmitt's printed cell there (%d/%d pairs SAME); reframe per "
              "kill criteria." % (num, cid, hit, len(hit), len(vs)))
        elif all(v == "DIFFERENT TYPE" for v in vs):
            A("- #%d `%s`: **SURVIVES-ALL** — all %d cross-group printed "
              "representatives are DIFFERENT types (snapshot language only)."
              % (num, cid, len(vs)))
        else:
            A("- #%d `%s`: mixed/incomplete: %s"
              % (num, cid, ", ".join(f"{r['pair']}:{r['verdict']}"
                                     for r in rs)))
    A("")
    A("## Notes")
    A("")
    A("- The pair queue (candidate f-vector x other printed group) is "
      "re-derived at runtime from `triage_phase1.SCHMITT_FVECTORS` and "
      "asserted equal to the hardcoded list — 55 pairs, matching the G5 "
      "doc's scan table (3+4+0+5+4+7+9+7+1+6+9).")
    A("- Cross-group rows in the 30 non-re-keyed tables rest on the "
      "single-pass digitization for their SEQUENCE placement; the specific "
      "rows used here were each verified visually this session (points were "
      "never digitized before this batch).")
    A("- Where a DIFFERENT verdict names a stored type, Schmitt's printed "
      "representative for that (group, f-vector) is itself a type our sweep "
      "also found — a same-f-two-types micro-fact, as in batch 1.")
    A("- Per-pair wall-clock cap %d s -> TIMEOUT-DEFERRED (recorded, never "
      "silent)." % TIMEOUT_S)
    A("- Certificate asserted per cell (run_pair, accepted): float/exact "
      "facet-count and p-vector agreement, 4*rho^2 <= D^2 exact cutoff, one "
      "canonical code across the whole orbit; printed f-vector reproduced "
      "(else FVEC-MISMATCH).")
    A("- Kill criteria live; none of these pairs can raise facet counts "
      "(max candidate F = 23, observed literature max 38).")
    A("")
    with open(OUT, "w") as fh:
        fh.write("\n".join(L))
    print("wrote", OUT)


if __name__ == "__main__":
    sys.exit(main())
