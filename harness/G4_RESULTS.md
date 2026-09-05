# G4 certificate results — V0-V3 ladder (2026-08-30)

Gate: `../ANCHORS.md` G4 (paper-I-standard ladder, V0-V3 per `../HARNESS_DESIGN_FABLE5_2026-08-27.md` §3). Generator: `g4_certify.py` (this run). Inputs: `phase1_types.json` stored witnesses, frozen G1 `spacegroups.json`, the G0/G2-validated pipeline. V1's independent audit shares no geometry code with `exact_cell.py`/`mint_tables.py` (fresh facet/volume/pairing implementations inside `g4_certify.py`, `_a_*`/`v1_audit`). V3 uses the banked `export_tables.py` + compiled `enumerate` + `burnside_generic.py` (POLYFORMS_II).

**LANGUAGE (stated once): G4 passing does NOT establish novelty. These types remain "not matched against the catalog snapshot of 2026-08-28"; novelty diligence is G5 and has not run on them. Kill criteria were live (facet count > 38 asserts; none hit).**

## `ceb70631e274e727` — IT(212) P4_332, f=(37, 57, 22), p=3^6 4^6 5^6 10^3 12^1, aut=3

Witness point (1/12, 1/12, 1/12), site stabilizer 3, orbit 8 conventional / 8 primitive. Candidate wall time 11.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation | **PASS** | 0.1s | IT(212) P4_332 p=(1/12, 1/12, 1/12) period=12 n_conv=8 T=8 f=(37,57,22) p-vec 3^6 4^6 5^6 10^3 12^1 aut=3 cutoff_D=24 4rho2=507/4 |
| V1 tiling certificate (generator) | **PASS** | 0.5s | detL=1728 T=8 vol=216 T*vol=1728 slots=176 paired 1:1; disjointness ball D=12 (D^2=144 >= 4rho2=507/4), ball sizes 40..40 sites/rep, all bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit | **PASS** | 8.6s | audit re-derived 8 cells x 22 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 216 each, T*vol == |det|; all 176 pairing claims verified full-facet both sides, slots covered exactly once |
| V2 symmetry certification | **PASS** | 0.0s | site=3, stab_geo=3 (ALL orthogonal maps, Gram-triple), aut_comb=3; chain site<=stab_geo contained, divisibility 3|3|3 holds; Bravais point group of L: order 48 (GL3(Z) Gram-preserving, proven coefficient bound), embedded ops all signed perms (checked, not assumed); stabilizer elements all signed perms |
| V3 Burnside identity | **PASS** | 1.8s | tables T=8 nbrs=22 |ops|=24 (24 proper, 0 improper; T*|site|=24), identity+closure exact; banked enumerate n<=4: fixed=[8, 88, 1384, 25064], free=[1, 5, 59, 1065]; burnside_generic: |ops|*free(n) == sum Fix_m(n) ALL PASS n<=4 (its independent fixed recount agrees) |

Symmetry reconciliation: site symmetry 3 <= geometric stabilizer 3 <= combinatorial aut 3 (containment + divisibility verified exactly). Bravais point group of the actual lattice: order 48, embedded ops ARE the signed permutations (checked, not assumed).

## `359beee832567a71` — IT(230) Ia-3d, f=(40, 61, 23), p=4^20 11^2 20^1, aut=4

Witness point (1/12, 1/6, 1/8), site stabilizer 2, orbit 48 conventional / 24 primitive. Candidate wall time 57.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation | **PASS** | 0.7s | IT(230) Ia-3d p=(1/12, 1/6, 1/8) period=24 n_conv=48 T=24 f=(40,61,23) p-vec 4^20 11^2 20^1 aut=4 cutoff_D=48 4rho2=176 |
| V1 tiling certificate (generator) | **PASS** | 7.2s | detL=6912 T=24 vol=288 T*vol=6912 slots=552 paired 1:1; disjointness ball D=14 (D^2=196 >= 4rho2=176), ball sizes 43..43 sites/rep, all bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit | **PASS** | 34.7s | audit re-derived 24 cells x 23 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 288 each, T*vol == |det|; all 552 pairing claims verified full-facet both sides, slots covered exactly once |
| V2 symmetry certification | **PASS** | 0.0s | site=2, stab_geo=2 (ALL orthogonal maps, Gram-triple), aut_comb=4; chain site<=stab_geo contained, divisibility 2|2|4 holds; Bravais point group of L: order 48 (GL3(Z) Gram-preserving, proven coefficient bound), embedded ops all signed perms (checked, not assumed); stabilizer elements all signed perms |
| V3 Burnside identity | **PASS** | 14.7s | tables T=24 nbrs=23 |ops|=48 (24 proper, 24 improper; T*|site|=48), identity+closure exact; banked enumerate n<=4: fixed=[24, 276, 5096, 111732], free=[1, 7, 112, 2349]; burnside_generic: |ops|*free(n) == sum Fix_m(n) ALL PASS n<=4 (its independent fixed recount agrees) |

Symmetry reconciliation: site symmetry 2 <= geometric stabilizer 2 <= combinatorial aut 4 (containment + divisibility verified exactly). Bravais point group of the actual lattice: order 48, embedded ops ARE the signed permutations (checked, not assumed).

## `8cf50403cf88c455` — IT(220) I-43d, f=(16, 25, 11), p=3^2 4^1 5^8, aut=4

Witness point (0, 0, 1/4), site stabilizer 2, orbit 24 conventional / 12 primitive. Candidate wall time 2.1s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation | **PASS** | 0.2s | IT(220) I-43d p=(0, 0, 1/4) period=12 n_conv=24 T=12 f=(16,25,11) p-vec 3^2 4^1 5^8 aut=4 cutoff_D=24 4rho2=51 |
| V1 tiling certificate (generator) | **PASS** | 0.7s | detL=864 T=12 vol=72 T*vol=864 slots=132 paired 1:1; disjointness ball D=8 (D^2=64 >= 4rho2=51), ball sizes 31..31 sites/rep, all bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit | **PASS** | 0.4s | audit re-derived 12 cells x 11 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 72 each, T*vol == |det|; all 132 pairing claims verified full-facet both sides, slots covered exactly once |
| V2 symmetry certification | **PASS** | 0.0s | site=2, stab_geo=2 (ALL orthogonal maps, Gram-triple), aut_comb=4; chain site<=stab_geo contained, divisibility 2|2|4 holds; Bravais point group of L: order 48 (GL3(Z) Gram-preserving, proven coefficient bound), embedded ops all signed perms (checked, not assumed); stabilizer elements all signed perms |
| V3 Burnside identity | **PASS** | 0.8s | tables T=12 nbrs=11 |ops|=24 (12 proper, 12 improper; T*|site|=24), identity+closure exact; banked enumerate n<=4: fixed=[12, 66, 524, 4866], free=[1, 4, 25, 209]; burnside_generic: |ops|*free(n) == sum Fix_m(n) ALL PASS n<=4 (its independent fixed recount agrees) |

Symmetry reconciliation: site symmetry 2 <= geometric stabilizer 2 <= combinatorial aut 4 (containment + divisibility verified exactly). Bravais point group of the actual lattice: order 48, embedded ops ARE the signed permutations (checked, not assumed).

---

# BATCH 2 (2026-08-30, later) — remaining 8 of the 11-candidate G4 queue

The 2 remaining Schmitt-collision-screen survivors (`SCHMITT_COLLISION_RESULTS.md`) followed by the 6 remaining ABSENT-all triage types (`TRIAGE_RESULT.md`; `8cf50403cf88c455` was certified in batch 1). Same ladder, same script, same language gate as above.

## `c314dedd38208a2e` — IT(212) P4_332, f=(30, 46, 18), p=3^4 4^2 5^8 7^2 9^2, aut=2

Witness point (1/12, 1/6, 1/8), site stabilizer 2, orbit 12 conventional / 12 primitive. Candidate wall time 8.4s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation | **PASS** | 0.1s | IT(212) P4_332 p=(1/12, 1/6, 1/8) period=24 n_conv=12 T=12 f=(30,46,18) p-vec 3^4 4^2 5^8 7^2 9^2 aut=2 cutoff_D=48 4rho2=1624/3 |
| V1 tiling certificate (generator) | **PASS** | 1.0s | detL=13824 T=12 vol=1152 T*vol=13824 slots=216 paired 1:1; disjointness ball D=24 (D^2=576 >= 4rho2=1624/3), ball sizes 60..60 sites/rep, all bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit | **PASS** | 5.4s | audit re-derived 12 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 216 pairing claims verified full-facet both sides, slots covered exactly once |
| V2 symmetry certification | **PASS** | 0.0s | site=2, stab_geo=2 (ALL orthogonal maps, Gram-triple), aut_comb=2; chain site<=stab_geo contained, divisibility 2|2|2 holds; Bravais point group of L: order 48 (GL3(Z) Gram-preserving, proven coefficient bound), embedded ops all signed perms (checked, not assumed); stabilizer elements all signed perms |
| V3 Burnside identity | **PASS** | 1.9s | tables T=12 nbrs=18 |ops|=24 (24 proper, 0 improper; T*|site|=24), identity+closure exact; banked enumerate n<=4: fixed=[12, 108, 1516, 25452], free=[1, 6, 69, 1081]; burnside_generic: |ops|*free(n) == sum Fix_m(n) ALL PASS n<=4 (its independent fixed recount agrees) |

Symmetry reconciliation: site symmetry 2 <= geometric stabilizer 2 <= combinatorial aut 2 (containment + divisibility verified exactly). Bravais point group of the actual lattice: order 48, embedded ops ARE the signed permutations (checked, not assumed).

## `aa6b0077c3234d24` — IT(214) I4_132, f=(30, 47, 19), p=3^4 4^5 5^6 6^2 10^2, aut=2

Witness point (0, 1/4, 1/12), site stabilizer 2, orbit 24 conventional / 12 primitive. Candidate wall time 9.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation | **PASS** | 0.3s | IT(214) I4_132 p=(0, 1/4, 1/12) period=12 n_conv=24 T=12 f=(30,47,19) p-vec 3^4 4^5 5^6 6^2 10^2 aut=2 cutoff_D=24 4rho2=115 |
| V1 tiling certificate (generator) | **PASS** | 1.4s | detL=864 T=12 vol=72 T*vol=864 slots=228 paired 1:1; disjointness ball D=11 (D^2=121 >= 4rho2=115), ball sizes 84..84 sites/rep, all bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit | **PASS** | 5.5s | audit re-derived 12 cells x 19 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 72 each, T*vol == |det|; all 228 pairing claims verified full-facet both sides, slots covered exactly once |
| V2 symmetry certification | **PASS** | 0.0s | site=2, stab_geo=2 (ALL orthogonal maps, Gram-triple), aut_comb=2; chain site<=stab_geo contained, divisibility 2|2|2 holds; Bravais point group of L: order 48 (GL3(Z) Gram-preserving, proven coefficient bound), embedded ops all signed perms (checked, not assumed); stabilizer elements all signed perms |
| V3 Burnside identity | **PASS** | 2.2s | tables T=12 nbrs=19 |ops|=24 (24 proper, 0 improper; T*|site|=24), identity+closure exact; banked enumerate n<=4: fixed=[12, 114, 1588, 25734], free=[1, 8, 72, 1118]; burnside_generic: |ops|*free(n) == sum Fix_m(n) ALL PASS n<=4 (its independent fixed recount agrees) |

Symmetry reconciliation: site symmetry 2 <= geometric stabilizer 2 <= combinatorial aut 2 (containment + divisibility verified exactly). Bravais point group of the actual lattice: order 48, embedded ops ARE the signed permutations (checked, not assumed).

## `f3d0f39a0b9676b9` — IT(214) I4_132, f=(10, 17, 9), p=3^4 4^3 5^2, aut=2

Witness point (0, 0, 1/4), site stabilizer 2, orbit 24 conventional / 12 primitive. Candidate wall time 1.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation | **PASS** | 0.2s | IT(214) I4_132 p=(0, 0, 1/4) period=12 n_conv=24 T=12 f=(10,17,9) p-vec 3^4 4^3 5^2 aut=2 cutoff_D=24 4rho2=99 |
| V1 tiling certificate (generator) | **PASS** | 0.5s | detL=864 T=12 vol=72 T*vol=864 slots=108 paired 1:1; disjointness ball D=10 (D^2=100 >= 4rho2=99), ball sizes 64..64 sites/rep, all bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit | **PASS** | 0.1s | audit re-derived 12 cells x 9 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 72 each, T*vol == |det|; all 108 pairing claims verified full-facet both sides, slots covered exactly once |
| V2 symmetry certification | **PASS** | 0.0s | site=2, stab_geo=2 (ALL orthogonal maps, Gram-triple), aut_comb=2; chain site<=stab_geo contained, divisibility 2|2|2 holds; Bravais point group of L: order 48 (GL3(Z) Gram-preserving, proven coefficient bound), embedded ops all signed perms (checked, not assumed); stabilizer elements all signed perms |
| V3 Burnside identity | **PASS** | 0.6s | tables T=12 nbrs=9 |ops|=24 (24 proper, 0 improper; T*|site|=24), identity+closure exact; banked enumerate n<=4: fixed=[12, 54, 320, 2136], free=[1, 4, 16, 99]; burnside_generic: |ops|*free(n) == sum Fix_m(n) ALL PASS n<=4 (its independent fixed recount agrees) |

Symmetry reconciliation: site symmetry 2 <= geometric stabilizer 2 <= combinatorial aut 2 (containment + divisibility verified exactly). Bravais point group of the actual lattice: order 48, embedded ops ARE the signed permutations (checked, not assumed).

## `2de0a21129cabe90` — IT(201) Pn-3, f=(20, 33, 15), p=3^6 4^3 5^2 6^2 7^2, aut=1

Witness point (1/8, 1/6, 5/12), site stabilizer 1, orbit 24 conventional / 24 primitive. Candidate wall time 7.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation | **PASS** | 0.2s | IT(201) Pn-3 p=(1/8, 1/6, 5/12) period=24 n_conv=24 T=24 f=(20,33,15) p-vec 3^6 4^3 5^2 6^2 7^2 aut=1 cutoff_D=48 4rho2=500 |
| V1 tiling certificate (generator) | **PASS** | 2.4s | detL=13824 T=24 vol=576 T*vol=13824 slots=360 paired 1:1; disjointness ball D=23 (D^2=529 >= 4rho2=500), ball sizes 85..85 sites/rep, all bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit | **PASS** | 2.3s | audit re-derived 24 cells x 15 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 576 each, T*vol == |det|; all 360 pairing claims verified full-facet both sides, slots covered exactly once |
| V2 symmetry certification | **PASS** | 0.0s | site=1, stab_geo=1 (ALL orthogonal maps, Gram-triple), aut_comb=1; chain site<=stab_geo contained, divisibility 1|1|1 holds; Bravais point group of L: order 48 (GL3(Z) Gram-preserving, proven coefficient bound), embedded ops all signed perms (checked, not assumed); stabilizer elements all signed perms |
| V3 Burnside identity | **PASS** | 2.3s | tables T=24 nbrs=15 |ops|=24 (12 proper, 12 improper; T*|site|=24), identity+closure exact; banked enumerate n<=4: fixed=[24, 180, 1992, 25974], free=[1, 9, 85, 1099]; burnside_generic: |ops|*free(n) == sum Fix_m(n) ALL PASS n<=4 (its independent fixed recount agrees) |

Symmetry reconciliation: site symmetry 1 <= geometric stabilizer 1 <= combinatorial aut 1 (containment + divisibility verified exactly). Bravais point group of the actual lattice: order 48, embedded ops ARE the signed permutations (checked, not assumed).

## `c4ea3f32fdd6dc51` — IT(224) Pn-3m, f=(14, 23, 11), p=3^4 4^4 6^3, aut=2

Witness point (1/12, 3/8, 3/8), site stabilizer 2, orbit 24 conventional / 24 primitive. Candidate wall time 4.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation | **PASS** | 0.2s | IT(224) Pn-3m p=(1/12, 3/8, 3/8) period=24 n_conv=24 T=24 f=(14,23,11) p-vec 3^4 4^4 6^3 aut=2 cutoff_D=48 4rho2=472 |
| V1 tiling certificate (generator) | **PASS** | 1.7s | detL=13824 T=24 vol=576 T*vol=13824 slots=264 paired 1:1; disjointness ball D=22 (D^2=484 >= 4rho2=472), ball sizes 71..71 sites/rep, all bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit | **PASS** | 0.6s | audit re-derived 24 cells x 11 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 576 each, T*vol == |det|; all 264 pairing claims verified full-facet both sides, slots covered exactly once |
| V2 symmetry certification | **PASS** | 0.0s | site=2, stab_geo=2 (ALL orthogonal maps, Gram-triple), aut_comb=2; chain site<=stab_geo contained, divisibility 2|2|2 holds; Bravais point group of L: order 48 (GL3(Z) Gram-preserving, proven coefficient bound), embedded ops all signed perms (checked, not assumed); stabilizer elements all signed perms |
| V3 Burnside identity | **PASS** | 1.7s | tables T=24 nbrs=11 |ops|=48 (24 proper, 24 improper; T*|site|=48), identity+closure exact; banked enumerate n<=4: fixed=[24, 132, 1048, 9630], free=[1, 6, 25, 225]; burnside_generic: |ops|*free(n) == sum Fix_m(n) ALL PASS n<=4 (its independent fixed recount agrees) |

Symmetry reconciliation: site symmetry 2 <= geometric stabilizer 2 <= combinatorial aut 2 (containment + divisibility verified exactly). Bravais point group of the actual lattice: order 48, embedded ops ARE the signed permutations (checked, not assumed).

## `9b69eefb8bd8437c` — IT(224) Pn-3m, f=(11, 18, 9), p=3^2 4^5 5^2, aut=2

Witness point (1/12, 1/3, 1/3), site stabilizer 2, orbit 24 conventional / 24 primitive. Candidate wall time 2.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation | **PASS** | 0.1s | IT(224) Pn-3m p=(1/12, 1/3, 1/3) period=12 n_conv=24 T=24 f=(11,18,9) p-vec 3^2 4^5 5^2 aut=2 cutoff_D=24 4rho2=132 |
| V1 tiling certificate (generator) | **PASS** | 1.2s | detL=1728 T=24 vol=72 T*vol=1728 slots=216 paired 1:1; disjointness ball D=12 (D^2=144 >= 4rho2=132), ball sizes 102..102 sites/rep, all bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit | **PASS** | 0.2s | audit re-derived 24 cells x 9 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 72 each, T*vol == |det|; all 216 pairing claims verified full-facet both sides, slots covered exactly once |
| V2 symmetry certification | **PASS** | 0.0s | site=2, stab_geo=2 (ALL orthogonal maps, Gram-triple), aut_comb=2; chain site<=stab_geo contained, divisibility 2|2|2 holds; Bravais point group of L: order 48 (GL3(Z) Gram-preserving, proven coefficient bound), embedded ops all signed perms (checked, not assumed); stabilizer elements all signed perms |
| V3 Burnside identity | **PASS** | 1.1s | tables T=24 nbrs=9 |ops|=48 (24 proper, 24 improper; T*|site|=48), identity+closure exact; banked enumerate n<=4: fixed=[24, 108, 656, 4542], free=[1, 5, 16, 111]; burnside_generic: |ops|*free(n) == sum Fix_m(n) ALL PASS n<=4 (its independent fixed recount agrees) |

Symmetry reconciliation: site symmetry 2 <= geometric stabilizer 2 <= combinatorial aut 2 (containment + divisibility verified exactly). Bravais point group of the actual lattice: order 48, embedded ops ARE the signed permutations (checked, not assumed).

## `d2d935e5499e6e11` — IT(224) Pn-3m, f=(6, 11, 7), p=3^6 4^1, aut=4

Witness point (1/12, 1/12, 5/12), site stabilizer 2, orbit 24 conventional / 24 primitive. Candidate wall time 1.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation | **PASS** | 0.1s | IT(224) Pn-3m p=(1/12, 1/12, 5/12) period=12 n_conv=24 T=24 f=(6,11,7) p-vec 3^6 4^1 aut=4 cutoff_D=24 4rho2=108 |
| V1 tiling certificate (generator) | **PASS** | 0.7s | detL=1728 T=24 vol=72 T*vol=1728 slots=168 paired 1:1; disjointness ball D=11 (D^2=121 >= 4rho2=108), ball sizes 75..75 sites/rep, all bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit | **PASS** | 0.0s | audit re-derived 24 cells x 7 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 72 each, T*vol == |det|; all 168 pairing claims verified full-facet both sides, slots covered exactly once |
| V2 symmetry certification | **PASS** | 0.0s | site=2, stab_geo=2 (ALL orthogonal maps, Gram-triple), aut_comb=4; chain site<=stab_geo contained, divisibility 2|2|4 holds; Bravais point group of L: order 48 (GL3(Z) Gram-preserving, proven coefficient bound), embedded ops all signed perms (checked, not assumed); stabilizer elements all signed perms |
| V3 Burnside identity | **PASS** | 0.8s | tables T=24 nbrs=7 |ops|=48 (24 proper, 24 improper; T*|site|=48), identity+closure exact; banked enumerate n<=4: fixed=[24, 84, 392, 2046], free=[1, 4, 10, 53]; burnside_generic: |ops|*free(n) == sum Fix_m(n) ALL PASS n<=4 (its independent fixed recount agrees) |

Symmetry reconciliation: site symmetry 2 <= geometric stabilizer 2 <= combinatorial aut 4 (containment + divisibility verified exactly). Bravais point group of the actual lattice: order 48, embedded ops ARE the signed permutations (checked, not assumed).

## `f98a3ee5675fc121` — IT(224) Pn-3m, f=(10, 15, 7), p=3^2 4^3 6^2, aut=4

Witness point (1/8, 1/6, 5/12), site stabilizer 1, orbit 48 conventional / 48 primitive. Candidate wall time 7.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation | **PASS** | 0.3s | IT(224) Pn-3m p=(1/8, 1/6, 5/12) period=24 n_conv=48 T=48 f=(10,15,7) p-vec 3^2 4^3 6^2 aut=4 cutoff_D=48 4rho2=500 |
| V1 tiling certificate (generator) | **PASS** | 4.7s | detL=13824 T=48 vol=288 T*vol=13824 slots=336 paired 1:1; disjointness ball D=23 (D^2=529 >= 4rho2=500), ball sizes 176..176 sites/rep, all bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit | **PASS** | 0.4s | audit re-derived 48 cells x 7 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 288 each, T*vol == |det|; all 336 pairing claims verified full-facet both sides, slots covered exactly once |
| V2 symmetry certification | **PASS** | 0.0s | site=1, stab_geo=1 (ALL orthogonal maps, Gram-triple), aut_comb=4; chain site<=stab_geo contained, divisibility 1|1|4 holds; Bravais point group of L: order 48 (GL3(Z) Gram-preserving, proven coefficient bound), embedded ops all signed perms (checked, not assumed); stabilizer elements all signed perms |
| V3 Burnside identity | **PASS** | 2.2s | tables T=48 nbrs=7 |ops|=48 (24 proper, 24 improper; T*|site|=48), identity+closure exact; banked enumerate n<=4: fixed=[48, 168, 912, 5748], free=[1, 7, 19, 135]; burnside_generic: |ops|*free(n) == sum Fix_m(n) ALL PASS n<=4 (its independent fixed recount agrees) |

Symmetry reconciliation: site symmetry 1 <= geometric stabilizer 1 <= combinatorial aut 4 (containment + divisibility verified exactly). Bravais point group of the actual lattice: order 48, embedded ops ARE the signed permutations (checked, not assumed).

Total wall time 113s. Deterministic except the timing decimals. Certified artifacts: `g4_tables_<id>.json` (+ `.txt` enumerator input) per candidate.

Re-run for acceptance: `python3 g4_certify.py` (exit 0 required).
