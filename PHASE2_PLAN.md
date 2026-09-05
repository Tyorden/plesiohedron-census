# PHASE 2 PLAN — metric-parameterized sweeps, tetragonal groups first (2026-09-03)

Status: GROUNDWORK ONLY. G2b (metric controls) PASSED 21/21 in the builder's
run (harness/phase2/G2B_RESULT.md); acceptance requires the main-session
re-run of `phase2/g2b_controls.py` (exit 0). NO hunt sweep has been run.
Sources: HARNESS_DESIGN §2.1 Phase 2, §2.3, §6; ANCHORS G2b block; Schmitt
2016 §2.2.2 (printed pp. 27-48: b-ratio 1/2..7/2 in 1001 steps of 3/1000,
~10^6 grid points per b-ratio, 68 tetragonal groups).

## 0. What G2b established (the tools this plan runs on)

- `phase2/metric.py`: integer Gram matrices per crystal family from rational
  c/a (tetragonal diag(q^2,q^2,p^2); hexagonal family in the ITA hexagonal
  basis [[2q^2,-q^2,0],[-q^2,2q^2,0],[0,0,2p^2]]); exact bisectors, G-norm,
  exact coordinate bound for candidate completeness; R^T G R = G check.
- `phase2/sweep_voronoi_gram.py` (float proposal, delegates to the accepted
  Gram hook of sweep_voronoi.sweep after exact validation) and
  `phase2/exact_cell_gram.py` (exact clipper, metric-correct 4*rho^2 <= D^2
  certificate). Accepted modules untouched.
- Controls reproduced: hexagonal prism (P6/mmm 1a, three c/a), elongated
  dodecahedron (BCT = I4/mmm 2a and I4 2a, c/a in {3/2, 2, 7/2}) and truncated
  octahedron (c/a in {1/2, 1, 7/5}) by canonical code + aut; cubic identity
  metric byte-identical to the non-Gram path; three of Schmitt's printed
  tetragonal rows (IT 75/76/77) reproduce his f-vectors exactly, including the
  24-facet (44,66,24) cell at b-ratio 797/1000 — his point/b-ratio conventions
  are now confirmed for tetragonal groups (points in the space-group
  coordinate system; b-ratio = c/a).

## 1. Sweep design — tetragonal groups (IT 75-142, 68 groups) FIRST

Why tetragonal first: one metric parameter, orthogonal conventional basis
(diagonal Gram, cheapest exact arithmetic), Schmitt's tables for these groups
are fully printed (pp. 27-48) so type-level collision screening is possible
row by row, and his runners-up live here (IT(98) I4_122: second-most facets,
35). Hexagonal family (52 groups, also one parameter) is the SECOND batch with
the same machinery (metric.gram_hexagonal already gated by (a)).

Per group, the candidate set is a product ORBITS x B-RATIOS (orbits are
metric-independent; stabilizers depend only on the ops):

(i) POINT MENU (mirrors the accepted phase-1 menu, exact, from the frozen
    G1 ops only):
    - special positions: scan the per-coordinate denominator {1,2,3,4,6,8,12}
      grid (4096 points), keep stabilizer order > 1, dedupe by full orbit,
      one canonical representative per orbit, record stratum dimension
      (0 fixed Wyckoff point, 1 Wyckoff-line sample, 2 plane sample);
    - Wyckoff LINES get an extra 1-D refinement: for each line stratum the
      free coordinate is sampled at denominators up to 24 (the phase-1 gap
      "line regions between samples" is closed one level deeper);
    - 2 general-position rational controls per group (as phase 1);
    - Schmitt's printed generating points for the group (all rows, at their
      printed b-ratio) as COLLISION-SCREEN candidates — run through the same
      chain, f-vector must reproduce (else FVEC-MISMATCH quarantine), type
      recorded as "Schmitt-printed" in the store.
    Counts (exact, plan_counts.py, 57.6 s): 5,689 special-position orbits
    over the 68 groups (198 fixed points, 1,843 line samples, 3,648 plane
    samples) + 136 general controls = 5,825 orbits. Per-group table below.

(ii) B-RATIO GRID (c/a, rational, Schmitt's range 1/2..7/2):
    coarse: {1/2, 3/4, 1, 5/4, 3/2, 7/4, 2, 9/4, 5/2, 11/4, 3, 13/4, 7/2}
    (13 values, step 1/4) + the special values sqrt2-bracket {7/5, 3/2} (BCT
    transition; 3/2 already in) + Schmitt's printed non-grid b-ratios that
    appear in the IT(75)-IT(142) tables (797/1000, 3497/1000, 377/250,
    38/25, 2, ... — harvested from the pdftotext layer at run time and
    cross-read). Budget assumption: 18 b-ratio values.
    TRANSITION BISECTION (design §2.3, 1-D here): for each orbit, adjacent
    b-ratio values with different canonical codes get the interval bisected
    (denominator doubling, depth <= 4) to harvest thin strata; the same rule
    across grid-adjacent points at fixed b-ratio is carried over from the
    design but was NOT run in phase 1 and stays optional here (recorded
    either way).

(iii) CHAIN per (orbit, b-ratio): orbit.py -> sweep_gram (W=2, W=3 retry)
    -> exact_cell_gram (one exact representative per orbit; congruence
    argument as phase 1 — the group acts transitively by isometries of the
    Gram metric, asserted via R^T G R = G) -> canonical_code -> store.
    G3 invariant: nothing mints without exact agreement; degeneracy-flagged
    float cells are superseded by exact (recorded); non-simple vertices
    recorded, never fatal; lattice-degenerate orbits must match a seeded
    parallelohedron code or are quarantined.

## 2. Candidate counts and runtime estimate

- Candidates: 5,825 orbits x 13 b-ratios = 75,725 (coarse grid);
  x 18 = 104,850 (with Schmitt's printed values). Bisection adds at most
  ~2x on the transitions actually found (cap depth 4, cap per orbit).
- Cost per candidate, measured (G2b + plan_counts.py benchmark, single
  process, Apple M3 Max): float proposal 0.01-0.20 s (16-32 pts/cell,
  PERIOD up to 12012); exact clip + canon 0.03-0.71 s (F=5 to F=24; the
  24-facet Schmitt cell took 0.22 s total). Exact runs on every candidate
  whose float fingerprint is not already an exactly-confirmed type, so the
  worst case is exact everywhere: budget 0.3 s/candidate average.
- Wall: 75,725 x 0.3 s = 6.3 h single-core = ~32 min on 12 workers;
  104,850 candidates = ~45 min; with bisection and W=3 retries <= ~1.5 h.
  Phase-1 precedent: 1,597 orbits in 215 s (0.13 s/orbit) single process.
- Hexagonal-family batch (52 groups) is expected to be of the same order
  (orbit counts not yet enumerated; run plan_counts.py with family
  'hexagonal' before scheduling).

## 3. Kill criteria (carried over verbatim in force)

- Any cell with > 38 facets (float or exact) = assume bug until proven
  otherwise: quarantine the record, do not store as a type, re-derive by
  hand before anyone says "record".
- Schmitt-complete-and-contains-candidate => reframe to first-realization /
  naming, never novelty. All store language: "not matched against catalog
  snapshot of <date>". No public naming or announcement before G5.
- Crash or unflagged float/exact disagreement => quarantine, skip, never
  patch mid-run. Site-stabilizer order must divide the combinatorial aut
  order (else quarantine). Lattice-degenerate orbits must match a seeded
  parallelohedron code (else quarantine as a bug).
- Wall + disclosure rules apply; measurement framing on all claims.
- Phase-2 specific: any orbit whose exact cells DISAGREE in (F, p-vector)
  across the orbit at one b-ratio (congruence violated) => quarantine the
  group at that b-ratio (would indicate a Gram/ops incompatibility that the
  R^T G R = G assertion should have caught).

## 4. Deferred / open

- c/a = sqrt2 and other irrational transition values are not representable;
  the rational bracket approach is the policy (recorded in G2B_RESULT.md).
- Orthorhombic (two parameters; metric.gram_orthorhombic exists, ungated) and
  monoclinic/triclinic (NotImplementedError by design) remain deferred.
- Wyckoff-line denominators beyond 24 and 2-D plane refinement: later
  optimization, not in the first tetragonal run.

## Appendix — per-group orbit counts (plan_counts.py output, 2026-09-03)

```
tetragonal groups: 68; special-position orbits on the {1,2,3,4,6,8,12} grid: 5689 (dim0 198, dim1 1843, dim2 3648); general controls: 136; enumeration 57.6s
per group: number name n_ops mult dim0 dim1 dim2 general
    75 P4             4 1   0  48   0 2
    76 P4_1           4 1   0   0   0 2
    77 P4_2           4 1   0  32   0 2
    78 P4_3           4 1   0   0   0 2
    79 I4             8 2   0  24   0 2
    80 I4_1           8 2   0  16   0 2
    81 P-4            4 1   4  30   0 2
    82 I-4            8 2   4  14   0 2
    83 P4/m           8 1   6  21 126 2
    84 P4_2/m         8 1   6  13 126 2
    85 P4/n           8 1   4  23   0 2
    86 P4_2/n         8 1   4  15   0 2
    87 I4/m          16 2   5  10  63 2
    88 I4_1/a        16 2   4   7   0 2
    89 P422           8 1   6  63   0 2
    90 P42_12         8 1   2  37   0 2
    91 P4_122         8 1   0  48   0 2
    92 P4_12_12       8 1   0  16   0 2
    93 P4_222         8 1   6  55   0 2
    94 P4_22_12       8 1   2  29   0 2
    95 P4_322         8 1   0  48   0 2
    96 P4_32_12       8 1   0  16   0 2
    97 I422          16 2   4  38   0 2
    98 I4_122        16 2   2  37   0 2
    99 P4mm           8 1   0  48 336 2
   100 P4bm           8 1   0  32 112 2
   101 P4_2cm         8 1   0  24 112 2
   102 P4_2nm         8 1   0  24 112 2
   103 P4cc           8 1   0  24   0 2
   104 P4nc           8 1   0  24   0 2
   105 P4_2mc         8 1   0  32 224 2
   106 P4_2bc         8 1   0  16   0 2
   107 I4mm          16 2   0  24 168 2
   108 I4cm          16 2   0  16  56 2
   109 I4_1md        16 2   0  16 112 2
   110 I4_1cd        16 2   0   8   0 2
   111 P-42m          8 1   6  49 112 2
   112 P-42c          8 1   6  41   0 2
   113 P-42_1m        8 1   2  23 112 2
   114 P-42_1c        8 1   2  15   0 2
   115 P-4m2          8 1   4  44 224 2
   116 P-4c2          8 1   4  28   0 2
   117 P-4b2          8 1   4  28   0 2
   118 P-4n2          8 1   4  28   0 2
   119 I-4m2         16 2   4  28 112 2
   120 I-4c2         16 2   4  20   0 2
   121 I-42m         16 2   4  24  56 2
   122 I-42d         16 2   2  23   0 2
   123 P4/mmm        16 1   6  63 189 2
   124 P4/mcc        16 1   6  30  63 2
   125 P4/nbm        16 1   6  34  55 2
   126 P4/nnc        16 1   5  31   0 2
   127 P4/mbm        16 1   4  28 105 2
   128 P4/mnc        16 1   4  17  63 2
   129 P4/nmm        16 1   4  29 167 2
   130 P4/ncc        16 1   3  18   0 2
   131 P4_2/mmc      16 1   6  48 147 2
   132 P4_2/mcm      16 1   6  37 105 2
   133 P4_2/nbc      16 1   5  27   0 2
   134 P4_2/nnm      16 1   6  30  55 2
   135 P4_2/mbc      16 1   4  13  63 2
   136 P4_2/mnm      16 1   4  24 105 2
   137 P4_2/nmc      16 1   3  22 112 2
   138 P4_2/ncm      16 1   4  17  55 2
   139 I4/mmm        32 2   5  34  94 2
   140 I4/mcm        32 2   5  23  52 2
   141 I4_1/amd      32 2   4  21  55 2
   142 I4_1/acd      32 2   3  18   0 2

timing benchmark (full Gram chain, one orbit each; NOT stored):
  #123 P4/mmm c/a=3/4: 16 pts/cell, PERIOD 12012, F=5, aut=12, float 0.05s (W=2), exact+canon 0.03s, agree=True
  #139 I4/mmm c/a=5/4: 32 pts/cell, PERIOD 12012, F=6, aut=4, float 0.11s (W=2), exact+canon 0.08s, agree=True
  #142 I4_1/acd c/a=9/4: 32 pts/cell, PERIOD 12012, F=16, aut=1, float 0.20s (W=2), exact+canon 0.71s, agree=True
```

## Appendix 2 — hexagonal family, per-group orbit counts (plan_counts.py hexagonal, 2026-09-04; batch 2)

Run with `phase2/plan_counts.py hexagonal` (family argument added 2026-09-04; the
default 'tetragonal' output is unchanged). Recorded BEFORE the batch-2 sweep.

```
hexagonal groups: 52; special-position orbits on the {1,2,3,4,6,8,12} grid: 4547 (dim0 120, dim1 1525, dim2 2902); general controls: 104; enumeration 42.1s
per group: number name n_ops mult dim0 dim1 dim2 general
   143 P3             3 1   0  48   0 2
   144 P3_1           3 1   0   0   0 2
   145 P3_2           3 1   0   0   0 2
   146 R3             9 3   0  24   0 2
   147 P-3            6 1   4  23   0 2
   148 R-3           18 3   4  11   0 2
   149 P312           6 1   6  47   0 2
   150 P321           6 1   2  53   0 2
   151 P3_112         6 1   0  32   0 2
   152 P3_121         6 1   0  32   0 2
   153 P3_212         6 1   0  32   0 2
   154 P3_221         6 1   0  32   0 2
   155 R32           18 3   2  57   0 2
   156 P3m1           6 1   0  48 208 2
   157 P31m           6 1   0  32 240 2
   158 P3c1           6 1   0  24   0 2
   159 P31c           6 1   0  24   0 2
   160 R3m           18 3   0  24 136 2
   161 R3c           18 3   0  12   0 2
   162 P-31m         12 1   6  26 119 2
   163 P-31c         12 1   5  23   0 2
   164 P-3m1         12 1   4  37 103 2
   165 P-3c1         12 1   3  26   0 2
   166 R-3m          36 3   4  33  67 2
   167 R-3c          36 3   3  28   0 2
   168 P6             6 1   0  48   0 2
   169 P6_1           6 1   0   0   0 2
   170 P6_5           6 1   0   0   0 2
   171 P6_2           6 1   0  32   0 2
   172 P6_4           6 1   0  32   0 2
   173 P6_3           6 1   0  24   0 2
   174 P-6            6 1   6  21 254 2
   175 P6/m          12 1   6  21 126 2
   176 P6_3/m        12 1   5  10 127 2
   177 P622          12 1   6  47   0 2
   178 P6_122        12 1   0  32   0 2
   179 P6_522        12 1   0  32   0 2
   180 P6_222        12 1   4  42   0 2
   181 P6_422        12 1   4  42   0 2
   182 P6_322        12 1   4  38   0 2
   183 P6mm          12 1   0  48 208 2
   184 P6cc          12 1   0  24   0 2
   185 P6_3cm        12 1   0  16 120 2
   186 P6_3mc        12 1   0  24 104 2
   187 P-6m2         12 1   6  47 205 2
   188 P-6c2         12 1   6  22 127 2
   189 P-62m         12 1   4  44 217 2
   190 P-62c         12 1   4  25 127 2
   191 P6/mmm        24 1   6  47 141 2
   192 P6/mcc        24 1   6  22  63 2
   193 P6_3/mcm      24 1   5  27 108 2
   194 P6_3/mmc      24 1   5  30 102 2

timing benchmark (full Gram chain, one orbit each; NOT stored):
  #191 P6/mmm c/a=3/4: 24 pts/cell, PERIOD 12012, F=5, aut=12, float 0.08s (W=2), exact+canon 0.05s, agree=True
  #166 R-3m c/a=5/4: 36 pts/cell, PERIOD 12012, F=8, aut=8, float 0.14s (W=2), exact+canon 0.14s, agree=True
  #167 R-3c c/a=9/4: 36 pts/cell, PERIOD 12012, F=14, aut=1, float 0.18s (W=2), exact+canon 0.70s, agree=True
```

Candidates planned: 4,651 orbits x 13 coarse b = 60,463 (P1) + 958 printed rows
x groups (P2) + 4,651 x 5 Schmitt b (P3) + 1/24-line orbits x 13 (P4) + bisection
(P5). Batch-2 execution: rule 29 (foreground invocations with a per-invocation
budget, resume log) — see STATUS 2026-09-04 batch-2 entry.
