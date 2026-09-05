#!/usr/bin/env python
"""spacegroup_ops.py — freeze all 230 space groups into spacegroups.json.

Design spec: ../HARNESS_DESIGN_FABLE5_2026-08-27.md §1.1.
Acceptance gate: ../ANCHORS.md G1 (audited independently by audit_g1.py).

Source: spglib.get_symmetry_from_database(hall_number). For each ITA space-group
number 1..230 we take the SMALLEST hall number (spglib hall numbers 1..530) as the
single frozen setting. That convention yields, uniformly:
  - triclinic/orthorhombic/tetragonal/hexagonal/cubic: standard 'abc' setting,
    origin choice 1 where two origins exist (choice field records it);
  - monoclinic: unique axis b, cell choice 1 (choice 'b1' or 'b');
  - rhombohedral (R) groups: HEXAGONAL axes (choice 'H'), i.e. the triple
    conventional hex cell with 3 centering vectors.
The chosen hall number, hall symbol, and choice string are recorded per group so
downstream consumers know exactly which setting was frozen.

House invariant: floats propose, Fractions decide. spglib returns translations as
floats that must be exact multiples of 1/12; each is rationalized to
Fraction(round(12*t), 12) and HARD-FAILS unless the float is within 1e-9 of the
rationalization. Translations are stored as reduced "num/den" strings with den | 12.

Trust-but-verify (generator-side; the *independent* check is audit_g1.py, which
shares no code with this file): after rationalizing, each group's op set is
checked in exact Fractions for identity / closure under composition mod 1 /
inverses before being written.

Run:
  python3 spacegroup_ops.py
Writes: spacegroups.json (in this directory).
"""

import json
import os
import sys
from fractions import Fraction

import spglib

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(HERE, "spacegroups.json")

TOL = 1e-9  # max allowed |float - rationalized| ; hard-fail beyond this
N_HALL = 530  # spglib hall numbers 1..530
N_GROUPS = 230


def crystal_system(number: int) -> str:
    """ITA space-group number -> crystal system (standard ranges, ITA Vol A)."""
    if number <= 2:
        return "triclinic"
    if number <= 15:
        return "monoclinic"
    if number <= 74:
        return "orthorhombic"
    if number <= 142:
        return "tetragonal"
    if number <= 167:
        return "trigonal"
    if number <= 194:
        return "hexagonal"
    return "cubic"


def crystal_family(number: int) -> str:
    """Crystal family: trigonal + hexagonal systems merge into 'hexagonal'."""
    sys_ = crystal_system(number)
    return "hexagonal" if sys_ in ("trigonal", "hexagonal") else sys_


def rationalize(x: float) -> Fraction:
    """Float translation -> exact Fraction with denominator dividing 12.
    Hard-fail if the float is not within TOL of n/12 for integer n."""
    n = round(12.0 * x)
    if abs(x - n / 12.0) > TOL:
        raise SystemExit(
            f"RATIONALIZATION FAILURE: translation {x!r} is not within {TOL} "
            f"of {n}/12 — STOP (per harness rules, do not approximate)."
        )
    fr = Fraction(n % 12, 12)  # reduce mod 1 into [0,1); auto-reduces, den | 12
    assert 0 <= fr < 1 and 12 % fr.denominator == 0
    return fr


def frac_str(fr: Fraction) -> str:
    return f"{fr.numerator}/{fr.denominator}"


IDENT = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def op_key(R, t):
    """Hashable exact key for (R, t mod 1)."""
    return (tuple(tuple(row) for row in R), tuple(t))


def compose(R1, t1, R2, t2):
    """(R1,t1) ∘ (R2,t2) = (R1·R2, R1·t2 + t1) with t reduced mod 1 (exact)."""
    R = tuple(
        tuple(sum(R1[i][k] * R2[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )
    t = tuple(
        (sum(Fraction(R1[i][k]) * t2[k] for k in range(3)) + t1[i]) % 1
        for i in range(3)
    )
    return R, t


def verify_group_exact(ops):
    """Generator-side sanity: identity present, closed, inverses. Exact Fractions."""
    keys = {op_key(R, t) for R, t in ops}
    assert len(keys) == len(ops), "duplicate ops after mod-1 reduction"
    ident_key = (IDENT, (Fraction(0), Fraction(0), Fraction(0)))
    assert ident_key in keys, "identity missing"
    for R1, t1 in ops:
        has_inverse = False
        for R2, t2 in ops:
            Rc, tc = compose(R1, t1, R2, t2)
            assert op_key(Rc, tc) in keys, "closure violated"
            if op_key(Rc, tc) == ident_key:
                has_inverse = True
        assert has_inverse, "inverse missing"


def main():
    # Pick smallest hall number per ITA number (see module docstring for what
    # convention that fixes).
    chosen = {}  # number -> hall_number
    for hall in range(1, N_HALL + 1):
        sgt = spglib.get_spacegroup_type(hall)
        if sgt.number not in chosen:
            chosen[sgt.number] = hall
    assert sorted(chosen) == list(range(1, N_GROUPS + 1)), "not all 230 groups found"

    groups = []
    fam_counts = {}
    for number in range(1, N_GROUPS + 1):
        hall = chosen[number]
        sgt = spglib.get_spacegroup_type(hall)
        sym = spglib.get_symmetry_from_database(hall)
        rotations = sym["rotations"]
        translations = sym["translations"]

        ops = []
        for Rm, tv in zip(rotations, translations):
            R = tuple(tuple(int(x) for x in row) for row in Rm)
            t = tuple(rationalize(float(x)) for x in tv)
            ops.append((R, t))

        # generator-side exact sanity (independent re-check lives in audit_g1.py)
        verify_group_exact(ops)

        # centering info: letter from the international short symbol; vectors are
        # the translations of ops whose rotation part is the identity.
        letter = sgt.international_short[0]
        assert letter in "PABCIFR", f"unexpected centering letter {letter}"
        cent_vectors = sorted(
            tuple(frac_str(x) for x in t) for R, t in ops if R == IDENT
        )
        if letter == "R":
            mult = 3 if sgt.choice == "H" else 1
        else:
            mult = {"P": 1, "A": 2, "B": 2, "C": 2, "I": 2, "F": 4}[letter]
        assert len(cent_vectors) == mult, (
            f"group {number}: centering multiplicity mismatch "
            f"({len(cent_vectors)} pure translations vs expected {mult})"
        )

        fam = crystal_family(number)
        fam_counts[fam] = fam_counts.get(fam, 0) + 1

        groups.append(
            {
                "number": number,
                "hall_number": hall,
                "hall_symbol": sgt.hall_symbol,
                "setting_choice": sgt.choice,
                "international_short": sgt.international_short,
                "international_full": sgt.international_full,
                "pointgroup_international": sgt.pointgroup_international,
                "crystal_system": crystal_system(number),
                "crystal_family": fam,
                "centering": {
                    "letter": letter,
                    "multiplicity": mult,
                    "vectors": cent_vectors,
                },
                "n_ops": len(ops),
                "ops": [
                    {
                        "R": [list(row) for row in R],
                        "t": [frac_str(x) for x in t],
                    }
                    for R, t in ops
                ],
            }
        )

    doc = {
        "generated_by": "spacegroup_ops.py",
        "spglib_version": spglib.__version__,
        "setting_convention": (
            "smallest spglib hall number per ITA number: origin choice 1 where "
            "two origins exist; monoclinic unique axis b cell choice 1; "
            "rhombohedral groups on hexagonal (H) axes"
        ),
        "translation_denominator_bound": 12,
        "n_groups": len(groups),
        "crystal_family_counts": fam_counts,
        "groups": groups,
    }
    with open(OUT_PATH, "w") as f:
        json.dump(doc, f, indent=1)
    total_ops = sum(g["n_ops"] for g in groups)
    print(f"wrote {OUT_PATH}")
    print(f"spglib {spglib.__version__}; {len(groups)} groups; {total_ops} ops total")
    for fam, c in sorted(fam_counts.items()):
        print(f"  {fam}: {c} groups")


if __name__ == "__main__":
    sys.exit(main())
