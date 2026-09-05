#!/usr/bin/env python
"""sweep_voronoi.py — float Voronoi search phase (design doc §1.3).

Floats PROPOSE here; nothing from this module is a decision. Any cell summary
that would mint a new type must be re-derived exactly (exact_cell.clip_cell) —
design §1.3 "when is exact run", ANCHORS G3.

Ancestor: build_josehedron.py:80-115 (replicated block, scipy.spatial.Voronoi,
ridge readoff via ridge_points / ridge_vertices).

Guards (the g1_verify:83-84 bounding-box guard, float-phase analogue): a
central cell may not touch an unbounded ridge (-1 vertex), and none of its
Voronoi neighbors may lie in the outermost replication shell — either means
the (2W+1)^3 window is too small; raise, never truncate silently.

Degeneracy proposal flag (design §6.2a): a Voronoi vertex of a central cell
with >4 near-equidistant sites (relative tol 1e-9) marks the cell
degenerate_flag=True — the caller must route it to the exact clipper. Note
that permanently symmetric configurations (FCC, simple cubic) live on such
degeneracies; the flag is information, not an error.
"""
import itertools
from collections import defaultdict

import numpy as np
from scipy.spatial import Voronoi


def sweep(base_points, period, W=2, gram=None, degen_rtol=1e-9):
    """Replicate the integer orbit over a (2W+1)^3 block, run scipy Voronoi,
    and summarize each central cell.

    base_points: integer triples mod period (orbit.scale_orbit output).
    gram: optional rational Gram matrix for non-cubic cells; used only to build
      the float Cartesian embedding (Cholesky) for Qhull — a PROPOSAL, per the
      house rule. Exact decisions stay in fractional coordinates downstream.

    Returns a list (one dict per base point, in base_points order):
      facet_count, p_vector (sorted facet polygon sizes), neighbor_deltas
      (integer site deltas in fractional-scaled coords), degenerate_flag.
    """
    base_points = [tuple(int(x) for x in p) for p in base_points]
    rng = range(-W, W + 1)
    pts, tag = [], []
    for n in itertools.product(rng, rng, rng):
        for bi, (x, y, z) in enumerate(base_points):
            pts.append((x + period*n[0], y + period*n[1], z + period*n[2]))
            tag.append((bi, n))
    pts_int = np.array(pts, dtype=np.int64)
    X = pts_int.astype(float)
    if gram is not None:
        G = np.array([[float(g) for g in row] for row in gram])
        A = np.linalg.cholesky(G).T          # x^T G x = |A x|^2 (float proposal)
        X = X @ A.T
    vor = Voronoi(X)

    central = {bi: i for i, (bi, n) in enumerate(tag) if n == (0, 0, 0)}
    assert len(central) == len(base_points)

    ridge = defaultdict(list)
    for (p, q), rv in zip(vor.ridge_points, vor.ridge_vertices):
        ridge[p].append((q, rv))
        ridge[q].append((p, rv))

    out = []
    for bi in range(len(base_points)):
        pi = central[bi]
        cell = ridge[pi]
        for q, rv in cell:
            if -1 in rv:
                raise RuntimeError(
                    f"cell {bi}: unbounded ridge — window W={W} too small")
            if max(abs(c) for c in tag[q][1]) >= W:
                raise RuntimeError(
                    f"cell {bi}: neighbor in outermost shell — W={W} too small")
            assert len(rv) >= 3, f"cell {bi}: ridge with <3 vertices"
        sizes = tuple(sorted(len(rv) for _, rv in cell))
        deltas = [tuple(int(v) for v in (pts_int[q] - pts_int[pi]))
                  for q, _ in cell]
        vidx = sorted({i for _, rv in cell for i in rv})
        flag = False
        for i in vidx:
            d2 = np.sum((X - vor.vertices[i])**2, axis=1)
            m = d2.min()
            if int((d2 <= m * (1 + degen_rtol)).sum()) > 4:
                flag = True
                break
        out.append({'base_index': bi,
                    'facet_count': len(cell),
                    'p_vector': sizes,
                    'neighbor_deltas': deltas,
                    'degenerate_flag': flag})
    return out


def _selftest():
    # Simple cubic 2Z^3 -> cube; vertex has 8 equidistant sites -> flagged.
    cells = sweep([(0, 0, 0)], 2, W=2)
    assert cells[0]['p_vector'] == (4,)*6, cells[0]['p_vector']
    assert cells[0]['degenerate_flag'] is True
    # BCC -> truncated octahedron, simple (generic) -> unflagged.
    cells = sweep([(0, 0, 0), (1, 1, 1)], 2, W=2)
    assert all(c['p_vector'] == (4,)*6 + (6,)*8 for c in cells), \
        [c['p_vector'] for c in cells]
    assert all(c['degenerate_flag'] is False for c in cells)
    print("sweep_voronoi.py selftest: PASS (cube flagged-degenerate / "
          "truncated octahedron clean)")
    # FCC -> rhombic dodecahedron: informational only — Qhull may or may not
    # resolve the degenerate (6-equidistant) vertices cleanly; exact decides.
    cells = sweep([(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)], 2, W=2)
    print("  FCC (informational): p_vectors",
          sorted(set(c['p_vector'] for c in cells)),
          "flags", [c['degenerate_flag'] for c in cells])


if __name__ == "__main__":
    _selftest()
