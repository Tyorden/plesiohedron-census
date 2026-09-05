# Nice-point search — nicest presentation inside the certified open neighbourhood, top-3 pool cells per system (2026-09-04)

Staging only. Naming is Tyler's alone; this document proposes NO names. The nine
cells are the top 3 per system of POOL_RANKING_2026-09-04.md (accepted 2026-09-04
15:40): every one a certified space-filler (G4 ladder V0-V3, twice-derived) whose
computed open/wall verdict is OPEN (harness/phase2/WALL_OPEN_PHASE2.json, md5
6b257c551f6fb275dfabb03e992f57c2). Novelty wording, everywhere: "not matched against
the records checked as of 2026-09-04" — never "new". OPEN means "holds on the tested
neighbourhood", never an interval proof. AI disclosure: computed and written by a
Claude subagent (#153, Claude Fable 5.1) on 2026-09-04; provisional until the main
session re-runs the verify command at the end.

<!-- PREREG-BEGIN -->
## Pre-registered search and scoring (written 2026-09-04 15:10 PDT, BEFORE any chain evaluation)

Question: inside the neighbourhood WALL_OPEN_PHASE2 certified for each cell, is there a
generating point / c/a with a nicer exact presentation (smaller vertex-coordinate
denominators) that yields the SAME canonical combinatorial type?

Cells (9): the rank-1..3 rows per system of POOL_RANKING_2026-09-04.json (md5
75cacf7e762bda859234d2843888cb94): tetragonal `4e9c9b076cfec323` (IT 92), `164d4bd63d82d0c3`
(IT 76), `6797ab70c6015039` (IT 76); trigonal `a93f8fe7ecdc5851`, `e598ffd8a1cac138`,
`c0071756347c5a8a` (all IT 144); hexagonal `c49077384aaebeb0` (IT 178), `8d90c524c89922d9`,
`9c0b7e0c29dfebb2` (both IT 169).

Certified neighbourhood (read from WALL_OPEN_PHASE2.json, never widened): for each
on-stratum point direction d recorded in the cell's rows (the c1 tangent basis; asserted
equal to nullspace_basis(site stabilizer)) and for the metric direction, and for each sign,
the EXTENT is the largest tested |eps| such that every tested step on that side with
|eps'| <= |eps| is SAME (refinement rows included); 0 if the smallest tested step on that
side is not SAME. Point steps are in fractional coordinates of the ITA conventional cell
(hexagonal basis for IT 143-194); metric steps are relative, c/a -> c/a (1 + eps).

Search set per cell (exact rationals; enumerated by `nice_points_2026-09-04.py --plan`
before any chain evaluation — the enumeration is quoted below verbatim):
- points q = p0 + sum_i t_i d_i with t_i in [-ext_minus_i, +ext_plus_i] and EVERY
  coordinate of q a rational with denominator <= 48 (Farey set of order 48 on each
  direction's leading coordinate; for the dim-1 cells all three coordinates of the
  moved point must satisfy the bound);
- c/a values: rationals with denominator <= 16 in [b0 (1 - em), b0 (1 + ep)], plus the
  witness c/a itself (29/32 for `e598ffd8a1cac138` has denominator 32 and is kept as the
  witness value);
- candidates = points x c/a values; the witness is a member of every set.
The box is the PRODUCT of per-direction certified extents. WALL_OPEN tested axis-parallel
steps only; off-axis interior points (two or three coordinates moved, or a coordinate
moved together with c/a) and on-axis points strictly between tested steps were never
evaluated there. Their type-sameness is therefore a genuine test here, not a consequence.

Enumerated search set (from `--plan`, 2026-09-04 15:09 PDT):
- `4e9c9b076cfec323` tetragonal IT(92) P4_12_12 witness (5/24, 5/24, 0) c/a 5/4 (stratum dim 1): direction (1, 1, 0) extents [-1/48, +1/768]; metric relative extents [-1/96, +1/96] -> c/a band [475/384, 485/384], c/a candidates {5/4}; points 16; candidates 16
- `164d4bd63d82d0c3` tetragonal IT(76) P4_1 witness (1/8, 1/6, 5/12) c/a 5/4 (stratum dim 3): direction (0, 0, 1) extents [-1/48, +1/48]; direction (0, 1, 0) extents [-1/96, +1/96]; direction (1, 0, 0) extents [-1/192, +1/192]; metric relative extents [-1/96, +1/192] -> c/a band [475/384, 965/768], c/a candidates {5/4}; points 3045; candidates 3045
- `6797ab70c6015039` tetragonal IT(76) P4_1 witness (1/8, 1/6, 5/12) c/a 3/2 (stratum dim 3): direction (0, 0, 1) extents [-1/48, +1/48]; direction (0, 1, 0) extents [-1/192, +1/48]; direction (1, 0, 0) extents [-1/48, +1/192]; metric relative extents [-1/96, +1/96] -> c/a band [95/64, 97/64], c/a candidates {3/2}; points 10440; candidates 10440
- `a93f8fe7ecdc5851` trigonal IT(144) P3_1 witness (1/12, 3/8, 1/6) c/a 9/8 (stratum dim 3): direction (0, 0, 1) extents [-1/48, +1/48]; direction (0, 1, 0) extents [-1/384, +1/48]; direction (1, 0, 0) extents [-1/192, +1/768]; metric relative extents [-1/192, +1/192] -> c/a band [573/512, 579/512], c/a candidates {9/8}; points 2376; candidates 2376
- `e598ffd8a1cac138` trigonal IT(144) P3_1 witness (1/8, 1/6, 5/12) c/a 29/32 (stratum dim 3): direction (0, 0, 1) extents [-1/48, +1/48]; direction (0, 1, 0) extents [-1/768, +1/96]; direction (1, 0, 0) extents [-1/192, +1/768]; metric relative extents [-1/96, +1/384] -> c/a band [2755/3072, 11165/12288], c/a candidates {9/10, 29/32}; points 928; candidates 1856
- `c0071756347c5a8a` trigonal IT(144) P3_1 witness (1/12, 3/8, 1/6) c/a 1 (stratum dim 3): direction (0, 0, 1) extents [-1/48, +1/48]; direction (0, 1, 0) extents [-1/48, +1/48]; direction (1, 0, 0) extents [-1/384, +1/96]; metric relative extents [-1/96, +1/96] -> c/a band [95/96, 97/96], c/a candidates {1}; points 11220; candidates 11220
- `c49077384aaebeb0` hexagonal IT(178) P6_122 witness (1/12, 1/6, 1/4) c/a 5/4 (stratum dim 1): direction (1, 2, 0) extents [-1/192, +1/192]; metric relative extents [-1/96, +1/96] -> c/a band [475/384, 485/384], c/a candidates {5/4}; points 8; candidates 8
- `8d90c524c89922d9` hexagonal IT(169) P6_1 witness (1/12, 3/8, 1/6) c/a 11/8 (stratum dim 3): direction (0, 0, 1) extents [-1/48, +1/48]; direction (0, 1, 0) extents [-1/192, +1/192]; direction (1, 0, 0) extents [-1/96, +1/96]; metric relative extents [-1/192, +1/192] -> c/a band [2101/1536, 2123/1536], c/a candidates {11/8}; points 3696; candidates 3696
- `9c0b7e0c29dfebb2` hexagonal IT(169) P6_1 witness (1/12, 3/8, 1/6) c/a 3/4 (stratum dim 3): direction (0, 0, 1) extents [-1/48, +1/48]; direction (0, 1, 0) extents [-1/48, +1/192]; direction (1, 0, 0) extents [-1/1536, +1/48]; metric relative extents [-1/96, +1/384] -> c/a band [95/128, 385/512], c/a candidates {3/4}; points 10560; candidates 10560
- TOTAL candidates: 43217 (chain evaluations; SAME ones get a second derivation)
Note on what the enumeration already shows: only one cell (`e598ffd8a1cac138`) admits a
second c/a of denominator <= 16 inside its band (9/10); every other band around a
sweep c/a of denominator <= 8 contains no other such value. The c/a lever is therefore
almost entirely absent at this resolution; the search is a point search.

Chain (accepted, imported unchanged): sweep_phase2_tetragonal.evaluate /
sweep_phase2_hexagonal.evaluate — the SAME functions WALL_OPEN_PHASE2 used — on every
candidate; SAME iff the canonical code equals the store's canon_code for the cell;
DIFFERENT otherwise (the new type's code id and stored id, f, p, aut recorded);
ChainError -> QUARANTINE (recorded with its reason; neither SAME nor DIFFERENT). Every
SAME candidate is derived a SECOND time by g4_certify_gram.v0_rederive with the candidate
as a synthetic witness (asserts canonical code, f, p, aut against the frozen store) and
that exact cell (integer Gram metric, exact Fractions) supplies the vertices.

Niceness (lexicographic, smaller is nicer):
(a) m_lattice = lcm of the denominators of the SITE-CENTRED vertex coordinates in the
    conventional (lattice) basis — fractional coordinates of the ITA conventional cell,
    hexagonal basis (a, b, c) for IT 143-194; this is the pool ranking's m_lattice, so the
    witness value must reproduce the pool JSON (asserted);
(b) tetragonal: m_cartesian = least m with m x, m y, m (c/a) z integers over all
    site-centred vertices (integer Cartesian coordinates in units a/m; Cartesian rational
    iff c/a rational); hexagonal family: an integer Cartesian presentation does not exist in
    general (sqrt(3) in y), so (b) is m_eisenstein = lcm of the in-plane denominators
    (x + y*omega is an Eisenstein integer after scaling by m_eisenstein), with m_c (z
    denominators) and m_cartesian_sqrt3 (least m with (u, v sqrt(3), w)/m integers) reported;
(c) c/a simplicity: denominator, then numerator;
(d) lcm of the generating point's coordinate denominators; (e) the point (lexicographic).
Reported, not ranked: m_absolute_conventional (vertices not re-centred), stabilizer order,
non-simple vertex count, degeneracy flags. Top-3 presentations per cell go in the table;
the witness row is always shown for comparison.

Kill / discard criterion: any candidate whose exact type differs from the certified type
is DISCARDED from the presentation ranking and COUNTED. The count per cell is a check on
the open neighbourhood: EXPECTED 0. If nonzero, each changed candidate is located (which
coordinates moved; whether the step was axis-parallel from the witness) and the result is
reported as a finding about WALL_OPEN_PHASE2's step size / the product-of-intervals
reading of axis-tested extents, not as an error of this search and not as a change to any
OPEN verdict (those are statements about the tested steps). QUARANTINE counts are reported
alongside.

Josehedron comparison: the same functions applied to the Josehedron control (phase-1 store
`dfccc9ff6019ead5`, IT(220) Wyckoff 12a, generating point (3/8, 0, 1/4), cubic Gram) give
its site-centred vertex denominator in the conventional cubic basis (= its integer Cartesian
scale). Its published hook is integer vertex coordinates; the comparison states the best
scale found per cell against that number, and says plainly whether the hook exists here.

Compute plan: 43,217 chain evaluations at ~0.1 s each; multiprocessing Pool of 8 forked
workers (16 cores; protected PIDs 8014 / 7417 / 13578 untouched), run per cell in
foreground Bash calls with explicit timeouts (rule 29), per-cell result caches in
harness/phase2/nice_points_cells/ so no batch exceeds the call limit; the final JSON has
sorted keys and no timings, so the md5 is reproducible by a fresh full run.
<!-- PREREG-END -->

## Inputs and checks

- WALL_OPEN_PHASE2.json md5 6b257c551f6fb275dfabb03e992f57c2; POOL_RANKING_2026-09-04.json md5 75cacf7e762bda859234d2843888cb94; both stores sha256 as recorded in WALL_OPEN_PHASE2.json and unchanged after the run: True.
- Tangent directions read from the WALL_OPEN rows equal nullspace_basis(site stabilizer) (the c1 function) for all 9 cells; the witness point and c/a equal the pool-ranking rows and the stores' first_witness.
- Every candidate went through the accepted chain (S2/SH.evaluate); every SAME candidate was re-derived a second time by g4_certify_gram.v0_rederive as a synthetic witness (canonical code, f, p, aut asserted against the frozen store). The witness row's m_lattice (and m_cartesian, tetragonal) equals the pool-ranking value for all 9 cells (asserted).
- Candidates: 43217 over 9 cells; SAME 39659, DIFFERENT 3558, QUARANTINE 0; cells whose best presentation beats the witness: 6 of 9.
- Output JSON: harness/phase2/NICE_POINTS_2026-09-04.json (sorted keys, no timings), md5 cf6645fcbb96a530cbb71a2d20bb325a. 8 forked workers, foreground, per-cell caches in harness/phase2/nice_points_cells/ (runtime in STATUS.md).

## Per cell

### tetragonal #1 `4e9c9b076cfec323` IT(92) P4_12_12 — witness (5/24, 5/24, 0) at c/a 5/4, f = (40, 60, 22), p = 3^8 4^4 5^4 8^2 11^4, aut 2 / Isom 2

Search set: 16 points x 1 c/a values = 16 candidates (c/a candidates {5/4}); SAME 16, DIFFERENT 0, QUARANTINE 0, stabilizer-order changes 0.

| nice rank | generating point | c/a | m_lattice (site-centred, conventional) | m_cartesian | m_absolute | stab | nonsimple |
|---|---|---|---|---|---|---|---|
| 1 | (3/16, 3/16, 0) | 5/4 | 748000 | 149600 | 748000 | 2 | 0 |
| 2 | (1/5, 1/5, 0) | 5/4 | 14560000 | 2912000 | 14560000 | 2 | 0 |
| 3 | (5/24, 5/24, 0) | 5/4 | 38041920 | 7608384 | 38041920 | 2 | 0 |
| witness (3) | (5/24, 5/24, 0) | 5/4 | 38041920 | 7608384 | 38041920 | 2 | 0 |

Tellable coordinates: Generating point (3/16, 3/16, 0) at c/a = 5/4 in IT(92) P4_12_12 (f = (40, 60, 22), aut 2): the site-centred vertex coordinates in the conventional tetragonal basis have common denominator 748000; scaled by 149600 the vertices are integer Cartesian points (units a/149600, c = 5/4 a). This beats the sweep witness (5/24, 5/24, 0) at c/a = 5/4 (denominator 38041920, Cartesian scale 7608384; the witness ranks 3 of 16 type-preserving candidates). For scale: the Josehedron's vertices have denominator 24 in its conventional cubic cell.

### tetragonal #2 `164d4bd63d82d0c3` IT(76) P4_1 — witness (1/8, 1/6, 5/12) at c/a 5/4, f = (40, 60, 22), p = 3^6 4^6 5^2 6^4 11^4, aut 1 / Isom 1

Search set: 3045 points x 1 c/a values = 3045 candidates (c/a candidates {5/4}); SAME 2581, DIFFERENT 464, QUARANTINE 0, stabilizer-order changes 0.

| nice rank | generating point | c/a | m_lattice (site-centred, conventional) | m_cartesian | m_absolute | stab | nonsimple |
|---|---|---|---|---|---|---|---|
| 1 | (1/8, 1/6, 5/12) | 5/4 | 7257600 | 1451520 | 7257600 | 1 | 0 |
| 2 | (1/8, 1/6, 19/48) | 5/4 | 7257600 | 1451520 | 7257600 | 1 | 0 |
| 3 | (1/8, 1/6, 7/16) | 5/4 | 7257600 | 1451520 | 7257600 | 1 | 0 |
| witness (1) | (1/8, 1/6, 5/12) | 5/4 | 7257600 | 1451520 | 7257600 | 1 | 0 |

Tellable coordinates: Generating point (1/8, 1/6, 5/12) at c/a = 5/4 in IT(76) P4_1 (f = (40, 60, 22), aut 1): the site-centred vertex coordinates in the conventional tetragonal basis have common denominator 7257600; scaled by 1451520 the vertices are integer Cartesian points (units a/1451520, c = 5/4 a). No candidate in the search set beats the sweep witness; the witness is the best presentation found. The z coordinate is a free translation in this polar group (any z gives a congruent cell). For scale: the Josehedron's vertices have denominator 24 in its conventional cubic cell.

Polar group (every operation of IT(76) fixes the c direction): a shift of the generating point along z translates the whole orbit, so candidates that differ only in z are congruent cells with identical vertex denominators. The z-ties in the table are that congruence; the search is effectively over (x, y, c/a): 89 such classes kept the type, 16 changed it, 0 did both (a class doing both would contradict the congruence; 0 expected).

Type-changed candidates: 464 (discarded from the ranking; a finding about the box reading of WALL_OPEN_PHASE2's axis-tested extents). Axis-parallel from the witness (exactly one tested direction moved): 0; counting z as the free translation it is here, exactly one of (x, y, c/a) moved: 0. By number of point coordinates moved (+ca = c/a also moved): {'3+0': 448, '2+0': 16}. Other types reached: 086ac96faf390886 f=(36, 54, 20) p=3^2 4^8 5^6 10^4 aut 2 x464. Every changed candidate (point, c/a, type) is listed in the JSON (different_candidates); the full per-candidate rows, vertices included, are in the per-cell cache nice_points_cells/164d4bd63d82d0c3.json.

### tetragonal #3 `6797ab70c6015039` IT(76) P4_1 — witness (1/8, 1/6, 5/12) at c/a 3/2, f = (32, 48, 18), p = 3^4 4^4 5^4 6^2 9^4, aut 2 / Isom 1

Search set: 10440 points x 1 c/a values = 10440 candidates (c/a candidates {3/2}); SAME 10411, DIFFERENT 29, QUARANTINE 0, stabilizer-order changes 0.

| nice rank | generating point | c/a | m_lattice (site-centred, conventional) | m_cartesian | m_absolute | stab | nonsimple |
|---|---|---|---|---|---|---|---|
| 1 | (1/8, 3/16, 7/16) | 3/2 | 56160 | 37440 | 56160 | 1 | 0 |
| 2 | (1/8, 3/16, 13/32) | 3/2 | 56160 | 37440 | 56160 | 1 | 0 |
| 3 | (1/8, 3/16, 19/48) | 3/2 | 56160 | 37440 | 56160 | 1 | 0 |
| witness (30) | (1/8, 1/6, 5/12) | 3/2 | 466560 | 155520 | 466560 | 1 | 0 |

Tellable coordinates: Generating point (1/8, 3/16, 7/16) at c/a = 3/2 in IT(76) P4_1 (f = (32, 48, 18), aut 2): the site-centred vertex coordinates in the conventional tetragonal basis have common denominator 56160; scaled by 37440 the vertices are integer Cartesian points (units a/37440, c = 3/2 a). This beats the sweep witness (1/8, 1/6, 5/12) at c/a = 3/2 (denominator 466560, Cartesian scale 155520; the witness ranks 30 of 10411 type-preserving candidates). The z coordinate is a free translation in this polar group (any z gives a congruent cell). For scale: the Josehedron's vertices have denominator 24 in its conventional cubic cell.

Polar group (every operation of IT(76) fixes the c direction): a shift of the generating point along z translates the whole orbit, so candidates that differ only in z are congruent cells with identical vertex denominators. The z-ties in the table are that congruence; the search is effectively over (x, y, c/a): 359 such classes kept the type, 1 changed it, 0 did both (a class doing both would contradict the congruence; 0 expected).

Type-changed candidates: 29 (discarded from the ranking; a finding about the box reading of WALL_OPEN_PHASE2's axis-tested extents). Axis-parallel from the witness (exactly one tested direction moved): 0; counting z as the free translation it is here, exactly one of (x, y, c/a) moved: 0. By number of point coordinates moved (+ca = c/a also moved): {'3+0': 28, '2+0': 1}. Other types reached: 086ac96faf390886 f=(36, 54, 20) p=3^2 4^8 5^6 10^4 aut 2 x29. Every changed candidate (point, c/a, type) is listed in the JSON (different_candidates); the full per-candidate rows, vertices included, are in the per-cell cache nice_points_cells/6797ab70c6015039.json.

### trigonal #1 `a93f8fe7ecdc5851` IT(144) P3_1 — witness (1/12, 3/8, 1/6) at c/a 9/8, f = (32, 48, 18), p = 3^2 4^8 5^2 7^2 8^2 9^2, aut 1 / Isom 1

Search set: 2376 points x 1 c/a values = 2376 candidates (c/a candidates {9/8}); SAME 2244, DIFFERENT 132, QUARANTINE 0, stabilizer-order changes 0.

| nice rank | generating point | c/a | m_lattice (site-centred, hexagonal basis) | m_eisenstein (in-plane) | m_c | m_cartesian_sqrt3 | m_absolute | stab | nonsimple |
|---|---|---|---|---|---|---|---|---|---|
| 1 | (1/12, 3/8, 1/6) | 9/8 | 174960 | 6480 | 43740 | 38880 | 174960 | 1 | 0 |
| 2 | (1/12, 3/8, 7/48) | 9/8 | 174960 | 6480 | 43740 | 38880 | 174960 | 1 | 0 |
| 3 | (1/12, 3/8, 3/16) | 9/8 | 174960 | 6480 | 43740 | 38880 | 174960 | 1 | 0 |
| witness (1) | (1/12, 3/8, 1/6) | 9/8 | 174960 | 6480 | 43740 | 38880 | 174960 | 1 | 0 |

Tellable coordinates: Generating point (1/12, 3/8, 1/6) at c/a = 9/8 in IT(144) P3_1 (f = (32, 48, 18), aut 1): the site-centred vertex coordinates in the conventional hexagonal basis have common denominator 174960; in-plane coordinates x + y*omega are Eisenstein integers after scaling by 6480 (z denominators 43740); the sqrt(3)-Cartesian form (u, v*sqrt(3), w)/m needs m = 38880. No candidate in the search set beats the sweep witness; the witness is the best presentation found. The z coordinate is a free translation in this polar group (any z gives a congruent cell). For scale: the Josehedron's vertices have denominator 24 in its conventional cubic cell.

Polar group (every operation of IT(144) fixes the c direction): a shift of the generating point along z translates the whole orbit, so candidates that differ only in z are congruent cells with identical vertex denominators. The z-ties in the table are that congruence; the search is effectively over (x, y, c/a): 68 such classes kept the type, 4 changed it, 0 did both (a class doing both would contradict the congruence; 0 expected).

Type-changed candidates: 132 (discarded from the ranking; a finding about the box reading of WALL_OPEN_PHASE2's axis-tested extents). Axis-parallel from the witness (exactly one tested direction moved): 0; counting z as the free translation it is here, exactly one of (x, y, c/a) moved: 0. By number of point coordinates moved (+ca = c/a also moved): {'3+0': 128, '2+0': 4}. Other types reached: 6dba530a0828bdcf f=(36, 54, 20) p=3^8 4^2 5^2 7^4 9^2 10^2 aut 1 x132. Every changed candidate (point, c/a, type) is listed in the JSON (different_candidates); the full per-candidate rows, vertices included, are in the per-cell cache nice_points_cells/a93f8fe7ecdc5851.json.

### trigonal #2 `e598ffd8a1cac138` IT(144) P3_1 — witness (1/8, 1/6, 5/12) at c/a 29/32, f = (32, 48, 18), p = 3^4 4^4 5^4 6^2 9^4, aut 1 / Isom 1

Search set: 928 points x 2 c/a values = 1856 candidates (c/a candidates {9/10, 29/32}); SAME 1827, DIFFERENT 29, QUARANTINE 0, stabilizer-order changes 0.

| nice rank | generating point | c/a | m_lattice (site-centred, hexagonal basis) | m_eisenstein (in-plane) | m_c | m_cartesian_sqrt3 | m_absolute | stab | nonsimple |
|---|---|---|---|---|---|---|---|---|---|
| 1 | (1/8, 1/6, 5/12) | 9/10 | 151632000 | 4212000 | 466560 | 33696000 | 151632000 | 1 | 0 |
| 2 | (1/8, 1/6, 19/48) | 9/10 | 151632000 | 4212000 | 466560 | 33696000 | 151632000 | 1 | 0 |
| 3 | (1/8, 1/6, 7/16) | 9/10 | 151632000 | 4212000 | 466560 | 33696000 | 151632000 | 1 | 0 |
| witness (30) | (1/8, 1/6, 5/12) | 29/32 | 3400600320 | 4043520 | 454140 | 234524160 | 3400600320 | 1 | 0 |

Tellable coordinates: Generating point (1/8, 1/6, 5/12) at c/a = 9/10 in IT(144) P3_1 (f = (32, 48, 18), aut 1): the site-centred vertex coordinates in the conventional hexagonal basis have common denominator 151632000; in-plane coordinates x + y*omega are Eisenstein integers after scaling by 4212000 (z denominators 466560); the sqrt(3)-Cartesian form (u, v*sqrt(3), w)/m needs m = 33696000. This beats the sweep witness (1/8, 1/6, 5/12) at c/a = 29/32 (denominator 3400600320, Eisenstein scale 4043520; the witness ranks 30 of 1827 type-preserving candidates). The z coordinate is a free translation in this polar group (any z gives a congruent cell). For scale: the Josehedron's vertices have denominator 24 in its conventional cubic cell.

Polar group (every operation of IT(144) fixes the c direction): a shift of the generating point along z translates the whole orbit, so candidates that differ only in z are congruent cells with identical vertex denominators. The z-ties in the table are that congruence; the search is effectively over (x, y, c/a): 63 such classes kept the type, 1 changed it, 0 did both (a class doing both would contradict the congruence; 0 expected).

Type-changed candidates: 29 (discarded from the ranking; a finding about the box reading of WALL_OPEN_PHASE2's axis-tested extents). Axis-parallel from the witness (exactly one tested direction moved): 0; counting z as the free translation it is here, exactly one of (x, y, c/a) moved: 0. By number of point coordinates moved (+ca = c/a also moved): {'3+ca': 28, '2+ca': 1}. Other types reached: 1a36f90bbc759307 f=(28, 42, 16) p=4^8 5^4 8^4 aut 4 x29. Every changed candidate (point, c/a, type) is listed in the JSON (different_candidates); the full per-candidate rows, vertices included, are in the per-cell cache nice_points_cells/e598ffd8a1cac138.json.

### trigonal #3 `c0071756347c5a8a` IT(144) P3_1 — witness (1/12, 3/8, 1/6) at c/a 1, f = (28, 42, 16), p = 3^2 4^4 5^4 7^6, aut 1 / Isom 1

Search set: 11220 points x 1 c/a values = 11220 candidates (c/a candidates {1}); SAME 10263, DIFFERENT 957, QUARANTINE 0, stabilizer-order changes 0.

| nice rank | generating point | c/a | m_lattice (site-centred, hexagonal basis) | m_eisenstein (in-plane) | m_c | m_cartesian_sqrt3 | m_absolute | stab | nonsimple |
|---|---|---|---|---|---|---|---|---|---|
| 1 | (1/11, 4/11, 2/11) | 1 | 11297286 | 513513 | 726 | 11297286 | 11297286 | 1 | 0 |
| 2 | (1/11, 4/11, 5/33) | 1 | 11297286 | 513513 | 726 | 11297286 | 11297286 | 1 | 0 |
| 3 | (1/11, 4/11, 7/44) | 1 | 11297286 | 513513 | 726 | 11297286 | 22594572 | 1 | 0 |
| witness (100) | (1/12, 3/8, 1/6) | 1 | 6073608960 | 1518402240 | 11520 | 6073608960 | 6073608960 | 1 | 0 |

Tellable coordinates: Generating point (1/11, 4/11, 2/11) at c/a = 1 in IT(144) P3_1 (f = (28, 42, 16), aut 1): the site-centred vertex coordinates in the conventional hexagonal basis have common denominator 11297286; in-plane coordinates x + y*omega are Eisenstein integers after scaling by 513513 (z denominators 726); the sqrt(3)-Cartesian form (u, v*sqrt(3), w)/m needs m = 11297286. This beats the sweep witness (1/12, 3/8, 1/6) at c/a = 1 (denominator 6073608960, Eisenstein scale 1518402240; the witness ranks 100 of 10263 type-preserving candidates). The z coordinate is a free translation in this polar group (any z gives a congruent cell). For scale: the Josehedron's vertices have denominator 24 in its conventional cubic cell.

Polar group (every operation of IT(144) fixes the c direction): a shift of the generating point along z translates the whole orbit, so candidates that differ only in z are congruent cells with identical vertex denominators. The z-ties in the table are that congruence; the search is effectively over (x, y, c/a): 311 such classes kept the type, 29 changed it, 0 did both (a class doing both would contradict the congruence; 0 expected).

Type-changed candidates: 957 (discarded from the ranking; a finding about the box reading of WALL_OPEN_PHASE2's axis-tested extents). Axis-parallel from the witness (exactly one tested direction moved): 0; counting z as the free translation it is here, exactly one of (x, y, c/a) moved: 0. By number of point coordinates moved (+ca = c/a also moved): {'3+0': 928, '2+0': 29}. Other types reached: a99e46dd535bab3b f=(32, 48, 18) p=3^4 4^4 5^2 6^4 8^2 9^2 aut 1 x957. Every changed candidate (point, c/a, type) is listed in the JSON (different_candidates); the full per-candidate rows, vertices included, are in the per-cell cache nice_points_cells/c0071756347c5a8a.json.

### hexagonal #1 `c49077384aaebeb0` IT(178) P6_122 — witness (1/12, 1/6, 1/4) at c/a 5/4, f = (44, 66, 24), p = 3^8 4^2 5^6 6^4 9^2 14^2, aut 2 / Isom 2

Search set: 8 points x 1 c/a values = 8 candidates (c/a candidates {5/4}); SAME 8, DIFFERENT 0, QUARANTINE 0, stabilizer-order changes 0.

| nice rank | generating point | c/a | m_lattice (site-centred, hexagonal basis) | m_eisenstein (in-plane) | m_c | m_cartesian_sqrt3 | m_absolute | stab | nonsimple |
|---|---|---|---|---|---|---|---|---|---|
| 1 | (1/12, 1/6, 1/4) | 5/4 | 415800 | 16632 | 3300 | 166320 | 415800 | 2 | 0 |
| 2 | (3/34, 3/17, 1/4) | 5/4 | 2055122928 | 120889584 | 322524 | 4110245856 | 2055122928 | 2 | 0 |
| 3 | (2/23, 4/23, 1/4) | 5/4 | 97901395200 | 851316480 | 9998100 | 39160558080 | 97901395200 | 2 | 0 |
| witness (1) | (1/12, 1/6, 1/4) | 5/4 | 415800 | 16632 | 3300 | 166320 | 415800 | 2 | 0 |

Tellable coordinates: Generating point (1/12, 1/6, 1/4) at c/a = 5/4 in IT(178) P6_122 (f = (44, 66, 24), aut 2): the site-centred vertex coordinates in the conventional hexagonal basis have common denominator 415800; in-plane coordinates x + y*omega are Eisenstein integers after scaling by 16632 (z denominators 3300); the sqrt(3)-Cartesian form (u, v*sqrt(3), w)/m needs m = 166320. No candidate in the search set beats the sweep witness; the witness is the best presentation found. For scale: the Josehedron's vertices have denominator 24 in its conventional cubic cell.

### hexagonal #2 `8d90c524c89922d9` IT(169) P6_1 — witness (1/12, 3/8, 1/6) at c/a 11/8, f = (36, 54, 20), p = 3^4 4^4 5^4 6^4 7^2 11^2, aut 1 / Isom 1

Search set: 3696 points x 1 c/a values = 3696 candidates (c/a candidates {11/8}); SAME 2937, DIFFERENT 759, QUARANTINE 0, stabilizer-order changes 0.

| nice rank | generating point | c/a | m_lattice (site-centred, hexagonal basis) | m_eisenstein (in-plane) | m_c | m_cartesian_sqrt3 | m_absolute | stab | nonsimple |
|---|---|---|---|---|---|---|---|---|---|
| 1 | (2/27, 10/27, 4/27) | 11/8 | 28441081439400960 | 235050259829760 | 74065316248440 | 5171105716254720 | 28441081439400960 | 1 | 0 |
| 2 | (2/27, 10/27, 5/27) | 11/8 | 28441081439400960 | 235050259829760 | 74065316248440 | 5171105716254720 | 28441081439400960 | 1 | 0 |
| 3 | (2/27, 10/27, 1/6) | 11/8 | 28441081439400960 | 235050259829760 | 74065316248440 | 5171105716254720 | 9480360479800320 | 1 | 0 |
| witness (100) | (1/12, 3/8, 1/6) | 11/8 | 1352261721498364508832 | 11175716706598053792 | 56344238395765187868 | 245865767545157183424 | 1352261721498364508832 | 1 | 0 |

Tellable coordinates: Generating point (2/27, 10/27, 4/27) at c/a = 11/8 in IT(169) P6_1 (f = (36, 54, 20), aut 1): the site-centred vertex coordinates in the conventional hexagonal basis have common denominator 28441081439400960; in-plane coordinates x + y*omega are Eisenstein integers after scaling by 235050259829760 (z denominators 74065316248440); the sqrt(3)-Cartesian form (u, v*sqrt(3), w)/m needs m = 5171105716254720. This beats the sweep witness (1/12, 3/8, 1/6) at c/a = 11/8 (denominator 1352261721498364508832, Eisenstein scale 11175716706598053792; the witness ranks 100 of 2937 type-preserving candidates). The z coordinate is a free translation in this polar group (any z gives a congruent cell). For scale: the Josehedron's vertices have denominator 24 in its conventional cubic cell.

Polar group (every operation of IT(169) fixes the c direction): a shift of the generating point along z translates the whole orbit, so candidates that differ only in z are congruent cells with identical vertex denominators. The z-ties in the table are that congruence; the search is effectively over (x, y, c/a): 89 such classes kept the type, 23 changed it, 0 did both (a class doing both would contradict the congruence; 0 expected).

Type-changed candidates: 759 (discarded from the ranking; a finding about the box reading of WALL_OPEN_PHASE2's axis-tested extents). Axis-parallel from the witness (exactly one tested direction moved): 0; counting z as the free translation it is here, exactly one of (x, y, c/a) moved: 0. By number of point coordinates moved (+ca = c/a also moved): {'3+0': 736, '2+0': 23}. Other types reached: a35623e347ef03b4 f=(32, 48, 18) p=4^10 6^6 10^2 aut 2 x495; 322d5ff451e4101d f=(32, 48, 18) p=3^2 4^6 5^4 6^2 7^2 10^2 aut 1 x264. Every changed candidate (point, c/a, type) is listed in the JSON (different_candidates); the full per-candidate rows, vertices included, are in the per-cell cache nice_points_cells/8d90c524c89922d9.json.

### hexagonal #3 `9c0b7e0c29dfebb2` IT(169) P6_1 — witness (1/12, 3/8, 1/6) at c/a 3/4, f = (36, 54, 20), p = 3^4 4^8 5^2 7^4 13^2, aut 1 / Isom 1

Search set: 10560 points x 1 c/a values = 10560 candidates (c/a candidates {3/4}); SAME 9372, DIFFERENT 1188, QUARANTINE 0, stabilizer-order changes 0.

| nice rank | generating point | c/a | m_lattice (site-centred, hexagonal basis) | m_eisenstein (in-plane) | m_c | m_cartesian_sqrt3 | m_absolute | stab | nonsimple |
|---|---|---|---|---|---|---|---|---|---|
| 1 | (1/11, 4/11, 2/11) | 3/4 | 988416 | 988416 | 6864 | 1976832 | 988416 | 1 | 0 |
| 2 | (1/11, 4/11, 5/33) | 3/4 | 988416 | 988416 | 6864 | 1976832 | 988416 | 1 | 0 |
| 3 | (1/11, 4/11, 7/44) | 3/4 | 988416 | 988416 | 6864 | 1976832 | 988416 | 1 | 0 |
| witness (67) | (1/12, 3/8, 1/6) | 3/4 | 804980880 | 268326960 | 73260 | 536653920 | 804980880 | 1 | 0 |

Tellable coordinates: Generating point (1/11, 4/11, 2/11) at c/a = 3/4 in IT(169) P6_1 (f = (36, 54, 20), aut 1): the site-centred vertex coordinates in the conventional hexagonal basis have common denominator 988416; in-plane coordinates x + y*omega are Eisenstein integers after scaling by 988416 (z denominators 6864); the sqrt(3)-Cartesian form (u, v*sqrt(3), w)/m needs m = 1976832. This beats the sweep witness (1/12, 3/8, 1/6) at c/a = 3/4 (denominator 804980880, Eisenstein scale 268326960; the witness ranks 67 of 9372 type-preserving candidates). The z coordinate is a free translation in this polar group (any z gives a congruent cell). For scale: the Josehedron's vertices have denominator 24 in its conventional cubic cell.

Polar group (every operation of IT(169) fixes the c direction): a shift of the generating point along z translates the whole orbit, so candidates that differ only in z are congruent cells with identical vertex denominators. The z-ties in the table are that congruence; the search is effectively over (x, y, c/a): 284 such classes kept the type, 36 changed it, 0 did both (a class doing both would contradict the congruence; 0 expected).

Type-changed candidates: 1188 (discarded from the ranking; a finding about the box reading of WALL_OPEN_PHASE2's axis-tested extents). Axis-parallel from the witness (exactly one tested direction moved): 0; counting z as the free translation it is here, exactly one of (x, y, c/a) moved: 0. By number of point coordinates moved (+ca = c/a also moved): {'3+0': 1152, '2+0': 36}. Other types reached: 85244add8d1f2d55 f=(32, 48, 18) p=3^2 4^6 5^6 6^2 12^2 aut 1 x1188. Every changed candidate (point, c/a, type) is listed in the JSON (different_candidates); the full per-candidate rows, vertices included, are in the per-cell cache nice_points_cells/9c0b7e0c29dfebb2.json.

## Type-changed count (the check on the open neighbourhood)

3558 of 43217 candidates changed type; 0 quarantined; 0 of the changed candidates were axis-parallel from the witness (one tested direction moved), 3558 moved in two or more tested directions at once; treating z as the free translation it is in the seven polar-group cells (IT 76, 144, 169), the count of changed candidates with exactly one of (x, y, c/a) moved is 0. Per cell: `4e9c9b076cfec323` 0/16 (axis-parallel 0); `164d4bd63d82d0c3` 464/3045 (axis-parallel 0); `6797ab70c6015039` 29/10440 (axis-parallel 0); `a93f8fe7ecdc5851` 132/2376 (axis-parallel 0); `e598ffd8a1cac138` 29/1856 (axis-parallel 0); `c0071756347c5a8a` 957/11220 (axis-parallel 0); `c49077384aaebeb0` 0/8 (axis-parallel 0); `8d90c524c89922d9` 759/3696 (axis-parallel 0); `9c0b7e0c29dfebb2` 1188/10560 (axis-parallel 0).

Reading (a finding about WALL_OPEN_PHASE2's scheme, not an error of either computation): the on-axis extents held — no candidate that moved in a single tested direction changed type, so the OPEN verdicts and their tested steps stand as stated; the PRODUCT of the per-axis SAME intervals is not a type-constant box. Walls in the (point, c/a) parameter space are not axis-aligned, so a corner of the box can cross a wall that neither axis reaches. WALL_OPEN_PHASE2 never claimed the box (its scheme tests axis-parallel steps and says OPEN = every tested side SAME); the pre-registered expectation of 0 here was the box reading, and it is wrong. Consequence for naming: a chosen presentation must be re-certified at ITS OWN (point, c/a), which this search does for every SAME candidate; a presentation is not inherited from the witness's verdict.

## Josehedron comparison (stated honestly)

The Josehedron control through the same functions (phase-1 store `dfccc9ff6019ead5`, IT(220) Wyckoff 12a, generating point (3/8, 0, 1/4), f = (12, 22, 12), p = 3^4 4^8, aut 4): site-centred vertex coordinates in the conventional cubic basis have common denominator 24 (absolute conventional: 24); the cubic conventional basis is Cartesian, so that is its integer Cartesian scale. Its published hook is integer vertex coordinates at a small scale. Against that: the best presentation found here per cell (m_lattice, then the second scale) is listed above; tetragonal #1 `4e9c9b076cfec323` m_lattice 748000 / Cartesian 149600; tetragonal #2 `164d4bd63d82d0c3` m_lattice 7257600 / Cartesian 1451520; tetragonal #3 `6797ab70c6015039` m_lattice 56160 / Cartesian 37440; trigonal #1 `a93f8fe7ecdc5851` m_lattice 174960 / Eisenstein 6480; trigonal #2 `e598ffd8a1cac138` m_lattice 151632000 / Eisenstein 4212000; trigonal #3 `c0071756347c5a8a` m_lattice 11297286 / Eisenstein 513513; hexagonal #1 `c49077384aaebeb0` m_lattice 415800 / Eisenstein 16632; hexagonal #2 `8d90c524c89922d9` m_lattice 28441081439400960 / Eisenstein 235050259829760; hexagonal #3 `9c0b7e0c29dfebb2` m_lattice 988416 / Eisenstein 988416. None of the nine reaches a Josehedron-sized scale inside its certified neighbourhood on this grid; the integer-coordinate hook stays absent for these cells at this resolution (a statement about the search set, not an impossibility proof: the neighbourhood was tested along axes with steps down to 1/1536 and the grid here stops at denominator 48 / 16).

## Verify (main session, before acceptance)

```
cd <repo>/harness/phase2 && rm -rf nice_points_cells && NICE_JOBS=8 nice -n 10 python3 nice_points_2026-09-04.py; echo exit $?; md5 -q NICE_POINTS_2026-09-04.json   # must print cf6645fcbb96a530cbb71a2d20bb325a
```

Exit 0 and the md5 above are required. The script rewrites this file below the pre-registration block; the block itself is read back and never regenerated.
