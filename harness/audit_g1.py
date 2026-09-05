#!/usr/bin/env python
"""audit_g1.py — INDEPENDENT checker for gate G1 (../ANCHORS.md).

Deliberately shares NO functions with spacegroup_ops.py: it parses
spacegroups.json cold, does its own Fraction parsing, its own matrix algebra,
and sources expected group orders from its own hardcoded tables (provenance
below), not from the generator or from the JSON's n_ops field.

Per group, verified in EXACT Fractions:
  A. schema sanity: R entries are ints, det(R) = +/-1, t strings are "n/d"
     with 0 <= n/d < 1 and d | 12; no duplicate ops.
  B. identity op present.
  C. closure: for every ordered pair (a, b), a∘b (composition mod 1) is in
     the set. Composition (R1,t1)∘(R2,t2) = (R1·R2, R1·t2 + t1 mod 1).
  D. inverses: every op has an inverse in the set (product = identity).
  E. order: op count equals |point group| x centering multiplicity for the
     recorded setting.

Expected-order provenance (hardcoded, NOT queried from spglib and NOT read
from the generator output):
  - Point-group order per ITA space-group number: standard assignment of the
    230 space groups to the 32 crystallographic point classes, International
    Tables for Crystallography Vol. A (contiguous number ranges, e.g. 195-199
    -> 23, 221-230 -> m-3m). Encoded as (last_number_in_range, order) below.
  - Centering multiplicity of the conventional cell: P=1, A/B/C/I=2, F=4;
    rhombohedral R groups: 3 on hexagonal axes (choice 'H'), 1 on rhombohedral
    axes. Standard crystallography (ITA Vol. A, ch. 2.1).
  - Conventional-cell op count = point-group order x centering multiplicity.

Also runs the G1 cubic smoke test (design doc §"sanity cross-check"): the
frozen P4_232 and other cubic groups must have conventional op counts
24/48/96/192 according to point class and centering. NOTE: the 24 ops in
SCI_OEIS_josehedron/data/josehedron_tables.json are a QUOTIENT action on cell
IDs, not raw space-group ops, and are intentionally NOT compared here.

Exit status: 0 iff every check passes; prints per-family summary and a final
ALL PASS / FAIL line.

Run:
  python3 audit_g1.py
"""

import json
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(HERE, "spacegroups.json")

# --- expected point-group order per ITA number: (range_end, order) ------------
# ITA Vol. A point-class ranges. Range start is the previous entry's end + 1.
PG_ORDER_RANGES = [
    (1, 1),     # 1        : 1
    (2, 2),     # 2        : -1
    (5, 2),     # 3-5      : 2
    (9, 2),     # 6-9      : m
    (15, 4),    # 10-15    : 2/m
    (24, 4),    # 16-24    : 222
    (46, 4),    # 25-46    : mm2
    (74, 8),    # 47-74    : mmm
    (80, 4),    # 75-80    : 4
    (82, 4),    # 81-82    : -4
    (88, 8),    # 83-88    : 4/m
    (98, 8),    # 89-98    : 422
    (110, 8),   # 99-110   : 4mm
    (122, 8),   # 111-122  : -42m
    (142, 16),  # 123-142  : 4/mmm
    (146, 3),   # 143-146  : 3
    (148, 6),   # 147-148  : -3
    (155, 6),   # 149-155  : 32
    (161, 6),   # 156-161  : 3m
    (167, 12),  # 162-167  : -3m
    (173, 6),   # 168-173  : 6
    (174, 6),   # 174      : -6
    (176, 12),  # 175-176  : 6/m
    (182, 12),  # 177-182  : 622
    (186, 12),  # 183-186  : 6mm
    (190, 12),  # 187-190  : -62m
    (194, 24),  # 191-194  : 6/mmm
    (199, 12),  # 195-199  : 23
    (206, 24),  # 200-206  : m-3
    (214, 24),  # 207-214  : 432
    (220, 24),  # 215-220  : -43m
    (230, 48),  # 221-230  : m-3m
]


def expected_pg_order(number):
    for end, order in PG_ORDER_RANGES:
        if number <= end:
            return order
    raise ValueError(number)


def expected_centering_mult(symbol, choice):
    letter = symbol[0]
    if letter == "R":
        return 3 if choice == "H" else 1
    return {"P": 1, "A": 2, "B": 2, "C": 2, "I": 2, "F": 4}[letter]


# --- exact op algebra (own implementation, not imported) ----------------------

def parse_frac(s):
    num, den = s.split("/")
    f = Fraction(int(num), int(den))
    if not (0 <= f < 1):
        raise ValueError(f"translation {s} not in [0,1)")
    if 12 % f.denominator != 0:
        raise ValueError(f"translation {s}: denominator does not divide 12")
    return f


def det3(R):
    return (
        R[0][0] * (R[1][1] * R[2][2] - R[1][2] * R[2][1])
        - R[0][1] * (R[1][0] * R[2][2] - R[1][2] * R[2][0])
        + R[0][2] * (R[1][0] * R[2][1] - R[1][1] * R[2][0])
    )


def matmul(A, B):
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def matvec_plus_mod1(R, v, w):
    """R·v + w, each component reduced mod 1 (exact Fractions)."""
    return tuple(
        (sum(Fraction(R[i][k]) * v[k] for k in range(3)) + w[i]) % 1
        for i in range(3)
    )


IDENTITY = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
ZERO_T = (Fraction(0), Fraction(0), Fraction(0))


def audit_group(g):
    """Return list of failure strings (empty = pass)."""
    failures = []
    number = g["number"]
    ops = []
    for i, op in enumerate(g["ops"]):
        R = tuple(tuple(op["R"][r][c] for c in range(3)) for r in range(3))
        for row in R:
            for x in row:
                if not isinstance(x, int):
                    failures.append(f"op {i}: non-integer rotation entry {x!r}")
        if det3(R) not in (1, -1):
            failures.append(f"op {i}: det(R) = {det3(R)}, not +/-1")
        try:
            t = tuple(parse_frac(s) for s in op["t"])
        except ValueError as e:
            failures.append(f"op {i}: {e}")
            t = ZERO_T
        ops.append((R, t))
    if failures:
        return failures  # schema broken; group checks would be noise

    keyset = {(R, t) for R, t in ops}
    if len(keyset) != len(ops):
        failures.append("duplicate ops")
    ident = (IDENTITY, ZERO_T)
    if ident not in keyset:
        failures.append("identity op missing")

    # closure + inverses over all ordered pairs
    for R1, t1 in ops:
        inv_found = False
        for R2, t2 in ops:
            comp = (matmul(R1, R2), matvec_plus_mod1(R1, t2, t1))
            if comp not in keyset:
                failures.append(
                    f"closure violated: ({R1},{t1}) ∘ ({R2},{t2}) not in set"
                )
            if comp == ident:
                inv_found = True
        if not inv_found:
            failures.append(f"no inverse for ({R1},{t1})")

    # order check against independent expectation
    exp = expected_pg_order(number) * expected_centering_mult(
        g["international_short"], g["setting_choice"]
    )
    if len(ops) != exp:
        failures.append(f"op count {len(ops)} != expected {exp}")

    # centering self-consistency: pure translations must number the multiplicity
    pure = sum(1 for R, t in ops if R == IDENTITY)
    if pure != expected_centering_mult(g["international_short"], g["setting_choice"]):
        failures.append(f"{pure} pure-translation ops vs expected centering mult")
    return failures


# --- cubic smoke test (design doc sanity cross-check) -------------------------
# Conventional-cell op counts for spot-checked cubic groups, from the same
# hardcoded tables: |point class| x centering. Includes the frozen P4_232.
CUBIC_SPOT_CHECKS = {
    195: ("P23", 12),
    208: ("P4_232", 24),
    209: ("F432", 96),
    211: ("I432", 48),
    221: ("Pm-3m", 48),
    225: ("Fm-3m", 192),
    227: ("Fd-3m", 192),
    229: ("Im-3m", 96),
    230: ("Ia-3d", 96),
}


def main():
    with open(JSON_PATH) as f:
        doc = json.load(f)
    groups = doc["groups"]

    all_failures = {}
    fam_stats = {}  # family -> [n_groups, n_ops, n_failed_groups]
    numbers_seen = set()
    for g in groups:
        numbers_seen.add(g["number"])
        fails = audit_group(g)
        fam = g["crystal_family"]
        st = fam_stats.setdefault(fam, [0, 0, 0])
        st[0] += 1
        st[1] += len(g["ops"])
        if fails:
            st[2] += 1
            all_failures[g["number"]] = fails

    if numbers_seen != set(range(1, 231)):
        all_failures["coverage"] = [
            f"missing group numbers: {sorted(set(range(1, 231)) - numbers_seen)}"
        ]

    print("audit_g1: independent exact check of spacegroups.json")
    print(f"  file: {JSON_PATH}")
    print(f"  groups: {len(groups)}   total ops: {sum(len(g['ops']) for g in groups)}")
    print("per-family summary (groups / ops / failed):")
    for fam in sorted(fam_stats):
        n, o, bad = fam_stats[fam]
        print(f"  {fam:<13} {n:>3} groups  {o:>5} ops  {bad} failed")

    print("cubic smoke test (conventional op counts 24/48/96/192 by centering):")
    by_number = {g["number"]: g for g in groups}
    smoke_ok = True
    for num, (name, exp) in sorted(CUBIC_SPOT_CHECKS.items()):
        got = len(by_number[num]["ops"]) if num in by_number else None
        ok = got == exp
        smoke_ok &= ok
        print(f"  #{num} {name:<8} expected {exp:>3}  got {got}  {'ok' if ok else 'MISMATCH'}")
    if not smoke_ok:
        all_failures.setdefault("smoke", []).append("cubic smoke test mismatch")
    print(
        "  (josehedron_tables.json 24 ops are a quotient action on cell IDs —"
        " intentionally not compared)"
    )

    if all_failures:
        print("FAILURES:")
        for k in sorted(all_failures, key=str):
            for msg in all_failures[k][:10]:
                print(f"  group {k}: {msg}")
        print("G1 AUDIT: FAIL")
        return 1
    print("G1 AUDIT: ALL PASS "
          "(identity, exact closure mod 1, inverses, order = |pointgroup| x centering, "
          "centering count — all 230 groups)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
