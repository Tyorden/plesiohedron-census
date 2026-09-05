#!/usr/bin/env python
"""g2_seed_catalog.py — SEEDED CATALOG of the 5 parallelohedra (ANCHORS G2,
design doc §4 "Catalog comparison": codes computed from published vertex data,
never by transcribing face counts).

INDEPENDENCE REQUIREMENT (same spirit as G1's no-shared-code audit): this
builder must NOT import sweep_voronoi or exact_cell. Face structure is built
here by an EXACT convex-hull-free enumeration over the published integer
vertices (all-integer arithmetic; scipy is not used at all):

  For every unordered vertex triple, form the plane through it (integer normal
  = cross product, gcd-normalized, oriented outward w.r.t. the interior point
  0 — all five solids below are centered at the origin). A plane is a FACE
  plane iff every vertex lies exactly on or strictly inside it (integer sign
  test). The face's vertex set = the on-plane vertices. Verified exactly:
  every vertex lies on >= 3 face planes (genuine vertex), every face cycle is
  strictly convex and CCW as seen from outside (integer cross-dot > 0 for all
  consecutive triples — float atan2 only PROPOSES the cyclic order, the exact
  test DECIDES, house invariant), every edge lies in exactly 2 faces (asserted
  again structurally by canon_code.rotation_system).

The only shared module is canon_code (the type identity function itself —
catalog codes must be comparable to pipeline codes by construction; canon_code
has its own independent unit suite, test_canon.py).

PUBLISHED VERTEX DATA (exact integer coordinates; sources in-line):

  cube                  (+-1,+-1,+-1)                       f=(8,12,6)
                        [standard; e.g. Coxeter, Regular Polytopes, Table I]
  hexagonal prism       regular prism (+-1,0,+-1),(+-1/2,+-sqrt3/2,+-1) taken
                        through the exact rational AFFINE image diag(2, 4/sqrt3, 1):
                        (+-2,0,+-1),(+-1,+-2,+-1)           f=(12,18,8)
                        [combinatorial type is affine-invariant, so the rational
                        image carries the same map as the regular prism]
  rhombic dodecahedron  cube vertices (+-1,+-1,+-1) plus octahedron vertices
                        (+-2,0,0),(0,+-2,0),(0,0,+-2)       f=(14,24,12)
                        [standard; Coxeter; = FCC lattice Voronoi cell]
  elongated dodecahedron  standard elongation of the rhombic dodecahedron along
                        the 4-fold z-axis by 2 half-unit translates: the z>0 /
                        z<0 vertices shift by +-1, the four equatorial vertices
                        (+-2,0,0),(0,+-2,0) split into pairs at z=+-1:
                        (0,0,+-3),(+-1,+-1,+-2),(+-2,0,+-1),(0,+-2,+-1)
                                                            f=(18,28,12)
                        [Fedorov's elongated dodecahedron; the 4 equatorial
                        rhombi x+-y=+-2 become planar hexagons — verified
                        exactly below, not assumed]
  truncated octahedron  all permutations of (0,+-1,+-2)     f=(24,36,14)
                        [standard; Coxeter; = BCC lattice Voronoi cell]

Expected combinatorial automorphism orders (map automorphisms, reflections
included): cube 48, hexagonal prism 24 (D6h), rhombic dodecahedron 48,
elongated dodecahedron 16 (D4h), truncated octahedron 48. Asserted.

Run:
  python3 g2_seed_catalog.py
Writes: seed_catalog.json. Exit 0 iff all assertions pass.
"""
import itertools
import json
import math
import os
import sys
from math import gcd

from canon_code import canonical_code

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "seed_catalog.json")


def _sub(a, b): return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
def _dot(a, b): return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
def _cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


# ---- published vertex data (integers; documented in the module docstring) ----

def _cube():
    return [(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)]


def _hexagonal_prism():
    hexagon = [(2, 0), (1, 2), (-1, 2), (-2, 0), (-1, -2), (1, -2)]
    return [(x, y, z) for (x, y) in hexagon for z in (-1, 1)]


def _rhombic_dodecahedron():
    verts = _cube()
    for i in range(3):
        for s in (-2, 2):
            v = [0, 0, 0]; v[i] = s
            verts.append(tuple(v))
    return verts


def _elongated_dodecahedron():
    verts = [(0, 0, 3), (0, 0, -3)]
    verts += [(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-2, 2)]
    verts += [(x, 0, z) for x in (-2, 2) for z in (-1, 1)]
    verts += [(0, y, z) for y in (-2, 2) for z in (-1, 1)]
    return verts


def _truncated_octahedron():
    verts = set()
    for p in itertools.permutations((0, 1, 2)):
        for signs in itertools.product((-1, 1), repeat=3):
            # all sign choices on all coordinates; set() dedupes the 0*s copies
            verts.add(tuple(c * s for c, s in zip(p, signs)))
    return sorted(verts)


SOLIDS = [
    # name, vertex builder, published f-vector (V, E, F), expected aut order
    ("cube", _cube, (8, 12, 6), 48),
    ("hexagonal_prism", _hexagonal_prism, (12, 18, 8), 24),
    ("rhombic_dodecahedron", _rhombic_dodecahedron, (14, 24, 12), 48),
    ("elongated_dodecahedron", _elongated_dodecahedron, (18, 28, 12), 16),
    ("truncated_octahedron", _truncated_octahedron, (24, 36, 14), 48),
]


# ---- exact hull-free face enumeration -----------------------------------

def _normalize(a, b):
    g = gcd(gcd(abs(a[0]), abs(a[1])), gcd(abs(a[2]), abs(b)))
    if g > 1:
        a = (a[0]//g, a[1]//g, a[2]//g); b = b // g
    return a, b


def faces_exact(verts):
    """Exact face planes + on-vertex sets of conv(verts), origin interior.

    Returns [(outward_normal, offset, on_index_tuple)]. All-integer."""
    n = len(verts)
    faces = {}
    for i, j, k in itertools.combinations(range(n), 3):
        a = _cross(_sub(verts[j], verts[i]), _sub(verts[k], verts[i]))
        if a == (0, 0, 0):
            continue                        # collinear triple
        b = _dot(a, verts[i])
        if b < 0:
            a, b = (-a[0], -a[1], -a[2]), -b
        if b == 0:
            continue                        # plane through the interior point 0
        a, b = _normalize(a, b)
        if (a, b) in faces:
            continue
        vals = [_dot(a, v) - b for v in verts]
        if all(x <= 0 for x in vals):       # supporting plane => face
            faces[(a, b)] = tuple(m for m, x in enumerate(vals) if x == 0)
    out = [(a, b, on) for (a, b), on in sorted(faces.items())]
    # every vertex must be a genuine vertex: on >= 3 face planes
    inc = [0] * n
    for _, _, on in out:
        for m in on:
            inc[m] += 1
    assert all(c >= 3 for c in inc), f"non-vertex point in vertex data: {inc}"
    return out


def cycle_ccw(pts, normal):
    """Cyclic CCW-from-outside order of exact coplanar points. Float atan2
    PROPOSES; the integer strict-convexity cross-dot test DECIDES."""
    c = [sum(p[k] for p in pts) / len(pts) for k in range(3)]   # float, proposal
    u = _sub(pts[1], pts[0])
    w = _cross(normal, u)
    idx = sorted(range(len(pts)),
                 key=lambda m: math.atan2(_dot(_sub(pts[m], (0, 0, 0)), w) - _dot(c, w),
                                          _dot(_sub(pts[m], (0, 0, 0)), u) - _dot(c, u)))
    poly = [pts[m] for m in idx]
    for t in range(len(poly)):
        a, b, d = poly[t], poly[(t+1) % len(poly)], poly[(t+2) % len(poly)]
        assert _dot(_cross(_sub(b, a), _sub(d, b)), normal) > 0, \
            "exact convexity/CCW check failed on a catalog face"
    return poly


def build_solid(name, verts, fvec_pub):
    faces = faces_exact(verts)
    cycles = []
    for a, b, on in faces:
        pts = [verts[m] for m in on]
        poly = cycle_ccw(pts, a)
        vmap = {v: m for m, v in zip(on, pts)}
        cycles.append([vmap[p] for p in poly])
    V = len(verts)
    E2 = sum(len(c) for c in cycles)
    assert E2 % 2 == 0
    E, F = E2 // 2, len(cycles)
    assert (V, E, F) == tuple(fvec_pub), \
        f"{name}: computed f-vector {(V, E, F)} != published {fvec_pub}"
    assert V - E + F == 2, f"{name}: Euler failed"
    p_vector = tuple(sorted(len(c) for c in cycles))
    code, aut = canonical_code(cycles)      # rotation_system re-asserts
    return {                                # each dart in exactly one face etc.
        "name": name,
        "f_vector": [V, E, F],
        "p_vector": list(p_vector),
        "canon_code": code.decode("ascii"),
        "aut_order": aut,
    }


def main():
    entries = []
    ok_all = True
    for name, builder, fvec, aut_exp in SOLIDS:
        e = build_solid(name, builder(), fvec)
        ok = e["aut_order"] == aut_exp
        ok_all = ok_all and ok
        print(("PASS  " if ok else "FAIL  ")
              + f"{name}: f={tuple(e['f_vector'])} p={tuple(e['p_vector'])} "
                f"aut={e['aut_order']} (expected {aut_exp}) "
                f"code_len={len(e['canon_code'])}")
        entries.append(e)
    distinct = len({e["canon_code"] for e in entries}) == len(entries)
    print(("PASS  " if distinct else "FAIL  ")
          + "all 5 canonical codes pairwise distinct")
    ok_all = ok_all and distinct
    json.dump({"comment": "G2 seeded catalog: 5 parallelohedra from published "
                          "vertex data via exact hull-free face enumeration "
                          "(g2_seed_catalog.py; no sweep_voronoi/exact_cell "
                          "import — independence requirement)",
               "entries": entries},
              open(OUT, "w"), indent=1)
    print(("seed_catalog.json written: 5 entries. "
           if ok_all else "CATALOG BUILD FAILED. ") + OUT)
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
