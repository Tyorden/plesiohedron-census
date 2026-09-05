#!/usr/bin/env python
"""test_canon.py — required unit tests for canon_code.py (design §1.4, §6.6).

  (a) 20 random vertex relabelings (plus random cycle rotations and face-list
      shuffles) of the same polyhedron canonicalize identically;
  (b) mirror images (all cycles reversed) canonicalize identically — the
      orientation sweep works;
  (c) cube vs octahedron give different codes.
Extras: known automorphism orders (cube/octahedron/rhombic dodecahedron = 48,
tetrahedron = 24) and a non-simple-vertex case (rhombic dodecahedron from the
exact clipper) to exercise degree-4 rotation cycles.

Run: python3 test_canon.py
"""
import random
from fractions import Fraction as F

from canon_code import canonical_code
from exact_cell import clip_cell, order_cycle


def relabeled(cycles, perm, rng):
    """Apply a vertex relabeling + random cycle rotations + face shuffle.
    None of these changes the map, so the canonical code must not change."""
    out = []
    for cyc in cycles:
        c = [perm[v] for v in cyc]
        r = rng.randrange(len(c))
        out.append(c[r:] + c[:r])
    rng.shuffle(out)
    return out


def mirrored(cycles):
    return [list(reversed(c)) for c in cycles]


def octahedron_cycles():
    """Octahedron +-e_i; 8 triangular faces oriented CCW-from-outside via the
    exact order_cycle (outward normal = sign vector of the octant)."""
    vs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    vid = {v: i for i, v in enumerate(vs)}
    cycles = []
    for sx in (1, -1):
        for sy in (1, -1):
            for sz in (1, -1):
                tri = [(sx, 0, 0), (0, sy, 0), (0, 0, sz)]
                pts = [tuple(F(x) for x in p) for p in tri]
                poly = order_cycle(pts, (sx, sy, sz))
                cycles.append([vid[tuple(int(x) for x in p)] for p in poly])
    return cycles


def run():
    rng = random.Random(20260828)
    results = []

    # Reference solids: cube and rhombic dodecahedron via the exact clipper
    # (integration path: clip -> cycles -> canon), octahedron hand-built.
    cube = clip_cell((0, 0, 0), [(0, 0, 0)], 2)['facet_cycles']
    rhomb = clip_cell((0, 0, 0),
                      [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)], 2)['facet_cycles']
    octa = octahedron_cycles()

    cube_code, cube_aut = canonical_code(cube)
    octa_code, octa_aut = canonical_code(octa)
    rhomb_code, rhomb_aut = canonical_code(rhomb)
    tet_code, tet_aut = canonical_code([[0, 1, 2], [0, 2, 3], [0, 3, 1], [1, 3, 2]])

    # (a) 20 random relabelings, per solid class (cube, octa, rhombic dodeca).
    for name, cyc, code, aut in [("cube", cube, cube_code, cube_aut),
                                 ("octahedron", octa, octa_code, octa_aut),
                                 ("rhombic-dodeca", rhomb, rhomb_code, rhomb_aut)]:
        nv = len({v for c in cyc for v in c})
        ok = True
        for _ in range(20):
            perm = list(range(nv))
            rng.shuffle(perm)
            c2, a2 = canonical_code(relabeled(cyc, perm, rng))
            ok = ok and c2 == code and a2 == aut
        results.append((f"(a) 20 random relabelings invariant [{name}]", ok))

    # (b) mirror images canonicalize identically.
    results.append(("(b) mirror image invariant [cube]",
                    canonical_code(mirrored(cube))[0] == cube_code))
    results.append(("(b) mirror image invariant [octahedron]",
                    canonical_code(mirrored(octa))[0] == octa_code))
    results.append(("(b) mirror image invariant [rhombic-dodeca]",
                    canonical_code(mirrored(rhomb))[0] == rhomb_code))

    # (c) cube vs octahedron differ (and all four solids pairwise distinct).
    codes = [cube_code, octa_code, rhomb_code, tet_code]
    results.append(("(c) cube != octahedron", cube_code != octa_code))
    results.append(("(c) all four reference codes pairwise distinct",
                    len(set(codes)) == 4))

    # Extras: known automorphism orders (incl. reflections).
    results.append(("aut orders: cube 48 / octa 48 / rhombic 48 / tet 24",
                    (cube_aut, octa_aut, rhomb_aut, tet_aut) == (48, 48, 48, 24)))

    allpass = True
    for name, ok in results:
        print(("PASS  " if ok else "FAIL  ") + name)
        allpass = allpass and ok
    print("test_canon:", "ALL PASS" if allpass else "FAILED")
    return allpass


if __name__ == "__main__":
    import sys
    sys.exit(0 if run() else 1)
