#!/usr/bin/env python
"""R2 -- was the Satchelhedron's generating point (0, 0, 1/4) in Schmitt's
IT(220) grid?

Schmitt's recovered software (references/schmitt_repo_recovery, plesiohedron.cpp)
reads the generating points from an input file, so the grid itself is not in
the repository.  His dissertation (Sec. 2.2, p. 25 and the per-group blocks)
describes the grid as an "approximating grid" of rational points over the
reduced fundamental domain R_k of the normalizer, and prints for each group
the reduced domain (as a convex hull of rational vertices), the number of grid
points used, and one grid point per f-vector.  For IT(220):
   R220 = conv{(0,0,0), (+-1/8,+-1/8,1/8), (+-1/8,+-1/8,1/4)}   (9 vertices)
   "We used 1 000 677 997 grid points in the approximating grid."
   printed coordinates all have denominators dividing 6984 = 8 * 873 = 2^3 3^2 97.
Hypothesis (from the printed data): the grid is the set of points with
barycentric coordinates in (1/D) Z_{>=0} over a triangulation of R_k into
simplices on its printed vertices, boundary included.  Then the number of
grid points is  V + E (D-1) + T C(D-1,2) + S C(D-1,3)  for a triangulation
with V vertices, E edges, T triangles, S tetrahedra (Euler: V - E + T - S = 1),
and every coordinate has denominator dividing q D, q = lcm of the vertex
denominators.  This script (i) solves that identity for the three reduced
domains whose counts are printed (R220 / R214 / R230 / R199 share one domain
and one count; R201 / R224; R212) and reports every solution, (ii) verifies
that the printed IT(220) representative points all lie in R220 and have
denominators dividing 8 D, and (iii) decides membership of (0,0,1/4) and of
the whole 24d segment in R220, for the inferred D, by the barycentric parity
argument; the normalizer images of (0,0,1/4) inside R220 are enumerated with
the frozen IT(230) operations so that no other representative is missed.
Exact; deterministic."""
import os, sys, json, itertools, re
from fractions import Fraction as F
from math import comb, gcd
from common2 import *  # noqa
import orbit  # noqa: E402

# ---------------------------------------------------------------- (i) the count identity
def solve_count(N, nverts, q, M, label):
    """All (D, V, E, T, S) with M | qD, D <= 4M/q, V in [nverts, nverts+12], S >= 1, Euler = 1,
    V + E(D-1) + T C(D-1,2) + S C(D-1,3) = N."""
    sols = []
    Dmin = M // gcd(M, q)          # smallest D with M | qD
    for m in range(1, 5):
        D = Dmin * m
        c1, c2, c3 = D - 1, comb(D - 1, 2), comb(D - 1, 3)
        for S in range(1, 60):
            rem = N - S * c3
            if rem < 0:
                break
            for T in range(0, 200):
                rem2 = rem - T * c2
                if rem2 < 0:
                    break
                for V in range(nverts, nverts + 13):
                    E = V + T - S - 1           # Euler characteristic 1 (a ball)
                    if E >= 0 and V + E * c1 == rem2:
                        sols.append((D, V, E, T, S))
    return sols


COUNTS = [  # (label, printed count, printed vertices, vertex-denominator lcm q, max printed coordinate denominator M)
    ("R220 (= R214 = R230 = R199)", 1000677997, 9, 8, 6984),
    ("R201 (= R224)", 1001452269, 4, 4, 7264),
    ("R212", 1000964383, 7, 8, 4248),
]
L = ["## R2 -- Schmitt's IT(220) grid and the point (0, 0, 1/4)", "",
     "Source facts (references/Schmitt_2016_dissertation.pdf, text layer): the recovered code takes the generating points as an input file (plesiohedron.cpp), so the grid is not in the repository; "
     "Sec. 2.2 (p. 25) describes 'approximating F with an extremely fine point grid' over a fundamental domain of the normalizer; the IT(220) block (printed p. 141) gives R220 = conv{(0,0,0), (+-1/8,+-1/8,1/8), (+-1/8,+-1/8,1/4)} and "
     "'We used 1 000 677 997 grid points in the approximating grid'; every printed IT(220) coordinate has denominator dividing 6984 = 8 * 873.", "",
     "### (i) The count identity: barycentric grid of denominator D over a triangulation of the reduced domain on its printed vertices", "",
     "| domain | printed grid points | solutions (D, V, E, T, S) with M | qD, D <= 4M/q, Euler V-E+T-S = 1 |", "|---|---|---|"]
SOLS = {}
for label, N, nv, q, M in COUNTS:
    s = solve_count(N, nv, q, M, label)
    SOLS[label] = s
    L.append(f"| {label} | {N:,} | {s if s else 'none'} |")
D220 = [s for s in SOLS["R220 (= R214 = R230 = R199)"] if s[1] == 9]
assert len(D220) == 1, D220
D, V, E, T, S = D220[0]
assert (D, V, E, T, S) == (873, 9, 24, 25, 9)
assert SOLS["R201 (= R224)"] == [(1816, 4, 6, 4, 1)], SOLS["R201 (= R224)"]
assert (1062, 7, 16, 15, 5) in SOLS["R212"], SOLS["R212"]
L += ["", f"Reading: for R220 the identity has exactly one solution with the 9 printed vertices, D = {D} with (V, E, T, S) = ({V}, {E}, {T}, {S}), a triangulation of the 9-vertex domain into 9 tetrahedra "
      "(face check: 4S = 36 = 14 boundary triangles + 2 * 11 interior triangles; 16 polytope edges + 5 quadrilateral diagonals + 3 interior edges = 24). "
      "R201 is a single tetrahedron and the count is exactly C(1819, 3), so D = 1816 there. For R212 the solution on its 7 printed vertices is D = 1062 with (7, 16, 15, 5) "
      "(the printed denominators reach only 4248 = 8 * 1062 / 2 because every vertex coordinate of R212 is an odd multiple of 1/8 and D is even, so the numerators are even). "
      "Three groups, three exact matches of a nine-or-ten-digit count: the grid scheme is the barycentric grid described above, boundary included, and for IT(220) its denominator is D = 873, an odd number.", ""]

# ---------------------------------------------------------------- (ii) the printed IT(220) points lie in R220 with denominators | 6984
S_TXT = os.path.join(os.path.dirname(HERE), "..", "..", "..", "..")  # not used; text was extracted to the scratchpad by the session
# transcribed from the text layer (printed pp. 141-143): every IT(220) generating grid point
P220 = """(0, 0, 1/8) (0, 0, 73/582) (-1/8, -1/8, 1/8) (-1/8, -1/8, 1/4) (1/8, -1/24, 5/24) (-1/8, -227/6984, 355/2328) (143/1746, 289/3492, 295/3492)
(-1/8, -527/6984, 1219/6984) (1/8, -235/6984, 1/8) (1/8, -1/8, 1/4) (-673/6984, -587/6984, 1685/6984) (1/9, 0, 1/6) (-1/8, 15/776, 155/776)
(-1/8, 29/6984, 157/1164) (-37/1164, 67/582, 173/1164) (1/8, -175/6984, 611/3492) (109/3492, 109/3492, 109/1746) (-221/2328, 7/2328, 463/2328)
(-817/6984, -85/6984, 1379/6984) (-1/8, -197/2328, 1253/6984) (9/776, 277/2328, 833/6984) (-1/8, -83/776, 1331/6984) (145/2328, 145/2328, 1/8)
(31/1746, 109/873, 1369/6984) (1/8, 871/6984, 1/8) (0, 0, 0) (1/12, 73/1746, 581/3492) (-259/2328, -451/6984, 751/3492) (0, 9/388, 105/776)
(-503/6984, -791/6984, 11/72) (-1/8, 55/2328, 437/3492) (-13/3492, 10/97, 863/6984) (109/1746, 109/1746, 109/873) (-251/2328, -113/2328, 505/2328)
(289/3492, 145/1746, 293/3492) (-1/8, 27/776, 1189/6984) (-247/6984, -17/6984, 1627/6984) (-3/776, 719/6984, 133/873) (133/1746, 133/1746, 133/873)
(-455/6984, -871/6984, 545/3492) (289/3492, 145/1746, 73/873) (-455/6984, -7/72, 545/3492) (0, 43/873, 347/2328) (-455/6984, -655/6984, 545/3492)
(25/776, 25/776, 25/388) (1/8, 1/8, 1/8) (-737/6984, -95/2328, 1519/6984) (25/6984, 43/6984, 67/6984) (-63/776, -7/776, 1489/6984) (9/97, 3/97, 91/582)
(88/873, 353/3492, 127/1164) (95/873, 19/291, 19/97) (-521/6984, -689/6984, 545/3492) (8/97, 40/873, 137/873) (83/1164, 251/3492, 511/6984)
(235/2328, 47/776, 141/776) (119/6984, 121/6984, 31/1746) (707/6984, 425/6984, 1273/6984) (1/8, 45/776, 159/776) (1/8, 365/6984, 373/1746)
(647/6984, 389/6984, 1165/6984) (1/8, 115/2328, 247/1164)"""
pts220 = [tuple(F(x) for x in m.split(",")) for m in re.findall(r"\(([^)]*)\)", P220)]
assert len(pts220) == 62, len(pts220)   # 62 rows in the IT(220) table (matches the 62-row digitization)


def in_R220(p):
    x, y, z = p
    return abs(x) <= z and abs(y) <= z and abs(x) <= F(1, 8) and abs(y) <= F(1, 8) and z <= F(1, 4)


assert all(in_R220(p) for p in pts220)
assert all((c * 8 * D).denominator == 1 for p in pts220 for c in p)
L += ["### (ii) The 62 printed IT(220) generating points", "",
      f"All 62 lie in R220 (H-representation |x| <= z, |y| <= z, |x| <= 1/8, |y| <= 1/8, z <= 1/4, which equals the printed convex hull) and every coordinate times 8D = 6984 is an integer. "
      "Both facts are consistent with the scheme and are asserted by the script.", ""]

# ---------------------------------------------------------------- (iii) (0,0,1/4) and the 24d segment
def bary_face(p):
    """Minimal face of R220 containing p and the barycentric coordinates of p on it.
    Returns (face name, list of (vertex, weight)) or ('interior', None).  For the two
    square faces (top z=1/4; the middle square z=1/8 is not a face) and the four lateral
    rectangles, both diagonal triangulations are reported."""
    x, y, z = p
    eighth, quarter = F(1, 8), F(1, 4)
    verts = {"apex": (F(0), F(0), F(0))}
    for sx in (-1, 1):
        for sy in (-1, 1):
            verts[f"m{sx:+d}{sy:+d}"] = (sx * eighth, sy * eighth, eighth)
            verts[f"t{sx:+d}{sy:+d}"] = (sx * eighth, sy * eighth, quarter)
    # which facet planes are tight
    tight = []
    if z == quarter: tight.append("top")
    for s in (-1, 1):
        if x == s * eighth: tight.append(f"x={s:+d}/8")
        if y == s * eighth: tight.append(f"y={s:+d}/8")
        if x == s * z and z <= eighth: tight.append(f"|x|=z ({s:+d})")
        if y == s * z and z <= eighth: tight.append(f"|y|=z ({s:+d})")
    if not tight:
        return "interior", None
    # vertices of the minimal face = polytope vertices satisfying all tight planes
    def sat(v, name):
        vx, vy, vz = v
        if name == "top": return vz == quarter
        if name.startswith("x="): return vx == int(name[2:4]) * eighth
        if name.startswith("y="): return vy == int(name[2:4]) * eighth
        s = int(name[-3:-1])
        return (vx if name.startswith("|x|") else vy) == s * vz
    fv = [(n, v) for n, v in verts.items() if all(sat(v, t) for t in tight)]
    # barycentric coordinates: solve p = sum w_i v_i, sum w_i = 1 (least-squares free: face is a simplex or a quadrilateral)
    if len(fv) <= 3:
        # simplex face: solve exactly
        A = [[F(v[k]) for _, v in fv] for k in range(3)] + [[F(1)] * len(fv)]
        b = [x, y, z, F(1)]
        # gaussian elimination on the (4 x m) system
        m = len(fv)
        M_ = [row[:] + [b[i]] for i, row in enumerate(A)]
        r = 0; piv = []
        for c in range(m):
            pr = next((i for i in range(r, 4) if M_[i][c] != 0), None)
            if pr is None: continue
            M_[r], M_[pr] = M_[pr], M_[r]
            M_[r] = [v / M_[r][c] for v in M_[r]]
            for i in range(4):
                if i != r and M_[i][c] != 0:
                    f = M_[i][c]; M_[i] = [a - f * bb for a, bb in zip(M_[i], M_[r])]
            piv.append(c); r += 1
        assert all(M_[i][m] == 0 for i in range(r, 4)), "inconsistent"
        w = [M_[piv.index(c)][m] if c in piv else F(0) for c in range(m)]
        assert all(wi >= 0 for wi in w) and sum(wi * F(v[k]) for wi, (_, v) in zip(w, fv) for k in [0]) == x
        return "+".join(t for t in tight), [(n, wi) for (n, _), wi in zip(fv, w)]
    # quadrilateral face: two diagonal choices
    assert len(fv) == 4
    out = []
    names = [n for n, _ in fv]
    for diag in ((0, 2), (1, 3)):
        # triangles: (d0, d1, other) for each of the two 'other' vertices
        others = [i for i in range(4) if i not in diag]
        for o in others:
            tri = [fv[diag[0]], fv[diag[1]], fv[o]]
            A = [[F(v[k]) for _, v in tri] for k in range(3)] + [[F(1)] * 3]
            b = [x, y, z, F(1)]
            M_ = [row[:] + [b[i]] for i, row in enumerate(A)]
            r = 0; piv = []
            for c in range(3):
                pr = next((i for i in range(r, 4) if M_[i][c] != 0), None)
                if pr is None: continue
                M_[r], M_[pr] = M_[pr], M_[r]
                M_[r] = [v / M_[r][c] for v in M_[r]]
                for i in range(4):
                    if i != r and M_[i][c] != 0:
                        f = M_[i][c]; M_[i] = [a - f * bb for a, bb in zip(M_[i], M_[r])]
                piv.append(c); r += 1
            if any(M_[i][3] != 0 for i in range(r, 4)):
                continue
            w = [M_[piv.index(c)][3] for c in range(3)]
            if all(wi >= 0 for wi in w):
                out.append((f"diag {names[diag[0]]}-{names[diag[1]]}", [(n, wi) for (n, _), wi in zip(tri, w)]))
                break
    return "+".join(t for t in tight) + " (quadrilateral)", out


def is_grid(bary, D):
    return all((wi * D).denominator == 1 for _, wi in bary)


def images_in_R220(p):
    """All IT(230)-images of p (fractional, mod 1, with lattice shifts in {-1,0,1}^3) lying in R220."""
    g = GROUPS[230]
    imgs = set()
    for R, t in g["ops_exact"]:
        q = orbit.apply_op(R, t, p)          # reduced to [0,1)^3; R220 has x, y in [-1/8, 1/8], z in [0, 1/4]
        for sh in itertools.product((-1, 0), (-1, 0), (0,)):
            r = tuple(q[k] + sh[k] for k in range(3))
            if in_R220(r):
                imgs.add(r)
    return sorted(imgs)


p0 = (F(0), F(0), F(1, 4))
L += ["### (iii) The point (0, 0, 1/4) and the 24d segment in R220", ""]
L.append(f"IT(220) is a single-origin group and the operation tables agree with Schmitt's in the identical setting (SCHMITT_OPS_XCHECK), so (0, 0, 1/4) is (0, 0, 1/4) in his coordinates. "
         f"It lies in R220: it is the centre of the top square face z = 1/4, on both diagonals. Normalizer (Ia-3d, frozen IT(230) operations) images of the point inside R220:")
L.append("")
L.append("| image in R220 | minimal face | barycentric coordinates (per diagonal choice where the face is a quadrilateral) | grid point for D = 873? |")
L.append("|---|---|---|---|")
verdicts = []
for im in images_in_R220(p0):
    face, bary = bary_face(im)
    if face == "interior":
        L.append(f"| {pt_str(im)} | interior | (depends on the triangulation) | undecided |"); verdicts.append(None); continue
    if isinstance(bary[0], tuple) and isinstance(bary[0][1], list):   # quadrilateral: list of (diag, bary)
        cells = "; ".join(f"{d}: " + ", ".join(f"{n}={frac_str(w)}" for n, w in b) for d, b in bary)
        g = [is_grid(b, D) for _, b in bary]
        L.append(f"| {pt_str(im)} | {face} | {cells} | {'NO (either diagonal)' if not any(g) else 'depends on diagonal: ' + str(g)} |")
        verdicts.append(any(g))
    else:
        cells = ", ".join(f"{n}={frac_str(w)}" for n, w in bary)
        g = is_grid(bary, D)
        L.append(f"| {pt_str(im)} | {face} | {cells} | {'YES' if g else 'NO'} |")
        verdicts.append(g)
assert verdicts and all(v is False for v in verdicts), verdicts
L += ["", f"Verdict: (0, 0, 1/4) is NOT a grid point of Schmitt's IT(220) grid. Every representative of it in R220 sits on a face diagonal with barycentric weight 1/2, and D = {D} is odd.", ""]

# the 24d line: images of generic line points, and which parameter values are grid points
L += ["The 24d line (x, 0, 1/4). For sample parameters the images in R220 and their faces:", "",
      "| x | images in R220 | faces |", "|---|---|---|"]
line_pts = [F(1, 1000), F(1, 97), F(7, 200), F(1, 13), F(1, 12), F(1, 3), F(-1, 1000)]
for xx in line_pts:
    ims = images_in_R220((xx, F(0), F(1, 4)))
    faces = [bary_face(im)[0] for im in ims]
    L.append(f"| {frac_str(xx)} | {'; '.join(pt_str(i) for i in ims)} | {'; '.join(faces)} |")
# the top-face segment: (x, 0, 1/4) with |x| <= 1/8; barycentric weights in the triangle containing it
L.append("")
L.append("On the top face the segment y = 0, |x| <= 1/8 lies in whichever triangle of the diagonal triangulation contains it; its barycentric coordinates are "
         "(1/2 + 4x, -4x, 1/2) for x <= 0 in the triangle on that side (and symmetrically for x >= 0): one weight is 1/2 for every x, so for odd D no point of the "
         "segment is a grid point.  Grid points of the 24d line therefore come only from its other normalizer images in R220, listed above for sample x.")
# enumerate the grid points on all images of the line: scan x = k/(8D) over one period and test each image
grid_x = []
for k in range(0, 8 * D):
    xx = F(k, 8 * D)
    ims = images_in_R220((xx, F(0), F(1, 4)))
    hit = False
    for im in ims:
        face, bary = bary_face(im)
        if face == "interior":
            continue
        if isinstance(bary[0], tuple) and isinstance(bary[0][1], list):
            if any(is_grid(b, D) for _, b in bary):
                hit = True
        elif is_grid(bary, D):
            hit = True
    if hit:
        grid_x.append(xx)
L.append("")
L.append(f"Scan of x = k/(8D), k = 0..8D-1 (all candidate grid values on the line, since grid coordinates have denominators dividing 8D): {len(grid_x)} parameter values of the 24d line are grid points "
         f"(via some boundary image in R220; interior images, if any, are not decidable without his triangulation and are counted as misses). "
         f"Smallest positive: {frac_str(grid_x[0]) if grid_x and grid_x[0] != 0 else (frac_str(grid_x[1]) if len(grid_x) > 1 else 'none')}; "
         f"x = 0 is {'IN' if F(0) in grid_x else 'NOT in'} the set; values in (0, 1/12): {len([x for x in grid_x if 0 < x < F(1, 12)])}; values in (1/12, 1/3]: {len([x for x in grid_x if F(1, 12) < x <= F(1, 3)])}.")
open(os.path.join(HERE, "r2_schmitt_grid.md"), "w").write("\n".join(L) + "\n")
json.dump(dict(D=D, VETS=(V, E, T, S), solutions={k: v for k, v in SOLS.items()}, point_in_grid=False,
               line_grid_x=[frac_str(x) for x in grid_x]), open(os.path.join(HERE, "r2_schmitt_grid.json"), "w"), indent=1)
print("\n".join(L))
