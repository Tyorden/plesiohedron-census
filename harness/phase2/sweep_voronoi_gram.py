#!/usr/bin/env python
"""sweep_voronoi_gram.py — float Voronoi SEARCH phase under a Gram metric.

Phase-2 SIBLING of ../sweep_voronoi.py (untouched). Honest reuse note: the
accepted sweep() already carries the design's Gram hook (it Cholesky-embeds
a `gram` argument into Cartesian coordinates for Qhull). This module adds what
the hook lacks and phase 2 needs, without editing it:

  1. EXACT validation of the metric before any float touches it: symmetric,
     positive definite (Sylvester, Fractions), and — when a group entry is
     given — R^T G R = G for every op (metric.gram_compatible).
  2. A well-conditioned PROPOSAL embedding: the integer Gram matrices from
     metric.py can carry entries like 10^6 (b-ratio 797/1000); Qhull is given
     G / max|G_ij| (a uniform similarity — same Voronoi combinatorics) so
     embedded coordinates stay O(period * W). Proposal-side rescaling only.
  3. Exact G-norm distances of the proposed neighbors (Fractions, from the
     integer site deltas — floats never enter this number), for reports.

Floats PROPOSE here; nothing from this module is a decision (ANCHORS G3).
Every cell summary that would mint a type is re-derived by
exact_cell_gram.clip_cell_gram.
"""
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))          # ../ : accepted modules

from sweep_voronoi import sweep                       # noqa: E402
import metric                                          # noqa: E402


def sweep_gram(base_points, period, gram, W=2, degen_rtol=1e-9, entry=None):
    """Replicate the integer orbit over a (2W+1)^3 block, embed with the Gram
    metric (float, proposal), run scipy Voronoi via the accepted sweep(), and
    summarize each central cell. Adds 'neighbor_gnorm2' (exact Fractions in
    the G-norm of the integer-scaled Gram) to each cell dict.

    Raises RuntimeError (from sweep) on the window guards; ValueError if the
    metric is not an exact symmetric positive-definite Gram matrix or is not
    preserved by the group's ops."""
    if not metric.is_positive_definite(gram):
        raise ValueError("gram is not a symmetric positive-definite matrix")
    G, _ = metric.scale_to_integers(gram)
    if entry is not None and not metric.gram_compatible(entry, G):
        raise ValueError(f"group #{entry['number']}: ops do not preserve gram")
    m = max(abs(x) for row in G for x in row)
    G_prop = [[F(x, m) for x in row] for row in G]     # similarity; floats later
    cells = sweep(base_points, period, W=W, gram=G_prop, degen_rtol=degen_rtol)
    for c in cells:
        c['neighbor_gnorm2'] = [metric.gnorm2(G, d) for d in c['neighbor_deltas']]
        c['gram'] = G
    return cells


def _selftest():
    # Hexagonal lattice c/a = 1 -> hexagonal prism; every neighbor at a
    # G-distance^2 of 2 (six in-plane, |a|^2 = 2 in the scaled Gram) or 2 (c).
    cells = sweep_gram([(0, 0, 0)], 1, metric.gram_hexagonal(1), W=2)
    assert cells[0]['p_vector'] == (4,) * 6 + (6,) * 2, cells[0]['p_vector']
    assert sorted(cells[0]['neighbor_gnorm2']) == [2] * 8
    # BCT c/a = 7/2 -> 12 facets (8 quads + 4 hexagons) proposed.
    cells = sweep_gram([(0, 0, 0), (1, 1, 1)], 2, metric.gram_tetragonal(F(7, 2)), W=2)
    assert all(c['p_vector'] == (4,) * 8 + (6,) * 4 for c in cells), \
        [c['p_vector'] for c in cells]
    # Bad metric rejected exactly.
    try:
        sweep_gram([(0, 0, 0)], 1, ((1, 2, 0), (2, 1, 0), (0, 0, 1)))
        raise AssertionError("indefinite Gram accepted")
    except ValueError:
        pass
    print("sweep_voronoi_gram.py selftest: PASS (hex prism proposal / BCT 7/2 "
          "proposal / indefinite metric rejected)")


if __name__ == "__main__":
    _selftest()
