#!/usr/bin/env python3
"""
Type-level check raised by RECONCILIATION.md: Schmitt 2016 prints f = (16,25,11)
(the Satchelhedron's f-vector) in TWO tetragonal tables, IT(134) P4_2/nnm and
IT(141) I4_1/amd, both ITA two-origin groups whose printed rows the store never
absorbed (they were quarantined in pass P2 and reproduced only by the read-only
origin check). This script pushes those two printed points, converted to our
origin-choice-1 setting with the shifts recovered in
harness/phase2_schmitt_origin_check.json (every shift that reproduced ALL rows
of the group is run; all must agree), through the ACCEPTED phase-2 exact chain
(harness/sweep_phase2_tetragonal.evaluate, read-only import) and compares the
canonical code with the Satchelhedron's stored code and with every code in the
phase-2 store.

Run (from anywhere):
  python3 \
    <repo>/catalog/check_satchelhedron_tetragonal_rows.py
Writes: SATCHELHEDRON_TETRAGONAL_ROWS.md (this folder). Exit 0 iff both rows
reproduce the printed f-vector under every shift and all shifts agree on the code.
Wording: a DIFFERENT verdict is not a novelty claim; a SAME verdict would be a
type-level collision (first-realization reframe per the kill criteria).
"""
import ast
import gzip
import hashlib
import json
import os
import re
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
HARNESS = os.path.join(ROOT, "harness")
sys.path.insert(0, HARNESS)
import sweep_phase2_tetragonal as S2   # noqa: E402  (accepted module, read-only)

SATCHEL = "8cf50403cf88c455"


def main():
    p2 = json.loads(gzip.open(os.path.join(HARNESS, "phase2_types.json.gz"), "rb").read())
    want = re.search(r"sha256\s+([0-9a-f]{64})", open(os.path.join(HARNESS, "phase2_types.SHA256SUMS")).read()).group(1)
    assert hashlib.sha256(gzip.open(os.path.join(HARNESS, "phase2_types.json.gz"), "rb").read()).hexdigest() == want
    code2id = {v["canon_code"]: k for k, v in p2["types"].items()}
    sat_code = p2["types"][SATCHEL]["canon_code"]
    tables = json.load(open(os.path.join(HARNESS, "schmitt_tetragonal_tables.json")))
    origin = json.load(open(os.path.join(HARNESS, "phase2_schmitt_origin_check.json")))["two_origin"]
    rows = []
    for key, blk in tables.items():
        if key == "_meta":
            continue
        for r in blk["rows"]:
            if r["f"] == [16, 25, 11]:
                for g in blk["groups"]:
                    rows.append((g, blk["symbols"][str(g)], r))
    assert [g for g, _, _ in rows] == [134, 141], rows
    out = ["# Satchelhedron vs Schmitt's two tetragonal (16,25,11) rows - type-level check\n",
           "Raised by RECONCILIATION.md. Accepted phase-2 exact chain (`harness/sweep_phase2_tetragonal.evaluate`: exact orbit, Gram metric, float proposal, exact clip with the 4*rho^2 <= D^2 certificate asserted, orbit congruence, canonical code); origin-choice-2 -> origin-choice-1 shifts from `harness/phase2_schmitt_origin_check.json` (all shifts that reproduced every printed row of the group are run and must agree).\n",
           f"Satchelhedron stored code sha1[:16] = `{SATCHEL}`, f=(16,25,11), p=3^2 4^1 5^8, aut 4.\n",
           "| IT | symbol | printed c/a | printed point (his coords) | shift | our point | exact f | p-vector | aut | code == Satchelhedron? | stored id (any) | secs |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    ok = True
    verdicts = []
    all_codes = set()
    for g, sym, r in rows:
        info = origin[str(g)]
        shifts = [tuple(F(x) for x in ast.literal_eval(s)) for s in info["shifts_all_rows"]]
        assert tuple(F(x) for x in info["best_shift"]) in shifts
        codes = set()
        for s in shifts:
            p = tuple(F(x) + y for x, y in zip(r["pt"], s))
            res = S2.evaluate(g, p, F(r["b"]), "catalog_check")
            f_ok = list(res["fvec"]) == r["f"]
            ok &= f_ok
            codes.add(res["code_str"])
            all_codes.add(res["code_str"])
            same = res["code_str"] == sat_code
            sid = code2id.get(res["code_str"], "not stored")
            out.append(f"| {g} | {sym} | {r['b']} | ({','.join(r['pt'])}) | +({','.join(str(x) for x in s)}) | ({','.join(str(x) for x in p)}) | {tuple(res['fvec'])}{'' if f_ok else ' MISMATCH'} | {S2.pvec_compact(res['pvec'])} | {res['aut']} | {'SAME TYPE' if same else 'DIFFERENT'} | {sid} | {res['seconds']:.1f} |")
            verdicts.append((g, same, sid, f_ok))
        if len(codes) != 1:
            ok = False
            out.append(f"| {g} | | | | ALL SHIFTS | | | | | SHIFTS DISAGREE ({len(codes)} codes) | | |")
    out.append("")
    if all(v[3] for v in verdicts):
        n_same = sum(1 for v in verdicts if v[1])
        n_types = len(all_codes | {sat_code})
        if n_same == 0:
            out.append(f"**Verdict: both printed (16,25,11) cells reproduce their printed f-vector under every documented shift and are DIFFERENT combinatorial types from the Satchelhedron** (and, per the last column, whether either is any stored type). "
                       f"This is not a novelty claim: his tables print one representative per (group, f-vector) from a grid sampling; the Satchelhedron remains 'not matched against the records checked as of 2026-09-04'. New micro-fact of the Josehedron/Schmitt-220 class: f = (16,25,11) is realised by at least {n_types} distinct combinatorial types across the survey (the Satchelhedron plus one per printed row; codes pairwise distinct).\n")
        else:
            out.append(f"**Verdict: {n_same} printed row(s) give the SAME canonical code as the Satchelhedron: TYPE-LEVEL COLLISION.** Per the kill criteria the Satchelhedron would reframe to a first-realization-in-IT(220) statement; every public wording must change. Report to the main session before anything else.\n")
    else:
        out.append("**Verdict: at least one row did not reproduce its printed f-vector; no conclusion (check the shift conventions).**\n")
    out.append("Provenance: script `catalog/check_satchelhedron_tetragonal_rows.py`, exact arithmetic throughout, deterministic; main-session re-run required before acceptance. Computed with the assistance of Claude (Anthropic).\n")
    open(os.path.join(HERE, "SATCHELHEDRON_TETRAGONAL_ROWS.md"), "w").write("\n".join(out))
    print("\n".join(out))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
