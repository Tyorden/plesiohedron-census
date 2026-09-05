# G4 certificate results — PHASE 2 (tetragonal, Gram metric), V0-V3 ladder (2026-09-04)

Gate: `../ANCHORS.md` G4 (paper-I-standard ladder V0-V3, `../HARNESS_DESIGN_FABLE5_2026-08-27.md` §3) applied through the accepted Gram chain (`phase2/metric.py`, `phase2/sweep_voronoi_gram.py`, `phase2/exact_cell_gram.py`, G2b). Generator: `g4_certify_gram.py` (this run; sibling of the accepted cubic `g4_certify.py`, which is unmodified and whose metric-independent pieces — exact vector bits, coordinate-space fan volume, the independent affine audit `v1_audit`/`_a_*`, banked V3 tool paths — are imported). Inputs: `phase2_types.json` stored witnesses (the 14 collision-screen survivors of `COLLISION_PHASE2_RESULTS.md`; #8 `cd4fb52572edcb73` reframed and excluded), frozen G1 `spacegroups.json`. V3 uses the banked `export_tables.py` + compiled `enumerate` + `burnside_generic.py` (POLYFORMS_II) and then the INDEPENDENT `../publication/verify_counts_independent.py` (dual-implementation bar, n<=5 under a 15-min cap).

**METRIC CONVENTIONS.** Sites/vertices in the ITA conventional (crystal) basis of the frozen ops, integer-scaled by PERIOD; metric = integer Gram G = diag(q^2, q^2, p^2) for c/a = p/q. All distances are G-norms; bisectors 2(r-c)^T G x = r^T G r - c^T G c; the cutoff 4 rho^2 <= D^2 holds in the G-norm with the candidate block proven complete by |x_i| <= D sqrt((G^-1)_ii). **Volumes are crystal-basis (coordinate-space) measures**; the Euclidean volume is that times the SAME factor sqrt(det G)/q^3 for the cell, the lattice covolume and the torus, so T * vol(cell) = covol(L) = detL is an exact-rational identity in the crystal basis, equivalent to the Euclidean one. Facets and full-facet pairings are affine (metric-free); the metric enters the tiling certificate through the Voronoi bisector claims, verified in the G-norm by the generator (V1d) and re-verified by the audit's fresh Gram layer.

**V3 tables are metric-independent adjacency data** (which cells share a facet; point ops mod L acting on cell IDs) — stated once; the metric has already done its work in V1/V2.

**LANGUAGE (stated once): G4 passing does NOT establish novelty. Every type below remains "not matched against the catalog snapshot of 2026-09-03"; G5 is separate and has not closed. Kill criteria were live (facet count > 38 asserts; none hit).**

## Sanity gate (cubic control, run first)

- GATE 1 PASS: I4/mmm #139 origin orbit at c/a=1 (G=I, same integer sites [(0, 0, 0), (6, 6, 6)] period 12 as Im-3m #229) through the Gram ladder == accepted cubic ladder on Im-3m #229 origin: all 14 compared numbers identical (code, f, p, aut, T, detL, vol, slots, geometric stabilizer 48, Bravais 48, |ops| 48, proper 24, fixed/free n<=4): {'code': '((1, 2, 3), (0, 4, 5), (0, 5, 6), (0, 7, 8), (1, 9, 10), (1, 11, 2), (2, 12, 13), (3, 13, 14), (3, 14, 9), (4, 8, 15), (4, 15, 16), (5, 16, 17), (6, 17, 18), (6, 18, 7), (7, 19, 8), (9, 20, 10), (10, 21, 11), (11, 21, 12), (12, 22, 13), (14, 22, 20), (15, 19, 23), (16, 23, 17), (18, 23, 19), (20, 22, 21))', 'f': (24, 36, 14), 'p': (4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6), 'aut': 48, 'T': 1, 'detL': 864, 'vol': '864', 'slots': 14, 'site': 16, 'stab_geo': 48, 'brav': 48, 'n_ops': 48, 'n_proper': 24, 'fixed': [1, 7, 67, 734], 'free': [1, 2, 6, 35]}; the one legitimate difference is the SITE symmetry (Im-3m origin 48 vs I4/mmm origin 16) and the ladder's |H/L|=48 vs T*|site|=16 check correctly reports the honeycomb's full group as LARGER than I4/mmm (it is Im-3m); Isom(solid)=48 (Isom+=24); independent enumerator reached n=5 (2s)
- GATE 2 PASS: ceb70631e274e727 IT(212) witness (1/12,1/12,1/12) through the Gram ladder with G=I reproduces G4_RESULTS.md exactly: {'T': 8, 'detL': 1728, 'vol': '216', 'site': 3, 'stab_geo': 3, 'aut': 3, 'brav': 48, 'n_ops': 24, 'n_proper': 24, 'fixed': [8, 88, 1384, 25064], 'free': [1, 5, 59, 1065]}; Isom(solid)=3, |H/L|=24=T*|site|=24, independent enumerator reached n=5 (22s)

## #1 `4e9c9b076cfec323` — IT(92) P4_12_12, f=(40, 60, 22), p=3^8 4^4 5^4 8^2 11^4, aut=2

Witness point (5/24, 5/24, 0), c/a = 5/4, site stabilizer 2, orbit 4 conventional / 4 primitive, stratum dim 1. Candidate wall time 10.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(92) P4_12_12 p=(5/24, 5/24, 0) c/a=5/4 G=diag(16,16,25) period=24 n_conv=4 T=4 site=2 dim=1 f=(40,60,22) p-vec 3^8 4^4 5^4 8^2 11^4 aut=2 W=2 nonsimple=0 cutoff_D2=57600 4rho2_G=116653/9 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.3s | detL=13824 T=4 vol=3456 T*vol=13824 (crystal-basis measure) slots=88 paired 1:1; disjointness G-ball D2=4rho2=116653/9 (coord bound (29, 29, 23)), ball sizes 24..24 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 6.5s | audit re-derived 4 cells x 22 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 3456 each, T*vol == |det|; all 88 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 480 shared-vertex G-equidistance checks, 3520 vertex-side checks, 88 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 16 (embedded ops all signed perms); honeycomb point group |H/L|=8 (0 improper) vs T*|site|=8: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.3s | tables T=4 nbrs=22 |ops|=8 (8 proper, 0 improper; T*|site|=8), identity+closure exact; hands: 0 of 4 classes of the other hand; banked enumerate n<=4: fixed=[4, 44, 668, 11704], free=[1, 6, 89, 1472]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[4, 44, 668, 11704, 222708], free=[1, 6, 89, 1472, 27929], one-sided=[1, 6, 89, 1472, 27929], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 16. Honeycomb point group |H/L| = 8 (0 improper) vs T*|site| = 8: the full symmetry group of the honeycomb IS exactly the generating group G.

## #3 `f654982d74d740f6` — IT(141) I4_1/amd, f=(38, 57, 21), p=3^6 4^7 6^3 8^2 10^2 14^1, aut=2

Witness point (0, 1/12, 1/12), c/a = 1/2, site stabilizer 2, orbit 16 conventional / 8 primitive, stratum dim 2. Candidate wall time 18.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(141) I4_1/amd p=(0, 1/12, 1/12) c/a=1/2 G=diag(4,4,1) period=12 n_conv=16 T=8 site=2 dim=2 f=(38,57,21) p-vec 3^6 4^7 6^3 8^2 10^2 14^1 aut=2 W=2 nonsimple=0 cutoff_D2=2304 4rho2_G=1953/8 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.5s | detL=864 T=8 vol=108 T*vol=864 (crystal-basis measure) slots=168 paired 1:1; disjointness G-ball D2=4rho2=1953/8 (coord bound (8, 8, 16)), ball sizes 42..42 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 10.2s | audit re-derived 8 cells x 21 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 108 each, T*vol == |det|; all 168 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 912 shared-vertex G-equidistance checks, 6384 vertex-side checks, 168 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=1, improper=1; solid achiral), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 16 (embedded ops all signed perms); honeycomb point group |H/L|=16 (8 improper) vs T*|site|=16: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.7s | tables T=8 nbrs=21 |ops|=16 (8 proper, 8 improper; T*|site|=16), identity+closure exact; hands: inconsistent (achiral solid); banked enumerate n<=4: fixed=[8, 84, 1280, 22542], free=[1, 10, 88, 1499]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[8, 84, 1280, 22542, 430680], free=[1, 10, 88, 1499, 27134], one-sided=[1, 16, 160, 2902, 53835], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 1, solid achiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 16. Honeycomb point group |H/L| = 16 (8 improper) vs T*|site| = 16: the full symmetry group of the honeycomb IS exactly the generating group G.

## #4 `4f6d3e68cbd9e729` — IT(98) I4_122, f=(42, 63, 23), p=3^6 4^5 5^2 6^6 8^2 12^1 14^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 3/4, site stabilizer 1, orbit 16 conventional / 8 primitive, stratum dim 3. Candidate wall time 23.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.4s | IT(98) I4_122 p=(1/12, 3/8, 1/6) c/a=3/4 G=diag(16,16,9) period=24 n_conv=16 T=8 site=1 dim=3 f=(42,63,23) p-vec 3^6 4^5 5^2 6^6 8^2 12^1 14^1 aut=1 W=2 nonsimple=0 cutoff_D2=36864 4rho2_G=34914448/5625 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.4s | detL=6912 T=8 vol=864 T*vol=6912 (crystal-basis measure) slots=184 paired 1:1; disjointness G-ball D2=4rho2=34914448/5625 (coord bound (20, 20, 27)), ball sizes 58..58 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 15.1s | audit re-derived 8 cells x 23 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 864 each, T*vol == |det|; all 184 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1008 shared-vertex G-equidistance checks, 7728 vertex-side checks, 184 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 16 (embedded ops all signed perms); honeycomb point group |H/L|=8 (0 improper) vs T*|site|=8: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.7s | tables T=8 nbrs=23 |ops|=8 (8 proper, 0 improper; T*|site|=8), identity+closure exact; hands: 0 of 8 classes of the other hand; banked enumerate n<=4: fixed=[8, 92, 1512, 29116], free=[1, 17, 189, 3723]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[8, 92, 1512, 29116, 613720], free=[1, 17, 189, 3723, 76715], one-sided=[1, 17, 189, 3723, 76715], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 16. Honeycomb point group |H/L| = 8 (0 improper) vs T*|site| = 8: the full symmetry group of the honeycomb IS exactly the generating group G.

## #5 `1497877268495988` — IT(91) P4_122, f=(32, 48, 18), p=3^4 4^4 5^4 6^2 8^2 10^2, aut=2

Witness point (0, 1/12, 0), c/a = 1/2, site stabilizer 2, orbit 4 conventional / 4 primitive, stratum dim 1. Candidate wall time 4.4s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(91) P4_122 p=(0, 1/12, 0) c/a=1/2 G=diag(4,4,1) period=12 n_conv=4 T=4 site=2 dim=1 f=(32,48,18) p-vec 3^4 4^4 5^4 6^2 8^2 10^2 aut=2 W=2 nonsimple=0 cutoff_D2=2304 4rho2_G=480385/484 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.2s | detL=1728 T=4 vol=432 T*vol=1728 (crystal-basis measure) slots=72 paired 1:1; disjointness G-ball D2=4rho2=480385/484 (coord bound (16, 16, 32)), ball sizes 76..76 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 2.4s | audit re-derived 4 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 432 each, T*vol == |det|; all 72 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 384 shared-vertex G-equidistance checks, 2304 vertex-side checks, 72 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 16 (embedded ops all signed perms); honeycomb point group |H/L|=8 (0 improper) vs T*|site|=8: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.7s | tables T=4 nbrs=18 |ops|=8 (8 proper, 0 improper; T*|site|=8), identity+closure exact; hands: 0 of 4 classes of the other hand; banked enumerate n<=4: fixed=[4, 36, 468, 7048], free=[1, 8, 63, 926]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[4, 36, 468, 7048, 115200], free=[1, 8, 63, 926, 14464], one-sided=[1, 8, 63, 926, 14464], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 16. Honeycomb point group |H/L| = 8 (0 improper) vs T*|site| = 8: the full symmetry group of the honeycomb IS exactly the generating group G.

## #6 `e0d18e5ea938d649` — IT(122) I-42d, f=(36, 54, 20), p=3^4 4^8 8^8, aut=2

Witness point (1/24, 1/4, 1/8), c/a = 1, site stabilizer 2, orbit 8 conventional / 4 primitive, stratum dim 1. Candidate wall time 6.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(122) I-42d p=(1/24, 1/4, 1/8) c/a=1 G=diag(1,1,1) period=24 n_conv=8 T=4 site=2 dim=1 f=(36,54,20) p-vec 3^4 4^8 8^8 aut=2 W=2 nonsimple=0 cutoff_D2=2304 4rho2_G=472 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.4s | detL=6912 T=4 vol=1728 T*vol=6912 (crystal-basis measure) slots=80 paired 1:1; disjointness G-ball D2=4rho2=472 (coord bound (22, 22, 22)), ball sizes 30..30 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 3.9s | audit re-derived 4 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1728 each, T*vol == |det|; all 80 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 432 shared-vertex G-equidistance checks, 2880 vertex-side checks, 80 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 48 (embedded ops all signed perms); honeycomb point group |H/L|=8 (4 improper) vs T*|site|=8: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.3s | tables T=4 nbrs=20 |ops|=8 (4 proper, 4 improper; T*|site|=8), identity+closure exact; hands: 2 of 4 classes of the other hand; banked enumerate n<=4: fixed=[4, 40, 552, 8818], free=[1, 6, 74, 1119]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[4, 40, 552, 8818, 153240], free=[1, 6, 74, 1119, 19230], one-sided=[2, 12, 148, 2235, 38460], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 48. Honeycomb point group |H/L| = 8 (4 improper) vs T*|site| = 8: the full symmetry group of the honeycomb IS exactly the generating group G.

## #7 `6797ab70c6015039` — IT(76) P4_1, f=(32, 48, 18), p=3^4 4^4 5^4 6^2 9^4, aut=2

Witness point (1/8, 1/6, 5/12), c/a = 3/2, site stabilizer 1, orbit 4 conventional / 4 primitive, stratum dim 3. Candidate wall time 4.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(76) P4_1 p=(1/8, 1/6, 5/12) c/a=3/2 G=diag(4,4,9) period=24 n_conv=4 T=4 site=1 dim=3 f=(32,48,18) p-vec 3^4 4^4 5^4 6^2 9^4 aut=2 W=2 nonsimple=0 cutoff_D2=20736 4rho2_G=1612052/405 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.3s | detL=13824 T=4 vol=3456 T*vol=13824 (crystal-basis measure) slots=72 paired 1:1; disjointness G-ball D2=4rho2=1612052/405 (coord bound (32, 32, 22)), ball sizes 26..26 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 2.6s | audit re-derived 4 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 3456 each, T*vol == |det|; all 72 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 384 shared-vertex G-equidistance checks, 2304 vertex-side checks, 72 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 16 (embedded ops all signed perms); honeycomb point group |H/L|=4 (0 improper) vs T*|site|=4: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.3s | tables T=4 nbrs=18 |ops|=4 (4 proper, 0 improper; T*|site|=4), identity+closure exact; hands: 0 of 4 classes of the other hand; banked enumerate n<=4: fixed=[4, 36, 452, 6556], free=[1, 9, 113, 1639]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[4, 36, 452, 6556, 103224], free=[1, 9, 113, 1639, 25806], one-sided=[1, 9, 113, 1639, 25806], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 16. Honeycomb point group |H/L| = 4 (0 improper) vs T*|site| = 4: the full symmetry group of the honeycomb IS exactly the generating group G.

## #9 `086ac96faf390886` — IT(76) P4_1, f=(36, 54, 20), p=3^2 4^8 5^6 10^4, aut=2

Witness point (1/8, 1/6, 5/12), c/a = 7/5, site stabilizer 1, orbit 4 conventional / 4 primitive, stratum dim 3. Candidate wall time 6.5s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(76) P4_1 p=(1/8, 1/6, 5/12) c/a=7/5 G=diag(25,25,49) period=24 n_conv=4 T=4 site=1 dim=3 f=(36,54,20) p-vec 3^2 4^8 5^6 10^4 aut=2 W=2 nonsimple=0 cutoff_D2=112896 4rho2_G=10624321/441 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.3s | detL=13824 T=4 vol=3456 T*vol=13824 (crystal-basis measure) slots=80 paired 1:1; disjointness G-ball D2=4rho2=10624321/441 (coord bound (32, 32, 23)), ball sizes 26..26 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 4.2s | audit re-derived 4 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 3456 each, T*vol == |det|; all 80 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 432 shared-vertex G-equidistance checks, 2880 vertex-side checks, 80 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 16 (embedded ops all signed perms); honeycomb point group |H/L|=4 (0 improper) vs T*|site|=4: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.8s | tables T=4 nbrs=20 |ops|=4 (4 proper, 0 improper; T*|site|=4), identity+closure exact; hands: 0 of 4 classes of the other hand; banked enumerate n<=4: fixed=[4, 40, 560, 9056], free=[1, 10, 140, 2264]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[4, 40, 560, 9056, 159048], free=[1, 10, 140, 2264, 39762], one-sided=[1, 10, 140, 2264, 39762], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 16. Honeycomb point group |H/L| = 4 (0 improper) vs T*|site| = 4: the full symmetry group of the honeycomb IS exactly the generating group G.

## #10 `164d4bd63d82d0c3` — IT(76) P4_1, f=(40, 60, 22), p=3^6 4^6 5^2 6^4 11^4, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 5/4, site stabilizer 1, orbit 4 conventional / 4 primitive, stratum dim 3. Candidate wall time 10.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(76) P4_1 p=(1/8, 1/6, 5/12) c/a=5/4 G=diag(16,16,25) period=24 n_conv=4 T=4 site=1 dim=3 f=(40,60,22) p-vec 3^6 4^6 5^2 6^4 11^4 aut=1 W=2 nonsimple=0 cutoff_D2=57600 4rho2_G=130576/9 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.3s | detL=13824 T=4 vol=3456 T*vol=13824 (crystal-basis measure) slots=88 paired 1:1; disjointness G-ball D2=4rho2=130576/9 (coord bound (31, 31, 25)), ball sizes 28..28 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 6.8s | audit re-derived 4 cells x 22 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 3456 each, T*vol == |det|; all 88 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 480 shared-vertex G-equidistance checks, 3520 vertex-side checks, 88 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 16 (embedded ops all signed perms); honeycomb point group |H/L|=4 (0 improper) vs T*|site|=4: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.8s | tables T=4 nbrs=22 |ops|=4 (4 proper, 0 improper; T*|site|=4), identity+closure exact; hands: 0 of 4 classes of the other hand; banked enumerate n<=4: fixed=[4, 44, 676, 11988], free=[1, 11, 169, 2997]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[4, 44, 676, 11988, 230844], free=[1, 11, 169, 2997, 57711], one-sided=[1, 11, 169, 2997, 57711], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 16. Honeycomb point group |H/L| = 4 (0 improper) vs T*|site| = 4: the full symmetry group of the honeycomb IS exactly the generating group G.

## #11 `5dc2479b9bc14edc` — IT(98) I4_122, f=(42, 63, 23), p=3^8 4^5 5^2 6^2 8^3 10^2 16^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 9/16, site stabilizer 1, orbit 16 conventional / 8 primitive, stratum dim 3. Candidate wall time 25.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(98) I4_122 p=(1/12, 3/8, 1/6) c/a=9/16 G=diag(256,256,81) period=24 n_conv=16 T=8 site=1 dim=3 f=(42,63,23) p-vec 3^8 4^5 5^2 6^2 8^3 10^2 16^1 aut=1 W=2 nonsimple=0 cutoff_D2=589824 4rho2_G=4444649/50 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.9s | detL=6912 T=8 vol=864 T*vol=6912 (crystal-basis measure) slots=184 paired 1:1; disjointness G-ball D2=4rho2=4444649/50 (coord bound (19, 19, 34)), ball sizes 62..62 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 16.9s | audit re-derived 8 cells x 23 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 864 each, T*vol == |det|; all 184 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1008 shared-vertex G-equidistance checks, 7728 vertex-side checks, 184 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 16 (embedded ops all signed perms); honeycomb point group |H/L|=8 (0 improper) vs T*|site|=8: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.5s | tables T=8 nbrs=23 |ops|=8 (8 proper, 0 improper; T*|site|=8), identity+closure exact; hands: 0 of 8 classes of the other hand; banked enumerate n<=4: fixed=[8, 92, 1544, 30206], free=[1, 17, 193, 3863]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[8, 92, 1544, 30206, 644704], free=[1, 17, 193, 3863, 80588], one-sided=[1, 17, 193, 3863, 80588], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 16. Honeycomb point group |H/L| = 8 (0 improper) vs T*|site| = 8: the full symmetry group of the honeycomb IS exactly the generating group G.

## #12 `3ebbca7ed2eda199` — IT(98) I4_122, f=(40, 60, 22), p=3^4 4^8 5^2 6^5 8^1 12^1 16^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 1/2, site stabilizer 1, orbit 16 conventional / 8 primitive, stratum dim 3. Candidate wall time 19.5s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(98) I4_122 p=(1/12, 3/8, 1/6) c/a=1/2 G=diag(4,4,1) period=24 n_conv=16 T=8 site=1 dim=3 f=(40,60,22) p-vec 3^4 4^8 5^2 6^5 8^1 12^1 16^1 aut=1 W=2 nonsimple=0 cutoff_D2=9216 4rho2_G=33488/25 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.8s | detL=6912 T=8 vol=864 T*vol=6912 (crystal-basis measure) slots=176 paired 1:1; disjointness G-ball D2=4rho2=33488/25 (coord bound (19, 19, 37)), ball sizes 63..63 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 12.2s | audit re-derived 8 cells x 22 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 864 each, T*vol == |det|; all 176 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 960 shared-vertex G-equidistance checks, 7040 vertex-side checks, 176 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 16 (embedded ops all signed perms); honeycomb point group |H/L|=8 (0 improper) vs T*|site|=8: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 5.1s | tables T=8 nbrs=22 |ops|=8 (8 proper, 0 improper; T*|site|=8), identity+closure exact; hands: 0 of 8 classes of the other hand; banked enumerate n<=4: fixed=[8, 88, 1416, 26406], free=[1, 17, 177, 3394]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[8, 88, 1416, 26406, 535448], free=[1, 17, 177, 3394, 66931], one-sided=[1, 17, 177, 3394, 66931], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 16. Honeycomb point group |H/L| = 8 (0 improper) vs T*|site| = 8: the full symmetry group of the honeycomb IS exactly the generating group G.

## #13 `7575121042ade3b3` — IT(98) I4_122, f=(32, 48, 18), p=4^11 6^4 8^1 10^2, aut=2

Witness point (1/12, 1/12, 0), c/a = 7/4, site stabilizer 2, orbit 8 conventional / 4 primitive, stratum dim 1. Candidate wall time 4.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(98) I4_122 p=(1/12, 1/12, 0) c/a=7/4 G=diag(16,16,49) period=12 n_conv=8 T=4 site=2 dim=1 f=(32,48,18) p-vec 4^11 6^4 8^1 10^2 aut=2 W=2 nonsimple=0 cutoff_D2=28224 4rho2_G=412849/128 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.4s | detL=864 T=4 vol=216 T*vol=864 (crystal-basis measure) slots=72 paired 1:1; disjointness G-ball D2=4rho2=412849/128 (coord bound (15, 15, 9)), ball sizes 40..40 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 2.5s | audit re-derived 4 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 216 each, T*vol == |det|; all 72 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 384 shared-vertex G-equidistance checks, 2304 vertex-side checks, 72 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 16 (embedded ops all signed perms); honeycomb point group |H/L|=8 (0 improper) vs T*|site|=8: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.6s | tables T=4 nbrs=18 |ops|=8 (8 proper, 0 improper; T*|site|=8), identity+closure exact; hands: 0 of 4 classes of the other hand; banked enumerate n<=4: fixed=[4, 36, 484, 7550], free=[1, 8, 65, 989]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[4, 36, 484, 7550, 128072], free=[1, 8, 65, 989, 16078], one-sided=[1, 8, 65, 989, 16078], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 16. Honeycomb point group |H/L| = 8 (0 improper) vs T*|site| = 8: the full symmetry group of the honeycomb IS exactly the generating group G.

## #14 `213c7a114d5a97a8` — IT(98) I4_122, f=(42, 63, 23), p=3^6 4^4 5^4 6^5 8^2 10^1 16^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 11/16, site stabilizer 1, orbit 16 conventional / 8 primitive, stratum dim 3. Candidate wall time 24.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(98) I4_122 p=(1/12, 3/8, 1/6) c/a=11/16 G=diag(256,256,121) period=24 n_conv=16 T=8 site=1 dim=3 f=(42,63,23) p-vec 3^6 4^4 5^4 6^5 8^2 10^1 16^1 aut=1 W=2 nonsimple=0 cutoff_D2=589824 4rho2_G=4837369/50 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.5s | detL=6912 T=8 vol=864 T*vol=6912 (crystal-basis measure) slots=184 paired 1:1; disjointness G-ball D2=4rho2=4837369/50 (coord bound (20, 20, 29)), ball sizes 60..60 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 16.3s | audit re-derived 8 cells x 23 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 864 each, T*vol == |det|; all 184 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1008 shared-vertex G-equidistance checks, 7728 vertex-side checks, 184 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 16 (embedded ops all signed perms); honeycomb point group |H/L|=8 (0 improper) vs T*|site|=8: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.6s | tables T=8 nbrs=23 |ops|=8 (8 proper, 0 improper; T*|site|=8), identity+closure exact; hands: 0 of 8 classes of the other hand; banked enumerate n<=4: fixed=[8, 92, 1528, 29842], free=[1, 17, 191, 3817]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[8, 92, 1528, 29842, 638960], free=[1, 17, 191, 3817, 79870], one-sided=[1, 17, 191, 3817, 79870], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 16. Honeycomb point group |H/L| = 8 (0 improper) vs T*|site| = 8: the full symmetry group of the honeycomb IS exactly the generating group G.

## #15 `2e8e49eb28497267` — IT(95) P4_322, f=(40, 60, 22), p=3^6 4^7 5^2 6^1 8^3 10^2 14^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 53/40, site stabilizer 1, orbit 8 conventional / 8 primitive, stratum dim 3. Candidate wall time 20.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(95) P4_322 p=(1/12, 3/8, 1/6) c/a=53/40 G=diag(1600,1600,2809) period=24 n_conv=8 T=8 site=1 dim=3 f=(40,60,22) p-vec 3^6 4^7 5^2 6^1 8^3 10^2 14^1 aut=1 W=2 nonsimple=0 cutoff_D2=6471936 4rho2_G=1092836 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.9s | detL=13824 T=8 vol=1728 T*vol=13824 (crystal-basis measure) slots=176 paired 1:1; disjointness G-ball D2=4rho2=1092836 (coord bound (27, 27, 20)), ball sizes 35..35 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 14.5s | audit re-derived 8 cells x 22 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1728 each, T*vol == |det|; all 176 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 960 shared-vertex G-equidistance checks, 7040 vertex-side checks, 176 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 16 (embedded ops all signed perms); honeycomb point group |H/L|=8 (0 improper) vs T*|site|=8: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 5.0s | tables T=8 nbrs=22 |ops|=8 (8 proper, 0 improper; T*|site|=8), identity+closure exact; hands: 0 of 8 classes of the other hand; banked enumerate n<=4: fixed=[8, 88, 1384, 25140], free=[1, 15, 173, 3204]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[8, 88, 1384, 25140, 495544], free=[1, 15, 173, 3204, 61943], one-sided=[1, 15, 173, 3204, 61943], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 16. Honeycomb point group |H/L| = 8 (0 improper) vs T*|site| = 8: the full symmetry group of the honeycomb IS exactly the generating group G.

## #2 `49cedbdd58376fac` — IT(92) P4_12_12, f=(44, 66, 24), p=3^10 4^4 6^4 7^2 12^4, aut=2

**LABEL: WALL/TRANSITION TYPE (thin band in (x,b), COLLISION_PHASE2_RESULTS.md perturbation #2) — certified as a tiling like the others; its finalist status is a main-session call.**

Witness point (5/24, 5/24, 0), c/a = 19/16, site stabilizer 2, orbit 4 conventional / 4 primitive, stratum dim 1. Candidate wall time 14.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(92) P4_12_12 p=(5/24, 5/24, 0) c/a=19/16 G=diag(256,256,361) period=24 n_conv=4 T=4 site=2 dim=1 f=(44,66,24) p-vec 3^10 4^4 6^4 7^2 12^4 aut=2 W=2 nonsimple=0 cutoff_D2=831744 4rho2_G=203536 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.3s | detL=13824 T=4 vol=3456 T*vol=13824 (crystal-basis measure) slots=96 paired 1:1; disjointness G-ball D2=4rho2=203536 (coord bound (29, 29, 24)), ball sizes 24..24 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 10.2s | audit re-derived 4 cells x 24 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 3456 each, T*vol == |det|; all 96 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 528 shared-vertex G-equidistance checks, 4224 vertex-side checks, 96 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 16 (embedded ops all signed perms); honeycomb point group |H/L|=8 (0 improper) vs T*|site|=8: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 4.1s | tables T=4 nbrs=24 |ops|=8 (8 proper, 0 improper; T*|site|=8), identity+closure exact; hands: 0 of 4 classes of the other hand; banked enumerate n<=4: fixed=[4, 48, 792, 15060], free=[1, 7, 105, 1901]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[4, 48, 792, 15060, 310884], free=[1, 7, 105, 1901, 38968], one-sided=[1, 7, 105, 1901, 38968], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 16. Honeycomb point group |H/L| = 8 (0 improper) vs T*|site| = 8: the full symmetry group of the honeycomb IS exactly the generating group G.

## Per-cell verdict table

| # | type | IT | c/a | f | V0 | V1 gen | V1 audit | V2 | V3 | Burnside identity | open/wall (carried over) | wall |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `4e9c9b076cfec323` | 92 | 5/4 | (40, 60, 22) | PASS | PASS | PASS | PASS | PASS | PASS banked n<=4 + independent n<=5 (all + proper) | OPEN (perturbation: point OPEN / b OPEN) | 10s |
| 3 | `f654982d74d740f6` | 141 | 1/2 | (38, 57, 21) | PASS | PASS | PASS | PASS | PASS | PASS banked n<=4 + independent n<=5 (all + proper) | OPEN (perturbation: point OPEN / b OPEN) | 19s |
| 4 | `4f6d3e68cbd9e729` | 98 | 3/4 | (42, 63, 23) | PASS | PASS | PASS | PASS | PASS | PASS banked n<=4 + independent n<=5 (all + proper) | open-likely (triage, 5 b) | 24s |
| 5 | `1497877268495988` | 91 | 1/2 | (32, 48, 18) | PASS | PASS | PASS | PASS | PASS | PASS banked n<=4 + independent n<=5 (all + proper) | open-likely (triage, 7 b) | 4s |
| 6 | `e0d18e5ea938d649` | 122 | 1 | (36, 54, 20) | PASS | PASS | PASS | PASS | PASS | PASS banked n<=4 + independent n<=5 (all + proper) | open-likely (triage, 5 b) | 7s |
| 7 | `6797ab70c6015039` | 76 | 3/2 | (32, 48, 18) | PASS | PASS | PASS | PASS | PASS | PASS banked n<=4 + independent n<=5 (all + proper) | open-likely (triage, 8 b) | 4s |
| 9 | `086ac96faf390886` | 76 | 7/5 | (36, 54, 20) | PASS | PASS | PASS | PASS | PASS | PASS banked n<=4 + independent n<=5 (all + proper) | open-likely (triage, 5 b) | 6s |
| 10 | `164d4bd63d82d0c3` | 76 | 5/4 | (40, 60, 22) | PASS | PASS | PASS | PASS | PASS | PASS banked n<=4 + independent n<=5 (all + proper) | open-likely (triage, 3 b) | 10s |
| 11 | `5dc2479b9bc14edc` | 98 | 9/16 | (42, 63, 23) | PASS | PASS | PASS | PASS | PASS | PASS banked n<=4 + independent n<=5 (all + proper) | open-likely (triage, 3 b; metric-thin P5-only) | 26s |
| 12 | `3ebbca7ed2eda199` | 98 | 1/2 | (40, 60, 22) | PASS | PASS | PASS | PASS | PASS | PASS banked n<=4 + independent n<=5 (all + proper) | indeterminate (triage, 2 b) | 20s |
| 13 | `7575121042ade3b3` | 98 | 7/4 | (32, 48, 18) | PASS | PASS | PASS | PASS | PASS | PASS banked n<=4 + independent n<=5 (all + proper) | open-likely (triage, 8 b) | 5s |
| 14 | `213c7a114d5a97a8` | 98 | 11/16 | (42, 63, 23) | PASS | PASS | PASS | PASS | PASS | PASS banked n<=4 + independent n<=5 (all + proper) | indeterminate (triage, 2 b; metric-thin P5-only) | 25s |
| 15 | `2e8e49eb28497267` | 95 | 53/40 | (40, 60, 22) | PASS | PASS | PASS | PASS | PASS | PASS banked n<=4 + independent n<=5 (all + proper) | open-likely (triage, 4 b; metric-thin P5-only) | 21s |
| 2 | `49cedbdd58376fac` | 92 | 19/16 | (44, 66, 24) | PASS | PASS | PASS | PASS | PASS | PASS banked n<=4 + independent n<=5 (all + proper) | WALL/THIN BAND (perturbation: point WALL to 1/1536 / b OPEN) | 15s |

Notes: (i) `e0d18e5ea938d649` (#6) is witnessed at c/a = 1, where the BCT lattice of I-42d is metrically cubic (BCC) — its Bravais point group in G is therefore 48, not 16; the honeycomb point group is still |H/L| = 8 = T*|site| (the SITE SET, not the lattice, decides), so its full symmetry group is I-42d. The type also occurs at c/a in {55/64, 7/8, 5/4, 41/32} in the store, where the lattice is genuinely tetragonal. (ii) `6797ab70c6015039` (#7) and `086ac96faf390886` (#9) have combinatorial aut 2 but Isom(solid) = 1: the map automorphism is not realised by any G-isometry at the witness (a combinatorial-only symmetry). (iii) `f654982d74d740f6` (#3, I4_1/amd) is the only achiral solid (its site symmetry contains a mirror); every other solid is chiral and every other honeycomb here is a proper (chiral) honeycomb with all translation classes of one hand. (iv) For every cell |H/L| = T*|site|: the full symmetry group of each honeycomb is exactly its generating space group (as in the cubic round).

## Isometry vs site vs aut summary

| # | type | IT | site | Isom_fix_site | Isom(solid) | Isom+ | solid | aut | \|H/L\| | T*site | full group = G |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `4e9c9b076cfec323` | 92 | 2 | 2 | 2 | 2 | chiral | 2 | 8 | 8 | yes |
| 3 | `f654982d74d740f6` | 141 | 2 | 2 | 2 | 1 | achiral | 2 | 16 | 16 | yes |
| 4 | `4f6d3e68cbd9e729` | 98 | 1 | 1 | 1 | 1 | chiral | 1 | 8 | 8 | yes |
| 5 | `1497877268495988` | 91 | 2 | 2 | 2 | 2 | chiral | 2 | 8 | 8 | yes |
| 6 | `e0d18e5ea938d649` | 122 | 2 | 2 | 2 | 2 | chiral | 2 | 8 | 8 | yes |
| 7 | `6797ab70c6015039` | 76 | 1 | 1 | 1 | 1 | chiral | 2 | 4 | 4 | yes |
| 9 | `086ac96faf390886` | 76 | 1 | 1 | 1 | 1 | chiral | 2 | 4 | 4 | yes |
| 10 | `164d4bd63d82d0c3` | 76 | 1 | 1 | 1 | 1 | chiral | 1 | 4 | 4 | yes |
| 11 | `5dc2479b9bc14edc` | 98 | 1 | 1 | 1 | 1 | chiral | 1 | 8 | 8 | yes |
| 12 | `3ebbca7ed2eda199` | 98 | 1 | 1 | 1 | 1 | chiral | 1 | 8 | 8 | yes |
| 13 | `7575121042ade3b3` | 98 | 2 | 2 | 2 | 2 | chiral | 2 | 8 | 8 | yes |
| 14 | `213c7a114d5a97a8` | 98 | 1 | 1 | 1 | 1 | chiral | 1 | 8 | 8 | yes |
| 15 | `2e8e49eb28497267` | 95 | 1 | 1 | 1 | 1 | chiral | 1 | 8 | 8 | yes |
| 2 | `49cedbdd58376fac` | 92 | 2 | 2 | 2 | 2 | chiral | 2 | 8 | 8 | yes |

## Counts reached (banked n<=4 == independent; independent to n<=5)

| # | type | fixed (indep, n=1..reached) | free | one-sided | indep reached | indep wall |
|---|---|---|---|---|---|---|
| 1 | `4e9c9b076cfec323` | [4, 44, 668, 11704, 222708] | [1, 6, 89, 1472, 27929] | [1, 6, 89, 1472, 27929] | 5 | 3s |
| 3 | `f654982d74d740f6` | [8, 84, 1280, 22542, 430680] | [1, 10, 88, 1499, 27134] | [1, 16, 160, 2902, 53835] | 5 | 6s |
| 4 | `4f6d3e68cbd9e729` | [8, 92, 1512, 29116, 613720] | [1, 17, 189, 3723, 76715] | [1, 17, 189, 3723, 76715] | 5 | 6s |
| 5 | `1497877268495988` | [4, 36, 468, 7048, 115200] | [1, 8, 63, 926, 14464] | [1, 8, 63, 926, 14464] | 5 | 1s |
| 6 | `e0d18e5ea938d649` | [4, 40, 552, 8818, 153240] | [1, 6, 74, 1119, 19230] | [2, 12, 148, 2235, 38460] | 5 | 2s |
| 7 | `6797ab70c6015039` | [4, 36, 452, 6556, 103224] | [1, 9, 113, 1639, 25806] | [1, 9, 113, 1639, 25806] | 5 | 1s |
| 9 | `086ac96faf390886` | [4, 40, 560, 9056, 159048] | [1, 10, 140, 2264, 39762] | [1, 10, 140, 2264, 39762] | 5 | 2s |
| 10 | `164d4bd63d82d0c3` | [4, 44, 676, 11988, 230844] | [1, 11, 169, 2997, 57711] | [1, 11, 169, 2997, 57711] | 5 | 2s |
| 11 | `5dc2479b9bc14edc` | [8, 92, 1544, 30206, 644704] | [1, 17, 193, 3863, 80588] | [1, 17, 193, 3863, 80588] | 5 | 6s |
| 12 | `3ebbca7ed2eda199` | [8, 88, 1416, 26406, 535448] | [1, 17, 177, 3394, 66931] | [1, 17, 177, 3394, 66931] | 5 | 4s |
| 13 | `7575121042ade3b3` | [4, 36, 484, 7550, 128072] | [1, 8, 65, 989, 16078] | [1, 8, 65, 989, 16078] | 5 | 1s |
| 14 | `213c7a114d5a97a8` | [8, 92, 1528, 29842, 638960] | [1, 17, 191, 3817, 79870] | [1, 17, 191, 3817, 79870] | 5 | 6s |
| 15 | `2e8e49eb28497267` | [8, 88, 1384, 25140, 495544] | [1, 15, 173, 3204, 61943] | [1, 15, 173, 3204, 61943] | 5 | 4s |
| 2 | `49cedbdd58376fac` | [4, 48, 792, 15060, 310884] | [1, 7, 105, 1901, 38968] | [1, 7, 105, 1901, 38968] | 5 | 4s |

## Deferrals / failures

- none

Total wall time 220s. Deterministic except the timing columns. Artifacts: `g4p2_tables_<id>.json` (+ `.txt` enumerator input, `_indep.json` independent-enumerator record) per cell; `g4p2_control_*` for the sanity gate.

Re-run for acceptance: `python3 g4_certify_gram.py` (exit 0 required).
