"""Shared exact helpers for the round-2 computations (2026-09-03).
Reuses the round-1 helpers (common.py: exact_cell_at, cell_volume, rederive,
frozen GROUPS / TYPES) unchanged, and re-implements the exact smallest-
enclosing-sphere routine of c4_roundness.py (that file has no main guard, so
it is not imported).  All arithmetic is fractions.Fraction; floats appear only
in the final percentages."""
import os, sys, math, itertools
from fractions import Fraction as F
HERE = os.path.dirname(os.path.abspath(__file__))
R1 = os.path.join(HERE, "..", "round1_computations")
sys.path.insert(0, R1)
from common import *  # noqa: F401,F403  (HARNESS, GROUPS, TYPES, CELLS, exact_cell_at, cell_volume, rederive, det3, frac_str, pt_str, pvec_compact, code_id)
sys.path.insert(0, HARNESS)  # noqa: F405
HERE = os.path.dirname(os.path.abspath(__file__))   # re-set: the star import above brought round1's HERE along; outputs belong here


def sub(a, b): return tuple(a[k] - b[k] for k in range(3))
def dot(a, b): return sum(a[k] * b[k] for k in range(3))
def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def solve3(M, b):
    A = [list(map(F, M[i])) + [F(b[i])] for i in range(3)]
    for c in range(3):
        piv = next((i for i in range(c, 3) if A[i][c] != 0), None)
        if piv is None:
            return None
        A[c], A[piv] = A[piv], A[c]
        A[c] = [x / A[c][c] for x in A[c]]
        for i in range(3):
            if i != c and A[i][c] != 0:
                f = A[i][c]; A[i] = [a - f * bb for a, bb in zip(A[i], A[c])]
    return [A[i][3] for i in range(3)]


def min_sphere_of(S):
    """Smallest sphere with the points of S on its boundary (|S| in 1..4); None if degenerate."""
    if len(S) == 1:
        return S[0], F(0)
    if len(S) == 2:
        c = tuple((S[0][k] + S[1][k]) / 2 for k in range(3)); return c, dot(sub(S[0], c), sub(S[0], c))
    a = S[0]
    if len(S) == 3:
        u, v = sub(S[1], a), sub(S[2], a); nrm = cross(u, v)
        if nrm == (0, 0, 0):
            return None
        x = solve3([list(u), list(v), list(nrm)], [dot(u, u) / 2, dot(v, v) / 2, 0])
        if x is None:
            return None
        c = tuple(a[k] + x[k] for k in range(3)); return c, dot(x, x)
    u, v, w = sub(S[1], a), sub(S[2], a), sub(S[3], a)
    if det3(u, v, w) == 0:  # noqa: F405
        return None
    x = solve3([list(u), list(v), list(w)], [dot(u, u) / 2, dot(v, v) / 2, dot(w, w) / 2])
    c = tuple(a[k] + x[k] for k in range(3)); return c, dot(x, x)


def mes(verts):
    """Exact minimal enclosing sphere of a finite point set: the least sphere among
    those determined by 2, 3 or 4 of the points that contains all of them."""
    best = None
    n = len(verts)
    for k in (2, 3, 4):
        for S in itertools.combinations(range(n), k):
            s = min_sphere_of([verts[i] for i in S])
            if s is None:
                continue
            c, r2 = s
            if best is not None and r2 >= best[1]:
                continue
            if all(dot(sub(v, c), sub(v, c)) <= r2 for v in verts):
                best = (c, r2, S)
    return best


def pct(vol, r2):
    """100 * vol / ((4/3) pi r^3); the only float step."""
    return 100.0 * float(vol) / (4.0 / 3.0 * math.pi * float(r2) ** 1.5)


def hull_faces(verts):
    """Exact face enumeration of the convex hull of integer/rational points whose
    interior contains the origin: every plane through three vertices that has all
    vertices weakly on one side is a face plane (pattern of g2_seed_catalog.py)."""
    faces = {}
    n = len(verts)
    for i, j, k in itertools.combinations(range(n), 3):
        nrm = cross(sub(verts[j], verts[i]), sub(verts[k], verts[i]))
        if nrm == (0, 0, 0):
            continue
        b = dot(nrm, verts[i])
        if b < 0:
            nrm = tuple(-x for x in nrm); b = -b
        if b == 0:
            continue
        vals = [dot(nrm, v) - b for v in verts]
        if all(x <= 0 for x in vals):
            on = tuple(m for m, x in enumerate(vals) if x == 0)
            key = tuple(F(x) / b for x in nrm)   # normalise so that <key, v> = 1 on the face
            faces[key] = on
    return faces


def order_face(pts, nrm):
    """Cyclic order of coplanar points about their centroid (float proposal, exact convexity check)."""
    c = tuple(sum(p[k] for p in pts) / len(pts) for k in range(3))
    # exact: pick u in the plane, v = nrm x u; sort by atan2 of exact-dot floats (proposal), then verify exactly
    u = sub(pts[0], c)
    v = cross(nrm, u)
    ang = sorted(range(len(pts)), key=lambda m: math.atan2(float(dot(sub(pts[m], c), v)), float(dot(sub(pts[m], c), u))))
    poly = [pts[m] for m in ang]
    for a in range(len(poly)):
        p0, p1, p2 = poly[a - 1], poly[a], poly[(a + 1) % len(poly)]
        assert dot(cross(sub(p1, p0), sub(p2, p1)), nrm) > 0, "face not strictly convex CCW"
    return poly


def hull_volume(verts):
    """Exact volume of conv(verts) (origin interior), via the face enumeration."""
    faces = hull_faces(verts)
    vol6 = F(0)
    for nrm, on in faces.items():
        poly = order_face([verts[m] for m in on], nrm)
        for t in range(1, len(poly) - 1):
            d = det3(poly[0], poly[t], poly[t + 1])  # noqa: F405
            assert d > 0
            vol6 += d
    return vol6 / 6, faces
