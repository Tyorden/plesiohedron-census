#!/usr/bin/env python
"""exact_cell_gram.py — exact-Fraction Voronoi cell under a rational Gram
metric (design doc §1.3 "Exact phase", generalization (a)+(b) of clip_cell).

Phase-2 SIBLING of ../exact_cell.py (which stays untouched and still raises
NotImplementedError for gram != None). Reused from the accepted module by
import: order_cycle (float-propose / exact-verify facet cycles) and _dot.
Re-implemented here because the ancestor hard-codes the Euclidean bisector
and a scalar box half-size: _clip_gram (Gram bisectors, per-axis box) and
candidates_near_gram (G-norm ball, per-axis block range).

Everything is fractions.Fraction / int. The Gram matrix is taken RATIONAL,
symmetric, positive definite (checked exactly) and scaled to integers
internally (uniform similarity — type-preserving), so bisector planes have
integer coefficients when centers are integers.

PROVABLE CUTOFF, metric-correct (ANCHORS G2b (e)). Work in the G-norm
|x|_G = sqrt(x^T G x), which is a genuine norm (triangle inequality holds in
any inner-product space). Candidates = every site r != c with |r-c|_G^2 <= D2.
COMPLETENESS of the candidate list: by Cauchy-Schwarz in the G-inner product,
x_i = <G^-1 e_i, x>_G, so |x_i| <= sqrt((G^-1)_ii) |x|_G; metric.coord_bound
returns integers B_i with B_i^2 >= D2 (G^-1)_ii, hence every site in the
G-ball has |r_i - c_i| <= B_i and block offsets |n_i| <= B_i // period + 1 —
the enumeration covers the ball. THE 4*rho^2 <= D^2 ARGUMENT: let rho^2 =
max_v |v-c|_G^2 over the clipped cell's exact vertices. If 4 rho^2 <= D2 then
for every cell point v and every site r with |r-c|_G > D:
|v-r|_G >= |r-c|_G - |v-c|_G > D - rho >= rho >= |v-c|_G, so v stays strictly
on c's side of the bisector — no uncounted site cuts. The starting box has
per-axis half-size B_i (from coord_bound with the same D2), so every box-face
point x has |x_i - c_i| = B_i, hence |x-c|_G >= B_i / sqrt((G^-1)_ii) >= D >
rho: a surviving box facet would put a vertex at G-distance > rho —
impossible once the certificate holds (and asserted anyway, g1 guard). On
failure D2 quadruples (D doubles) and the clip reruns.

Output dict is a superset of exact_cell.clip_cell's: facet_cycles (vertex-id
cycles CCW from outside — orientation via the coordinate-space triple
product, which the Cartesian embedding x -> A x with det A > 0 preserves),
neighbors, vertices (exact Fraction triples in the LATTICE basis), p_vector,
facet_count, n_vertices, n_edges, nonsimple_vertices, cutoff_D2, rho2
(G-norm), gram (integer Gram used), gram_scale.
"""
import itertools
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))          # ../ : accepted modules

from exact_cell import order_cycle, _dot              # noqa: E402
import metric                                          # noqa: E402


def candidates_near_gram(center, base_points, period, G, D2):
    """All sites r != center of the periodic set with |r-center|_G^2 <= D2,
    sorted by G-distance. Complete for the G-ball by the coordinate bound."""
    B = metric.coord_bound(G, D2)
    K = tuple(B[i] // period + 1 for i in range(3))
    out = []
    for n in itertools.product(range(-K[0], K[0] + 1),
                               range(-K[1], K[1] + 1),
                               range(-K[2], K[2] + 1)):
        for q in base_points:
            r = (q[0] + period * n[0], q[1] + period * n[1], q[2] + period * n[2])
            if r == center:
                continue
            d = (r[0] - center[0], r[1] - center[1], r[2] - center[2])
            d2 = metric.gnorm2(G, d)
            if d2 <= D2:
                out.append((d2, r))
    out.sort()
    return [r for _, r in out], B


def _clip_gram(center, cands, G, B):
    """Exact halfspace intersection: start box with per-axis half-sizes B_i
    around center, cut by the G-bisector of each candidate. Vertices carry
    frozensets of defining plane indices (g1_verify.py:27-77 pattern)."""
    planes = []                          # (a int 3-tuple, b Fraction, tag): a.x <= b
    for i in range(3):
        for s in (1, -1):
            a = [0, 0, 0]; a[i] = s
            planes.append((tuple(a), F(s * center[i] + B[i]), ('box', i, s)))
    verts = []
    for sx in (-B[0], B[0]):
        for sy in (-B[1], B[1]):
            for sz in (-B[2], B[2]):
                v = (F(center[0] + sx), F(center[1] + sy), F(center[2] + sz))
                on = frozenset(j for j, (a, b, t) in enumerate(planes)
                               if _dot(a, v) == b)
                verts.append((v, on))
    for r in cands:
        a, b = metric.bisector(G, center, r)
        b = F(b)
        idx = len(planes)
        val = [_dot(a, v) - b for v, _ in verts]
        if all(x <= 0 for x in val):
            continue                     # bisector does not cut
        planes.append((a, b, ('nbr', r)))
        newv = [(v, on) for (v, on), x in zip(verts, val) if x < 0]
        newv += [(v, on | {idx}) for (v, on), x in zip(verts, val) if x == 0]
        n = len(verts)
        for i in range(n):
            if val[i] >= 0:
                continue
            for j in range(n):
                if val[j] <= 0:
                    continue
                shared = verts[i][1] & verts[j][1]
                if len(shared) < 2:
                    continue
                t = val[i] / (val[i] - val[j])          # in (0,1), exact
                v = tuple(verts[i][0][k] + t * (verts[j][0][k] - verts[i][0][k])
                          for k in range(3))
                newv.append((v, shared | {idx}))
        seen = {}
        for v, on in newv:
            seen[v] = seen.get(v, frozenset()) | on
        verts = [(v, frozenset(on)) for v, on in seen.items()]
    return verts, planes


def clip_cell_gram(center, base_points, period, gram, D2=None):
    """Exact Voronoi cell of `center` in the periodic set (base_points mod
    period, integer lattice-basis coordinates) under the rational Gram
    metric `gram`. See module docstring for the certificate."""
    assert metric.is_positive_definite(gram), "Gram matrix not symmetric PD"
    G, scale = metric.scale_to_integers(gram)
    center = tuple(int(x) for x in center)
    base_points = [tuple(int(x) for x in p) for p in base_points]
    if D2 is None:
        # D >= 2 * period in every axis direction: D2 = 4 period^2 max_i G_ii
        D2 = 4 * period * period * max(G[i][i] for i in range(3))
    while True:
        cands, B = candidates_near_gram(center, base_points, period, G, D2)
        verts, planes = _clip_gram(center, cands, G, B)
        rho2 = max(metric.gnorm2(G, (v[0] - center[0], v[1] - center[1],
                                     v[2] - center[2])) for v, _ in verts)
        if 4 * rho2 <= D2:               # provable cutoff, exact comparison
            break
        D2 *= 4
    facs = []
    for j, (a, b, tag) in enumerate(planes):
        vs = [v for v, on in verts if j in on]
        if len(vs) >= 3:
            assert tag[0] == 'nbr', f"box facet survived (g1 guard): {tag}"
            facs.append((a, tag[1], vs))
    used = sorted({v for _, _, vs in facs for v in vs})
    vid = {v: i for i, v in enumerate(used)}
    cycles, nbrs = [], []
    for a, r, vs in facs:
        poly = order_cycle(vs, a)
        assert len(poly) == len(vs)
        cycles.append([vid[v] for v in poly])
        nbrs.append(r)
    inc = [0] * len(used)
    for cyc in cycles:
        for i in cyc:
            inc[i] += 1
    assert all(k >= 3 for k in inc), "facet vertex with <3 incident facets"
    E2 = sum(len(c) for c in cycles)
    assert E2 % 2 == 0
    return {
        'center': center,
        'facet_cycles': cycles,
        'neighbors': nbrs,
        'vertices': used,
        'p_vector': tuple(sorted(len(c) for c in cycles)),
        'facet_count': len(cycles),
        'n_vertices': len(used),
        'n_edges': E2 // 2,
        'nonsimple_vertices': sum(1 for k in inc if k > 3),
        'cutoff_D2': D2,
        'rho2': rho2,
        'gram': G,
        'gram_scale': scale,
    }


def _selftest():
    # Identity metric must reproduce exact_cell.clip_cell byte-for-byte on the
    # G2 controls (vertices, neighbors, p-vector).
    from exact_cell import clip_cell
    I = metric.gram_cubic()
    for pts in ([(0, 0, 0)],
                [(0, 0, 0), (1, 1, 1)],
                [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]):
        e0 = clip_cell((0, 0, 0), pts, 2)
        e1 = clip_cell_gram((0, 0, 0), pts, 2, I)
        assert e0['vertices'] == e1['vertices'], "vertex sets differ (identity metric)"
        assert set(e0['neighbors']) == set(e1['neighbors'])
        assert e0['p_vector'] == e1['p_vector']
        assert e0['nonsimple_vertices'] == e1['nonsimple_vertices']
    # Anisotropic sanity: simple tetragonal lattice Z^3 with c/a = 3 is still
    # a box (6 quads), cutoff certificate must hold in the G-norm.
    e = clip_cell_gram((0, 0, 0), [(0, 0, 0)], 1, metric.gram_tetragonal(3))
    assert e['p_vector'] == (4,) * 6 and 4 * e['rho2'] <= e['cutoff_D2']
    # Hexagonal lattice (c/a = 1): hexagonal prism 6 quads + 2 hexagons, V=12.
    e = clip_cell_gram((0, 0, 0), [(0, 0, 0)], 1, metric.gram_hexagonal(1))
    assert e['p_vector'] == (4,) * 6 + (6,) * 2 and e['n_vertices'] == 12 \
        and e['nonsimple_vertices'] == 0, (e['p_vector'], e['n_vertices'])
    print("exact_cell_gram.py selftest: PASS (identity metric == clip_cell on "
          "SC/BCC/FCC; tetragonal box; hexagonal prism)")


if __name__ == "__main__":
    _selftest()
