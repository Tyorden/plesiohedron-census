#!/usr/bin/env python
"""repro_crash.py — deterministic reproduction of the two PHASE2 crashes
(PHASE2_RESULT.md addendum, 2026-09-04): Schmitt printed rows at b = 3497/1000,
IT(80) I4_1 point (353/1413, 235/942, 0) [printed f = (32, 48, 18)] and
IT(110) I4_1cd point (1/4, 1411/5652, 0) [printed f = (24, 36, 14)], both
PERIOD 5652. Runs the sweep's own chain (sweep_phase2_tetragonal.evaluate,
kind = schmitt_printed) on exactly those (group, point, b) and reports the
outcome: before the order_cycle fix -> AssertionError "facet ordering failed
exact convexity check"; after -> f-vector vs printed. Exit 0 iff both rows
reproduce the printed f-vector; exit 1 otherwise.

Rows come from schmitt_tetragonal_rows_harvested.json (the harvested table
the run used), matched on (group, b_ratio, point)."""
import json
import os
import sys
import traceback
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sweep_phase2_tetragonal as S2                 # noqa: E402

CRASH_ROWS = [(80, ("353/1413", "235/942", "0"), "3497/1000"),
              (110, ("1/4", "1411/5652", "0"), "3497/1000")]


def main():
    rows = json.load(open(os.path.join(HERE, "schmitt_tetragonal_rows_harvested.json")))["rows"]
    ok_all = True
    for num, pt, b in CRASH_ROWS:
        printed = [r["f_vector"] for r in rows
                   if num in r["groups"] and r["b_ratio"] == b and tuple(r["point"]) == pt]
        assert len(printed) == 1, (num, pt, b, printed)
        printed = tuple(printed[0])
        p = tuple(F(x) for x in pt)
        print(f"IT({num}) point {pt} b={b}: printed f-vector {printed}")
        try:
            r = S2.evaluate(num, p, F(b), "schmitt_printed")
        except Exception as exc:
            print(f"  CRASH: {type(exc).__name__}: {exc}")
            traceback.print_exc(limit=3)
            ok_all = False
            continue
        print(f"  exact f-vector {r['fvec']}  p-vector {S2.pvec_compact(r['pvec'])}  "
              f"aut {r['aut']}  period {r['period']}  cutoff_D2 {r['cutoff_D2']}  "
              f"congruence_checked {r['congruence_checked']}  "
              f"match_printed={'YES' if tuple(r['fvec']) == printed else 'NO'}")
        ok_all &= tuple(r["fvec"]) == printed
    print("RESULT:", "both rows reproduce printed f-vectors" if ok_all else "FAIL")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
