# Track-4 certificate log — 2026-09-03

Cells re-run in this invocation: laves, engel; other entries are reproduced from track4_results.json (their own earlier run).

## Engel's 38-facet stereohedron (`engel`)

| stage | verdict | wall | detail |
|---|---|---|---|
| V0 exact derivation vs literature | **PASS** | 1.2s | IT(214) I4_132 p=(427/6984, 761/6984, 1421/6984) period=6984 n_conv=48 T=24 stab=1 stratum_dim=3 f=(70,106,38) p-vec 3^12 4^11 5^6 6^5 8^1 16^1 20^1 28^1 aut=1 nonsimple=2 W=2 float==exact (degenerate-flagged, exact decides) cutoff_D=13968 4rho2=38489568; FACETS 38 == literature 38; not in Phase-1 store (general position, T=24) |
| V1 tiling certificate (generator) | **PASS** | 13.8s | detL=170326685952 T=24 vol=7096945248 T*vol=170326685952 slots=912 paired 1:1; disjointness ball D=6204 (D^2=38489616 >= 4rho2=38489568), ball sizes 155..155 sites/rep, all bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit | **PASS** | 523.1s | audit re-derived 24 cells x 38 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 7096945248 each, T*vol == |det|; all 912 pairing claims verified full-facet both sides, slots covered exactly once |
| V2 symmetry certification | **PASS** | 0.0s | site=1, stab_geo=1 (ALL orthogonal maps, Gram-triple), aut_comb=1; chain site<=stab_geo contained, divisibility 1|1|1 holds; Bravais point group of L: order 48 (GL3(Z) Gram-preserving, proven coefficient bound), embedded ops all signed perms (checked, not assumed); stabilizer elements all signed perms |
| V3 Burnside identity | **PASS** | 32.0s | tables T=24 nbrs=38 |ops|=24 (24 proper, 0 improper; T*|site|=24), identity+closure exact; banked enumerate n<=4: fixed=[24, 456, 13384, 477102], free=[1, 25, 559, 20051]; burnside_generic: |ops|*free(n) == sum Fix_m(n) ALL PASS n<=4 (its independent fixed recount agrees) |

## Laves graph plesiohedron (`laves`)

| stage | verdict | wall | detail |
|---|---|---|---|
| V0 exact derivation vs literature | **PASS** | 0.1s | IT(214) I4_132 p=(1/8, 1/8, 1/8) period=24 n_conv=8 T=4 stab=6 stratum_dim=0 f=(30,45,17) p-vec 4^6 5^6 6^2 8^3 aut=12 nonsimple=0 W=2 float==exact cutoff_D=48 4rho2=504; FACETS 17 == literature 17; canonical code == store type 8c69db9e84095469 |
| V1 tiling certificate (generator) | **PASS** | 0.1s | detL=6912 T=4 vol=1728 T*vol=6912 slots=68 paired 1:1; disjointness ball D=23 (D^2=529 >= 4rho2=504), ball sizes 35..35 sites/rep, all bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit | **PASS** | 1.5s | audit re-derived 4 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1728 each, T*vol == |det|; all 68 pairing claims verified full-facet both sides, slots covered exactly once |
| V2 symmetry certification | **PASS** | 0.0s | site=6, stab_geo=6 (ALL orthogonal maps, Gram-triple), aut_comb=12; chain site<=stab_geo contained, divisibility 6|6|12 holds; Bravais point group of L: order 48 (GL3(Z) Gram-preserving, proven coefficient bound), embedded ops all signed perms (checked, not assumed); stabilizer elements all signed perms |
| V3 Burnside identity | **PASS** | 0.5s | tables T=4 nbrs=17 |ops|=24 (24 proper, 0 improper; T*|site|=24), identity+closure exact; banked enumerate n<=4: fixed=[4, 34, 416, 6000], free=[1, 4, 22, 278]; burnside_generic: |ops|*free(n) == sum Fix_m(n) ALL PASS n<=4 (its independent fixed recount agrees) |

Total wall 911s. Verdict: ALL LADDERS PASS.
