#!/usr/bin/env python
"""plan_counts.py — PHASE2_PLAN groundwork numbers (NOT a hunt sweep).

Two things, both recorded in PHASE2_PLAN.md:
  1. Exact candidate counts for the tetragonal phase: for each of the 68
     tetragonal groups (IT 75-142) enumerate, with the frozen G1 ops, the
     special-position orbits on the phase-1 point menu (per-coordinate
     denominators {1,2,3,4,6,8,12}: 4096 grid points, exact stabilizer test,
     orbit-deduped) with stratum dimension (0 = fixed point, 1 = line sample,
     2 = plane sample), plus 2 general-position controls per group. Orbits are
     metric-independent, so candidates = orbits x b-ratio grid values.
  2. A timing benchmark: the full Gram chain on THREE general-position cells
     (P4/mmm #123, I4/mmm #139, I4_1/acd #142) at one b-ratio each. Nothing
     is stored, no types minted — a stopwatch, not a sweep.

Run: python3 plan_counts.py [tetragonal|hexagonal]
(family argument added 2026-09-04 for batch 2; default 'tetragonal' reproduces
the 2026-09-03 output; 'hexagonal' = IT 143-194 with metric.gram_hexagonal and a
benchmark on #191, #166, #167.)
"""
import itertools
import os
import sys
import time
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import orbit                                            # noqa: E402
import metric                                           # noqa: E402
from sweep_voronoi_gram import sweep_gram               # noqa: E402
from exact_cell_gram import clip_cell_gram              # noqa: E402
from canon_code import canonical_code                   # noqa: E402

DENS = (1, 2, 3, 4, 6, 8, 12)
COORDS = sorted({F(n, d) for d in DENS for n in range(d)})      # 16 values
GENERAL = [(F(1, 7), F(2, 11), F(3, 13)), (F(3, 17), F(5, 19), F(7, 23)),
           (F(2, 9), F(5, 27), F(11, 29))]


def stratum_dim(stab):
    """dim of the common fixed linear space of the stabilizer's rotation parts."""
    rows = []
    for R, _ in stab:
        for i in range(3):
            rows.append([F(R[i][j]) - (1 if i == j else 0) for j in range(3)])
    # rank via Gaussian elimination (exact)
    rank, m = 0, [r[:] for r in rows]
    for col in range(3):
        piv = next((r for r in range(rank, len(m)) if m[r][col] != 0), None)
        if piv is None:
            continue
        m[rank], m[piv] = m[piv], m[rank]
        for r in range(len(m)):
            if r != rank and m[r][col] != 0:
                f = m[r][col] / m[rank][col]
                m[r] = [a - f * b for a, b in zip(m[r], m[rank])]
        rank += 1
    return 3 - rank


FAMILIES = {                     # family -> (expected group count, Gram, benchmark (group, c/a))
    "tetragonal": (68, metric.gram_tetragonal, ((123, F(3, 4)), (139, F(5, 4)), (142, F(9, 4)))),
    "hexagonal": (52, metric.gram_hexagonal, ((191, F(3, 4)), (166, F(5, 4)), (167, F(9, 4)))),
}


def main(family="tetragonal"):
    """family: 'tetragonal' (default; output unchanged from the 2026-09-03 run)
    or 'hexagonal' (batch 2, added 2026-09-04: trigonal + hexagonal groups
    IT 143-194 on hexagonal axes, Gram = metric.gram_hexagonal)."""
    n_expected, gram_fn, bench_spec = FAMILIES[family]
    groups = orbit.load_groups()
    tet = [g for n, g in sorted(groups.items()) if g["crystal_family"] == family]
    assert len(tet) == n_expected
    t0 = time.time()
    total = {0: 0, 1: 0, 2: 0}
    per_group = []
    for g in tet:
        seen, dims = set(), {0: 0, 1: 0, 2: 0}
        for p in itertools.product(COORDS, repeat=3):
            key = tuple(p)
            if key in seen:
                continue
            stab = orbit.site_stabilizer(g, p)
            if len(stab) == 1:
                continue
            ob = orbit.orbit(g, p)
            seen |= set(ob["points"])
            dims[stratum_dim(stab)] += 1
        ngen = sum(1 for q in GENERAL if len(orbit.site_stabilizer(g, q)) == 1)
        per_group.append((g["number"], g["international_short"], g["n_ops"],
                          g["centering"]["multiplicity"], dims, min(ngen, 2)))
        for k in dims:
            total[k] += dims[k]
    n_special = sum(total.values())
    n_general = sum(x[5] for x in per_group)
    t_enum = time.time() - t0
    print(f"{family} groups: {n_expected}; special-position orbits on the "
          f"{{1,2,3,4,6,8,12}} grid: {n_special} (dim0 {total[0]}, dim1 {total[1]}, "
          f"dim2 {total[2]}); general controls: {n_general}; enumeration {t_enum:.1f}s")
    print("per group: number name n_ops mult dim0 dim1 dim2 general")
    for num, name, nops, mult, dims, ngen in per_group:
        print(f"  {num:4d} {name:12s} {nops:3d} {mult} {dims[0]:3d} {dims[1]:3d} "
              f"{dims[2]:3d} {ngen}")

    # timing benchmark: three general-position cells, one b-ratio each
    print("\ntiming benchmark (full Gram chain, one orbit each; NOT stored):")
    bench = []
    for num, b in bench_spec:
        g = groups[num]
        p = GENERAL[0]
        t1 = time.time()
        ob = orbit.orbit(g, p)
        pts, period = orbit.scale_orbit(ob["points"])
        G = gram_fn(b)
        W = 2
        while True:
            try:
                cf = sweep_gram(pts, period, G, W=W, entry=g); break
            except RuntimeError:
                W += 1
        tf = time.time() - t1
        t2 = time.time()
        e = clip_cell_gram(pts[0], pts, period, G)      # one representative
        code, aut = canonical_code(e["facet_cycles"])
        te = time.time() - t2
        ok = e["facet_count"] == cf[0]["facet_count"] and e["p_vector"] == cf[0]["p_vector"]
        bench.append((num, g["international_short"], b, ob["n_conventional"], period,
                      e["facet_count"], tf, te, ok))
        print(f"  #{num} {g['international_short']} c/a={b}: {ob['n_conventional']} pts/cell, "
              f"PERIOD {period}, F={e['facet_count']}, aut={aut}, float {tf:.2f}s "
              f"(W={W}), exact+canon {te:.2f}s, agree={ok}")
    return per_group, total, n_general, bench


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "tetragonal")
