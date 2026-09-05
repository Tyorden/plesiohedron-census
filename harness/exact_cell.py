#!/usr/bin/env python
"""exact_cell.py — exact-Fraction Voronoi cell via halfspace clipping.

Generalized clip_cell. Ancestor: SCI_OEIS_josehedron/scripts/g1_verify.py:27-77
(vertices carry frozensets of defining planes; edge crossings via
t = val_i/(val_i - val_j); facet readoff by on-plane vertex count). Euclidean
metric for the cubic phase.

TODO(Gram-metric hook, design §1.3 / §6.1): for a non-cubic conventional cell
with rational Gram matrix G, the bisector of centers c, r is
    2 (r-c)^T G x = r^T G r - c^T G c        (rational plane),
the candidate sort key is the G-norm |r-c|_G^2, and the cutoff proof below must
replace Euclidean balls with G-balls (needs a rational lower bound on the least
eigenvalue of G to keep the block enumeration complete). clip_cell(...,
gram=...) raises NotImplementedError until that phase; nothing else in this
module assumes gram is None.

Provable cutoff radius (checked EXACTLY, house rule: floats propose, Fractions
decide — this module is all-Fraction): candidates are every site r with
|r-c|^2 <= D^2; the block range K = D//period + 1 covers the Euclidean D-ball,
so the candidate list is complete by construction. After clipping, let
rho^2 = max_v |v-c|^2 over the cell's exact vertices. If 4*rho^2 <= D^2 then no
site with |r-c| > D can cut: for every cell point v,
|v-r| >= |r-c| - |v-c| > D - rho >= rho >= |v-c|, so v stays strictly on c's
side of the bisector. On failure D doubles and the clip reruns. The starting
bounding box (half-size D) may leave no surviving facet (g1_verify:83-84 guard).
"""
import functools
import itertools
import math
from fractions import Fraction as F


def _sub(a, b): return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
def _dot(a, b): return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
def _cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def candidates_near(center, base_points, period, D):
    """All sites r != center of the periodic set with |r-center|^2 <= D^2,
    sorted by squared distance. Complete for the D-ball: any such r has block
    offsets |n_i| <= D/period + 1."""
    K = D // period + 1
    out = []
    for n in itertools.product(range(-K, K+1), repeat=3):
        for q in base_points:
            r = (q[0]+period*n[0], q[1]+period*n[1], q[2]+period*n[2])
            if r == center:
                continue
            d2 = (r[0]-center[0])**2 + (r[1]-center[1])**2 + (r[2]-center[2])**2
            if d2 <= D*D:
                out.append((d2, r))
    out.sort()
    return [r for _, r in out]


def _clip(center, cands, B):
    """Exact halfspace intersection: start box of half-size B around center,
    cut by the bisector of each candidate site. Vertices carry frozensets of
    defining plane indices (g1_verify.py:27-77, adapted)."""
    planes = []                          # (a int 3-tuple, b Fraction, tag): a.x <= b
    for i in range(3):
        for s in (1, -1):
            a = [0, 0, 0]; a[i] = s
            planes.append((tuple(a), F(s*center[i] + B), ('box', i, s)))
    verts = []
    for sx in (-B, B):
        for sy in (-B, B):
            for sz in (-B, B):
                v = (F(center[0]+sx), F(center[1]+sy), F(center[2]+sz))
                on = frozenset(j for j, (a, b, t) in enumerate(planes)
                               if _dot(a, v) == b)
                verts.append((v, on))
    for r in cands:
        a = tuple(2*(r[k]-center[k]) for k in range(3))
        b = F(sum(r[k]*r[k] - center[k]*center[k] for k in range(3)))
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
                v = tuple(verts[i][0][k] + t*(verts[j][0][k]-verts[i][0][k])
                          for k in range(3))
                newv.append((v, shared | {idx}))
        seen = {}
        for v, on in newv:
            seen[v] = seen.get(v, frozenset()) | on
        verts = [(v, frozenset(on)) for v, on in seen.items()]
    return verts, planes


def _convex_cycle_ok(poly, normal):
    """EXACT strict-convexity test of a cyclic vertex order: every consecutive
    triple turns left as seen from the outward normal. This is the DECIDING
    check of order_cycle, unchanged in strength; False is never accepted."""
    for t in range(len(poly)):
        a, b, cc = poly[t], poly[(t+1) % len(poly)], poly[(t+2) % len(poly)]
        if not _dot(_cross(_sub(b, a), _sub(cc, b)), normal) > 0:
            return False
    return True


def order_cycle_exact(pts, normal):
    """EXACT fallback ordering (2026-09-04, ORDER_CYCLE_FIX): sort the coplanar
    points around their exact centroid c in the oriented in-plane frame
    (u, w) = (pts[1]-pts[0], normal x u), using only the rational 2-D
    projections x = (p-c).u, y = (p-c).w and sign comparisons: half-plane
    first ([0,pi) before [pi,2pi)), then the sign of x_a y_b - y_a x_b.
    u x w = normal |u|^2 (u lies in the plane), so CCW in (x, y) is CCW seen
    from outside. For a convex facet the vertex centroid is interior and no
    two vertices share a direction from it, so the comparator is a strict
    total order. No floating point anywhere."""
    c = tuple(sum(p[k] for p in pts) / len(pts) for k in range(3))
    u = _sub(pts[1], pts[0])
    w = _cross(normal, u)
    xy = [(_dot(_sub(p, c), u), _dot(_sub(p, c), w)) for p in pts]

    def half(v):                       # 0: angle in [0, pi); 1: in [pi, 2 pi)
        return 0 if (v[1] > 0 or (v[1] == 0 and v[0] > 0)) else 1

    def cmp(i, j):
        a, b = xy[i], xy[j]
        ha, hb = half(a), half(b)
        if ha != hb:
            return -1 if ha < hb else 1
        cr = a[0]*b[1] - a[1]*b[0]
        return -1 if cr > 0 else (1 if cr < 0 else 0)
    return [pts[m] for m in sorted(range(len(pts)), key=functools.cmp_to_key(cmp))]


def order_cycle(pts, normal):
    """Cyclic order of coplanar exact points, CCW as seen from outside (outward
    normal). Float atan2 PROPOSES the order; the exact cross-product convexity
    check DECIDES (audit_t1_independent.py facets() pattern, lines 58-74).
    FALLBACK (2026-09-04): if the float proposal fails the exact check (seen on
    two PERIOD-5652 Schmitt rows, where the (u, w) frame is so anisotropic
    that every float angle collapses to +-pi/2), order_cycle_exact supplies
    the order and must pass the SAME check. Whenever the float order passes
    it is returned unchanged, so accepted outputs are byte-identical."""
    c = tuple(sum(p[k] for p in pts) / len(pts) for k in range(3))
    u = _sub(pts[1], pts[0])
    w = _cross(normal, u)
    ang = sorted(range(len(pts)),
                 key=lambda m: math.atan2(float(_dot(_sub(pts[m], c), w)),
                                          float(_dot(_sub(pts[m], c), u))))
    poly = [pts[m] for m in ang]
    if not _convex_cycle_ok(poly, normal):
        poly = order_cycle_exact(pts, normal)        # floats failed: exact decides
    assert _convex_cycle_ok(poly, normal), \
        "facet ordering failed exact convexity check"
    return poly


def clip_cell(center, base_points, period, gram=None, D=None):
    """Exact Voronoi cell of `center` in the periodic set (base_points mod period).

    Returns dict: facet_cycles (vertex-id cycles, all CCW-from-outside),
    neighbors (site per facet), vertices (exact Fraction triples by id),
    p_vector, facet_count, n_vertices, nonsimple_vertices, cutoff_D, rho2.
    """
    if gram is not None:
        raise NotImplementedError(
            "TODO Gram-metric phase (design §1.3): bisector 2(r-c)^T G x = "
            "r^T G r - c^T G c, G-norm sort, G-ball cutoff bound")
    center = tuple(int(x) for x in center)
    D = D if D is not None else 2 * period
    while True:
        cands = candidates_near(center, base_points, period, D)
        verts, planes = _clip(center, cands, B=D)
        rho2 = max(sum((v[k]-center[k])**2 for k in range(3)) for v, _ in verts)
        if 4 * rho2 <= D * D:            # provable cutoff, exact comparison
            break
        D *= 2
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
    return {
        'center': center,
        'facet_cycles': cycles,
        'neighbors': nbrs,
        'vertices': used,
        'p_vector': tuple(sorted(len(c) for c in cycles)),
        'facet_count': len(cycles),
        'n_vertices': len(used),
        # design §6.2: >3 non-redundant planes through a vertex = non-simple
        # (permanent for symmetric configs like FCC; flagged, never hidden)
        'nonsimple_vertices': sum(1 for k in inc if k > 3),
        'cutoff_D': D,
        'rho2': rho2,
    }


def _selftest():
    # Simple cubic 2Z^3 -> cube: 6 quads, 8 simple vertices.
    c = clip_cell((0, 0, 0), [(0, 0, 0)], 2)
    assert c['p_vector'] == (4,)*6 and c['n_vertices'] == 8 \
        and c['nonsimple_vertices'] == 0, c['p_vector']
    # BCC -> truncated octahedron: 6 squares + 8 hexagons, simple.
    c = clip_cell((0, 0, 0), [(0, 0, 0), (1, 1, 1)], 2)
    assert c['p_vector'] == (4,)*6 + (6,)*8 and c['n_vertices'] == 24 \
        and c['nonsimple_vertices'] == 0, c['p_vector']
    # FCC -> rhombic dodecahedron: 12 rhombi, 6 non-simple (degree-4) vertices.
    c = clip_cell((0, 0, 0), [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)], 2)
    assert c['p_vector'] == (4,)*12 and c['n_vertices'] == 14 \
        and c['nonsimple_vertices'] == 6, (c['p_vector'], c['nonsimple_vertices'])
    print("exact_cell.py selftest: PASS (cube / truncated octahedron / rhombic "
          "dodecahedron incl. non-simple vertex flag)")


if __name__ == "__main__":
    _selftest()
