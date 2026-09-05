# Round-2 computations for the seven-shape paper (2026-09-03)

Scripts r1-r8 in this directory; all exact (fractions.Fraction) on the frozen harness (orbit.py, exact_cell.py, canon_code.py, phase1_types.json) and the round-1 helpers (round1_computations/common.py). Regenerate with run_all.sh; each script's stdout is in r*_run.log. Written by Claude (Fable 5.1) in a Claude Code session as the round-2 fix-editor task, in answer to paper/REVIEW_COLD_R2_2026-09-03.md (W2, W3(f), W5, W7, W9, Q2-Q6; r7 checks the printed frequency sums, r8 the reduced domains of IT(201)/IT(224)); machine results, not AI-generated numbers. Acceptance: main-session re-run of run_all.sh, exit 0.

## R1 -- roundness of classical cells under both conventions

Bernhard's convention (arXiv:2604.07160, p. 6, PDF text layer, verbatim): "The Josehedron fills ~47.98% of the volume of its outer circumsphere. This is slightly superior to another SFPH, the rhombic dodecahedron at ~47.75%, though the latter has 16 vertices. The cube, in comparison, only occupies ~36.76% of its circumsphere. The maximal hexagonal prism (also an SFPH, and a suspected candidate by reddit user "st3f-ping") inscribed in a unit sphere occupies ~47.75%. The Josehedron is therefore, by a small margin, the "roundest" SFPH known to date." Earlier on the same page his outer circumsphere is the sphere through the farthest vertices about the cell's centre (Fig. 4, R2), and for the regular dodecahedron he writes "its circumsphere (the sphere through all vertices)". For every cell below the site-centred sphere and the smallest enclosing sphere coincide (the symmetry group of each cell fixes only its centre), so the two conventions agree and the values are Bernhard's.

| cell | f | p | vol | rho^2 (site) | r^2 (MES) | coincide | roundness (site) | roundness (MES) | closed form |
|---|---|---|---|---|---|---|---|---|---|
| cube (P lattice) | (8, 12, 6) | 4^6 | 8 | 3 | 3 | YES | 36.7553% | 36.7553% | 2/(sqrt3 pi) |
| rhombic dodecahedron (F lattice) | (14, 24, 12) | 4^12 | 2 | 1 | 1 | YES | 47.7465% | 47.7465% | 3/(2 pi) |
| truncated octahedron (I lattice) | (24, 36, 14) | 4^6 6^8 | 4 | 5/4 | 5/4 | YES | 68.3292% | 68.3292% | 24/(5 sqrt5 pi) |
| elongated dodecahedron (seed member, elongation e=1) | (18, 28, 12) | 4^8 6^4 | 32 | 9 | 9 | YES | 28.2942% | 28.2942% | 8/(9 pi) |
| Josehedron (control; Bernhard prints ~47.98%) | (12, 22, 12) | 3^4 4^8 | 128/3 | 23/3 | 23/3 | YES | 47.9833% | 47.9833% | - |
| Laves-graph cell (IT(214) 8a, (30,45,17)) | (30, 45, 17) | 4^6 5^6 6^2 8^3 | 1728 | 126 | 126 | YES | 29.1675% | 29.1675% | - |
| hexagonal prism, maximal inscribed (Bernhard's; h/s = sqrt2) | (12,18,8) | 4^6 6^2 | closed form | | | YES | 47.7465% | 47.7465% | 3/(2 pi) |
| hexagonal prism, equilateral (h = s) | (12,18,8) | 4^6 6^2 | closed form | | | YES | 44.3811% | 44.3811% | 9 sqrt3/(5 sqrt5 pi) |

Elongated dodecahedron family (vertices (0,0,+-(2+e)), (+-1,+-1,+-(1+e)), (+-2,0,+-e), (0,+-2,+-e), e >= 0): vol = 16(1+e), rho^2 = (2+e)^2, ratio = 12(1+e)/(pi (2+e)^3), strictly decreasing in e from 3/(2 pi) = 47.75% at e = 0 (the rhombic dodecahedron); the seed member is e = 1.

Finding: the truncated octahedron (the Voronoi cell of the body-centred cubic lattice, the paper's gate-G2 control) fills 68.3292% of its circumsphere under Bernhard's convention, above the Josehedron's 47.9833%. The cube (36.7553%), rhombic dodecahedron (47.7465%) and maximal hexagonal prism (47.7465%) reproduce his printed 36.76%, 47.75%, 47.75%, which fixes the convention. Bernhard's text restricts the comparison to the cells he names; it does not exclude lattice Voronoi cells by any stated rule, and the truncated octahedron appears in his own Table 1 as the Voronoi cell of several minimal-surface point sets.

## R2 -- Schmitt's IT(220) grid and the point (0, 0, 1/4)

Source facts (references/Schmitt_2016_dissertation.pdf, text layer): the recovered code takes the generating points as an input file (plesiohedron.cpp), so the grid is not in the repository; Sec. 2.2 (p. 25) describes 'approximating F with an extremely fine point grid' over a fundamental domain of the normalizer; the IT(220) block (printed p. 141) gives R220 = conv{(0,0,0), (+-1/8,+-1/8,1/8), (+-1/8,+-1/8,1/4)} and 'We used 1 000 677 997 grid points in the approximating grid'; every printed IT(220) coordinate has denominator dividing 6984 = 8 * 873.

### (i) The count identity: barycentric grid of denominator D over a triangulation of the reduced domain on its printed vertices

| domain | printed grid points | solutions (D, V, E, T, S) with M | qD, D <= 4M/q, Euler V-E+T-S = 1 |
|---|---|---|
| R220 (= R214 = R230 = R199) | 1,000,677,997 | [(873, 9, 24, 25, 9)] |
| R201 (= R224) | 1,001,452,269 | [(1816, 4, 6, 4, 1)] |
| R212 | 1,000,964,383 | [(1062, 7, 16, 15, 5)] |

Reading: for R220 the identity has exactly one solution with the 9 printed vertices, D = 873 with (V, E, T, S) = (9, 24, 25, 9), a triangulation of the 9-vertex domain into 9 tetrahedra (face check: 4S = 36 = 14 boundary triangles + 2 * 11 interior triangles; 16 polytope edges + 5 quadrilateral diagonals + 3 interior edges = 24). R201 is a single tetrahedron and the count is exactly C(1819, 3), so D = 1816 there. For R212 the solution on its 7 printed vertices is D = 1062 with (7, 16, 15, 5) (the printed denominators reach only 4248 = 8 * 1062 / 2 because every vertex coordinate of R212 is an odd multiple of 1/8 and D is even, so the numerators are even). Three groups, three exact matches of a nine-or-ten-digit count: the grid scheme is the barycentric grid described above, boundary included, and for IT(220) its denominator is D = 873, an odd number.

### (ii) The 62 printed IT(220) generating points

All 62 lie in R220 (H-representation |x| <= z, |y| <= z, |x| <= 1/8, |y| <= 1/8, z <= 1/4, which equals the printed convex hull) and every coordinate times 8D = 6984 is an integer. Both facts are consistent with the scheme and are asserted by the script.

### (iii) The point (0, 0, 1/4) and the 24d segment in R220

IT(220) is a single-origin group and the operation tables agree with Schmitt's in the identical setting (SCHMITT_OPS_XCHECK), so (0, 0, 1/4) is (0, 0, 1/4) in his coordinates. It lies in R220: it is the centre of the top square face z = 1/4, on both diagonals. Normalizer (Ia-3d, frozen IT(230) operations) images of the point inside R220:

| image in R220 | minimal face | barycentric coordinates (per diagonal choice where the face is a quadrilateral) | grid point for D = 873? |
|---|---|---|---|
| (0, 0, 1/4) | top (quadrilateral) | diag t-1-1-t+1-1: t-1-1=0, t+1-1=1/2, t-1+1=1/2; diag t-1+1-t+1+1: t-1+1=0, t+1+1=1/2, t-1-1=1/2 | NO (either diagonal) |

Verdict: (0, 0, 1/4) is NOT a grid point of Schmitt's IT(220) grid. Every representative of it in R220 sits on a face diagonal with barycentric weight 1/2, and D = 873 is odd.

The 24d line (x, 0, 1/4). For sample parameters the images in R220 and their faces:

| x | images in R220 | faces |
|---|---|---|
| 1/1000 | (1/1000, 0, 1/4) | top (quadrilateral) |
| 1/97 | (1/97, 0, 1/4) | top (quadrilateral) |
| 7/200 | (7/200, 0, 1/4) | top (quadrilateral) |
| 1/13 | (1/13, 0, 1/4) | top (quadrilateral) |
| 1/12 | (1/12, 0, 1/4) | top (quadrilateral) |
| 1/3 | (-1/12, 0, 1/4) | top (quadrilateral) |
| -1/1000 | (-1/1000, 0, 1/4) | top (quadrilateral) |

On the top face the segment y = 0, |x| <= 1/8 lies in whichever triangle of the diagonal triangulation contains it; its barycentric coordinates are (1/2 + 4x, -4x, 1/2) for x <= 0 in the triangle on that side (and symmetrically for x >= 0): one weight is 1/2 for every x, so for odd D no point of the segment is a grid point.  Grid points of the 24d line therefore come only from its other normalizer images in R220, listed above for sample x.

Scan of x = k/(8D), k = 0..8D-1 (all candidate grid values on the line, since grid coordinates have denominators dividing 8D): 0 parameter values of the 24d line are grid points (via some boundary image in R220; interior images, if any, are not decidable without his triangulation and are counted as misses). Smallest positive: none; x = 0 is NOT in the set; values in (0, 1/12): 0; values in (1/12, 1/3]: 0.

## R3 -- identity of Schmitt's printed IT(220) (22,35,15) representative

Printed point (-1/8, 55/2328, 437/3492), frequency 52 090 897 (printed p. 142). Recomputed through the frozen chain: f = (22, 35, 15) (equals the printed f-vector; run accepted), p = 3^4 4^6 6^2 7^2 8^1, aut = 1, site-symmetry order = 1 (general position), T = 24, non-simple vertices = 4, canonical-code id c92d39651f11573d.

| comparison | f | p | aut | same type? |
|---|---|---|---|---|
| A: wall neighbour x < 0, stored 0ee26ed471c923e2 | (22, 35, 15) | 3^4 5^10 8^1 | 2 | NO |
| B: wall neighbour 0 < x < 1/12, recomputed at (1/96, 0, 1/4) | (22, 35, 15) | 3^6 4^1 6^8 | 2 | NO |
| stored (22,35,15) type 0ee26ed471c923e2 (first witness IT(220) ('0', '1/4', '1/3')) | (22, 35, 15) | 3^4 5^10 8^1 | 2 | NO |
| stored (22,35,15) type 21d94ee4a2af0f9f (first witness IT(218) ('1/8', '1/6', '5/12')) | (22, 35, 15) | 3^6 4^1 5^4 6^1 7^2 8^1 | 1 | NO |
| stored (22,35,15) type c5b97d7745060a86 (first witness IT(201) ('1/12', '3/8', '1/6')) | (22, 35, 15) | 3^6 4^3 5^2 7^2 8^2 | 1 | NO |
| stored (22,35,15) type cea2f3246210cd55 (first witness IT(199) ('1/12', '3/8', '1/6')) | (22, 35, 15) | 3^2 4^7 5^4 8^2 | 2 | NO |

Verdict: It is NEITHER wall neighbour: a third (22,35,15) type in IT(220), not stored by the sweep.
The printed point has x = -1/8 (a lateral face of R220) and site-symmetry order 1; it is not on the 24d line (y = 0, z = 1/4), and its frequency of 52 million grid points marks a three-dimensional type region. The (22,35,15) entry in Schmitt's IT(220) table therefore records a general-position type, and the two wall neighbours of the Satchelhedron share only its f-vector.

## R4 -- site symmetry of the Ordenhedron's non-simple vertices (IT(201) Pn-3, generating point (1/8, 1/6, 5/12))

| vertex (integer scaling, PERIOD 24) | fractional | facets at v | |Stab_G(v)| | point group | |N(v)| (equidistant sites) | |N(v)| mod |H| | H free on N(v) | forced |N(v)| > 4? |
|---|---|---|---|---|---|---|---|---|
| (-3, 3, 3) | (-1/8, 1/8, 1/8) | 4 | 3 | 3 | 6 | 0 | yes | yes |
| (0, 0, 0) | (0, 0, 0) | 5 | 12 | 23 | 12 | 0 | yes | yes |
| (6, 6, 6) | (1/4, 1/4, 1/4) | 4 | 6 | -3 | 6 | 0 | yes | yes |
| (6, 6, 18) | (1/4, 1/4, 3/4) | 4 | 6 | -3 | 6 | 0 | yes | yes |
| (9, 9, 15) | (3/8, 3/8, 5/8) | 4 | 3 | 3 | 6 | 0 | yes | yes |

Reading: a stabilizer of order h acting freely on the equidistant sites makes |N(v)| a multiple of h; with h in {3, 6, 12} no multiple of h equals 4, so more than four sites are equidistant from v for every general-position generating point of Pn-3 on the same symmetry element, and more than four cells meet at v. That degeneracy is forced by the group. The number of facets of the Ordenhedron at v (4 or 5) equals the degree of the site in the Delaunay polytope conv N(v) and is a property of the cell at this generating point; a free action of order 3 on six cospherical sites is compatible with a triangular prism (degree 3) as well as an octahedron (degree 4), so the facet count is read from the cell, not derived from H.
Summary: stabilizer orders [3, 12, 6, 6, 3], point groups ['3', '23', '-3', '-3', '3'], |N(v)| = [6, 12, 6, 6, 6], facets at v = [4, 5, 4, 4, 4]; all five forced in the sense above: True.

## R5 -- extent of the Ordenhedron's type region (coarse box scan, IT(201) 24h)

Box (1/8, 1/6, 5/12) + (i, j, k)/96, i, j, k in -4..4: 389 of 729 points give the Ordenhedron type (53.4%); 0 of the 729 points lie on special positions.
Other types met in the box (f, p: count): (20, 32, 14) 3^2 4^7 5^2 6^1 7^2: 114; (22, 35, 15) 3^4 4^7 6^1 7^2 10^1: 65; (15, 26, 13) 3^8 4^1 6^4: 48; (14, 23, 11) 3^4 4^2 5^4 6^1: 42; (14, 23, 11) 3^4 4^4 6^3: 35; (22, 35, 15) 3^6 4^3 5^2 7^2 8^2: 16; (18, 29, 13) 3^2 4^5 5^4 6^2: 7; (14, 23, 11) 3^2 4^7 6^2: 6; (11, 18, 9) 3^2 4^5 5^2: 3; (17, 28, 13) 3^5 4^4 6^3 7^1: 2; (16, 27, 13) 3^6 4^3 6^4: 1; (6, 11, 7) 3^6 4^1: 1

First step (in units of 1/96) at which the type changes along each axis, up to 12 steps: x-: 4, x+: 4, y-: 4, y+: 4, z-: 4, z+: 4

Reading: this is a sampling estimate on a grid of step 1/96 in a box of half-width 1/24, not a computation of the region; it bounds the region from inside only where every sampled point in a direction agreed.

## R6 -- Wyckoff letters of the Laves-graph type sightings (spglib 2.7.0 on the frozen orbits)

| group | point | site-symmetry order (frozen ops) | orbit / conventional cell | orbit / primitive cell | Wyckoff (ITA, from multiplicity and site order) | site symmetry | spglib symmetry of the point set | same canonical code |
|---|---|---|---|---|---|---|---|---|
| IT(199) I2_13 | (1/8, 1/8, 1/8) | 3 | 8 | 4 | 8a | .3. | IT(214) I4_132 | yes |
| IT(199) I2_13 | (1/8, 3/8, 5/8) | 3 | 8 | 4 | 8a | .3. | IT(214) I4_132 | yes |
| IT(212) P4_332 | (1/8, 3/8, 5/8) | 3 | 8 | 8 | 8c | .3. | IT(214) I4_132 | yes |
| IT(213) P4_132 | (1/8, 1/8, 1/8) | 3 | 8 | 8 | 8c | .3. | IT(214) I4_132 | yes |
| IT(214) I4_132 | (1/8, 1/8, 1/8) | 6 | 8 | 4 | 8a | .32 | IT(214) I4_132 | yes |
| IT(214) I4_132 | (1/8, 3/8, 5/8) | 6 | 8 | 4 | 8b | .32 | IT(214) I4_132 | yes |

Reading: every sighting is an eight-point orbit per conventional cell (the vertex set of one Laves graph). In IT(212) P4_332 the sighted orbit is 8c at (1/8, 3/8, 5/8), site symmetry .3.; in IT(213) P4_132 it is 8c at (1/8, 1/8, 1/8); in IT(199) I2_13 it is 8a (.3.); in IT(214) I4_132 both (1/8, 1/8, 1/8) and (1/8, 3/8, 5/8) are eight-point orbits with site symmetry .32 (8a and 8b). The four-point orbits 4a/4b of IT(212)/IT(213) (site symmetry .32) were not among the sightings of this type. spglib on each eight-point set returns I4_132 (the point set's own symmetry), which is why the letters are read from the generating group's position list.

## R7 -- Schmitt's printed frequencies versus his printed grid-point counts (36 cubic groups)

| group | grid points printed | rows | sum of printed frequencies | shortfall | shortfall % | rows == digitization |
|---|---|---|---|---|---|---|
| IT(195) | 1,001,452,269 | 9 | 1,001,452,269 | 0 | 0.000% | yes |
| IT(196) | 1,001,452,269 | 5 | 754,268,881 | 247,183,388 | 24.682% | yes |
| IT(197) | 1,001,452,269 | 27 | 995,516,869 | 5,935,400 | 0.593% | yes |
| IT(198) | 1,000,677,997 | 18 | 1,000,677,997 | 0 | 0.000% | yes |
| IT(199) | 1,000,677,997 | 44 | 983,336,039 | 17,341,958 | 1.733% | yes |
| IT(200) | 1,001,452,269 | 7 | 992,615,065 | 8,837,204 | 0.882% | yes |
| IT(201) | 1,001,452,269 | 16 | 982,187,680 | 19,264,589 | 1.924% | yes |
| IT(202) | 1,001,452,269 | 8 | 611,734,438 | 389,717,831 | 38.915% | yes |
| IT(203) | 1,000,520,885 | 12 | 916,270,542 | 84,250,343 | 8.421% | yes |
| IT(204) | 1,001,452,269 | 21 | 842,609,590 | 158,842,679 | 15.861% | yes |
| IT(205) | 1,000,520,885 | 24 | 1,000,222,027 | 298,858 | 0.030% | yes |
| IT(206) | 1,000,677,997 | 72 | 837,910,948 | 162,767,049 | 16.266% | yes |
| IT(207) | 1,001,452,269 | 6 | 643,130,784 | 358,321,485 | 35.780% | yes |
| IT(208) | 1,001,452,269 | 27 | 1,001,452,266 | 3 | 0.000% | yes |
| IT(209) | 1,001,452,269 | 7 | 659,063,243 | 342,389,026 | 34.189% | yes |
| IT(210) | 1,000,520,885 | 18 | 469,047,465 | 531,473,420 | 53.120% | yes |
| IT(211) | 1,001,452,269 | 27 | 862,471,968 | 138,980,301 | 13.878% | yes |
| IT(212) (=213) | 1,000,964,383 | 105 | 1,000,964,383 | 0 | 0.000% | yes |
| IT(214) | 1,000,677,997 | 102 | 999,967,862 | 710,135 | 0.071% | yes |
| IT(215) | 1,001,452,269 | 8 | 1,001,452,268 | 1 | 0.000% | yes |
| IT(216) | 1,001,452,269 | 5 | 999,404,972 | 2,047,297 | 0.204% | yes |
| IT(217) | 1,001,452,269 | 20 | 1,001,452,267 | 2 | 0.000% | yes |
| IT(218) | 1,001,452,269 | 30 | 1,001,452,267 | 2 | 0.000% | yes |
| IT(219) | 1,001,452,269 | 8 | 933,258,294 | 68,193,975 | 6.810% | yes |
| IT(220) | 1,000,677,997 | 62 | 999,239,552 | 1,438,445 | 0.144% | yes |
| IT(221) | 1,001,452,269 | 5 | 1,001,452,268 | 1 | 0.000% | yes |
| IT(222) | 1,001,452,269 | 11 | 1,000,454,838 | 997,431 | 0.100% | yes |
| IT(223) | 1,001,452,269 | 20 | 1,001,452,267 | 2 | 0.000% | yes |
| IT(224) | 1,001,452,269 | 8 | 1,001,452,269 | 0 | 0.000% | yes |
| IT(225) | 1,001,452,269 | 6 | 1,001,452,269 | 0 | 0.000% | yes |
| IT(226) | 1,001,452,269 | 7 | 1,001,452,269 | 0 | 0.000% | yes |
| IT(227) | 1,000,520,885 | 11 | 1,000,520,885 | 0 | 0.000% | yes |
| IT(228) | 1,000,520,885 | 16 | 998,063,347 | 2,457,538 | 0.246% | yes |
| IT(229) | 1,001,452,269 | 16 | 1,001,452,269 | 0 | 0.000% | yes |
| IT(230) | 1,000,677,997 | 93 | 386,091,376 | 614,586,621 | 61.417% | yes |

Rows parsed: 986 counting IT(213) as a copy of IT(212) (the digitization has 986). Blocks whose f-vector sets differ from the digitization: none.
Groups with a shortfall (printed frequencies do not exhaust the printed grid): [196, 197, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 228, 230]; groups where they match exactly: 8 of 35.
IT(201): 19,264,589 of 1,001,452,269 grid points (1.92%) carry no printed f-vector. The Ordenhedron's type region, estimated in R5 at about half of a cube of side 1/12 about its generating point, is about 3% of the reduced domain R201 (volume 1/96) if that box is representative; the shortfall and that estimate are of the same order. Nothing more is inferred here.

## R8 -- Schmitt's reduced domains for IT(201) and IT(224), and the Ordenhedron / Pn-3m cells

### IT(201) in Schmitt's coordinates (origin choice 2)

Among the settings of the frozen Im-3m with origin k/4 (1,1,1), those normalizing the group are k = [1, 3]: the normalizer's m-3m point is the group's 23 point at (1/4,1/4,1/4), not the -3 centre at the origin. Fundamental-domain test of the printed tetrahedron R = conv{(0,0,0), (1/2,0,0), (1/2,1/2,0), (1/4,1/4,1/4)}: number of normalizer images inside R for 1000 seeded random points, under the normalizer (origin 1/4): {0: 762, 4: 238}; under Im-3m at origin 0 (whose asymmetric unit R is): {1: 1000}. So R is a fundamental domain of Im-3m at the origin, not of the normalizer of IT(201) in these coordinates; the normalizer images of R cover about 23.8% of the parameter space, with multiplicity where they cover.

**O** ((20, 33, 15)): generating point (1/8, 1/6, 5/12) in our setting = (7/8, 11/12, 1/6) in his; normalizer images in R: 0 (none: the whole normalizer orbit of the point misses the sampled domain). (Under Im-3m at origin 0 the point has 1 image in R, at (1/6, 1/8, 1/12); that image is not equivalent to the generating point under the group's normalizer.)

### IT(224) in Schmitt's coordinates (origin choice 2)

Among the settings of the frozen Im-3m with origin k/4 (1,1,1), those normalizing the group are k = [1, 3]: the normalizer's m-3m point is the group's 23 point at (1/4,1/4,1/4), not the -3 centre at the origin. Fundamental-domain test of the printed tetrahedron R = conv{(0,0,0), (1/2,0,0), (1/2,1/2,0), (1/4,1/4,1/4)}: number of normalizer images inside R for 1000 seeded random points, under the normalizer (origin 1/4): {0: 762, 4: 238}; under Im-3m at origin 0 (whose asymmetric unit R is): {1: 1000}. So R is a fundamental domain of Im-3m at the origin, not of the normalizer of IT(224) in these coordinates; the normalizer images of R cover about 23.8% of the parameter space, with multiplicity where they cover.

**P7** ((10, 15, 7)): generating point (1/8, 1/6, 5/12) in our setting = (7/8, 11/12, 1/6) in his; normalizer images in R: 0 (none: the whole normalizer orbit of the point misses the sampled domain). (Under Im-3m at origin 0 the point has 1 image in R, at (1/6, 1/8, 1/12); that image is not equivalent to the generating point under the group's normalizer.)

**P11** ((14, 23, 11)): generating point (1/12, 3/8, 3/8) in our setting = (5/6, 1/8, 1/8) in his; normalizer images in R: 0 (none: the whole normalizer orbit of the point misses the sampled domain). (Under Im-3m at origin 0 the point has 1 image in R, at (1/6, 1/8, 1/8); that image is not equivalent to the generating point under the group's normalizer.)

### Control: IT(220) and its normalizer Ia-3d (single origin)

The frozen Ia-3d operations at their own origin normalize the frozen I-43d operations, and each of 1000 seeded random points has exactly one Ia-3d image in R220 except the rare point on a face, which has two ({1: 1000}), so R220 is a fundamental domain of the normalizer and the R2 argument stands.

Reading: for the two-origin groups IT(201) and IT(224) the printed reduced domain is the asymmetric unit of Im-3m in its standard setting, which is the normalizer's fundamental domain when the group is written with origin choice 1 (origin at the 23 point) but not with origin choice 2, the setting of his operation tables and of his printed grid points. In his coordinates the normalizer images of the domain cover only part of the parameter space. The generating points of the Ordenhedron and of both Pn-3m cells lie in the uncovered part, so no point of his IT(201) or IT(224) grid generates a cell congruent to any of the three. This is a statement about the printed domain and the printed coordinates; it does not say whether the error is in the computation or only in the printing of the domain.
