#!/usr/bin/env python
"""schmitt_220_check.py — is Schmitt's IT(220) f=(12,22,12) cell the Josehedron?

Schmitt 2016 (references/Schmitt_2016_dissertation.pdf, ch. 2 table for
IT(220) = I-43d, printed p. 141): grid sampling of the reduced fundamental
domain found f-vector (12, 22, 12) at generating grid point
x = (143/1746, 289/3492, 295/3492), frequency 46 of 1,000,677,997 points.
The Josehedron (Bernhard 2025) lives in IT(220) (spglib on the generating
orbit: Wyckoff 12a, site symmetry -4, order 4 == G0 aut order) with the same
f-vector. f-vector match is NOT type match — this script decides it exactly:

  1. Recompute the Josehedron's canonical code from the G0 orbit (BASE/8).
  2. Orbit Schmitt's rational point under the frozen IT(220) coset list
     (spacegroups.json, G1-verified), scale exactly, run the same
     float-sweep -> exact-clip -> canonical-code pipeline.
  3. Compare codes (type-level, orientation-preserving planar isomorphism
     with mirror handled inside canon_code).

Caveats recorded up front: Schmitt's grid coordinates are stated "in the
coordinate system of the space group" (§2.2), i.e. conventional IT(220)
coordinates — same convention as spacegroups.json (spglib, IT setting).
IT(220) has a single origin choice. If the codes DIFFER, the f-vector
coincidence is just that, and the conclusion is only "type not identified";
if they MATCH, the Josehedron's combinatorial type appears (unnamed) in
Schmitt's 2016 survey data.

Run: python3 schmitt_220_check.py
Writes: SCHMITT_220_CHECK_RESULT.md. Exit 0 iff the pipeline ran clean
(either verdict); nonzero on internal inconsistency.
"""
import os
import sys
from fractions import Fraction as F

import orbit
from sweep_voronoi import sweep
from exact_cell import clip_cell
from canon_code import canonical_code

HERE = os.path.dirname(os.path.abspath(__file__))

# Josehedron generating orbit, VERBATIM from g0_regression.py (Table 4 minima)
JOSE_BASE = [(0, 2, 3), (0, 6, 1), (1, 0, 6), (2, 3, 0), (2, 5, 4), (3, 0, 2),
             (4, 2, 5), (4, 6, 7), (5, 4, 2), (6, 1, 0), (6, 7, 4), (7, 4, 6)]
JOSE_PERIOD = 8

# Schmitt's generating grid point for f=(12,22,12) in IT(220), verbatim
X = (F(143, 1746), F(289, 3492), F(295, 3492))


def cell_codes(pts, P, label):
    """Run float sweep + exact clip + canon code over every cell; return
    (codes, f_vectors, p_vectors, degen_flags)."""
    cells_f = sweep(pts, P, W=2)
    cells_e = [clip_cell(c, pts, P) for c in pts]
    for e, f in zip(cells_e, cells_f):
        assert e['facet_count'] == f['facet_count'], \
            f"{label}: float/exact facet count disagree"
        assert e['p_vector'] == f['p_vector'], \
            f"{label}: float/exact p-vector disagree"
        assert 4 * e['rho2'] <= e['cutoff_D']**2, \
            f"{label}: provable cutoff violated"
    codes = [canonical_code(e['facet_cycles']) for e in cells_e]
    fvecs = sorted(set((e['n_vertices'], e['n_edges'], e['facet_count'])
                       if 'n_edges' in e else
                       (e['n_vertices'],
                        sum(len(c) for c in e['facet_cycles']) // 2,
                        e['facet_count'])
                       for e in cells_e))
    pvecs = sorted(set(e['p_vector'] for e in cells_e))
    return codes, fvecs, pvecs, cells_e


def main():
    lines = []

    def say(s):
        print(s)
        lines.append(s)

    # --- 1. Josehedron reference code (recomputed, not read from a file)
    fracs = [tuple(F(x, JOSE_PERIOD) for x in p) for p in JOSE_BASE]
    jpts, jP = orbit.scale_orbit(fracs)
    jcodes, jf, jp, _ = cell_codes(jpts, jP, "josehedron")
    jset = set(cd for cd, _ in jcodes)
    assert len(jset) == 1, "josehedron orbit produced >1 code (regression!)"
    jcode, jaut = jcodes[0]
    say(f"Josehedron reference: f-vectors {jf}, p-vectors {jp}, "
        f"aut={jaut}, code_len={len(jcode)}")

    # --- 2. Schmitt point orbit under frozen IT(220)
    groups = orbit.load_groups()
    entry = groups[220]
    orb = orbit.orbit(entry, X)
    say(f"Schmitt point orbit under IT(220): n_conventional="
        f"{orb['n_conventional']}, general_position={orb['general_position']}, "
        f"stabilizer_order={orb['stabilizer_order']}")
    spts, sP = orbit.scale_orbit(orb['points'])
    say(f"scaled PERIOD={sP}, {len(spts)} points/conventional cell")

    scodes, sf, sp, _ = cell_codes(spts, sP, "schmitt220")
    sset = set(cd for cd, _ in scodes)
    assert len(sset) == 1, "schmitt orbit produced >1 code (cells congruent?!)"
    scode, saut = scodes[0]
    say(f"Schmitt cell: f-vectors {sf}, p-vectors {sp}, "
        f"aut={saut}, code_len={len(scode)}")

    # --- 3. Verdict
    match = (scode == jcode)
    say("")
    say("VERDICT: " + (
        "MATCH — the cell at Schmitt's IT(220) grid point is combinatorially "
        "THE JOSEHEDRON. Its type appears (unnamed) in Schmitt's 2016 survey "
        "data, nine years before Bernhard 2025."
        if match else
        "NO MATCH — same f-vector, different combinatorial type. The "
        "Josehedron's type is NOT identified in Schmitt's in-text IT(220) "
        "table at this point; absence remains evidence, not proof."))

    with open(os.path.join(HERE, "SCHMITT_220_CHECK_RESULT.md"), "w") as fh:
        fh.write("# Schmitt IT(220) f=(12,22,12) vs Josehedron — exact type "
                 "comparison (2026-08-28)\n\n")
        fh.write("Pipeline: orbit.py (frozen G1 spacegroups.json) -> "
                 "sweep_voronoi (float, W=2) -> exact_cell (Fractions) -> "
                 "canon_code. Source table: Schmitt 2016 printed p. 141 "
                 "(references/Schmitt_2016_dissertation.pdf), point "
                 "x=(143/1746, 289/3492, 295/3492), frequency 46.\n\n")
        fh.write("```\n" + "\n".join(lines) + "\n```\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
