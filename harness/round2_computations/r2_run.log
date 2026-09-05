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
