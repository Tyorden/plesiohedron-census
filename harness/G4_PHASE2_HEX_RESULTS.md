# G4 certificate results — PHASE 2 BATCH 2 (hexagonal family, Gram metric in the ITA hexagonal basis), V0-V3 ladder (2026-09-04)

Gate: `../ANCHORS.md` G4 (paper-I-standard ladder V0-V3, `../HARNESS_DESIGN_FABLE5_2026-08-27.md` §3) applied through the accepted Gram chain (`phase2/metric.py` gram_hexagonal, `phase2/sweep_voronoi_gram.py`, `phase2/exact_cell_gram.py`; G2b + G2c). Generator: `g4_certify_hex.py` (this run) driving the ladder functions of the accepted tetragonal `g4_certify_gram.py` UNCHANGED (V0-V3, `run_ladder`); the only edits to that file are the family switch in `gram_of` (hexagonal -> `metric.gram_hexagonal`) and the optional `INDEP_WORKERS` hook (default None = previous behaviour; its tetragonal `--gate-only` output is identical after the edit). The metric-independent pieces of the accepted cubic `g4_certify.py` (exact vector bits, fan volume, the independent affine audit `v1_audit`/`_a_*`, banked V3 tool paths) are imported as before. Inputs: `phase2_hexagonal_types.json` (sha256 7494c7b26114a68f... verified before the run) stored witnesses of the 151 collision-screen survivors (`COLLISION_PHASE2_HEX_RESULTS.md`, ranking = `triage_phase2_hex_shortlist.json` survivors_ranked), frozen G1 `spacegroups.json`. V3 uses the banked `export_tables.py` + compiled `enumerate` + `burnside_generic.py` (POLYFORMS_II) and then the INDEPENDENT `../publication/verify_counts_independent.py` (dual-implementation bar, n<=5 under a 4-min cap, --workers 2 per cell).

**METRIC CONVENTIONS.** Sites/vertices in the ITA HEXAGONAL basis of the frozen ops (a = b, gamma = 120 deg; rhombohedral groups on hexagonal axes, obverse setting), integer-scaled by PERIOD; metric = integer Gram G = [[2q^2, -q^2, 0], [-q^2, 2q^2, 0], [0, 0, 2p^2]] for c/a = p/q. All distances are G-norms; bisectors 2(r-c)^T G x = r^T G r - c^T G c; the cutoff 4 rho^2 <= D^2 holds in the G-norm with the candidate block proven complete by |x_i| <= D sqrt((G^-1)_ii). **Volumes are crystal-basis (coordinate-space) measures**; the Euclidean volume (a = 1) is that times the SAME factor (sqrt 3 / 2)(c/a) for the cell, the lattice covolume and the torus, so T * vol(cell) = covol(L) = detL is an exact-rational identity in the crystal basis, equivalent to the Euclidean one. Facets and full-facet pairings are affine (metric-free); the metric enters the tiling certificate through the Voronoi bisector claims, verified in the G-norm by the generator (V1d) and re-verified by the audit's fresh Gram layer.

**V3 tables are metric-independent adjacency data** (which cells share a facet; point ops mod L acting on cell IDs) — stated once; the metric has already done its work in V1/V2.

**LANGUAGE (stated once): G4 passing does NOT establish novelty. Every type below remains "not matched against the records checked as of 2026-09-04"; no naming; G5 is separate and has not closed. Kill criteria were live (facet count > 38 asserts in V0 — the family's menu maximum is 24; "observed max 38" is folklore, never proven; any V-rung FAIL stops the batch).**

## Sanity gates (run first, all three PASS before any survivor)

- GATE (i) PASS: P6/mmm #191 origin orbit at c/a=1 (G=((2, -1, 0), (-1, 2, 0), (0, 0, 2)), period 12, 1 site) through the hexagonal ladder == the seed hexagonal-prism certificate: code == seed, f=(12,18,8), aut 24, site 24, geometric stabilizer (Isom_fix_site) 24, Isom(solid) 24 (Isom+ 12), Bravais point group of the hexagonal lattice 24, T=1, |H/L|=24 = T*|site|; Burnside counts n<=4 from the ladder (banked enumerate + independent verify_counts_independent.py, reached n=5) fixed=[1, 4, 24, 168] free=[1, 2, 5, 20] one-sided=[1, 2, 5, 23] EQUAL to the fresh independent hexagonal-prism polyform enumeration written in this file (8 neighbours = the 8 integer vectors of minimal G-norm; point group = the 24 integer matrices preserving G, brute-forced in [-2,2]^9, 12 proper): fixed=[1, 4, 24, 168] free=[1, 2, 5, 20] one-sided=[1, 2, 5, 23] (3s)
- GATE (ii) PASS: R-3m #166 origin orbit at c/a=3 (rhombohedral lattice on hexagonal axes, 3 sites/conventional cell, period 12, G=((2, -1, 0), (-1, 2, 0), (0, 0, 18))) through the hexagonal ladder reproduces the ACCEPTED cubic ladder (g4_certify.py functions, unmodified) on the Fm-3m #225 origin orbit number for number in every lattice-independent quantity: canonical code (== seed rhombic_dodecahedron), f=(14, 24, 12), p=4^12, aut 48, T=1, slots 12, 6 non-simple vertices, FIXED counts n<=4 [1, 6, 50, 475] == [1, 6, 50, 475]. EXPECTED metric-dependent differences, all explained: {'site': (48, 12), 'stab_geo': (48, 12), 'brav': (48, 12), 'n_ops': (48, 12), 'n_proper': (24, 6), 'free': ([1, 1, 4, 20], [1, 2, 8, 54]), 'detL': (432, 576), 'vol': ('432', '576')} — at c/a=3 the rhombohedral lattice is not metrically cubic (FCC is at the irrational c/a=sqrt6), so site symmetry, Isom_fix_site, Isom(solid), Bravais group and |H/L| are all -3m (12) instead of m-3m (48) [|H/L|=12=T*|site|, full group IS R-3m]; FREE counts are orbits under the honeycomb's OWN symmetry group (12 vs 48 ops), hence free_hex(n) >= free_cubic(n) with equality only at n=1 (pre-run prediction free_hex(2)=2 vs 1: confirmed); detL/vol are crystal-basis measures in different bases (rhombohedral-on-hexagonal-axes vs cubic F) and are not comparable. VERIFIED: the unimodular change of basis M=((-1, 1, 0), (1, 0, 0), (1, -1, 1)) carries the 12 hexagonal-basis neighbour vectors onto the 12 cubic-basis ones and conjugates the 12 hexagonal honeycomb ops into a subgroup of the 48 cubic ones (fresh code); independent enumerator reached n=5 (1s)
- GATE (iii) PASS: banked tetragonal g4p2 row 1497877268495988 (IT(91) P4_122, #5 of G4_PHASE2_RESULTS.md) through the extended code: V0-V3 all PASS; tables JSON byte-identical to the banked g4p2_tables_1497877268495988.json (10780 bytes); banked counts fixed=[4, 36, 468, 7048] free=[1, 8, 63, 926] and the independent rows n<=5 identical to the banked _indep.json; V2 numbers (site, Isom_fix, Isom, Isom+, improper, aut, Bravais, |H/L|) = (2, 2, 2, 2, 0, 2, 16, 8) identical to the banked doc (6s)

Gate (i) Burnside comparison (n = 1..4):

| source | fixed | free | one-sided |
|---|---|---|---|
| ladder (banked enumerate + independent verify_counts_independent.py) | [1, 4, 24, 168] | [1, 2, 5, 20] | [1, 2, 5, 23] |
| fresh hexagonal-prism polyform enumerator (this file) | [1, 4, 24, 168] | [1, 2, 5, 20] | [1, 2, 5, 23] |

Gate (ii) number-for-number table (cubic reference = accepted g4_certify.py functions on Fm-3m #225 origin; hexagonal = this ladder on R-3m #166 origin at c/a = 3):

| quantity | cubic Fm-3m #225 | hexagonal R-3m #166 c/a=3 | class |
|---|---|---|---|
| code | == seed | == seed | lattice-independent (must agree) |
| f | [14, 24, 12] | [14, 24, 12] | lattice-independent (must agree) |
| p | 4^12 | 4^12 | lattice-independent (must agree) |
| aut | 48 | 48 | lattice-independent (must agree) |
| T | 1 | 1 | lattice-independent (must agree) |
| slots | 12 | 12 | lattice-independent (must agree) |
| fixed | [1, 6, 50, 475] | [1, 6, 50, 475] | lattice-independent (must agree) |
| free | [1, 1, 4, 20] | [1, 2, 8, 54] | metric-dependent (expected to differ, explained above) |
| site | 48 | 12 | metric-dependent (expected to differ, explained above) |
| stab_geo | 48 | 12 | metric-dependent (expected to differ, explained above) |
| brav | 48 | 12 | metric-dependent (expected to differ, explained above) |
| n_ops | 48 | 12 | metric-dependent (expected to differ, explained above) |
| n_proper | 24 | 6 | metric-dependent (expected to differ, explained above) |
| detL | 432 | 576 | metric-dependent (expected to differ, explained above) |
| vol | 432 | 576 | metric-dependent (expected to differ, explained above) |

## Summary table (all survivors, collision-screen rank order)

| # | id | IT | c/a | f | aut | V0 | V1 gen | V1 audit | V2 | V3 | chiral? | site = Isom? | \|H/L\| = T·\|site\|? | open/wall (carried from triage) | wall |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `c49077384aaebeb0` | 178 P6_122 | 5/4 | (44, 66, 24) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 12 b) | 39s |
| 2 | `59585d778cb3a7a4` | 178 P6_122 | 3/4 | (40, 60, 22) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 22 b) | 27s |
| 3 | `095ce61d28388c98` | 178 P6_122 | 1 | (40, 60, 22) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 24 b) | 29s |
| 4 | `9be0f2271a14b6a9` | 178 P6_122 | 1 | (36, 54, 20) | 4 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 20 b) | 19s |
| 5 | `2d654c836f3731c6` | 178 P6_122 | 1 | (36, 54, 20) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 30 b) | 19s |
| 6 | `b0f80776885f3ae1` | 178 P6_122 | 1/2 | (36, 54, 20) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 17 b) | 19s |
| 7 | `a348875c3f707895` | 178 P6_122 | 1/2 | (36, 54, 20) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 21 b) | 20s |
| 8 | `dcc38ea9177089b9` | 178 P6_122 | 1/2 | (36, 54, 20) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 3 b) | 21s |
| 9 | `5b86a254c715306c` | 169 P6_1 | 797/1000 | (40, 60, 22) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 6 b) | 28s |
| 10 | `f05f0b009e0929f6` | 169 P6_1 | 3/4 | (32, 48, 18) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 39 b) | 11s |
| 11 | `d70e6901953070e7` | 155 R32 | 3/4 | (38, 58, 22) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 3 b) | 20s |
| 12 | `e1a38303b2378f17` | 169 P6_1 | 1277/2000 | (40, 60, 22) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b; metric-thin: P5-only) | 28s |
| 13 | `c82ebc15c49c1413` | 154 P3_221 | 527/1000 | (38, 57, 21) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b) | 21s |
| 14 | `f6f8b3050a1eef42` | 178 P6_122 | 3/4 | (38, 57, 21) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b) | 46s |
| 15 | `9c0b7e0c29dfebb2` | 169 P6_1 | 3/4 | (36, 54, 20) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b) | 15s |
| 16 | `87c94384d7851cb2` | 155 R32 | 797/1000 | (34, 52, 20) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 8 b) | 17s |
| 17 | `a35623e347ef03b4` | 169 P6_1 | 5/4 | (32, 48, 18) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 32 b) | 12s |
| 18 | `e98412e7cb95aea2` | 152 P3_121 | 3/4 | (32, 48, 18) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 30 b) | 5s |
| 19 | `ac4489d658eb445e` | 178 P6_122 | 797/1000 | (36, 54, 20) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 6 b) | 46s |
| 20 | `c53bc05bc306c97d` | 166 R-3m | 7/8 | (31, 48, 19) | 2 | PASS | PASS | PASS | PASS | PASS | achiral | yes | yes | open-likely (triage, 14 b) | 16s |
| 21 | `8cc8c5ab3cf36d8f` | 178 P6_122 | 5/4 | (36, 54, 20) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b) | 40s |
| 22 | `646b518ccf3bd724` | 169 P6_1 | 15/16 | (36, 54, 20) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 6 b; metric-thin: P5-only) | 18s |
| 23 | `7a448bed1119dfad` | 178 P6_122 | 1/2 | (36, 54, 20) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b) | 40s |
| 24 | `7e023be581e7c50a` | 154 P3_221 | 3/4 | (36, 54, 20) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b) | 16s |
| 25 | `7e05ce00d8a7cbf6` | 178 P6_122 | 137/160 | (38, 57, 21) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b; metric-thin: P5-only) | 52s |
| 26 | `59b28b3a59c27092` | 155 R32 | 1277/2000 | (34, 52, 20) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 6 b; metric-thin: P5-only) | 18s |
| 27 | `d9ac68100a276dfe` | 169 P6_1 | 2777/4000 | (36, 54, 20) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 3 b; metric-thin: P5-only) | 21s |
| 28 | `6f4101f83371033d` | 169 P6_1 | 2331/4000 | (36, 54, 20) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b; metric-thin: P5-only) | 19s |
| 29 | `f0b07b168368759b` | 148 R-3 | 3/4 | (14, 24, 12) | 4 | PASS | PASS | PASS | PASS | PASS | achiral | NO (2 vs 4) | NO (12 vs 6) | open-likely (triage, 41 b) | 1s |
| 30 | `56918d2cff883e22` | 148 R-3 | 1 | (22, 34, 14) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 49 b) | 4s |
| 31 | `f429e996b3f455a6` | 148 R-3 | 3/4 | (26, 40, 16) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 16 b) | 7s |
| 32 | `71d2c9953ca110b8` | 169 P6_1 | 39/32 | (36, 54, 20) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | 19s |
| 33 | `8d90c524c89922d9` | 169 P6_1 | 11/8 | (36, 54, 20) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | 17s |
| 34 | `9d4396ca0b08fc3c` | 166 R-3m | 3/4 | (19, 30, 13) | 2 | PASS | PASS | PASS | PASS | PASS | achiral | yes | yes | open-likely (triage, 63 b) | 4s |
| 35 | `07d543d89e2934f2` | 152 P3_121 | 33/32 | (36, 54, 20) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | indeterminate (triage, 2 b; metric-thin: P5-only) | 17s |
| 36 | `2081d7b9a734e4fe` | 155 R32 | 11/8 | (32, 50, 20) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | 15s |
| 37 | `257b627a90b78038` | 180 P6_222 | 1 | (22, 35, 15) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 24 b) | 5s |
| 38 | `3ddc41389e6d484f` | 171 P6_2 | 1 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 8 b) | 10s |
| 39 | `64203f15fcf6c09b` | 155 R32 | 1/2 | (20, 32, 14) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 23 b) | 2s |
| 40 | `d718e083bd23d2b1` | 178 P6_122 | 1 | (32, 48, 18) | 4 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b) | 27s |
| 41 | `f14a8c4e7c5b3e3a` | 180 P6_222 | 7/4 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 10 b) | 28s |
| 42 | `29bbba1adec778da` | 171 P6_2 | 5/4 | (28, 42, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 15 b) | 6s |
| 43 | `66563d07a1110a25` | 154 P3_221 | 1 | (36, 54, 20) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 16s |
| 44 | `ce3b42c8a4ceff6f` | 151 P3_112 | 1/2 | (34, 51, 19) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 6 b) | 13s |
| 45 | `7b9cfe26fe4a9c4b` | 146 R3 | 5/4 | (18, 30, 14) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 32 b) | 2s |
| 46 | `2b9726574a0a8bed` | 171 P6_2 | 1/2 | (30, 45, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 9 b) | 8s |
| 47 | `f07d69523ef41b37` | 178 P6_122 | 3/2 | (20, 36, 18) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 10s |
| 48 | `16025e0680843c36` | 169 P6_1 | 1 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 7 b) | 12s |
| 49 | `d10bb4a25bbf4c80` | 154 P3_221 | 797/1000 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 6 b) | 13s |
| 50 | `e0bf1a48f096c10d` | 180 P6_222 | 1 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 6 b) | 28s |
| 51 | `b2430fc4bea4e06d` | 154 P3_221 | 1/2 | (34, 51, 19) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 3 b) | 12s |
| 52 | `bff9b24ce78050f5` | 144 P3_1 | 1 | (28, 42, 16) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 9 b) | 3s |
| 53 | `4db369a636f4396b` | 151 P3_112 | 3/2 | (18, 30, 14) | 4 | PASS | PASS | PASS | PASS | PASS | chiral | NO (2 vs 4) | NO (12 vs 6) | indeterminate (triage, 2 b) | 2s |
| 54 | `042c19cbfdc869cb` | 178 P6_122 | 3/2 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b) | 26s |
| 55 | `23594bd7053503aa` | 153 P3_212 | 1 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b) | 10s |
| 56 | `f5fbebffa76808d5` | 179 P6_522 | 5/4 | (31, 47, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b) | 27s |
| 57 | `057255f61286b052` | 167 R-3c | 1/2 | (24, 38, 16) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 7 b) | 9s |
| 58 | `e198aac88f223892` | 153 P3_212 | 3/4 | (30, 45, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 12 b) | 9s |
| 59 | `d07f950b8309de82` | 171 P6_2 | 67/80 | (30, 45, 17) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b; metric-thin: P5-only) | 10s |
| 60 | `a182e87006c7a00d` | 179 P6_522 | 3/2 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b) | 26s |
| 61 | `a46cbaad3c23e834` | 155 R32 | 1/2 | (32, 49, 19) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | indeterminate (triage, 2 b) | 13s |
| 62 | `dd3fb07fe11d73d3` | 179 P6_522 | 2 | (31, 47, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b) | 27s |
| 63 | `36c92427e3d084dc` | 166 R-3m | 5/4 | (19, 30, 13) | 2 | PASS | PASS | PASS | PASS | PASS | achiral | yes | yes | open-likely (triage, 16 b) | 4s |
| 64 | `bc59e5d778f60d1f` | 178 P6_122 | 3/4 | (29, 44, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 7 b) | 21s |
| 65 | `cbead3df2d2f1d0e` | 154 P3_221 | 1277/2000 | (34, 51, 19) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b; metric-thin: P5-only) | 17s |
| 66 | `85244add8d1f2d55` | 169 P6_1 | 1/2 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 3 b) | 11s |
| 67 | `2165f5c5260120de` | 152 P3_121 | 527/1000 | (30, 45, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b) | 10s |
| 68 | `437fbe758a6dd8e3` | 179 P6_522 | 1/2 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 3 b) | 26s |
| 69 | `36ec4ad2f530e145` | 151 P3_112 | 3/4 | (30, 45, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 9 b) | 8s |
| 70 | `fcffad0da2b5b62f` | 154 P3_221 | 15/16 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 6 b; metric-thin: P5-only) | 11s |
| 71 | `505a4911e298c933` | 181 P6_422 | 2 | (28, 42, 16) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 8 b) | 19s |
| 72 | `24a6b511067d37b2` | 178 P6_122 | 5/4 | (30, 45, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b) | 22s |
| 73 | `30f2a1e483babf55` | 178 P6_122 | 11/4 | (29, 44, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b) | 27s |
| 74 | `37aa18e6e10583be` | 155 R32 | 9/8 | (30, 47, 19) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 3 b; metric-thin: P5-only) | 11s |
| 75 | `7715c7010e513b71` | 181 P6_422 | 1 | (30, 45, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 8 b) | 22s |
| 76 | `0b5d9beb0fc972f6` | 179 P6_522 | 13/8 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b; metric-thin: P5-only) | 29s |
| 77 | `322d5ff451e4101d` | 169 P6_1 | 11/8 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | indeterminate (triage, 3 b; metric-thin: P5-only) | 11s |
| 78 | `34351050a4f29035` | 178 P6_122 | 1 | (28, 42, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 11 b) | 17s |
| 79 | `c0071756347c5a8a` | 144 P3_1 | 1 | (28, 42, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 9 b) | 3s |
| 80 | `d9bf7fb7a80eaa38` | 155 R32 | 5/4 | (30, 47, 19) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | indeterminate (triage, 2 b) | 13s |
| 81 | `847d2695a14ae424` | 152 P3_121 | 5/4 | (29, 44, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b) | 9s |
| 82 | `090dcafb7ce9cb08` | 166 R-3m | 1/2 | (20, 32, 14) | 2 | PASS | PASS | PASS | PASS | PASS | achiral | yes | yes | open-likely (triage, 6 b) | 6s |
| 83 | `9bc4922a7b574aa6` | 166 R-3m | 3/4 | (17, 28, 13) | 2 | PASS | PASS | PASS | PASS | PASS | achiral | yes | yes | open-likely (triage, 10 b) | 5s |
| 84 | `43e4e46001b4d8b9` | 181 P6_422 | 31/16 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b; metric-thin: P5-only) | 29s |
| 85 | `af8b2135c913b13b` | 181 P6_422 | 7/8 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 3 b) | 27s |
| 86 | `74a69fba4266de3b` | 167 R-3c | 527/1000 | (28, 43, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 6 b) | 26s |
| 87 | `c3b4b14633c9d4d5` | 155 R32 | 1 | (28, 43, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 6 b) | 8s |
| 88 | `e19babba732f5fd4` | 179 P6_522 | 7/4 | (29, 44, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 3 b) | 24s |
| 89 | `7472d8ba000c8056` | 152 P3_121 | 9/8 | (22, 36, 16) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | 2s |
| 90 | `d0c5a15c25ab6413` | 152 P3_121 | 17/16 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 3 b; metric-thin: P5-only) | 11s |
| 91 | `d770abfcee4deb90` | 153 P3_212 | 19/16 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 3 b; metric-thin: P5-only) | 11s |
| 92 | `4a560e459032166a` | 154 P3_221 | 7/8 | (28, 42, 16) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b) | 7s |
| 93 | `5beb94b61eb66eb1` | 178 P6_122 | 1/2 | (27, 41, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b) | 17s |
| 94 | `95934e84555dc2ea` | 179 P6_522 | 1/2 | (26, 40, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b) | 17s |
| 95 | `d0ed9179c6947b5f` | 155 R32 | 1/2 | (16, 26, 12) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 25 b) | 3s |
| 96 | `0948aa6184f13a8a` | 179 P6_522 | 5/4 | (30, 45, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b) | 21s |
| 97 | `272aefcd5e48ba49` | 179 P6_522 | 9/8 | (29, 44, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b; metric-thin: P5-only) | 22s |
| 98 | `466b12546dd936c3` | 161 R3c | 527/1000 | (26, 40, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b) | 8s |
| 99 | `4885ce1e70fa9713` | 179 P6_522 | 3/4 | (27, 41, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 7 b) | 17s |
| 100 | `3d6b109f392fda19` | 154 P3_221 | 3/2 | (33, 50, 19) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 13s |
| 101 | `e598ffd8a1cac138` | 144 P3_1 | 29/32 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | indeterminate (triage, 2 b; metric-thin: P5-only) | 5s |
| 102 | `a93f8fe7ecdc5851` | 144 P3_1 | 9/8 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | 5s |
| 103 | `aef8972953d53d20` | 171 P6_2 | 81/64 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | 12s |
| 104 | `72bcd959be4ab7dd` | 152 P3_121 | 5/4 | (28, 42, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b) | 7s |
| 105 | `ab801b11bead62ef` | 166 R-3m | 7/4 | (19, 30, 13) | 2 | PASS | PASS | PASS | PASS | PASS | achiral | yes | yes | open-likely (triage, 6 b) | 6s |
| 106 | `2c121297dbaa80af` | 154 P3_221 | 1 | (28, 42, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 7 b) | 6s |
| 107 | `9d0b36ad5caceb2e` | 167 R-3c | 7/8 | (22, 35, 15) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 5 b) | 13s |
| 108 | `d176b8d859dd651a` | 178 P6_122 | 5/2 | (32, 48, 18) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 30s |
| 109 | `60eb4282db04fca2` | 179 P6_522 | 11/8 | (30, 45, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b; metric-thin: P5-only) | 23s |
| 110 | `f43b45fd6383b36b` | 155 R32 | 19/16 | (26, 41, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 3 b; metric-thin: P5-only) | 8s |
| 111 | `4ff9d77aa9f8194a` | 167 R-3c | 3/4 | (24, 37, 15) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 8 b) | 14s |
| 112 | `6de3dac5f334cfed` | 167 R-3c | 1/2 | (26, 40, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b) | 21s |
| 113 | `105e41c2798e6180` | 148 R-3 | 2 | (16, 27, 13) | 6 | PASS | PASS | PASS | PASS | PASS | achiral | NO (3 vs 6) | NO (12 vs 6) | wall-suspect (triage, 1 b; metric-thin: 1b) | 2s |
| 114 | `542cbe76934b484b` | 154 P3_221 | 5/4 | (29, 44, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 8s |
| 115 | `75bbbcb4a37e70e8` | 146 R3 | 67/80 | (27, 41, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b; metric-thin: P5-only) | 3s |
| 116 | `cff2d5fb5e0d4149` | 171 P6_2 | 1/2 | (23, 35, 14) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b) | 4s |
| 117 | `4b6055c7aa3d341b` | 178 P6_122 | 17/8 | (25, 38, 15) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b; metric-thin: P5-only) | 16s |
| 118 | `7e79f1c38b5516bf` | 178 P6_122 | 3/2 | (22, 34, 14) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 5s |
| 119 | `d7c638d7fa23127e` | 169 P6_1 | 3/2 | (25, 39, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 6s |
| 120 | `0417061f8f56488e` | 152 P3_121 | 1/2 | (20, 32, 14) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 9 b) | 4s |
| 121 | `6cc34ed38aa354e1` | 181 P6_422 | 1/2 | (22, 34, 14) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b) | 10s |
| 122 | `5838282f46223111` | 152 P3_121 | 7/4 | (29, 44, 17) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 8s |
| 123 | `cda1d1c03659b67d` | 148 R-3 | 527/1000 | (22, 34, 14) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 7 b) | 5s |
| 124 | `161b09808f4c1863` | 178 P6_122 | 2 | (18, 30, 14) | 4 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 4s |
| 125 | `c92eef8763d02d8a` | 179 P6_522 | 3/2 | (25, 39, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 16s |
| 126 | `3a491fd6426d90b2` | 146 R3 | 33/32 | (24, 38, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | indeterminate (triage, 2 b; metric-thin: P5-only) | 3s |
| 127 | `5b679d8b0a3147c3` | 152 P3_121 | 17/16 | (24, 38, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | indeterminate (triage, 2 b; metric-thin: P5-only) | 5s |
| 128 | `fac4317d5a65b959` | 148 R-3 | 9/8 | (24, 38, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | indeterminate (triage, 2 b; metric-thin: P5-only) | 6s |
| 129 | `27d463eac6cda5ea` | 171 P6_2 | 5331/8000 | (27, 41, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | indeterminate (triage, 2 b; metric-thin: P5-only) | 7s |
| 130 | `919d30fd9021b5ee` | 154 P3_221 | 51/32 | (25, 38, 15) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 3 b; metric-thin: P5-only) | 5s |
| 131 | `6074c5fa5d2dffc5` | 148 R-3 | 3/4 | (16, 26, 12) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 19 b) | 3s |
| 132 | `5e68ffe7582a0657` | 167 R-3c | 1/2 | (20, 31, 13) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 8 b) | 11s |
| 133 | `1ba26ab2c0999b93` | 148 R-3 | 1/2 | (20, 32, 14) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b) | 5s |
| 134 | `27dbb77012555d28` | 161 R3c | 4439/8000 | (26, 40, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | 8s |
| 135 | `c18a9b1cb2a5d168` | 148 R-3 | 1/2 | (26, 40, 16) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 7s |
| 136 | `d1f1121757598de0` | 154 P3_221 | 9/4 | (15, 25, 12) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | indeterminate (triage, 2 b) | 2s |
| 137 | `b27ba8dbcbc2891a` | 161 R3c | 1/2 | (22, 34, 14) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | open-likely (triage, 4 b) | 5s |
| 138 | `457c20cf036ae496` | 180 P6_222 | 3/2 | (11, 20, 11) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 2s |
| 139 | `11a9fe078850b5cd` | 179 P6_522 | 65/32 | (25, 38, 15) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | 15s |
| 140 | `5f812747976b224a` | 148 R-3 | 39/32 | (20, 32, 14) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | indeterminate (triage, 2 b; metric-thin: P5-only) | 4s |
| 141 | `c95a5fcf4d681568` | 166 R-3m | 3/2 | (12, 21, 11) | 2 | PASS | PASS | PASS | PASS | PASS | achiral | yes | yes | indeterminate (triage, 2 b) | 3s |
| 142 | `f7bd7cd9eae6436b` | 166 R-3m | 1 | (16, 27, 13) | 2 | PASS | PASS | PASS | PASS | PASS | achiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 4s |
| 143 | `75c9be976d704515` | 152 P3_121 | 9/8 | (18, 28, 12) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | 1s |
| 144 | `8463196a30c6643f` | 179 P6_522 | 2 | (23, 36, 15) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 13s |
| 145 | `487490cdf474e568` | 148 R-3 | 1277/2000 | (20, 32, 14) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | indeterminate (triage, 2 b; metric-thin: P5-only) | 4s |
| 146 | `f0e2036d295195b4` | 152 P3_121 | 9/8 | (12, 20, 10) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b,P5-only) | 1s |
| 147 | `67b1ede4b021a4fc` | 155 R32 | 3/2 | (17, 29, 14) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 4s |
| 148 | `34e5e7acce18b5cd` | 166 R-3m | 3/2 | (14, 23, 11) | 2 | PASS | PASS | PASS | PASS | PASS | achiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 3s |
| 149 | `fa9c370d30741970` | 180 P6_222 | 3/2 | (9, 16, 9) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 1s |
| 150 | `400cba5c78326d1d` | 167 R-3c | 1 | (17, 28, 13) | 1 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 7s |
| 151 | `78e755ffdff3a2f5` | 146 R3 | 3/4 | (14, 24, 12) | 2 | PASS | PASS | PASS | PASS | PASS | chiral | yes | yes | wall-suspect (triage, 1 b; metric-thin: 1b) | 1s |

## Aggregate

- Survivors certified: 151 of 151; ALL FIVE RUNGS PASS: 151; any FAIL: 0; any DEFERRED / over-cap: 0.
- Per-rung verdict counts: V0: PASS 151; V1 gen: PASS 151; V1 audit: PASS 151; V2: PASS 151; V3: PASS 151.
- Max facet count observed among the survivors: 24 (kill bar 38 never approached; store menu max 24).
- Chirality of the solids: 140 chiral, 11 achiral (#20 `c53bc05bc306c97d`, #29 `f0b07b168368759b`, #34 `9d4396ca0b08fc3c`, #63 `36c92427e3d084dc`, #82 `090dcafb7ce9cb08`, #83 `9bc4922a7b574aa6`, #105 `ab801b11bead62ef`, #113 `105e41c2798e6180`, #141 `c95a5fcf4d681568`, #142 `f7bd7cd9eae6436b`, #148 `34e5e7acce18b5cd`).
- Chiral honeycombs with all translation classes of one hand: 121; chiral solids with classes of BOTH hands present (the honeycomb is achiral although the solid is chiral — its group contains improper ops: inversion in R-3 / R-3c, the c-glide in R3c): 19, by first-witness group: IT(148) R-3: 9, IT(161) R3c: 3, IT(167) R-3c: 7.
- Isom(solid) > site symmetry: 3 cell(s) — #29 `f0b07b168368759b` IT(148) site 2, Isom_fix_site 4, Isom(solid) 4 (Isom+ 2), aut 4, |H/L| 12 vs T*|site| 6 (full group LARGER than G); double-check (fresh, in-worker): every listed isometry re-verified G-orthogonal and vertex-permuting; per isometry (det, fixes site, linear part in site group, maps site set to itself) = [(1, True, True, True), (1, True, False, True), (-1, True, False, True), (-1, True, True, True)]; #53 `4db369a636f4396b` IT(151) site 2, Isom_fix_site 4, Isom(solid) 4 (Isom+ 4), aut 4, |H/L| 12 vs T*|site| 6 (full group LARGER than G); double-check (fresh, in-worker): every listed isometry re-verified G-orthogonal and vertex-permuting; per isometry (det, fixes site, linear part in site group, maps site set to itself) = [(1, True, True, True), (1, True, True, True), (1, True, False, True), (1, True, False, True)]; #113 `105e41c2798e6180` IT(148) site 3, Isom_fix_site 6, Isom(solid) 6 (Isom+ 3), aut 6, |H/L| 12 vs T*|site| 6 (full group LARGER than G); double-check (fresh, in-worker): every listed isometry re-verified G-orthogonal and vertex-permuting; per isometry (det, fixes site, linear part in site group, maps site set to itself) = [(1, True, True, True), (1, True, True, True), (1, True, True, True), (-1, True, False, True), (-1, True, False, True), (-1, True, False, True)].
- Isom_fix_site > site symmetry: 3 cell(s) — #29 `f0b07b168368759b`, #53 `4db369a636f4396b`, #113 `105e41c2798e6180`.
- Combinatorial-only symmetry (aut > Isom(solid)): 15 cell(s) — #4 `9be0f2271a14b6a9` (aut 4, Isom 2), #10 `f05f0b009e0929f6` (aut 2, Isom 1), #17 `a35623e347ef03b4` (aut 2, Isom 1), #30 `56918d2cff883e22` (aut 2, Isom 1), #31 `f429e996b3f455a6` (aut 2, Isom 1), #40 `d718e083bd23d2b1` (aut 4, Isom 1), #45 `7b9cfe26fe4a9c4b` (aut 2, Isom 1), #52 `bff9b24ce78050f5` (aut 2, Isom 1), #59 `d07f950b8309de82` (aut 2, Isom 1), #71 `505a4911e298c933` (aut 2, Isom 1), #92 `4a560e459032166a` (aut 2, Isom 1), #95 `d0ed9179c6947b5f` (aut 2, Isom 1), #124 `161b09808f4c1863` (aut 4, Isom 2), #136 `d1f1121757598de0` (aut 2, Isom 1), #151 `78e755ffdff3a2f5` (aut 2, Isom 1).
- |H/L| != T*|site| (full symmetry group larger than the generating group): 3 cell(s) — #29 `f0b07b168368759b` (|H/L| 12, T*|site| 6), #53 `4db369a636f4396b` (|H/L| 12, T*|site| 6), #113 `105e41c2798e6180` (|H/L| 12, T*|site| 6).
- Generating-group identification (fresh check from the frozen ops, parent process: every hexagonal-family group whose orbit of the witness point equals the cell's site set; the largest point-op count |H_conv|/centering among them can never exceed the ladder's |H/L| — asserted for every cell — and equals it when the full group is in the frozen list, directly or after an origin shift in (Z/P)^3): identified for 151 of 151 cells; the cells with |H/L| > T*|site| are honeycombs of a SUPERGROUP of the first-witness group (the witness point is a special position whose orbit is the same set under the supergroup, where its site symmetry is larger): #29 `f0b07b168368759b` first witness IT(148) site 2 -> full group IT(166) R-3m (site symmetry 4 there = |H/L|/T = Isom_fix_site); store sightings in the full group: 136; #53 `4db369a636f4396b` first witness IT(151) site 2 -> full group IT(181) P6_422 with origin shift ('0', '0', '1/3') (site symmetry 4 there = |H/L|/T = Isom_fix_site); store sightings in the full group: 3; #113 `105e41c2798e6180` first witness IT(148) site 3 -> full group IT(166) R-3m (site symmetry 6 there = |H/L|/T = Isom_fix_site); store sightings in the full group: 2.
- Bravais point-group orders of the actual lattices in G: 12: 46, 24: 105 (24 = hexagonal P lattice 6/mmm; 12 = rhombohedral R lattice -3m; no rational c/a makes either metrically cubic).
- Independent enumerator depth reached: n=5: 151.
- Total wall time this doc: 26s (sum of per-cell walls 2049s; cells ran 5 in parallel, independent enumerator --workers 2).

## Isometry vs site vs aut summary

| # | id | IT | site | Isom_fix_site | Isom(solid) | Isom+ | solid | aut | \|H/L\| | T*site | full group = G | full group (frozen-list identification) | Bravais |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `c49077384aaebeb0` | 178 | 2 | 2 | 2 | 2 | chiral | 2 | 12 | 12 | yes | 178 P6_122 | 24 |
| 2 | `59585d778cb3a7a4` | 178 | 2 | 2 | 2 | 2 | chiral | 2 | 12 | 12 | yes | 178 P6_122 | 24 |
| 3 | `095ce61d28388c98` | 178 | 2 | 2 | 2 | 2 | chiral | 2 | 12 | 12 | yes | 178 P6_122 | 24 |
| 4 | `9be0f2271a14b6a9` | 178 | 2 | 2 | 2 | 2 | chiral | 4 | 12 | 12 | yes | 178 P6_122 | 24 |
| 5 | `2d654c836f3731c6` | 178 | 2 | 2 | 2 | 2 | chiral | 2 | 12 | 12 | yes | 178 P6_122 | 24 |
| 6 | `b0f80776885f3ae1` | 178 | 2 | 2 | 2 | 2 | chiral | 2 | 12 | 12 | yes | 178 P6_122 | 24 |
| 7 | `a348875c3f707895` | 178 | 2 | 2 | 2 | 2 | chiral | 2 | 12 | 12 | yes | 178 P6_122 | 24 |
| 8 | `dcc38ea9177089b9` | 178 | 2 | 2 | 2 | 2 | chiral | 2 | 12 | 12 | yes | 178 P6_122 | 24 |
| 9 | `5b86a254c715306c` | 169 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 169 P6_1 | 24 |
| 10 | `f05f0b009e0929f6` | 169 | 1 | 1 | 1 | 1 | chiral | 2 | 6 | 6 | yes | 169 P6_1 | 24 |
| 11 | `d70e6901953070e7` | 155 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 155 R32 | 12 |
| 12 | `e1a38303b2378f17` | 169 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 169 P6_1 | 24 |
| 13 | `c82ebc15c49c1413` | 154 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 154 P3_221 | 24 |
| 14 | `f6f8b3050a1eef42` | 178 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 178 P6_122 | 24 |
| 15 | `9c0b7e0c29dfebb2` | 169 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 169 P6_1 | 24 |
| 16 | `87c94384d7851cb2` | 155 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 155 R32 | 12 |
| 17 | `a35623e347ef03b4` | 169 | 1 | 1 | 1 | 1 | chiral | 2 | 6 | 6 | yes | 169 P6_1 | 24 |
| 18 | `e98412e7cb95aea2` | 152 | 2 | 2 | 2 | 2 | chiral | 2 | 6 | 6 | yes | 152 P3_121 | 24 |
| 19 | `ac4489d658eb445e` | 178 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 178 P6_122 | 24 |
| 20 | `c53bc05bc306c97d` | 166 | 2 | 2 | 2 | 1 | achiral | 2 | 12 | 12 | yes | 166 R-3m | 12 |
| 21 | `8cc8c5ab3cf36d8f` | 178 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 178 P6_122 | 24 |
| 22 | `646b518ccf3bd724` | 169 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 169 P6_1 | 24 |
| 23 | `7a448bed1119dfad` | 178 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 178 P6_122 | 24 |
| 24 | `7e023be581e7c50a` | 154 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 154 P3_221 | 24 |
| 25 | `7e05ce00d8a7cbf6` | 178 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 178 P6_122 | 24 |
| 26 | `59b28b3a59c27092` | 155 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 155 R32 | 12 |
| 27 | `d9ac68100a276dfe` | 169 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 169 P6_1 | 24 |
| 28 | `6f4101f83371033d` | 169 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 169 P6_1 | 24 |
| 29 | `f0b07b168368759b` | 148 | 2 | 4 | 4 | 2 | achiral | 4 | 12 | 6 | NO | 166 R-3m | 12 |
| 30 | `56918d2cff883e22` | 148 | 1 | 1 | 1 | 1 | chiral | 2 | 6 | 6 | yes | 148 R-3 | 12 |
| 31 | `f429e996b3f455a6` | 148 | 1 | 1 | 1 | 1 | chiral | 2 | 6 | 6 | yes | 148 R-3 | 12 |
| 32 | `71d2c9953ca110b8` | 169 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 169 P6_1 | 24 |
| 33 | `8d90c524c89922d9` | 169 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 169 P6_1 | 24 |
| 34 | `9d4396ca0b08fc3c` | 166 | 2 | 2 | 2 | 1 | achiral | 2 | 12 | 12 | yes | 166 R-3m | 12 |
| 35 | `07d543d89e2934f2` | 152 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 152 P3_121 | 24 |
| 36 | `2081d7b9a734e4fe` | 155 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 155 R32 | 12 |
| 37 | `257b627a90b78038` | 180 | 2 | 2 | 2 | 2 | chiral | 2 | 12 | 12 | yes | 180 P6_222 | 24 |
| 38 | `3ddc41389e6d484f` | 171 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 171 P6_2 | 24 |
| 39 | `64203f15fcf6c09b` | 155 | 2 | 2 | 2 | 2 | chiral | 2 | 6 | 6 | yes | 155 R32 | 12 |
| 40 | `d718e083bd23d2b1` | 178 | 1 | 1 | 1 | 1 | chiral | 4 | 12 | 12 | yes | 178 P6_122 | 24 |
| 41 | `f14a8c4e7c5b3e3a` | 180 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 180 P6_222 | 24 |
| 42 | `29bbba1adec778da` | 171 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 171 P6_2 | 24 |
| 43 | `66563d07a1110a25` | 154 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 154 P3_221 | 24 |
| 44 | `ce3b42c8a4ceff6f` | 151 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 151 P3_112 | 24 |
| 45 | `7b9cfe26fe4a9c4b` | 146 | 1 | 1 | 1 | 1 | chiral | 2 | 3 | 3 | yes | 146 R3 | 12 |
| 46 | `2b9726574a0a8bed` | 171 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 171 P6_2 | 24 |
| 47 | `f07d69523ef41b37` | 178 | 2 | 2 | 2 | 2 | chiral | 2 | 12 | 12 | yes | 178 P6_122 | 24 |
| 48 | `16025e0680843c36` | 169 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 169 P6_1 | 24 |
| 49 | `d10bb4a25bbf4c80` | 154 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 154 P3_221 | 24 |
| 50 | `e0bf1a48f096c10d` | 180 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 180 P6_222 | 24 |
| 51 | `b2430fc4bea4e06d` | 154 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 154 P3_221 | 24 |
| 52 | `bff9b24ce78050f5` | 144 | 1 | 1 | 1 | 1 | chiral | 2 | 3 | 3 | yes | 144 P3_1 | 24 |
| 53 | `4db369a636f4396b` | 151 | 2 | 4 | 4 | 4 | chiral | 4 | 12 | 6 | NO | 181 P6_422 (origin shift ('0', '0', '1/3')) | 24 |
| 54 | `042c19cbfdc869cb` | 178 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 178 P6_122 | 24 |
| 55 | `23594bd7053503aa` | 153 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 153 P3_212 | 24 |
| 56 | `f5fbebffa76808d5` | 179 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 179 P6_522 | 24 |
| 57 | `057255f61286b052` | 167 | 2 | 2 | 2 | 2 | chiral | 2 | 12 | 12 | yes | 167 R-3c | 12 |
| 58 | `e198aac88f223892` | 153 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 153 P3_212 | 24 |
| 59 | `d07f950b8309de82` | 171 | 1 | 1 | 1 | 1 | chiral | 2 | 6 | 6 | yes | 171 P6_2 | 24 |
| 60 | `a182e87006c7a00d` | 179 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 179 P6_522 | 24 |
| 61 | `a46cbaad3c23e834` | 155 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 155 R32 | 12 |
| 62 | `dd3fb07fe11d73d3` | 179 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 179 P6_522 | 24 |
| 63 | `36c92427e3d084dc` | 166 | 2 | 2 | 2 | 1 | achiral | 2 | 12 | 12 | yes | 166 R-3m | 12 |
| 64 | `bc59e5d778f60d1f` | 178 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 178 P6_122 | 24 |
| 65 | `cbead3df2d2f1d0e` | 154 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 154 P3_221 | 24 |
| 66 | `85244add8d1f2d55` | 169 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 169 P6_1 | 24 |
| 67 | `2165f5c5260120de` | 152 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 152 P3_121 | 24 |
| 68 | `437fbe758a6dd8e3` | 179 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 179 P6_522 | 24 |
| 69 | `36ec4ad2f530e145` | 151 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 151 P3_112 | 24 |
| 70 | `fcffad0da2b5b62f` | 154 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 154 P3_221 | 24 |
| 71 | `505a4911e298c933` | 181 | 1 | 1 | 1 | 1 | chiral | 2 | 12 | 12 | yes | 181 P6_422 | 24 |
| 72 | `24a6b511067d37b2` | 178 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 178 P6_122 | 24 |
| 73 | `30f2a1e483babf55` | 178 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 178 P6_122 | 24 |
| 74 | `37aa18e6e10583be` | 155 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 155 R32 | 12 |
| 75 | `7715c7010e513b71` | 181 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 181 P6_422 | 24 |
| 76 | `0b5d9beb0fc972f6` | 179 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 179 P6_522 | 24 |
| 77 | `322d5ff451e4101d` | 169 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 169 P6_1 | 24 |
| 78 | `34351050a4f29035` | 178 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 178 P6_122 | 24 |
| 79 | `c0071756347c5a8a` | 144 | 1 | 1 | 1 | 1 | chiral | 1 | 3 | 3 | yes | 144 P3_1 | 24 |
| 80 | `d9bf7fb7a80eaa38` | 155 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 155 R32 | 12 |
| 81 | `847d2695a14ae424` | 152 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 152 P3_121 | 24 |
| 82 | `090dcafb7ce9cb08` | 166 | 2 | 2 | 2 | 1 | achiral | 2 | 12 | 12 | yes | 166 R-3m | 12 |
| 83 | `9bc4922a7b574aa6` | 166 | 2 | 2 | 2 | 1 | achiral | 2 | 12 | 12 | yes | 166 R-3m | 12 |
| 84 | `43e4e46001b4d8b9` | 181 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 181 P6_422 | 24 |
| 85 | `af8b2135c913b13b` | 181 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 181 P6_422 | 24 |
| 86 | `74a69fba4266de3b` | 167 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 167 R-3c | 12 |
| 87 | `c3b4b14633c9d4d5` | 155 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 155 R32 | 12 |
| 88 | `e19babba732f5fd4` | 179 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 179 P6_522 | 24 |
| 89 | `7472d8ba000c8056` | 152 | 2 | 2 | 2 | 2 | chiral | 2 | 6 | 6 | yes | 152 P3_121 | 24 |
| 90 | `d0c5a15c25ab6413` | 152 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 152 P3_121 | 24 |
| 91 | `d770abfcee4deb90` | 153 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 153 P3_212 | 24 |
| 92 | `4a560e459032166a` | 154 | 1 | 1 | 1 | 1 | chiral | 2 | 6 | 6 | yes | 154 P3_221 | 24 |
| 93 | `5beb94b61eb66eb1` | 178 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 178 P6_122 | 24 |
| 94 | `95934e84555dc2ea` | 179 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 179 P6_522 | 24 |
| 95 | `d0ed9179c6947b5f` | 155 | 1 | 1 | 1 | 1 | chiral | 2 | 6 | 6 | yes | 155 R32 | 12 |
| 96 | `0948aa6184f13a8a` | 179 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 179 P6_522 | 24 |
| 97 | `272aefcd5e48ba49` | 179 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 179 P6_522 | 24 |
| 98 | `466b12546dd936c3` | 161 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 161 R3c | 12 |
| 99 | `4885ce1e70fa9713` | 179 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 179 P6_522 | 24 |
| 100 | `3d6b109f392fda19` | 154 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 154 P3_221 | 24 |
| 101 | `e598ffd8a1cac138` | 144 | 1 | 1 | 1 | 1 | chiral | 1 | 3 | 3 | yes | 144 P3_1 | 24 |
| 102 | `a93f8fe7ecdc5851` | 144 | 1 | 1 | 1 | 1 | chiral | 1 | 3 | 3 | yes | 144 P3_1 | 24 |
| 103 | `aef8972953d53d20` | 171 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 171 P6_2 | 24 |
| 104 | `72bcd959be4ab7dd` | 152 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 152 P3_121 | 24 |
| 105 | `ab801b11bead62ef` | 166 | 2 | 2 | 2 | 1 | achiral | 2 | 12 | 12 | yes | 166 R-3m | 12 |
| 106 | `2c121297dbaa80af` | 154 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 154 P3_221 | 24 |
| 107 | `9d0b36ad5caceb2e` | 167 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 167 R-3c | 12 |
| 108 | `d176b8d859dd651a` | 178 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 178 P6_122 | 24 |
| 109 | `60eb4282db04fca2` | 179 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 179 P6_522 | 24 |
| 110 | `f43b45fd6383b36b` | 155 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 155 R32 | 12 |
| 111 | `4ff9d77aa9f8194a` | 167 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 167 R-3c | 12 |
| 112 | `6de3dac5f334cfed` | 167 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 167 R-3c | 12 |
| 113 | `105e41c2798e6180` | 148 | 3 | 6 | 6 | 3 | achiral | 6 | 12 | 6 | NO | 166 R-3m | 12 |
| 114 | `542cbe76934b484b` | 154 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 154 P3_221 | 24 |
| 115 | `75bbbcb4a37e70e8` | 146 | 1 | 1 | 1 | 1 | chiral | 1 | 3 | 3 | yes | 146 R3 | 12 |
| 116 | `cff2d5fb5e0d4149` | 171 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 171 P6_2 | 24 |
| 117 | `4b6055c7aa3d341b` | 178 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 178 P6_122 | 24 |
| 118 | `7e79f1c38b5516bf` | 178 | 2 | 2 | 2 | 2 | chiral | 2 | 12 | 12 | yes | 178 P6_122 | 24 |
| 119 | `d7c638d7fa23127e` | 169 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 169 P6_1 | 24 |
| 120 | `0417061f8f56488e` | 152 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 152 P3_121 | 24 |
| 121 | `6cc34ed38aa354e1` | 181 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 181 P6_422 | 24 |
| 122 | `5838282f46223111` | 152 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 152 P3_121 | 24 |
| 123 | `cda1d1c03659b67d` | 148 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 148 R-3 | 12 |
| 124 | `161b09808f4c1863` | 178 | 2 | 2 | 2 | 2 | chiral | 4 | 12 | 12 | yes | 178 P6_122 | 24 |
| 125 | `c92eef8763d02d8a` | 179 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 179 P6_522 | 24 |
| 126 | `3a491fd6426d90b2` | 146 | 1 | 1 | 1 | 1 | chiral | 1 | 3 | 3 | yes | 146 R3 | 12 |
| 127 | `5b679d8b0a3147c3` | 152 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 152 P3_121 | 24 |
| 128 | `fac4317d5a65b959` | 148 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 148 R-3 | 12 |
| 129 | `27d463eac6cda5ea` | 171 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 171 P6_2 | 24 |
| 130 | `919d30fd9021b5ee` | 154 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 154 P3_221 | 24 |
| 131 | `6074c5fa5d2dffc5` | 148 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 148 R-3 | 12 |
| 132 | `5e68ffe7582a0657` | 167 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 167 R-3c | 12 |
| 133 | `1ba26ab2c0999b93` | 148 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 148 R-3 | 12 |
| 134 | `27dbb77012555d28` | 161 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 161 R3c | 12 |
| 135 | `c18a9b1cb2a5d168` | 148 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 148 R-3 | 12 |
| 136 | `d1f1121757598de0` | 154 | 1 | 1 | 1 | 1 | chiral | 2 | 6 | 6 | yes | 154 P3_221 | 24 |
| 137 | `b27ba8dbcbc2891a` | 161 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 161 R3c | 12 |
| 138 | `457c20cf036ae496` | 180 | 2 | 2 | 2 | 2 | chiral | 2 | 12 | 12 | yes | 180 P6_222 | 24 |
| 139 | `11a9fe078850b5cd` | 179 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 179 P6_522 | 24 |
| 140 | `5f812747976b224a` | 148 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 148 R-3 | 12 |
| 141 | `c95a5fcf4d681568` | 166 | 2 | 2 | 2 | 1 | achiral | 2 | 12 | 12 | yes | 166 R-3m | 12 |
| 142 | `f7bd7cd9eae6436b` | 166 | 2 | 2 | 2 | 1 | achiral | 2 | 12 | 12 | yes | 166 R-3m | 12 |
| 143 | `75c9be976d704515` | 152 | 2 | 2 | 2 | 2 | chiral | 2 | 6 | 6 | yes | 152 P3_121 | 24 |
| 144 | `8463196a30c6643f` | 179 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 179 P6_522 | 24 |
| 145 | `487490cdf474e568` | 148 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 148 R-3 | 12 |
| 146 | `f0e2036d295195b4` | 152 | 2 | 2 | 2 | 2 | chiral | 2 | 6 | 6 | yes | 152 P3_121 | 24 |
| 147 | `67b1ede4b021a4fc` | 155 | 1 | 1 | 1 | 1 | chiral | 1 | 6 | 6 | yes | 155 R32 | 12 |
| 148 | `34e5e7acce18b5cd` | 166 | 2 | 2 | 2 | 1 | achiral | 2 | 12 | 12 | yes | 166 R-3m | 12 |
| 149 | `fa9c370d30741970` | 180 | 2 | 2 | 2 | 2 | chiral | 2 | 12 | 12 | yes | 180 P6_222 | 24 |
| 150 | `400cba5c78326d1d` | 167 | 1 | 1 | 1 | 1 | chiral | 1 | 12 | 12 | yes | 167 R-3c | 12 |
| 151 | `78e755ffdff3a2f5` | 146 | 1 | 1 | 1 | 1 | chiral | 2 | 3 | 3 | yes | 146 R3 | 12 |

## Counts reached (banked n<=4 == independent; independent to n<=5)

| # | id | fixed (indep, n=1..reached) | free | one-sided | indep reached | indep wall |
|---|---|---|---|---|---|---|
| 1 | `c49077384aaebeb0` | [6, 72, 1248, 24960, 541158] | [1, 8, 110, 2115, 45211] | [1, 8, 110, 2115, 45211] | 5 | 19s |
| 2 | `59585d778cb3a7a4` | [6, 66, 1026, 18366, 356628] | [1, 9, 91, 1583, 29814] | [1, 9, 91, 1583, 29814] | 5 | 14s |
| 3 | `095ce61d28388c98` | [6, 66, 1062, 19818, 401286] | [1, 8, 94, 1691, 33540] | [1, 8, 94, 1691, 33540] | 5 | 16s |
| 4 | `9be0f2271a14b6a9` | [6, 60, 864, 14484, 263982] | [1, 8, 77, 1248, 22079] | [1, 8, 77, 1248, 22079] | 5 | 10s |
| 5 | `2d654c836f3731c6` | [6, 60, 852, 14058, 252336] | [1, 8, 76, 1214, 21105] | [1, 8, 76, 1214, 21105] | 5 | 10s |
| 6 | `b0f80776885f3ae1` | [6, 60, 828, 13206, 228894] | [1, 9, 74, 1153, 19151] | [1, 9, 74, 1153, 19151] | 5 | 9s |
| 7 | `a348875c3f707895` | [6, 60, 840, 13674, 241674] | [1, 9, 75, 1193, 20216] | [1, 9, 75, 1193, 20216] | 5 | 10s |
| 8 | `dcc38ea9177089b9` | [6, 60, 900, 15828, 303294] | [1, 9, 80, 1377, 25360] | [1, 9, 80, 1377, 25360] | 5 | 11s |
| 9 | `5b86a254c715306c` | [6, 66, 1002, 17592, 335520] | [1, 11, 167, 2932, 55920] | [1, 11, 167, 2932, 55920] | 5 | 8s |
| 10 | `f05f0b009e0929f6` | [6, 54, 690, 10308, 167652] | [1, 9, 115, 1718, 27942] | [1, 9, 115, 1718, 27942] | 5 | 4s |
| 11 | `d70e6901953070e7` | [6, 66, 1022, 18453, 364038] | [1, 15, 171, 3135, 60673] | [1, 15, 171, 3135, 60673] | 5 | 8s |
| 12 | `e1a38303b2378f17` | [6, 66, 1002, 17592, 335520] | [1, 11, 167, 2932, 55920] | [1, 11, 167, 2932, 55920] | 5 | 8s |
| 13 | `c82ebc15c49c1413` | [6, 63, 924, 15609, 286068] | [1, 13, 154, 2637, 47678] | [1, 13, 154, 2637, 47678] | 5 | 7s |
| 14 | `f6f8b3050a1eef42` | [12, 126, 1896, 33276, 637080] | [1, 16, 158, 2852, 53090] | [1, 16, 158, 2852, 53090] | 5 | 22s |
| 15 | `9c0b7e0c29dfebb2` | [6, 60, 828, 13224, 229620] | [1, 10, 138, 2204, 38270] | [1, 10, 138, 2204, 38270] | 5 | 6s |
| 16 | `87c94384d7851cb2` | [6, 60, 848, 14052, 254562] | [1, 14, 142, 2396, 42427] | [1, 14, 142, 2396, 42427] | 5 | 6s |
| 17 | `a35623e347ef03b4` | [6, 54, 702, 10542, 171888] | [1, 9, 117, 1757, 28648] | [1, 9, 117, 1757, 28648] | 5 | 4s |
| 18 | `e98412e7cb95aea2` | [3, 27, 339, 4917, 77418] | [1, 6, 61, 839, 12964] | [1, 6, 61, 839, 12964] | 5 | 2s |
| 19 | `ac4489d658eb445e` | [12, 120, 1728, 28878, 524988] | [1, 15, 144, 2476, 43749] | [1, 15, 144, 2476, 43749] | 5 | 19s |
| 20 | `c53bc05bc306c97d` | [6, 57, 782, 12396, 213738] | [1, 8, 70, 1082, 17881] | [1, 14, 131, 2125, 35623] | 5 | 8s |
| 21 | `8cc8c5ab3cf36d8f` | [12, 120, 1704, 27900, 495720] | [1, 14, 142, 2381, 41310] | [1, 14, 142, 2381, 41310] | 5 | 18s |
| 22 | `646b518ccf3bd724` | [6, 60, 852, 14106, 254274] | [1, 10, 142, 2351, 42379] | [1, 10, 142, 2351, 42379] | 5 | 6s |
| 23 | `7a448bed1119dfad` | [12, 120, 1752, 29862, 556392] | [1, 16, 146, 2571, 46366] | [1, 16, 146, 2571, 46366] | 5 | 19s |
| 24 | `7e023be581e7c50a` | [6, 60, 840, 13611, 239664] | [1, 12, 140, 2294, 39944] | [1, 12, 140, 2294, 39944] | 5 | 6s |
| 25 | `7e05ce00d8a7cbf6` | [12, 126, 1872, 32196, 602316] | [1, 15, 156, 2749, 50193] | [1, 15, 156, 2749, 50193] | 5 | 21s |
| 26 | `59b28b3a59c27092` | [6, 60, 848, 13917, 248970] | [1, 14, 142, 2374, 41495] | [1, 14, 142, 2374, 41495] | 5 | 6s |
| 27 | `d9ac68100a276dfe` | [6, 60, 852, 14028, 251172] | [1, 10, 142, 2338, 41862] | [1, 10, 142, 2338, 41862] | 5 | 6s |
| 28 | `6f4101f83371033d` | [6, 60, 828, 13224, 229620] | [1, 10, 138, 2204, 38270] | [1, 10, 138, 2204, 38270] | 5 | 6s |
| 29 | `f0b07b168368759b` | [3, 18, 158, 1596, 17523] | [1, 3, 18, 147, 1503] | [1, 5, 30, 282, 2950] | 5 | 1s |
| 30 | `56918d2cff883e22` | [6, 42, 410, 4620, 56520] | [1, 8, 69, 781, 9420] | [2, 14, 138, 1540, 18840] | 5 | 2s |
| 31 | `f429e996b3f455a6` | [6, 48, 524, 6618, 90924] | [1, 9, 88, 1116, 15154] | [2, 16, 176, 2206, 30308] | 5 | 2s |
| 32 | `71d2c9953ca110b8` | [6, 60, 852, 14058, 252336] | [1, 10, 142, 2343, 42056] | [1, 10, 142, 2343, 42056] | 5 | 6s |
| 33 | `8d90c524c89922d9` | [6, 60, 828, 13206, 228816] | [1, 10, 138, 2201, 38136] | [1, 10, 138, 2201, 38136] | 5 | 6s |
| 34 | `9d4396ca0b08fc3c` | [6, 39, 356, 3777, 43602] | [1, 6, 33, 341, 3665] | [1, 10, 60, 660, 7267] | 5 | 2s |
| 35 | `07d543d89e2934f2` | [6, 60, 840, 13713, 244062] | [1, 12, 140, 2313, 40677] | [1, 12, 140, 2313, 40677] | 5 | 6s |
| 36 | `2081d7b9a734e4fe` | [6, 60, 888, 15330, 288180] | [1, 12, 150, 2584, 48030] | [1, 12, 150, 2584, 48030] | 5 | 7s |
| 37 | `257b627a90b78038` | [6, 45, 474, 5871, 79614] | [1, 7, 43, 523, 6675] | [1, 7, 43, 523, 6675] | 5 | 3s |
| 38 | `3ddc41389e6d484f` | [6, 54, 690, 10263, 166248] | [1, 11, 115, 1734, 27708] | [1, 11, 115, 1734, 27708] | 5 | 4s |
| 39 | `64203f15fcf6c09b` | [3, 21, 217, 2613, 34221] | [1, 6, 40, 461, 5744] | [1, 6, 40, 461, 5744] | 5 | 1s |
| 40 | `d718e083bd23d2b1` | [12, 108, 1452, 22434, 375288] | [1, 13, 121, 1920, 31274] | [1, 13, 121, 1920, 31274] | 5 | 14s |
| 41 | `f14a8c4e7c5b3e3a` | [12, 108, 1356, 19782, 314328] | [1, 14, 113, 1708, 26194] | [1, 14, 113, 1708, 26194] | 5 | 13s |
| 42 | `29bbba1adec778da` | [6, 48, 540, 7074, 100914] | [1, 10, 90, 1200, 16819] | [1, 10, 90, 1200, 16819] | 5 | 2s |
| 43 | `66563d07a1110a25` | [6, 60, 852, 14112, 254820] | [1, 12, 142, 2378, 42470] | [1, 12, 142, 2378, 42470] | 5 | 6s |
| 44 | `ce3b42c8a4ceff6f` | [6, 57, 774, 12159, 207354] | [1, 14, 129, 2086, 34559] | [1, 14, 129, 2086, 34559] | 5 | 6s |
| 45 | `7b9cfe26fe4a9c4b` | [3, 21, 213, 2517, 32355] | [1, 7, 73, 839, 10785] | [1, 7, 73, 839, 10785] | 5 | 1s |
| 46 | `2b9726574a0a8bed` | [6, 51, 612, 8517, 128826] | [1, 10, 102, 1436, 21471] | [1, 10, 102, 1436, 21471] | 5 | 3s |
| 47 | `f07d69523ef41b37` | [6, 54, 726, 11292, 190698] | [1, 6, 65, 961, 15958] | [1, 6, 65, 961, 15958] | 5 | 8s |
| 48 | `16025e0680843c36` | [6, 54, 702, 10656, 176088] | [1, 9, 117, 1776, 29348] | [1, 9, 117, 1776, 29348] | 5 | 4s |
| 49 | `d10bb4a25bbf4c80` | [6, 54, 678, 9852, 155712] | [1, 11, 113, 1665, 25952] | [1, 11, 113, 1665, 25952] | 5 | 4s |
| 50 | `e0bf1a48f096c10d` | [12, 108, 1452, 23283, 410268] | [1, 15, 121, 2015, 34189] | [1, 15, 121, 2015, 34189] | 5 | 15s |
| 51 | `b2430fc4bea4e06d` | [6, 57, 762, 11742, 196488] | [1, 12, 127, 1989, 32748] | [1, 12, 127, 1989, 32748] | 5 | 5s |
| 52 | `bff9b24ce78050f5` | [3, 24, 276, 3690, 53577] | [1, 8, 92, 1230, 17859] | [1, 8, 92, 1230, 17859] | 5 | 1s |
| 53 | `4db369a636f4396b` | [3, 21, 201, 2208, 26310] | [1, 4, 22, 205, 2248] | [1, 4, 22, 205, 2248] | 5 | 1s |
| 54 | `042c19cbfdc869cb` | [12, 108, 1380, 20472, 330216] | [1, 12, 115, 1743, 27518] | [1, 12, 115, 1743, 27518] | 5 | 13s |
| 55 | `23594bd7053503aa` | [6, 54, 690, 10266, 166176] | [1, 13, 115, 1759, 27696] | [1, 13, 115, 1759, 27696] | 5 | 4s |
| 56 | `f5fbebffa76808d5` | [12, 108, 1428, 22200, 377472] | [1, 13, 119, 1901, 31456] | [1, 13, 119, 1901, 31456] | 5 | 14s |
| 57 | `057255f61286b052` | [6, 48, 556, 7536, 111324] | [1, 6, 51, 652, 9329] | [2, 11, 102, 1290, 18658] | 5 | 5s |
| 58 | `e198aac88f223892` | [6, 51, 624, 8898, 138078] | [1, 13, 104, 1535, 23013] | [1, 13, 104, 1535, 23013] | 5 | 4s |
| 59 | `d07f950b8309de82` | [6, 51, 612, 8526, 129030] | [1, 10, 102, 1438, 21505] | [1, 10, 102, 1438, 21505] | 5 | 3s |
| 60 | `a182e87006c7a00d` | [12, 108, 1356, 19674, 310224] | [1, 12, 113, 1677, 25852] | [1, 12, 113, 1677, 25852] | 5 | 12s |
| 61 | `a46cbaad3c23e834` | [6, 57, 770, 12018, 203934] | [1, 14, 129, 2061, 33989] | [1, 14, 129, 2061, 33989] | 5 | 5s |
| 62 | `dd3fb07fe11d73d3` | [12, 108, 1404, 21318, 353136] | [1, 11, 117, 1802, 29428] | [1, 11, 117, 1802, 29428] | 5 | 13s |
| 63 | `36c92427e3d084dc` | [6, 39, 364, 3924, 45918] | [1, 6, 34, 353, 3858] | [1, 9, 62, 675, 7653] | 5 | 2s |
| 64 | `bc59e5d778f60d1f` | [12, 102, 1248, 17808, 276384] | [1, 13, 104, 1536, 23032] | [1, 13, 104, 1536, 23032] | 5 | 11s |
| 65 | `cbead3df2d2f1d0e` | [6, 57, 786, 12498, 215610] | [1, 12, 131, 2115, 35935] | [1, 12, 131, 2115, 35935] | 5 | 6s |
| 66 | `85244add8d1f2d55` | [6, 54, 654, 9162, 139686] | [1, 9, 109, 1527, 23281] | [1, 9, 109, 1527, 23281] | 5 | 4s |
| 67 | `2165f5c5260120de` | [6, 51, 612, 8496, 128004] | [1, 11, 102, 1444, 21334] | [1, 11, 102, 1444, 21334] | 5 | 3s |
| 68 | `437fbe758a6dd8e3` | [12, 108, 1380, 20418, 328404] | [1, 14, 115, 1762, 27367] | [1, 14, 115, 1762, 27367] | 5 | 12s |
| 69 | `36ec4ad2f530e145` | [6, 51, 612, 8520, 128952] | [1, 12, 102, 1460, 21492] | [1, 12, 102, 1460, 21492] | 5 | 3s |
| 70 | `fcffad0da2b5b62f` | [6, 54, 690, 10281, 166914] | [1, 11, 115, 1737, 27819] | [1, 11, 115, 1737, 27819] | 5 | 4s |
| 71 | `505a4911e298c933` | [12, 96, 1080, 14130, 201240] | [1, 13, 90, 1231, 16770] | [1, 13, 90, 1231, 16770] | 5 | 8s |
| 72 | `24a6b511067d37b2` | [12, 102, 1248, 17676, 271860] | [1, 12, 104, 1515, 22655] | [1, 12, 104, 1515, 22655] | 5 | 11s |
| 73 | `30f2a1e483babf55` | [12, 102, 1248, 17718, 273444] | [1, 11, 104, 1507, 22787] | [1, 11, 104, 1507, 22787] | 5 | 10s |
| 74 | `37aa18e6e10583be` | [6, 57, 778, 12339, 213036] | [1, 12, 131, 2089, 35506] | [1, 12, 131, 2089, 35506] | 5 | 6s |
| 75 | `7715c7010e513b71` | [12, 102, 1272, 18408, 289800] | [1, 14, 106, 1597, 24150] | [1, 14, 106, 1597, 24150] | 5 | 11s |
| 76 | `0b5d9beb0fc972f6` | [12, 108, 1428, 21984, 368604] | [1, 12, 119, 1870, 30717] | [1, 12, 119, 1870, 30717] | 5 | 14s |
| 77 | `322d5ff451e4101d` | [6, 54, 678, 9816, 154116] | [1, 9, 113, 1636, 25686] | [1, 9, 113, 1636, 25686] | 5 | 4s |
| 78 | `34351050a4f29035` | [12, 96, 1080, 14130, 201048] | [1, 12, 90, 1220, 16754] | [1, 12, 90, 1220, 16754] | 5 | 8s |
| 79 | `c0071756347c5a8a` | [3, 24, 264, 3354, 46299] | [1, 8, 88, 1118, 15433] | [1, 8, 88, 1118, 15433] | 5 | 1s |
| 80 | `d9bf7fb7a80eaa38` | [6, 57, 802, 13248, 238860] | [1, 12, 135, 2241, 39810] | [1, 12, 135, 2241, 39810] | 5 | 6s |
| 81 | `847d2695a14ae424` | [6, 51, 624, 8871, 137076] | [1, 10, 104, 1497, 22846] | [1, 10, 104, 1497, 22846] | 5 | 4s |
| 82 | `090dcafb7ce9cb08` | [6, 42, 434, 5313, 71310] | [1, 7, 40, 481, 5988] | [1, 11, 73, 925, 11885] | 5 | 3s |
| 83 | `9bc4922a7b574aa6` | [6, 39, 380, 4365, 54822] | [1, 6, 35, 393, 4602] | [1, 10, 64, 760, 9137] | 5 | 3s |
| 84 | `43e4e46001b4d8b9` | [12, 108, 1380, 20508, 331836] | [1, 14, 115, 1768, 27653] | [1, 14, 115, 1768, 27653] | 5 | 13s |
| 85 | `af8b2135c913b13b` | [12, 108, 1356, 19737, 312060] | [1, 14, 113, 1704, 26005] | [1, 14, 113, 1704, 26005] | 5 | 13s |
| 86 | `74a69fba4266de3b` | [12, 102, 1192, 16086, 235656] | [1, 11, 100, 1369, 19638] | [2, 21, 200, 2726, 39276] | 5 | 10s |
| 87 | `c3b4b14633c9d4d5` | [6, 51, 644, 9456, 150948] | [1, 12, 108, 1619, 25158] | [1, 12, 108, 1619, 25158] | 5 | 3s |
| 88 | `e19babba732f5fd4` | [12, 102, 1296, 19278, 312864] | [1, 11, 108, 1637, 26072] | [1, 11, 108, 1637, 26072] | 5 | 13s |
| 89 | `7472d8ba000c8056` | [3, 24, 276, 3648, 52275] | [1, 5, 50, 621, 8762] | [1, 5, 50, 621, 8762] | 5 | 1s |
| 90 | `d0c5a15c25ab6413` | [6, 54, 690, 10254, 165906] | [1, 11, 115, 1734, 27651] | [1, 11, 115, 1734, 27651] | 5 | 5s |
| 91 | `d770abfcee4deb90` | [6, 54, 678, 9864, 155994] | [1, 12, 113, 1679, 25999] | [1, 12, 113, 1679, 25999] | 5 | 4s |
| 92 | `4a560e459032166a` | [6, 48, 528, 6732, 93414] | [1, 10, 88, 1142, 15569] | [1, 10, 88, 1142, 15569] | 5 | 2s |
| 93 | `5beb94b61eb66eb1` | [12, 96, 1104, 14658, 211332] | [1, 13, 92, 1275, 17611] | [1, 13, 92, 1275, 17611] | 5 | 8s |
| 94 | `95934e84555dc2ea` | [12, 96, 1152, 16152, 246444] | [1, 13, 96, 1404, 20537] | [1, 13, 96, 1404, 20537] | 5 | 9s |
| 95 | `d0ed9179c6947b5f` | [6, 36, 296, 2814, 29130] | [1, 9, 50, 492, 4855] | [1, 9, 50, 492, 4855] | 5 | 1s |
| 96 | `0948aa6184f13a8a` | [12, 102, 1200, 16368, 242700] | [1, 12, 100, 1404, 20225] | [1, 12, 100, 1404, 20225] | 5 | 10s |
| 97 | `272aefcd5e48ba49` | [12, 102, 1248, 17952, 282288] | [1, 13, 104, 1549, 23524] | [1, 13, 104, 1549, 23524] | 5 | 11s |
| 98 | `466b12546dd936c3` | [6, 48, 536, 6948, 97998] | [1, 8, 90, 1158, 16333] | [2, 16, 180, 2316, 32666] | 5 | 3s |
| 99 | `4885ce1e70fa9713` | [12, 96, 1104, 14820, 217392] | [1, 13, 92, 1289, 18116] | [1, 13, 92, 1289, 18116] | 5 | 9s |
| 100 | `3d6b109f392fda19` | [6, 57, 774, 12156, 207126] | [1, 11, 129, 2045, 34521] | [1, 11, 129, 2045, 34521] | 5 | 5s |
| 101 | `e598ffd8a1cac138` | [3, 27, 351, 5289, 86460] | [1, 9, 117, 1763, 28820] | [1, 9, 117, 1763, 28820] | 5 | 2s |
| 102 | `a93f8fe7ecdc5851` | [3, 27, 345, 5097, 81780] | [1, 9, 115, 1699, 27260] | [1, 9, 115, 1699, 27260] | 5 | 2s |
| 103 | `aef8972953d53d20` | [6, 54, 690, 10245, 165438] | [1, 11, 115, 1732, 27573] | [1, 11, 115, 1732, 27573] | 5 | 4s |
| 104 | `72bcd959be4ab7dd` | [6, 48, 528, 6720, 93000] | [1, 10, 88, 1141, 15500] | [1, 10, 88, 1141, 15500] | 5 | 2s |
| 105 | `ab801b11bead62ef` | [6, 39, 364, 3972, 47154] | [1, 6, 34, 355, 3961] | [1, 9, 62, 683, 7859] | 5 | 2s |
| 106 | `2c121297dbaa80af` | [6, 48, 528, 6708, 92604] | [1, 10, 88, 1139, 15434] | [1, 10, 88, 1139, 15434] | 5 | 2s |
| 107 | `9d0b36ad5caceb2e` | [12, 90, 940, 11466, 152952] | [1, 10, 79, 980, 12746] | [2, 19, 158, 1949, 25492] | 5 | 6s |
| 108 | `d176b8d859dd651a` | [12, 108, 1380, 20454, 329736] | [1, 12, 115, 1742, 27478] | [1, 12, 115, 1742, 27478] | 5 | 12s |
| 109 | `60eb4282db04fca2` | [12, 102, 1248, 17742, 274212] | [1, 12, 104, 1519, 22851] | [1, 12, 104, 1519, 22851] | 5 | 11s |
| 110 | `f43b45fd6383b36b` | [6, 51, 628, 8994, 140148] | [1, 11, 106, 1528, 23358] | [1, 11, 106, 1528, 23358] | 5 | 3s |
| 111 | `4ff9d77aa9f8194a` | [12, 90, 940, 11346, 148812] | [1, 10, 79, 971, 12401] | [2, 19, 158, 1931, 24802] | 5 | 6s |
| 112 | `6de3dac5f334cfed` | [12, 96, 1096, 14538, 209316] | [1, 11, 92, 1246, 17443] | [2, 21, 184, 2478, 34886] | 5 | 9s |
| 113 | `105e41c2798e6180` | [2, 13, 120, 1271, 14576] | [1, 4, 16, 143, 1327] | [1, 4, 20, 228, 2432] | 5 | 1s |
| 114 | `542cbe76934b484b` | [6, 51, 624, 8883, 137544] | [1, 10, 104, 1498, 22924] | [1, 10, 104, 1498, 22924] | 5 | 4s |
| 115 | `75bbbcb4a37e70e8` | [3, 24, 272, 3591, 51594] | [1, 8, 92, 1197, 17198] | [1, 8, 92, 1197, 17198] | 5 | 1s |
| 116 | `cff2d5fb5e0d4149` | [6, 42, 414, 4686, 57600] | [1, 8, 69, 790, 9600] | [1, 8, 69, 790, 9600] | 5 | 2s |
| 117 | `4b6055c7aa3d341b` | [12, 90, 972, 12210, 166920] | [1, 10, 81, 1043, 13910] | [1, 10, 81, 1043, 13910] | 5 | 6s |
| 118 | `7e79f1c38b5516bf` | [6, 42, 426, 5058, 65364] | [1, 5, 39, 437, 5485] | [1, 5, 39, 437, 5485] | 5 | 3s |
| 119 | `d7c638d7fa23127e` | [6, 48, 552, 7380, 107100] | [1, 8, 92, 1230, 17850] | [1, 8, 92, 1230, 17850] | 5 | 3s |
| 120 | `0417061f8f56488e` | [6, 42, 426, 4998, 63630] | [1, 9, 71, 853, 10605] | [1, 9, 71, 853, 10605] | 5 | 2s |
| 121 | `6cc34ed38aa354e1` | [12, 84, 828, 9516, 119112] | [1, 12, 69, 840, 9926] | [1, 12, 69, 840, 9926] | 5 | 5s |
| 122 | `5838282f46223111` | [6, 51, 624, 8766, 133446] | [1, 10, 104, 1478, 22241] | [1, 10, 104, 1478, 22241] | 5 | 3s |
| 123 | `cda1d1c03659b67d` | [6, 42, 410, 4599, 56052] | [1, 8, 69, 778, 9342] | [2, 14, 138, 1533, 18684] | 5 | 2s |
| 124 | `161b09808f4c1863` | [6, 42, 426, 5088, 66312] | [1, 5, 39, 439, 5567] | [1, 5, 39, 439, 5567] | 5 | 3s |
| 125 | `c92eef8763d02d8a` | [12, 96, 1128, 15474, 231060] | [1, 11, 94, 1323, 19255] | [1, 11, 94, 1323, 19255] | 5 | 9s |
| 126 | `3a491fd6426d90b2` | [3, 24, 278, 3759, 55368] | [1, 8, 94, 1253, 18456] | [1, 8, 94, 1253, 18456] | 5 | 1s |
| 127 | `5b679d8b0a3147c3` | [6, 48, 552, 7353, 106230] | [1, 10, 92, 1248, 17705] | [1, 10, 92, 1248, 17705] | 5 | 2s |
| 128 | `fac4317d5a65b959` | [6, 48, 544, 7146, 102126] | [1, 9, 92, 1205, 17021] | [2, 16, 184, 2382, 34042] | 5 | 2s |
| 129 | `27d463eac6cda5ea` | [6, 48, 552, 7350, 106446] | [1, 9, 92, 1236, 17741] | [1, 9, 92, 1236, 17741] | 5 | 3s |
| 130 | `919d30fd9021b5ee` | [6, 45, 474, 5772, 76500] | [1, 10, 79, 987, 12750] | [1, 10, 79, 987, 12750] | 5 | 2s |
| 131 | `6074c5fa5d2dffc5` | [6, 36, 296, 2820, 29244] | [1, 7, 50, 479, 4874] | [2, 12, 100, 940, 9748] | 5 | 1s |
| 132 | `5e68ffe7582a0657` | [12, 78, 672, 6594, 69876] | [1, 9, 56, 571, 5823] | [2, 17, 112, 1132, 11646] | 5 | 3s |
| 133 | `1ba26ab2c0999b93` | [6, 42, 422, 4947, 63366] | [1, 8, 71, 837, 10561] | [2, 14, 142, 1649, 21122] | 5 | 2s |
| 134 | `27dbb77012555d28` | [6, 48, 524, 6618, 90924] | [1, 8, 88, 1103, 15154] | [2, 16, 176, 2206, 30308] | 5 | 2s |
| 135 | `c18a9b1cb2a5d168` | [6, 48, 536, 6909, 96756] | [1, 9, 90, 1166, 16126] | [2, 16, 180, 2303, 32252] | 5 | 2s |
| 136 | `d1f1121757598de0` | [6, 36, 300, 2850, 29292] | [1, 7, 50, 483, 4882] | [1, 7, 50, 483, 4882] | 5 | 1s |
| 137 | `b27ba8dbcbc2891a` | [6, 42, 410, 4614, 56418] | [1, 7, 69, 769, 9403] | [2, 14, 138, 1538, 18806] | 5 | 1s |
| 138 | `457c20cf036ae496` | [6, 33, 258, 2352, 23412] | [1, 5, 24, 214, 1973] | [1, 5, 24, 214, 1973] | 5 | 1s |
| 139 | `11a9fe078850b5cd` | [12, 90, 972, 12168, 165612] | [1, 10, 81, 1039, 13801] | [1, 10, 81, 1039, 13801] | 5 | 6s |
| 140 | `5f812747976b224a` | [6, 42, 418, 4818, 60288] | [1, 8, 71, 816, 10048] | [2, 14, 142, 1606, 20096] | 5 | 2s |
| 141 | `c95a5fcf4d681568` | [6, 33, 254, 2250, 21660] | [1, 5, 24, 206, 1827] | [1, 8, 43, 393, 3610] | 5 | 1s |
| 142 | `f7bd7cd9eae6436b` | [6, 39, 364, 3924, 45918] | [1, 6, 34, 353, 3858] | [1, 9, 62, 675, 7653] | 5 | 2s |
| 143 | `75c9be976d704515` | [3, 18, 150, 1443, 15060] | [1, 4, 28, 250, 2537] | [1, 4, 28, 250, 2537] | 5 | 0s |
| 144 | `8463196a30c6643f` | [12, 90, 972, 12168, 165612] | [1, 10, 81, 1039, 13801] | [1, 10, 81, 1039, 13801] | 5 | 6s |
| 145 | `487490cdf474e568` | [6, 42, 410, 4659, 57768] | [1, 8, 69, 788, 9628] | [2, 14, 138, 1553, 19256] | 5 | 1s |
| 146 | `f0e2036d295195b4` | [3, 15, 111, 945, 8691] | [1, 3, 21, 162, 1468] | [1, 3, 21, 162, 1468] | 5 | 0s |
| 147 | `67b1ede4b021a4fc` | [6, 42, 426, 5028, 64590] | [1, 9, 73, 857, 10765] | [1, 9, 73, 857, 10765] | 5 | 2s |
| 148 | `34e5e7acce18b5cd` | [6, 33, 262, 2412, 24120] | [1, 5, 25, 218, 2032] | [1, 7, 45, 413, 4020] | 5 | 1s |
| 149 | `fa9c370d30741970` | [6, 27, 168, 1224, 9744] | [1, 5, 16, 118, 826] | [1, 5, 16, 118, 826] | 5 | 0s |
| 150 | `400cba5c78326d1d` | [12, 78, 712, 7524, 86532] | [1, 9, 60, 650, 7211] | [2, 17, 120, 1290, 14422] | 5 | 3s |
| 151 | `78e755ffdff3a2f5` | [3, 18, 158, 1611, 17811] | [1, 6, 54, 537, 5937] | [1, 6, 54, 537, 5937] | 5 | 0s |

## Per-cell certificates

### #1 `c49077384aaebeb0` — IT(178) P6_122, f=(44, 66, 24), p=3^8 4^2 5^6 6^4 9^2 14^2, aut=2

Witness point (1/12, 1/6, 1/4), c/a = 5/4, site stabilizer 2, orbit 6 conventional / 6 primitive, stratum dim 1. Open/wall label (triage, carried): open-likely (triage, 12 b). Candidate wall time 38.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(178) P6_122 p=(1/12, 1/6, 1/4) c/a=5/4 G=diag(16,16,25) period=12 n_conv=6 T=6 site=2 dim=1 f=(44,66,24) p-vec 3^8 4^2 5^6 6^4 9^2 14^2 aut=2 W=2 nonsimple=0 cutoff_D2=14400 4rho2_G=2896 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.7s | detL=1728 T=6 vol=288 T*vol=1728 (crystal-basis measure) slots=144 paired 1:1; disjointness G-ball D2=4rho2=2896 (coord bound (16, 16, 11)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 17.2s | audit re-derived 6 cells x 24 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 288 each, T*vol == |det|; all 144 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 792 shared-vertex G-equidistance checks, 6336 vertex-side checks, 144 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 20.9s | tables T=6 nbrs=24 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 72, 1248, 24960], free=[1, 8, 110, 2115]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 72, 1248, 24960, 541158], free=[1, 8, 110, 2115, 45211], one-sided=[1, 8, 110, 2115, 45211], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 19s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #2 `59585d778cb3a7a4` — IT(178) P6_122, f=(40, 60, 22), p=3^8 4^4 5^4 6^2 10^2 14^2, aut=2

Witness point (1/12, 1/6, 1/4), c/a = 3/4, site stabilizer 2, orbit 6 conventional / 6 primitive, stratum dim 1. Open/wall label (triage, carried): open-likely (triage, 22 b). Candidate wall time 27.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(178) P6_122 p=(1/12, 1/6, 1/4) c/a=3/4 G=diag(16,16,9) period=12 n_conv=6 T=6 site=2 dim=1 f=(40,60,22) p-vec 3^8 4^4 5^4 6^2 10^2 14^2 aut=2 W=2 nonsimple=0 cutoff_D2=9216 4rho2_G=2307 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=1728 T=6 vol=288 T*vol=1728 (crystal-basis measure) slots=132 paired 1:1; disjointness G-ball D2=4rho2=2307 (coord bound (14, 14, 17)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 10.7s | audit re-derived 6 cells x 22 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 288 each, T*vol == |det|; all 132 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 720 shared-vertex G-equidistance checks, 5280 vertex-side checks, 132 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 15.5s | tables T=6 nbrs=22 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 66, 1026, 18366], free=[1, 9, 91, 1583]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 66, 1026, 18366, 356628], free=[1, 9, 91, 1583, 29814], one-sided=[1, 9, 91, 1583, 29814], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 14s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #3 `095ce61d28388c98` — IT(178) P6_122, f=(40, 60, 22), p=3^6 4^6 6^6 7^2 14^2, aut=2

Witness point (1/12, 1/6, 1/4), c/a = 1, site stabilizer 2, orbit 6 conventional / 6 primitive, stratum dim 1. Open/wall label (triage, carried): open-likely (triage, 24 b). Candidate wall time 28.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(178) P6_122 p=(1/12, 1/6, 1/4) c/a=1 G=diag(2,2,2) period=12 n_conv=6 T=6 site=2 dim=1 f=(40,60,22) p-vec 3^6 4^6 6^6 7^2 14^2 aut=2 W=2 nonsimple=0 cutoff_D2=1152 4rho2_G=8024/25 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.5s | detL=1728 T=6 vol=288 T*vol=1728 (crystal-basis measure) slots=132 paired 1:1; disjointness G-ball D2=4rho2=8024/25 (coord bound (15, 15, 13)), ball sizes 38..38 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 10.8s | audit re-derived 6 cells x 22 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 288 each, T*vol == |det|; all 132 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 720 shared-vertex G-equidistance checks, 5280 vertex-side checks, 132 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 17.2s | tables T=6 nbrs=22 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 66, 1062, 19818], free=[1, 8, 94, 1691]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 66, 1062, 19818, 401286], free=[1, 8, 94, 1691, 33540], one-sided=[1, 8, 94, 1691, 33540], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 16s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #4 `9be0f2271a14b6a9` — IT(178) P6_122, f=(36, 54, 20), p=3^2 4^12 6^2 9^2 12^2, aut=4

Witness point (1/8, 1/4, 1/4), c/a = 1, site stabilizer 2, orbit 6 conventional / 6 primitive, stratum dim 1. Open/wall label (triage, carried): open-likely (triage, 20 b). Candidate wall time 19.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(178) P6_122 p=(1/8, 1/4, 1/4) c/a=1 G=diag(2,2,2) period=24 n_conv=6 T=6 site=2 dim=1 f=(36,54,20) p-vec 3^2 4^12 6^2 9^2 12^2 aut=4 W=2 nonsimple=0 cutoff_D2=4608 4rho2_G=30056/27 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=30056/27 (coord bound (28, 28, 24)), ball sizes 26..26 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 7.5s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 648 shared-vertex G-equidistance checks, 4320 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=4; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|4 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 11.1s | tables T=6 nbrs=20 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 864, 14484], free=[1, 8, 77, 1248]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 864, 14484, 263982], free=[1, 8, 77, 1248, 22079], one-sided=[1, 8, 77, 1248, 22079], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 10s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 4 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #5 `2d654c836f3731c6` — IT(178) P6_122, f=(36, 54, 20), p=3^8 4^2 6^4 7^4 12^2, aut=2

Witness point (0, 1/8, 1/3), c/a = 1, site stabilizer 2, orbit 6 conventional / 6 primitive, stratum dim 1. Open/wall label (triage, carried): open-likely (triage, 30 b). Candidate wall time 18.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(178) P6_122 p=(0, 1/8, 1/3) c/a=1 G=diag(2,2,2) period=24 n_conv=6 T=6 site=2 dim=1 f=(36,54,20) p-vec 3^8 4^2 6^4 7^4 12^2 aut=2 W=2 nonsimple=0 cutoff_D2=4608 4rho2_G=1756280/1323 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=1756280/1323 (coord bound (30, 30, 26)), ball sizes 38..38 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 7.4s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 648 shared-vertex G-equidistance checks, 4320 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 10.6s | tables T=6 nbrs=20 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 852, 14058], free=[1, 8, 76, 1214]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 852, 14058, 252336], free=[1, 8, 76, 1214, 21105], one-sided=[1, 8, 76, 1214, 21105], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 10s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #6 `b0f80776885f3ae1` — IT(178) P6_122, f=(36, 54, 20), p=3^6 4^6 5^2 6^2 8^2 14^2, aut=2

Witness point (1/12, 1/6, 1/4), c/a = 1/2, site stabilizer 2, orbit 6 conventional / 6 primitive, stratum dim 1. Open/wall label (triage, carried): open-likely (triage, 17 b). Candidate wall time 19.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(178) P6_122 p=(1/12, 1/6, 1/4) c/a=1/2 G=diag(4,4,1) period=12 n_conv=6 T=6 site=2 dim=1 f=(36,54,20) p-vec 3^6 4^6 5^2 6^2 8^2 14^2 aut=2 W=2 nonsimple=0 cutoff_D2=2304 4rho2_G=120256/243 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.7s | detL=1728 T=6 vol=288 T*vol=1728 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=120256/243 (coord bound (13, 13, 23)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 8.1s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 288 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 648 shared-vertex G-equidistance checks, 4320 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 10.1s | tables T=6 nbrs=20 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 828, 13206], free=[1, 9, 74, 1153]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 828, 13206, 228894], free=[1, 9, 74, 1153, 19151], one-sided=[1, 9, 74, 1153, 19151], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 9s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #7 `a348875c3f707895` — IT(178) P6_122, f=(36, 54, 20), p=3^4 4^10 6^2 8^2 14^2, aut=2

Witness point (0, 1/12, 1/3), c/a = 1/2, site stabilizer 2, orbit 6 conventional / 6 primitive, stratum dim 1. Open/wall label (triage, carried): open-likely (triage, 21 b). Candidate wall time 19.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(178) P6_122 p=(0, 1/12, 1/3) c/a=1/2 G=diag(4,4,1) period=12 n_conv=6 T=6 site=2 dim=1 f=(36,54,20) p-vec 3^4 4^10 6^2 8^2 14^2 aut=2 W=2 nonsimple=0 cutoff_D2=2304 4rho2_G=15668/25 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.8s | detL=1728 T=6 vol=288 T*vol=1728 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=15668/25 (coord bound (15, 15, 26)), ball sizes 56..56 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 8.3s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 288 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 648 shared-vertex G-equidistance checks, 4320 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 10.5s | tables T=6 nbrs=20 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 840, 13674], free=[1, 9, 75, 1193]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 840, 13674, 241674], free=[1, 9, 75, 1193, 20216], one-sided=[1, 9, 75, 1193, 20216], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 10s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #8 `dcc38ea9177089b9` — IT(178) P6_122, f=(36, 54, 20), p=3^2 4^8 5^2 7^4 8^4, aut=2

Witness point (1/6, 7/12, 1/12), c/a = 1/2, site stabilizer 2, orbit 6 conventional / 6 primitive, stratum dim 1. Open/wall label (triage, carried): open-likely (triage, 3 b). Candidate wall time 20.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(178) P6_122 p=(1/6, 7/12, 1/12) c/a=1/2 G=diag(4,4,1) period=12 n_conv=6 T=6 site=2 dim=1 f=(36,54,20) p-vec 3^2 4^8 5^2 7^4 8^4 aut=2 W=2 nonsimple=0 cutoff_D2=2304 4rho2_G=92416/147 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.7s | detL=1728 T=6 vol=288 T*vol=1728 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=92416/147 (coord bound (15, 15, 26)), ball sizes 60..60 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 7.4s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 288 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 648 shared-vertex G-equidistance checks, 4320 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 12.3s | tables T=6 nbrs=20 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 900, 15828], free=[1, 9, 80, 1377]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 900, 15828, 303294], free=[1, 9, 80, 1377, 25360], one-sided=[1, 9, 80, 1377, 25360], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 11s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #9 `5b86a254c715306c` — IT(169) P6_1, f=(40, 60, 22), p=3^8 4^6 6^4 10^2 14^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 797/1000, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 6 b). Candidate wall time 27.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(169) P6_1 p=(1/12, 3/8, 1/6) c/a=797/1000 G=diag(1000000,1000000,635209) period=24 n_conv=6 T=6 site=1 dim=3 f=(40,60,22) p-vec 3^8 4^6 6^4 10^2 14^2 aut=1 W=2 nonsimple=0 cutoff_D2=2304000000 4rho2_G=1232254331512336/3140625 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.7s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=132 paired 1:1; disjointness G-ball D2=4rho2=1232254331512336/3140625 (coord bound (23, 23, 25)), ball sizes 24..24 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 18.6s | audit re-derived 6 cells x 22 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 132 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 720 shared-vertex G-equidistance checks, 5280 vertex-side checks, 132 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 8.2s | tables T=6 nbrs=22 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 66, 1002, 17592], free=[1, 11, 167, 2932]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 66, 1002, 17592, 335520], free=[1, 11, 167, 2932, 55920], one-sided=[1, 11, 167, 2932, 55920], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 8s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #10 `f05f0b009e0929f6` — IT(169) P6_1, f=(32, 48, 18), p=3^2 4^6 5^6 6^2 12^2, aut=2

Witness point (1/8, 1/6, 5/12), c/a = 3/4, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 39 b). Candidate wall time 10.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(169) P6_1 p=(1/8, 1/6, 5/12) c/a=3/4 G=diag(16,16,9) period=24 n_conv=6 T=6 site=1 dim=3 f=(32,48,18) p-vec 3^2 4^6 5^6 6^2 12^2 aut=2 W=2 nonsimple=0 cutoff_D2=36864 4rho2_G=115673392/12769 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=108 paired 1:1; disjointness G-ball D2=4rho2=115673392/12769 (coord bound (28, 28, 32)), ball sizes 32..32 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.7s | audit re-derived 6 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 108 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 576 shared-vertex G-equidistance checks, 3456 vertex-side checks, 108 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 4.3s | tables T=6 nbrs=18 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 54, 690, 10308], free=[1, 9, 115, 1718]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 54, 690, 10308, 167652], free=[1, 9, 115, 1718, 27942], one-sided=[1, 9, 115, 1718, 27942], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #11 `d70e6901953070e7` — IT(155) R32, f=(38, 58, 22), p=3^6 4^8 6^3 7^2 8^1 10^1 16^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 3/4, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 3 b). Candidate wall time 20.4s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(155) R32 p=(1/8, 1/6, 5/12) c/a=3/4 G=diag(16,16,9) period=24 n_conv=18 T=6 site=1 dim=3 f=(38,58,22) p-vec 3^6 4^8 6^3 7^2 8^1 10^1 16^1 aut=1 W=2 nonsimple=2 cutoff_D2=36864 4rho2_G=4432 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.6s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=132 paired 1:1; disjointness G-ball D2=4rho2=4432 (coord bound (20, 20, 23)), ball sizes 39..39 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 9.5s | audit re-derived 6 cells x 22 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 132 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 696 shared-vertex G-equidistance checks, 5016 vertex-side checks, 132 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 9.0s | tables T=6 nbrs=22 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 66, 1022, 18453], free=[1, 15, 171, 3135]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 66, 1022, 18453, 364038], free=[1, 15, 171, 3135, 60673], one-sided=[1, 15, 171, 3135, 60673], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 8s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #12 `e1a38303b2378f17` — IT(169) P6_1, f=(40, 60, 22), p=3^8 4^6 6^2 7^2 8^2 15^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1277/2000, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b; metric-thin: P5-only). Candidate wall time 27.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(169) P6_1 p=(1/8, 1/6, 5/12) c/a=1277/2000 G=diag(4000000,4000000,1630729) period=24 n_conv=6 T=6 site=1 dim=3 f=(40,60,22) p-vec 3^8 4^6 6^2 7^2 8^2 15^2 aut=1 W=2 nonsimple=0 cutoff_D2=9216000000 4rho2_G=526796332730099125428601408/246842098282546875 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.8s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=132 paired 1:1; disjointness G-ball D2=4rho2=526796332730099125428601408/246842098282546875 (coord bound (27, 27, 37)), ball sizes 32..32 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 18.5s | audit re-derived 6 cells x 22 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 132 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 720 shared-vertex G-equidistance checks, 5280 vertex-side checks, 132 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 8.4s | tables T=6 nbrs=22 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 66, 1002, 17592], free=[1, 11, 167, 2932]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 66, 1002, 17592, 335520], free=[1, 11, 167, 2932, 55920], one-sided=[1, 11, 167, 2932, 55920], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 8s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #13 `c82ebc15c49c1413` — IT(154) P3_221, f=(38, 57, 21), p=3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 527/1000, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b). Candidate wall time 21.1s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(154) P3_221 p=(1/8, 1/6, 5/12) c/a=527/1000 G=diag(1000000,1000000,277729) period=24 n_conv=6 T=6 site=1 dim=3 f=(38,57,21) p-vec 3^10 4^2 5^2 6^2 9^2 10^1 12^1 14^1 aut=1 W=2 nonsimple=0 cutoff_D2=2304000000 4rho2_G=610477116041795820253424/1206780239671875 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.8s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=126 paired 1:1; disjointness G-ball D2=4rho2=610477116041795820253424/1206780239671875 (coord bound (26, 26, 43)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 12.7s | audit re-derived 6 cells x 21 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 126 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 684 shared-vertex G-equidistance checks, 4788 vertex-side checks, 126 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 7.3s | tables T=6 nbrs=21 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 63, 924, 15609], free=[1, 13, 154, 2637]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 63, 924, 15609, 286068], free=[1, 13, 154, 2637, 47678], one-sided=[1, 13, 154, 2637, 47678], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 7s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #14 `f6f8b3050a1eef42` — IT(178) P6_122, f=(38, 57, 21), p=3^4 4^11 6^2 10^2 12^1 14^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 3/4, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b). Candidate wall time 46.1s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(178) P6_122 p=(1/12, 3/8, 1/6) c/a=3/4 G=diag(16,16,9) period=24 n_conv=12 T=12 site=1 dim=3 f=(38,57,21) p-vec 3^4 4^11 6^2 10^2 12^1 14^1 aut=1 W=2 nonsimple=0 cutoff_D2=36864 4rho2_G=14320/3 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.9s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=252 paired 1:1; disjointness G-ball D2=4rho2=14320/3 (coord bound (20, 20, 24)), ball sizes 31..31 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 20.3s | audit re-derived 12 cells x 21 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 252 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1368 shared-vertex G-equidistance checks, 9576 vertex-side checks, 252 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 23.6s | tables T=12 nbrs=21 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 126, 1896, 33276], free=[1, 16, 158, 2852]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 126, 1896, 33276, 637080], free=[1, 16, 158, 2852, 53090], one-sided=[1, 16, 158, 2852, 53090], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 22s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #15 `9c0b7e0c29dfebb2` — IT(169) P6_1, f=(36, 54, 20), p=3^4 4^8 5^2 7^4 13^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 3/4, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b). Candidate wall time 14.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(169) P6_1 p=(1/12, 3/8, 1/6) c/a=3/4 G=diag(16,16,9) period=24 n_conv=6 T=6 site=1 dim=3 f=(36,54,20) p-vec 3^4 4^8 5^2 7^4 13^2 aut=1 W=2 nonsimple=0 cutoff_D2=36864 4rho2_G=401776/67 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=401776/67 (coord bound (23, 23, 26)), ball sizes 22..22 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 7.9s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 648 shared-vertex G-equidistance checks, 4320 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.1s | tables T=6 nbrs=20 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 828, 13224], free=[1, 10, 138, 2204]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 828, 13224, 229620], free=[1, 10, 138, 2204, 38270], one-sided=[1, 10, 138, 2204, 38270], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #16 `87c94384d7851cb2` — IT(155) R32, f=(34, 52, 20), p=3^4 4^6 5^2 6^6 8^1 14^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 797/1000, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 8 b). Candidate wall time 17.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(155) R32 p=(1/8, 1/6, 5/12) c/a=797/1000 G=diag(1000000,1000000,635209) period=24 n_conv=18 T=6 site=1 dim=3 f=(34,52,20) p-vec 3^4 4^6 5^2 6^6 8^1 14^1 aut=1 W=2 nonsimple=2 cutoff_D2=2304000000 4rho2_G=306083600 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.4s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=306083600 (coord bound (21, 21, 22)), ball sizes 39..39 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 8.7s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 624 shared-vertex G-equidistance checks, 4080 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.7s | tables T=6 nbrs=20 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 848, 14052], free=[1, 14, 142, 2396]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 848, 14052, 254562], free=[1, 14, 142, 2396, 42427], one-sided=[1, 14, 142, 2396, 42427], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #17 `a35623e347ef03b4` — IT(169) P6_1, f=(32, 48, 18), p=4^10 6^6 10^2, aut=2

Witness point (1/8, 1/6, 5/12), c/a = 5/4, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 32 b). Candidate wall time 12.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(169) P6_1 p=(1/8, 1/6, 5/12) c/a=5/4 G=diag(16,16,25) period=24 n_conv=6 T=6 site=1 dim=3 f=(32,48,18) p-vec 4^10 6^6 10^2 aut=2 W=2 nonsimple=0 cutoff_D2=57600 4rho2_G=1632697666288/148051875 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.7s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=108 paired 1:1; disjointness G-ball D2=4rho2=1632697666288/148051875 (coord bound (31, 31, 22)), ball sizes 34..34 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 6.5s | audit re-derived 6 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 108 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 576 shared-vertex G-equidistance checks, 3456 vertex-side checks, 108 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 4.6s | tables T=6 nbrs=18 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 54, 702, 10542], free=[1, 9, 117, 1757]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 54, 702, 10542, 171888], free=[1, 9, 117, 1757, 28648], one-sided=[1, 9, 117, 1757, 28648], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #18 `e98412e7cb95aea2` — IT(152) P3_121, f=(32, 48, 18), p=3^4 4^6 6^2 8^6, aut=2

Witness point (0, 1/8, 1/6), c/a = 3/4, site stabilizer 2, orbit 3 conventional / 3 primitive, stratum dim 1. Open/wall label (triage, carried): open-likely (triage, 30 b). Candidate wall time 4.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(152) P3_121 p=(0, 1/8, 1/6) c/a=3/4 G=diag(16,16,9) period=24 n_conv=3 T=3 site=2 dim=1 f=(32,48,18) p-vec 3^4 4^6 6^2 8^6 aut=2 W=2 nonsimple=0 cutoff_D2=36864 4rho2_G=1776036/169 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.2s | detL=13824 T=3 vol=4608 T*vol=13824 (crystal-basis measure) slots=54 paired 1:1; disjointness G-ball D2=4rho2=1776036/169 (coord bound (30, 30, 35)), ball sizes 26..26 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 2.2s | audit re-derived 3 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 4608 each, T*vol == |det|; all 54 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 288 shared-vertex G-equidistance checks, 1728 vertex-side checks, 54 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.1s | tables T=3 nbrs=18 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 3 classes of the other hand; banked enumerate n<=4: fixed=[3, 27, 339, 4917], free=[1, 6, 61, 839]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[3, 27, 339, 4917, 77418], free=[1, 6, 61, 839, 12964], one-sided=[1, 6, 61, 839, 12964], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #19 `ac4489d658eb445e` — IT(178) P6_122, f=(36, 54, 20), p=4^13 5^2 6^1 9^2 10^1 12^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 797/1000, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 6 b). Candidate wall time 45.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(178) P6_122 p=(1/12, 3/8, 1/6) c/a=797/1000 G=diag(1000000,1000000,635209) period=24 n_conv=12 T=12 site=1 dim=3 f=(36,54,20) p-vec 4^13 5^2 6^1 9^2 10^1 12^1 aut=1 W=2 nonsimple=0 cutoff_D2=2304000000 4rho2_G=313390096 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 2.0s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=240 paired 1:1; disjointness G-ball D2=4rho2=313390096 (coord bound (21, 21, 23)), ball sizes 28..28 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 22.7s | audit re-derived 12 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 240 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1296 shared-vertex G-equidistance checks, 8640 vertex-side checks, 240 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 20.7s | tables T=12 nbrs=20 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 120, 1728, 28878], free=[1, 15, 144, 2476]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 120, 1728, 28878, 524988], free=[1, 15, 144, 2476, 43749], one-sided=[1, 15, 144, 2476, 43749], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 19s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #20 `c53bc05bc306c97d` — IT(166) R-3m, f=(31, 48, 19), p=3^4 4^8 5^4 8^2 16^1, aut=2

Witness point (1/12, 1/6, 11/24), c/a = 7/8, site stabilizer 2, orbit 18 conventional / 6 primitive, stratum dim 2. Open/wall label (triage, carried): open-likely (triage, 14 b). Candidate wall time 15.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(166) R-3m p=(1/12, 1/6, 11/24) c/a=7/8 G=diag(64,64,49) period=24 n_conv=18 T=6 site=2 dim=2 f=(31,48,19) p-vec 3^4 4^8 5^4 8^2 16^1 aut=2 W=2 nonsimple=3 cutoff_D2=147456 4rho2_G=26788 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.4s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=114 paired 1:1; disjointness G-ball D2=4rho2=26788 (coord bound (24, 24, 24)), ball sizes 66..66 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 4.9s | audit re-derived 6 cells x 19 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 114 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 576 shared-vertex G-equidistance checks, 3534 vertex-side checks, 114 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=1, improper=1; solid achiral), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 9.0s | tables T=6 nbrs=19 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: inconsistent (achiral solid); banked enumerate n<=4: fixed=[6, 57, 782, 12396], free=[1, 8, 70, 1082]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 57, 782, 12396, 213738], free=[1, 8, 70, 1082, 17881], one-sided=[1, 14, 131, 2125, 35623], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 8s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 1, solid achiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #21 `8cc8c5ab3cf36d8f` — IT(178) P6_122, f=(36, 54, 20), p=3^6 4^4 5^4 6^2 9^2 10^1 14^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 5/4, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b). Candidate wall time 39.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(178) P6_122 p=(1/12, 3/8, 1/6) c/a=5/4 G=diag(16,16,25) period=24 n_conv=12 T=12 site=1 dim=3 f=(36,54,20) p-vec 3^6 4^4 5^4 6^2 9^2 10^1 14^1 aut=1 W=2 nonsimple=0 cutoff_D2=57600 4rho2_G=808448/121 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 2.4s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=240 paired 1:1; disjointness G-ball D2=4rho2=808448/121 (coord bound (24, 24, 17)), ball sizes 30..30 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 17.2s | audit re-derived 12 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 240 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1296 shared-vertex G-equidistance checks, 8640 vertex-side checks, 240 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 19.8s | tables T=12 nbrs=20 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 120, 1704, 27900], free=[1, 14, 142, 2381]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 120, 1704, 27900, 495720], free=[1, 14, 142, 2381, 41310], one-sided=[1, 14, 142, 2381, 41310], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 18s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #22 `646b518ccf3bd724` — IT(169) P6_1, f=(36, 54, 20), p=3^6 4^4 5^2 6^4 7^2 13^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 15/16, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 6 b; metric-thin: P5-only). Candidate wall time 17.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(169) P6_1 p=(1/8, 1/6, 5/12) c/a=15/16 G=diag(256,256,225) period=24 n_conv=6 T=6 site=1 dim=3 f=(36,54,20) p-vec 3^6 4^4 5^2 6^4 7^2 13^2 aut=1 W=2 nonsimple=0 cutoff_D2=589824 4rho2_G=115188928/729 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=115188928/729 (coord bound (29, 29, 27)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 10.3s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 648 shared-vertex G-equidistance checks, 4320 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.5s | tables T=6 nbrs=20 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 852, 14106], free=[1, 10, 142, 2351]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 852, 14106, 254274], free=[1, 10, 142, 2351, 42379], one-sided=[1, 10, 142, 2351, 42379], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #23 `7a448bed1119dfad` — IT(178) P6_122, f=(36, 54, 20), p=3^2 4^10 5^2 6^2 8^2 12^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 1/2, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b). Candidate wall time 40.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(178) P6_122 p=(1/12, 3/8, 1/6) c/a=1/2 G=diag(4,4,1) period=24 n_conv=12 T=12 site=1 dim=3 f=(36,54,20) p-vec 3^2 4^10 5^2 6^2 8^2 12^2 aut=1 W=2 nonsimple=0 cutoff_D2=9216 4rho2_G=272320/243 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 2.8s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=240 paired 1:1; disjointness G-ball D2=4rho2=272320/243 (coord bound (20, 20, 34)), ball sizes 42..42 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 16.2s | audit re-derived 12 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 240 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1296 shared-vertex G-equidistance checks, 8640 vertex-side checks, 240 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 20.9s | tables T=12 nbrs=20 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 120, 1752, 29862], free=[1, 16, 146, 2571]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 120, 1752, 29862, 556392], free=[1, 16, 146, 2571, 46366], one-sided=[1, 16, 146, 2571, 46366], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 19s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #24 `7e023be581e7c50a` — IT(154) P3_221, f=(36, 54, 20), p=3^6 4^6 6^2 8^4 10^1 12^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 3/4, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b). Candidate wall time 16.4s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(154) P3_221 p=(1/8, 1/6, 5/12) c/a=3/4 G=diag(16,16,9) period=24 n_conv=6 T=6 site=1 dim=3 f=(36,54,20) p-vec 3^6 4^6 6^2 8^4 10^1 12^1 aut=1 W=2 nonsimple=0 cutoff_D2=36864 4rho2_G=3073733456/339889 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.7s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=3073733456/339889 (coord bound (28, 28, 32)), ball sizes 30..30 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 8.8s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 648 shared-vertex G-equidistance checks, 4320 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.7s | tables T=6 nbrs=20 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 840, 13611], free=[1, 12, 140, 2294]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 840, 13611, 239664], free=[1, 12, 140, 2294, 39944], one-sided=[1, 12, 140, 2294, 39944], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #25 `7e05ce00d8a7cbf6` — IT(178) P6_122, f=(38, 57, 21), p=3^4 4^8 5^2 6^3 8^2 12^1 14^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 137/160, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b; metric-thin: P5-only). Candidate wall time 52.4s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(178) P6_122 p=(1/12, 3/8, 1/6) c/a=137/160 G=diag(25600,25600,18769) period=24 n_conv=12 T=12 site=1 dim=3 f=(38,57,21) p-vec 3^4 4^8 5^2 6^3 8^2 12^1 14^1 aut=1 W=2 nonsimple=0 cutoff_D2=58982400 4rho2_G=8383888 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 2.1s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=252 paired 1:1; disjointness G-ball D2=4rho2=8383888 (coord bound (21, 21, 22)), ball sizes 30..30 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 27.2s | audit re-derived 12 cells x 21 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 252 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1368 shared-vertex G-equidistance checks, 9576 vertex-side checks, 252 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 22.8s | tables T=12 nbrs=21 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 126, 1872, 32196], free=[1, 15, 156, 2749]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 126, 1872, 32196, 602316], free=[1, 15, 156, 2749, 50193], one-sided=[1, 15, 156, 2749, 50193], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 21s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #26 `59b28b3a59c27092` — IT(155) R32, f=(34, 52, 20), p=3^8 4^2 5^2 6^4 8^3 14^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1277/2000, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 6 b; metric-thin: P5-only). Candidate wall time 17.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.4s | IT(155) R32 p=(1/8, 1/6, 5/12) c/a=1277/2000 G=diag(4000000,4000000,1630729) period=24 n_conv=18 T=6 site=1 dim=3 f=(34,52,20) p-vec 3^8 4^2 5^2 6^4 8^3 14^1 aut=1 W=2 nonsimple=2 cutoff_D2=9216000000 4rho2_G=131801557535764/140625 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.9s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=131801557535764/140625 (coord bound (18, 18, 24)), ball sizes 38..38 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 8.9s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 624 shared-vertex G-equidistance checks, 4080 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.5s | tables T=6 nbrs=20 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 848, 13917], free=[1, 14, 142, 2374]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 848, 13917, 248970], free=[1, 14, 142, 2374, 41495], one-sided=[1, 14, 142, 2374, 41495], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #27 `d9ac68100a276dfe` — IT(169) P6_1, f=(36, 54, 20), p=3^4 4^6 5^4 6^2 7^2 13^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 2777/4000, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 3 b; metric-thin: P5-only). Candidate wall time 21.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(169) P6_1 p=(1/8, 1/6, 5/12) c/a=2777/4000 G=diag(16000000,16000000,7711729) period=24 n_conv=6 T=6 site=1 dim=3 f=(36,54,20) p-vec 3^4 4^6 5^4 6^2 7^2 13^2 aut=1 W=2 nonsimple=0 cutoff_D2=36864000000 4rho2_G=10264647778612928459152996852/1167318032454421875 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.8s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=10264647778612928459152996852/1167318032454421875 (coord bound (28, 28, 34)), ball sizes 34..34 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 13.4s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 648 shared-vertex G-equidistance checks, 4320 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.8s | tables T=6 nbrs=20 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 852, 14028], free=[1, 10, 142, 2338]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 852, 14028, 251172], free=[1, 10, 142, 2338, 41862], one-sided=[1, 10, 142, 2338, 41862], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #28 `6f4101f83371033d` — IT(169) P6_1, f=(36, 54, 20), p=3^4 4^8 6^4 7^2 13^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 2331/4000, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b; metric-thin: P5-only). Candidate wall time 18.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(169) P6_1 p=(1/8, 1/6, 5/12) c/a=2331/4000 G=diag(16000000,16000000,5433561) period=24 n_conv=6 T=6 site=1 dim=3 f=(36,54,20) p-vec 3^4 4^8 6^4 7^2 13^2 aut=1 W=2 nonsimple=0 cutoff_D2=36864000000 4rho2_G=28122284764849574251854556/3384665139515625 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.8s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=28122284764849574251854556/3384665139515625 (coord bound (27, 27, 40)), ball sizes 34..34 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 11.7s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 648 shared-vertex G-equidistance checks, 4320 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.3s | tables T=6 nbrs=20 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 828, 13224], free=[1, 10, 138, 2204]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 828, 13224, 229620], free=[1, 10, 138, 2204, 38270], one-sided=[1, 10, 138, 2204, 38270], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #29 `f0b07b168368759b` — IT(148) R-3, f=(14, 24, 12), p=3^4 4^4 5^4, aut=4

Witness point (0, 1/2, 0), c/a = 3/4, site stabilizer 2, orbit 9 conventional / 3 primitive, stratum dim 0. Open/wall label (triage, carried): open-likely (triage, 41 b). Candidate wall time 1.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(148) R-3 p=(0, 1/2, 0) c/a=3/4 G=diag(16,16,9) period=12 n_conv=9 T=3 site=2 dim=0 f=(14,24,12) p-vec 3^4 4^4 5^4 aut=4 W=2 nonsimple=6 cutoff_D2=9216 4rho2_G=1344 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.1s | detL=576 T=3 vol=192 T*vol=576 (crystal-basis measure) slots=36 paired 1:1; disjointness G-ball D2=4rho2=1344 (coord bound (11, 11, 13)), ball sizes 26..26 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.1s | audit re-derived 3 cells x 12 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 192 each, T*vol == |det|; all 36 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 144 shared-vertex G-equidistance checks, 504 vertex-side checks, 36 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=4, Isom(solid)=4 (Isom+=2, improper=2; solid achiral), aut_comb=4; chain site<=Isom_fix (linear parts) contained, divisibility 2|4|4|4 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=6: full symmetry group of the honeycomb is LARGER than G (|H_cell|=4) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.0s | tables T=3 nbrs=12 |ops|=12 (6 proper, 6 improper; T*|site|=6), identity+closure exact; hands: inconsistent (achiral solid); banked enumerate n<=4: fixed=[3, 18, 158, 1596], free=[1, 3, 18, 147]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[3, 18, 158, 1596, 17523], free=[1, 3, 18, 147, 1503], one-sided=[1, 5, 30, 282, 2950], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 4 <= Isom(solid) 4 (Isom+ 2, solid achiral) <= combinatorial aut 4 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 6: the full symmetry group of the honeycomb is LARGER than G.

### #30 `56918d2cff883e22` — IT(148) R-3, f=(22, 34, 14), p=4^8 5^2 6^2 7^2, aut=2

Witness point (1/8, 1/6, 5/12), c/a = 1, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 49 b). Candidate wall time 4.4s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(148) R-3 p=(1/8, 1/6, 5/12) c/a=1 G=diag(2,2,2) period=24 n_conv=18 T=6 site=1 dim=3 f=(22,34,14) p-vec 4^8 5^2 6^2 7^2 aut=2 W=2 nonsimple=2 cutoff_D2=4608 4rho2_G=904 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.0s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=84 paired 1:1; disjointness G-ball D2=4rho2=904 (coord bound (25, 25, 22)), ball sizes 70..70 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.2s | audit re-derived 6 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 84 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 408 shared-vertex G-equidistance checks, 1848 vertex-side checks, 84 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (3 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.8s | tables T=6 nbrs=14 |ops|=6 (3 proper, 3 improper; T*|site|=6), identity+closure exact; hands: 3 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 42, 410, 4620], free=[1, 8, 69, 781]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 42, 410, 4620, 56520], free=[1, 8, 69, 781, 9420], one-sided=[2, 14, 138, 1540, 18840], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (3 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #31 `f429e996b3f455a6` — IT(148) R-3, f=(26, 40, 16), p=3^6 5^6 8^4, aut=2

Witness point (1/8, 1/6, 5/12), c/a = 3/4, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 16 b). Candidate wall time 7.1s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(148) R-3 p=(1/8, 1/6, 5/12) c/a=3/4 G=diag(16,16,9) period=24 n_conv=18 T=6 site=1 dim=3 f=(26,40,16) p-vec 3^6 5^6 8^4 aut=2 W=2 nonsimple=2 cutoff_D2=36864 4rho2_G=4432 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.3s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=96 paired 1:1; disjointness G-ball D2=4rho2=4432 (coord bound (20, 20, 23)), ball sizes 38..38 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 2.7s | audit re-derived 6 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 96 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 480 shared-vertex G-equidistance checks, 2496 vertex-side checks, 96 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (3 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.7s | tables T=6 nbrs=16 |ops|=6 (3 proper, 3 improper; T*|site|=6), identity+closure exact; hands: 3 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 48, 524, 6618], free=[1, 9, 88, 1116]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 48, 524, 6618, 90924], free=[1, 9, 88, 1116, 15154], one-sided=[2, 16, 176, 2206, 30308], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (3 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #32 `71d2c9953ca110b8` — IT(169) P6_1, f=(36, 54, 20), p=3^4 4^2 5^8 6^2 7^2 11^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 39/32, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b,P5-only). Candidate wall time 18.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(169) P6_1 p=(1/12, 3/8, 1/6) c/a=39/32 G=diag(1024,1024,1521) period=24 n_conv=6 T=6 site=1 dim=3 f=(36,54,20) p-vec 3^4 4^2 5^8 6^2 7^2 11^2 aut=1 W=2 nonsimple=0 cutoff_D2=3504384 4rho2_G=11534040315875/18852964 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.8s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=11534040315875/18852964 (coord bound (29, 29, 21)), ball sizes 30..30 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 10.9s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 648 shared-vertex G-equidistance checks, 4320 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.7s | tables T=6 nbrs=20 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 852, 14058], free=[1, 10, 142, 2343]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 852, 14058, 252336], free=[1, 10, 142, 2343, 42056], one-sided=[1, 10, 142, 2343, 42056], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #33 `8d90c524c89922d9` — IT(169) P6_1, f=(36, 54, 20), p=3^4 4^4 5^4 6^4 7^2 11^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 11/8, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b,P5-only). Candidate wall time 17.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(169) P6_1 p=(1/12, 3/8, 1/6) c/a=11/8 G=diag(64,64,121) period=24 n_conv=6 T=6 site=1 dim=3 f=(36,54,20) p-vec 3^4 4^4 5^4 6^4 7^2 11^2 aut=1 W=2 nonsimple=0 cutoff_D2=278784 4rho2_G=1196615144368/29451279 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.9s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=1196615144368/29451279 (coord bound (30, 30, 19)), ball sizes 28..28 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 9.9s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 648 shared-vertex G-equidistance checks, 4320 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.2s | tables T=6 nbrs=20 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 828, 13206], free=[1, 10, 138, 2201]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 828, 13206, 228816], free=[1, 10, 138, 2201, 38136], one-sided=[1, 10, 138, 2201, 38136], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #34 `9d4396ca0b08fc3c` — IT(166) R-3m, f=(19, 30, 13), p=4^8 5^4 8^1, aut=2

Witness point (1/24, 1/12, 1/12), c/a = 3/4, site stabilizer 2, orbit 18 conventional / 6 primitive, stratum dim 2. Open/wall label (triage, carried): open-likely (triage, 63 b). Candidate wall time 4.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(166) R-3m p=(1/24, 1/12, 1/12) c/a=3/4 G=diag(16,16,9) period=24 n_conv=18 T=6 site=2 dim=2 f=(19,30,13) p-vec 4^8 5^4 8^1 aut=2 W=2 nonsimple=3 cutoff_D2=36864 4rho2_G=4432 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.0s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=78 paired 1:1; disjointness G-ball D2=4rho2=4432 (coord bound (20, 20, 23)), ball sizes 44..44 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.7s | audit re-derived 6 cells x 13 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 78 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 360 shared-vertex G-equidistance checks, 1482 vertex-side checks, 78 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=1, improper=1; solid achiral), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.3s | tables T=6 nbrs=13 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: inconsistent (achiral solid); banked enumerate n<=4: fixed=[6, 39, 356, 3777], free=[1, 6, 33, 341]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 39, 356, 3777, 43602], free=[1, 6, 33, 341, 3665], one-sided=[1, 10, 60, 660, 7267], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 1, solid achiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #35 `07d543d89e2934f2` — IT(152) P3_121, f=(36, 54, 20), p=3^6 4^4 5^2 6^4 10^4, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 33/32, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): indeterminate (triage, 2 b; metric-thin: P5-only). Candidate wall time 16.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(152) P3_121 p=(1/8, 1/6, 5/12) c/a=33/32 G=diag(1024,1024,1089) period=24 n_conv=6 T=6 site=1 dim=3 f=(36,54,20) p-vec 3^6 4^4 5^2 6^4 10^4 aut=1 W=2 nonsimple=0 cutoff_D2=2509056 4rho2_G=145258996/225 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=145258996/225 (coord bound (29, 29, 25)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 9.2s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 648 shared-vertex G-equidistance checks, 4320 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.7s | tables T=6 nbrs=20 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 840, 13713], free=[1, 12, 140, 2313]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 840, 13713, 244062], free=[1, 12, 140, 2313, 40677], one-sided=[1, 12, 140, 2313, 40677], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #36 `2081d7b9a734e4fe` — IT(155) R32, f=(32, 50, 20), p=3^6 4^4 5^4 6^4 10^1 12^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 11/8, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b,P5-only). Candidate wall time 15.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.4s | IT(155) R32 p=(1/8, 1/6, 5/12) c/a=11/8 G=diag(64,64,121) period=24 n_conv=18 T=6 site=1 dim=3 f=(32,50,20) p-vec 3^6 4^4 5^4 6^4 10^1 12^1 aut=1 W=2 nonsimple=4 cutoff_D2=278784 4rho2_G=35984 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.8s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=35984 (coord bound (28, 28, 18)), ball sizes 59..59 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.5s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 600 shared-vertex G-equidistance checks, 3840 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 7.5s | tables T=6 nbrs=20 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 888, 15330], free=[1, 12, 150, 2584]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 888, 15330, 288180], free=[1, 12, 150, 2584, 48030], one-sided=[1, 12, 150, 2584, 48030], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 7s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #37 `257b627a90b78038` — IT(180) P6_222, f=(22, 35, 15), p=3^4 4^6 6^3 8^2, aut=2

Witness point (1/6, 7/12, 1/6), c/a = 1, site stabilizer 2, orbit 6 conventional / 6 primitive, stratum dim 1. Open/wall label (triage, carried): open-likely (triage, 24 b). Candidate wall time 5.5s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(180) P6_222 p=(1/6, 7/12, 1/6) c/a=1 G=diag(2,2,2) period=12 n_conv=6 T=6 site=2 dim=1 f=(22,35,15) p-vec 3^4 4^6 6^3 8^2 aut=2 W=2 nonsimple=4 cutoff_D2=1152 4rho2_G=344 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.3s | detL=1728 T=6 vol=288 T*vol=1728 (crystal-basis measure) slots=90 paired 1:1; disjointness G-ball D2=4rho2=344 (coord bound (16, 16, 14)), ball sizes 41..41 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.2s | audit re-derived 6 cells x 15 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 288 each, T*vol == |det|; all 90 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 420 shared-vertex G-equidistance checks, 1980 vertex-side checks, 90 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.8s | tables T=6 nbrs=15 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 45, 474, 5871], free=[1, 7, 43, 523]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 45, 474, 5871, 79614], free=[1, 7, 43, 523, 6675], one-sided=[1, 7, 43, 523, 6675], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #38 `3ddc41389e6d484f` — IT(171) P6_2, f=(32, 48, 18), p=3^6 4^2 5^2 6^3 7^2 9^2 10^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 8 b). Candidate wall time 10.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(171) P6_2 p=(1/8, 1/6, 5/12) c/a=1 G=diag(2,2,2) period=24 n_conv=6 T=6 site=1 dim=3 f=(32,48,18) p-vec 3^6 4^2 5^2 6^3 7^2 9^2 10^1 aut=1 W=3 nonsimple=0 cutoff_D2=4608 4rho2_G=1818811/1536 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=108 paired 1:1; disjointness G-ball D2=4rho2=1818811/1536 (coord bound (29, 29, 25)), ball sizes 30..30 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.0s | audit re-derived 6 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 108 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 576 shared-vertex G-equidistance checks, 3456 vertex-side checks, 108 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 4.5s | tables T=6 nbrs=18 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 54, 690, 10263], free=[1, 11, 115, 1734]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 54, 690, 10263, 166248], free=[1, 11, 115, 1734, 27708], one-sided=[1, 11, 115, 1734, 27708], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #39 `64203f15fcf6c09b` — IT(155) R32, f=(20, 32, 14), p=3^4 4^4 5^2 6^2 7^2, aut=2

Witness point (0, 1/24, 0), c/a = 1/2, site stabilizer 2, orbit 9 conventional / 3 primitive, stratum dim 1. Open/wall label (triage, carried): open-likely (triage, 23 b). Candidate wall time 2.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(155) R32 p=(0, 1/24, 0) c/a=1/2 G=diag(4,4,1) period=24 n_conv=9 T=3 site=2 dim=1 f=(20,32,14) p-vec 3^4 4^4 5^2 6^2 7^2 aut=2 W=2 nonsimple=4 cutoff_D2=9216 4rho2_G=511312/441 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.5s | detL=4608 T=3 vol=1536 T*vol=4608 (crystal-basis measure) slots=42 paired 1:1; disjointness G-ball D2=4rho2=511312/441 (coord bound (20, 20, 35)), ball sizes 42..42 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.4s | audit re-derived 3 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1536 each, T*vol == |det|; all 42 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 192 shared-vertex G-equidistance checks, 840 vertex-side checks, 42 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.2s | tables T=3 nbrs=14 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 3 classes of the other hand; banked enumerate n<=4: fixed=[3, 21, 217, 2613], free=[1, 6, 40, 461]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[3, 21, 217, 2613, 34221], free=[1, 6, 40, 461, 5744], one-sided=[1, 6, 40, 461, 5744], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #40 `d718e083bd23d2b1` — IT(178) P6_122, f=(32, 48, 18), p=4^13 8^4 12^1, aut=4

Witness point (1/12, 3/8, 1/6), c/a = 1, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b). Candidate wall time 26.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(178) P6_122 p=(1/12, 3/8, 1/6) c/a=1 G=diag(2,2,2) period=24 n_conv=12 T=12 site=1 dim=3 f=(32,48,18) p-vec 4^13 8^4 12^1 aut=4 W=2 nonsimple=0 cutoff_D2=4608 4rho2_G=19112/27 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.6s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=216 paired 1:1; disjointness G-ball D2=4rho2=19112/27 (coord bound (22, 22, 19)), ball sizes 27..27 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 9.7s | audit re-derived 12 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 216 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1152 shared-vertex G-equidistance checks, 6912 vertex-side checks, 216 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=4; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|4 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 15.4s | tables T=12 nbrs=18 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 108, 1452, 22434], free=[1, 13, 121, 1920]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 108, 1452, 22434, 375288], free=[1, 13, 121, 1920, 31274], one-sided=[1, 13, 121, 1920, 31274], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 14s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 4 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #41 `f14a8c4e7c5b3e3a` — IT(180) P6_222, f=(32, 48, 18), p=3^6 4^2 5^2 6^4 8^2 10^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 7/4, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 10 b). Candidate wall time 27.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.6s | IT(180) P6_222 p=(1/8, 1/6, 5/12) c/a=7/4 G=diag(16,16,49) period=24 n_conv=12 T=12 site=1 dim=3 f=(32,48,18) p-vec 3^6 4^2 5^2 6^4 8^2 10^2 aut=1 W=3 nonsimple=0 cutoff_D2=112896 4rho2_G=28687/3 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 3.4s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=216 paired 1:1; disjointness G-ball D2=4rho2=28687/3 (coord bound (29, 29, 14)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 9.4s | audit re-derived 12 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 216 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1152 shared-vertex G-equidistance checks, 6912 vertex-side checks, 216 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 14.3s | tables T=12 nbrs=18 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 108, 1356, 19782], free=[1, 14, 113, 1708]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 108, 1356, 19782, 314328], free=[1, 14, 113, 1708, 26194], one-sided=[1, 14, 113, 1708, 26194], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 13s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #42 `29bbba1adec778da` — IT(171) P6_2, f=(28, 42, 16), p=3^2 4^4 5^4 6^3 7^2 10^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 5/4, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 15 b). Candidate wall time 6.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(171) P6_2 p=(1/8, 1/6, 5/12) c/a=5/4 G=diag(16,16,25) period=24 n_conv=6 T=6 site=1 dim=3 f=(28,42,16) p-vec 3^2 4^4 5^4 6^3 7^2 10^1 aut=1 W=3 nonsimple=0 cutoff_D2=57600 4rho2_G=2939563/300 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=96 paired 1:1; disjointness G-ball D2=4rho2=2939563/300 (coord bound (29, 29, 20)), ball sizes 26..26 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 2.7s | audit re-derived 6 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 96 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 504 shared-vertex G-equidistance checks, 2688 vertex-side checks, 96 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.7s | tables T=6 nbrs=16 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 48, 540, 7074], free=[1, 10, 90, 1200]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 48, 540, 7074, 100914], free=[1, 10, 90, 1200, 16819], one-sided=[1, 10, 90, 1200, 16819], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #43 `66563d07a1110a25` — IT(154) P3_221, f=(36, 54, 20), p=3^8 4^2 6^5 8^2 10^3, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 15.5s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(154) P3_221 p=(1/8, 1/6, 5/12) c/a=1 G=diag(2,2,2) period=24 n_conv=6 T=6 site=1 dim=3 f=(36,54,20) p-vec 3^8 4^2 6^5 8^2 10^3 aut=1 W=2 nonsimple=0 cutoff_D2=4608 4rho2_G=2164837/1682 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.5s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=120 paired 1:1; disjointness G-ball D2=4rho2=2164837/1682 (coord bound (30, 30, 26)), ball sizes 38..38 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 8.0s | audit re-derived 6 cells x 20 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 120 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 648 shared-vertex G-equidistance checks, 4320 vertex-side checks, 120 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.8s | tables T=6 nbrs=20 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 60, 852, 14112], free=[1, 12, 142, 2378]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 60, 852, 14112, 254820], free=[1, 12, 142, 2378, 42470], one-sided=[1, 12, 142, 2378, 42470], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #44 `ce3b42c8a4ceff6f` — IT(151) P3_112, f=(34, 51, 19), p=3^6 4^6 6^2 8^3 12^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1/2, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 6 b). Candidate wall time 13.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(151) P3_112 p=(1/8, 1/6, 5/12) c/a=1/2 G=diag(4,4,1) period=24 n_conv=6 T=6 site=1 dim=3 f=(34,51,19) p-vec 3^6 4^6 6^2 8^3 12^2 aut=1 W=2 nonsimple=0 cutoff_D2=9216 4rho2_G=279200/121 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.9s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=114 paired 1:1; disjointness G-ball D2=4rho2=279200/121 (coord bound (28, 28, 49)), ball sizes 58..58 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.8s | audit re-derived 6 cells x 19 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 114 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 612 shared-vertex G-equidistance checks, 3876 vertex-side checks, 114 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.0s | tables T=6 nbrs=19 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 57, 774, 12159], free=[1, 14, 129, 2086]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 57, 774, 12159, 207354], free=[1, 14, 129, 2086, 34559], one-sided=[1, 14, 129, 2086, 34559], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #45 `7b9cfe26fe4a9c4b` — IT(146) R3, f=(18, 30, 14), p=3^4 4^6 6^4, aut=2

Witness point (1/8, 1/6, 5/12), c/a = 5/4, site stabilizer 1, orbit 9 conventional / 3 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 32 b). Candidate wall time 1.5s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(146) R3 p=(1/8, 1/6, 5/12) c/a=5/4 G=diag(16,16,25) period=24 n_conv=9 T=3 site=1 dim=3 f=(18,30,14) p-vec 3^4 4^6 6^4 aut=2 W=2 nonsimple=6 cutoff_D2=57600 4rho2_G=235904/25 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.4s | detL=4608 T=3 vol=1536 T*vol=4608 (crystal-basis measure) slots=42 paired 1:1; disjointness G-ball D2=4rho2=235904/25 (coord bound (29, 29, 20)), ball sizes 40..40 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.3s | audit re-derived 3 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1536 each, T*vol == |det|; all 42 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 180 shared-vertex G-equidistance checks, 756 vertex-side checks, 42 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=3 (0 improper) vs T*|site|=3: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 0.7s | tables T=3 nbrs=14 |ops|=3 (3 proper, 0 improper; T*|site|=3), identity+closure exact; hands: 0 of 3 classes of the other hand; banked enumerate n<=4: fixed=[3, 21, 213, 2517], free=[1, 7, 73, 839]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[3, 21, 213, 2517, 32355], free=[1, 7, 73, 839, 10785], one-sided=[1, 7, 73, 839, 10785], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 3 (0 improper) vs T*|site| = 3: the full symmetry group of the honeycomb IS exactly the generating group G.

### #46 `2b9726574a0a8bed` — IT(171) P6_2, f=(30, 45, 17), p=3^4 4^4 5^2 6^1 7^4 9^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1/2, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 9 b). Candidate wall time 8.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(171) P6_2 p=(1/8, 1/6, 5/12) c/a=1/2 G=diag(4,4,1) period=24 n_conv=6 T=6 site=1 dim=3 f=(30,45,17) p-vec 3^4 4^4 5^2 6^1 7^4 9^2 aut=1 W=2 nonsimple=0 cutoff_D2=9216 4rho2_G=538649404/275427 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.7s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=102 paired 1:1; disjointness G-ball D2=4rho2=538649404/275427 (coord bound (26, 26, 45)), ball sizes 39..39 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 3.7s | audit re-derived 6 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 102 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 540 shared-vertex G-equidistance checks, 3060 vertex-side checks, 102 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.8s | tables T=6 nbrs=17 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 51, 612, 8517], free=[1, 10, 102, 1436]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 51, 612, 8517, 128826], free=[1, 10, 102, 1436, 21471], one-sided=[1, 10, 102, 1436, 21471], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #47 `f07d69523ef41b37` — IT(178) P6_122, f=(20, 36, 18), p=3^10 4^4 5^2 8^2, aut=2

Witness point (1/6, 1/3, 1/4), c/a = 3/2, site stabilizer 2, orbit 6 conventional / 6 primitive, stratum dim 1. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 10.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(178) P6_122 p=(1/6, 1/3, 1/4) c/a=3/2 G=diag(4,4,9) period=12 n_conv=6 T=6 site=2 dim=1 f=(20,36,18) p-vec 3^10 4^4 5^2 8^2 aut=2 W=2 nonsimple=12 cutoff_D2=5184 4rho2_G=720 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.5s | detL=1728 T=6 vol=288 T*vol=1728 (crystal-basis measure) slots=108 paired 1:1; disjointness G-ball D2=4rho2=720 (coord bound (16, 16, 9)), ball sizes 34..34 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.9s | audit re-derived 6 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 288 each, T*vol == |det|; all 108 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 432 shared-vertex G-equidistance checks, 2160 vertex-side checks, 108 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 8.7s | tables T=6 nbrs=18 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 54, 726, 11292], free=[1, 6, 65, 961]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 54, 726, 11292, 190698], free=[1, 6, 65, 961, 15958], one-sided=[1, 6, 65, 961, 15958], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 8s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #48 `16025e0680843c36` — IT(169) P6_1, f=(32, 48, 18), p=3^2 4^4 5^8 6^2 11^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 7 b). Candidate wall time 12.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(169) P6_1 p=(1/8, 1/6, 5/12) c/a=1 G=diag(2,2,2) period=24 n_conv=6 T=6 site=1 dim=3 f=(32,48,18) p-vec 3^2 4^4 5^8 6^2 11^2 aut=1 W=2 nonsimple=0 cutoff_D2=4608 4rho2_G=10288403408/8137827 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=108 paired 1:1; disjointness G-ball D2=4rho2=10288403408/8137827 (coord bound (30, 30, 26)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 6.6s | audit re-derived 6 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 108 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 576 shared-vertex G-equidistance checks, 3456 vertex-side checks, 108 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 4.8s | tables T=6 nbrs=18 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 54, 702, 10656], free=[1, 9, 117, 1776]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 54, 702, 10656, 176088], free=[1, 9, 117, 1776, 29348], one-sided=[1, 9, 117, 1776, 29348], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #49 `d10bb4a25bbf4c80` — IT(154) P3_221, f=(32, 48, 18), p=3^6 4^2 5^4 7^2 8^2 10^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 797/1000, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 6 b). Candidate wall time 13.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(154) P3_221 p=(1/8, 1/6, 5/12) c/a=797/1000 G=diag(1000000,1000000,635209) period=24 n_conv=6 T=6 site=1 dim=3 f=(32,48,18) p-vec 3^6 4^2 5^4 7^2 8^2 10^2 aut=1 W=2 nonsimple=0 cutoff_D2=2304000000 4rho2_G=17652762004838821145863504/30361015097015625 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.7s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=108 paired 1:1; disjointness G-ball D2=4rho2=17652762004838821145863504/30361015097015625 (coord bound (28, 28, 31)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 8.2s | audit re-derived 6 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 108 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 576 shared-vertex G-equidistance checks, 3456 vertex-side checks, 108 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 4.1s | tables T=6 nbrs=18 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 54, 678, 9852], free=[1, 11, 113, 1665]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 54, 678, 9852, 155712], free=[1, 11, 113, 1665, 25952], one-sided=[1, 11, 113, 1665, 25952], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #50 `e0bf1a48f096c10d` — IT(180) P6_222, f=(32, 48, 18), p=4^8 5^6 6^2 10^1 12^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 6 b). Candidate wall time 28.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(180) P6_222 p=(1/8, 1/6, 5/12) c/a=1 G=diag(2,2,2) period=24 n_conv=12 T=12 site=1 dim=3 f=(32,48,18) p-vec 4^8 5^6 6^2 10^1 12^1 aut=1 W=2 nonsimple=0 cutoff_D2=4608 4rho2_G=81128/75 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.8s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=216 paired 1:1; disjointness G-ball D2=4rho2=81128/75 (coord bound (27, 27, 24)), ball sizes 46..46 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 10.0s | audit re-derived 12 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 216 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1152 shared-vertex G-equidistance checks, 6912 vertex-side checks, 216 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 16.2s | tables T=12 nbrs=18 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 108, 1452, 23283], free=[1, 15, 121, 2015]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 108, 1452, 23283, 410268], free=[1, 15, 121, 2015, 34189], one-sided=[1, 15, 121, 2015, 34189], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 15s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #51 `b2430fc4bea4e06d` — IT(154) P3_221, f=(34, 51, 19), p=3^8 4^2 5^2 6^2 8^3 12^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1/2, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 3 b). Candidate wall time 12.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(154) P3_221 p=(1/8, 1/6, 5/12) c/a=1/2 G=diag(4,4,1) period=24 n_conv=6 T=6 site=1 dim=3 f=(34,51,19) p-vec 3^8 4^2 5^2 6^2 8^3 12^2 aut=1 W=2 nonsimple=0 cutoff_D2=9216 4rho2_G=1957456/981 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.8s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=114 paired 1:1; disjointness G-ball D2=4rho2=1957456/981 (coord bound (26, 26, 45)), ball sizes 37..37 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 6.3s | audit re-derived 6 cells x 19 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 114 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 612 shared-vertex G-equidistance checks, 3876 vertex-side checks, 114 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 4.9s | tables T=6 nbrs=19 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 57, 762, 11742], free=[1, 12, 127, 1989]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 57, 762, 11742, 196488], free=[1, 12, 127, 1989, 32748], one-sided=[1, 12, 127, 1989, 32748], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 5s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #52 `bff9b24ce78050f5` — IT(144) P3_1, f=(28, 42, 16), p=4^8 5^4 8^4, aut=2

Witness point (1/8, 1/6, 5/12), c/a = 1, site stabilizer 1, orbit 3 conventional / 3 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 9 b). Candidate wall time 2.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.0s | IT(144) P3_1 p=(1/8, 1/6, 5/12) c/a=1 G=diag(2,2,2) period=24 n_conv=3 T=3 site=1 dim=3 f=(28,42,16) p-vec 4^8 5^4 8^4 aut=2 W=2 nonsimple=0 cutoff_D2=4608 4rho2_G=44342995/31104 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.2s | detL=13824 T=3 vol=4608 T*vol=13824 (crystal-basis measure) slots=48 paired 1:1; disjointness G-ball D2=4rho2=44342995/31104 (coord bound (31, 31, 27)), ball sizes 22..22 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.5s | audit re-derived 3 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 4608 each, T*vol == |det|; all 48 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 252 shared-vertex G-equidistance checks, 1344 vertex-side checks, 48 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=3 (0 improper) vs T*|site|=3: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.1s | tables T=3 nbrs=16 |ops|=3 (3 proper, 0 improper; T*|site|=3), identity+closure exact; hands: 0 of 3 classes of the other hand; banked enumerate n<=4: fixed=[3, 24, 276, 3690], free=[1, 8, 92, 1230]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[3, 24, 276, 3690, 53577], free=[1, 8, 92, 1230, 17859], one-sided=[1, 8, 92, 1230, 17859], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 3 (0 improper) vs T*|site| = 3: the full symmetry group of the honeycomb IS exactly the generating group G.

### #53 `4db369a636f4396b` — IT(151) P3_112, f=(18, 30, 14), p=3^4 4^6 6^4, aut=4

Witness point (0, 1/2, 0), c/a = 3/2, site stabilizer 2, orbit 3 conventional / 3 primitive, stratum dim 1. Open/wall label (triage, carried): indeterminate (triage, 2 b). Candidate wall time 1.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.0s | IT(151) P3_112 p=(0, 1/2, 0) c/a=3/2 G=diag(4,4,9) period=12 n_conv=3 T=3 site=2 dim=1 f=(18,30,14) p-vec 3^4 4^6 6^4 aut=4 W=2 nonsimple=6 cutoff_D2=5184 4rho2_G=768 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.1s | detL=1728 T=3 vol=576 T*vol=1728 (crystal-basis measure) slots=42 paired 1:1; disjointness G-ball D2=4rho2=768 (coord bound (16, 16, 10)), ball sizes 18..18 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.2s | audit re-derived 3 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 576 each, T*vol == |det|; all 42 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 180 shared-vertex G-equidistance checks, 756 vertex-side checks, 42 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=2, Isom_fix_site=4, Isom(solid)=4 (Isom+=4, improper=0; solid CHIRAL), aut_comb=4; chain site<=Isom_fix (linear parts) contained, divisibility 2|4|4|4 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb is LARGER than G (|H_cell|=4) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.4s | tables T=3 nbrs=14 |ops|=12 (12 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 3 classes of the other hand; banked enumerate n<=4: fixed=[3, 21, 201, 2208], free=[1, 4, 22, 205]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[3, 21, 201, 2208, 26310], free=[1, 4, 22, 205, 2248], one-sided=[1, 4, 22, 205, 2248], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 4 <= Isom(solid) 4 (Isom+ 4, solid chiral) <= combinatorial aut 4 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb is LARGER than G.

### #54 `042c19cbfdc869cb` — IT(178) P6_122, f=(32, 48, 18), p=3^6 4^2 5^2 6^2 7^2 8^3 10^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 3/2, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b). Candidate wall time 25.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(178) P6_122 p=(1/8, 1/6, 5/12) c/a=3/2 G=diag(4,4,9) period=24 n_conv=12 T=12 site=1 dim=3 f=(32,48,18) p-vec 3^6 4^2 5^2 6^2 7^2 8^3 10^1 aut=1 W=2 nonsimple=0 cutoff_D2=20736 4rho2_G=325168/147 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 2.7s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=216 paired 1:1; disjointness G-ball D2=4rho2=325168/147 (coord bound (28, 28, 16)), ball sizes 29..29 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 9.1s | audit re-derived 12 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 216 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1152 shared-vertex G-equidistance checks, 6912 vertex-side checks, 216 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 13.7s | tables T=12 nbrs=18 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 108, 1380, 20472], free=[1, 12, 115, 1743]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 108, 1380, 20472, 330216], free=[1, 12, 115, 1743, 27518], one-sided=[1, 12, 115, 1743, 27518], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 13s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #55 `23594bd7053503aa` — IT(153) P3_212, f=(32, 48, 18), p=3^6 4^2 5^2 6^3 7^2 8^1 10^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b). Candidate wall time 10.1s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(153) P3_212 p=(1/8, 1/6, 5/12) c/a=1 G=diag(2,2,2) period=24 n_conv=6 T=6 site=1 dim=3 f=(32,48,18) p-vec 3^6 4^2 5^2 6^3 7^2 8^1 10^2 aut=1 W=2 nonsimple=0 cutoff_D2=4608 4rho2_G=1384088/1083 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=108 paired 1:1; disjointness G-ball D2=4rho2=1384088/1083 (coord bound (30, 30, 26)), ball sizes 38..38 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.0s | audit re-derived 6 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 108 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 576 shared-vertex G-equidistance checks, 3456 vertex-side checks, 108 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 4.4s | tables T=6 nbrs=18 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 54, 690, 10266], free=[1, 13, 115, 1759]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 54, 690, 10266, 166176], free=[1, 13, 115, 1759, 27696], one-sided=[1, 13, 115, 1759, 27696], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #56 `f5fbebffa76808d5` — IT(179) P6_522, f=(31, 47, 18), p=3^3 4^2 5^7 6^3 7^2 10^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 5/4, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b). Candidate wall time 26.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(179) P6_522 p=(1/12, 3/8, 1/6) c/a=5/4 G=diag(16,16,25) period=24 n_conv=12 T=12 site=1 dim=3 f=(31,47,18) p-vec 3^3 4^2 5^7 6^3 7^2 10^1 aut=1 W=2 nonsimple=1 cutoff_D2=57600 4rho2_G=11822848/1369 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 2.0s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=216 paired 1:1; disjointness G-ball D2=4rho2=11822848/1369 (coord bound (27, 27, 19)), ball sizes 39..39 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 9.2s | audit re-derived 12 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 216 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1128 shared-vertex G-equidistance checks, 6696 vertex-side checks, 216 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 15.2s | tables T=12 nbrs=18 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 108, 1428, 22200], free=[1, 13, 119, 1901]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 108, 1428, 22200, 377472], free=[1, 13, 119, 1901, 31456], one-sided=[1, 13, 119, 1901, 31456], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 14s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #57 `057255f61286b052` — IT(167) R-3c, f=(24, 38, 16), p=3^6 4^2 6^6 7^2, aut=2

Witness point (0, 3/8, 1/4), c/a = 1/2, site stabilizer 2, orbit 18 conventional / 6 primitive, stratum dim 1. Open/wall label (triage, carried): open-likely (triage, 7 b). Candidate wall time 8.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(167) R-3c p=(0, 3/8, 1/4) c/a=1/2 G=diag(4,4,1) period=24 n_conv=18 T=6 site=2 dim=1 f=(24,38,16) p-vec 3^6 4^2 6^6 7^2 aut=2 W=2 nonsimple=4 cutoff_D2=9216 4rho2_G=976 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.7s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=96 paired 1:1; disjointness G-ball D2=4rho2=976 (coord bound (19, 19, 32)), ball sizes 46..46 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.6s | audit re-derived 6 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 96 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 456 shared-vertex G-equidistance checks, 2304 vertex-side checks, 96 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 5.2s | tables T=6 nbrs=16 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: 3 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 48, 556, 7536], free=[1, 6, 51, 652]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 48, 556, 7536, 111324], free=[1, 6, 51, 652, 9329], one-sided=[2, 11, 102, 1290, 18658], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 5s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #58 `e198aac88f223892` — IT(153) P3_212, f=(30, 45, 17), p=3^2 4^5 5^4 6^4 10^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 3/4, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 12 b). Candidate wall time 9.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(153) P3_212 p=(1/8, 1/6, 5/12) c/a=3/4 G=diag(16,16,9) period=24 n_conv=6 T=6 site=1 dim=3 f=(30,45,17) p-vec 3^2 4^5 5^4 6^4 10^2 aut=1 W=2 nonsimple=0 cutoff_D2=36864 4rho2_G=2798800/289 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=102 paired 1:1; disjointness G-ball D2=4rho2=2798800/289 (coord bound (29, 29, 33)), ball sizes 43..43 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 4.1s | audit re-derived 6 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 102 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 540 shared-vertex G-equidistance checks, 3060 vertex-side checks, 102 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 4.2s | tables T=6 nbrs=17 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 51, 624, 8898], free=[1, 13, 104, 1535]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 51, 624, 8898, 138078], free=[1, 13, 104, 1535, 23013], one-sided=[1, 13, 104, 1535, 23013], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #59 `d07f950b8309de82` — IT(171) P6_2, f=(30, 45, 17), p=3^4 4^3 5^2 6^5 8^2 10^1, aut=2

Witness point (1/8, 1/6, 5/12), c/a = 67/80, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b; metric-thin: P5-only). Candidate wall time 10.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(171) P6_2 p=(1/8, 1/6, 5/12) c/a=67/80 G=diag(6400,6400,4489) period=24 n_conv=6 T=6 site=1 dim=3 f=(30,45,17) p-vec 3^4 4^3 5^2 6^5 8^2 10^1 aut=2 W=2 nonsimple=0 cutoff_D2=14745600 4rho2_G=37109681000872768/10310671875 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.7s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=102 paired 1:1; disjointness G-ball D2=4rho2=37109681000872768/10310671875 (coord bound (28, 28, 29)), ball sizes 26..26 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.6s | audit re-derived 6 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 102 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 540 shared-vertex G-equidistance checks, 3060 vertex-side checks, 102 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.5s | tables T=6 nbrs=17 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 51, 612, 8526], free=[1, 10, 102, 1438]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 51, 612, 8526, 129030], free=[1, 10, 102, 1438, 21505], one-sided=[1, 10, 102, 1438, 21505], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #60 `a182e87006c7a00d` — IT(179) P6_522, f=(32, 48, 18), p=3^6 4^1 5^2 6^3 7^2 8^4, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 3/2, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b). Candidate wall time 26.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(179) P6_522 p=(1/8, 1/6, 5/12) c/a=3/2 G=diag(4,4,9) period=24 n_conv=12 T=12 site=1 dim=3 f=(32,48,18) p-vec 3^6 4^1 5^2 6^3 7^2 8^4 aut=1 W=2 nonsimple=0 cutoff_D2=20736 4rho2_G=58288/25 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 3.0s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=216 paired 1:1; disjointness G-ball D2=4rho2=58288/25 (coord bound (28, 28, 17)), ball sizes 38..38 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 9.5s | audit re-derived 12 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 216 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1152 shared-vertex G-equidistance checks, 6912 vertex-side checks, 216 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 13.3s | tables T=12 nbrs=18 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 108, 1356, 19674], free=[1, 12, 113, 1677]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 108, 1356, 19674, 310224], free=[1, 12, 113, 1677, 25852], one-sided=[1, 12, 113, 1677, 25852], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 12s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #61 `a46cbaad3c23e834` — IT(155) R32, f=(32, 49, 19), p=3^4 4^8 5^2 6^2 8^1 10^1 14^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1/2, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): indeterminate (triage, 2 b). Candidate wall time 12.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.4s | IT(155) R32 p=(1/8, 1/6, 5/12) c/a=1/2 G=diag(4,4,1) period=24 n_conv=18 T=6 site=1 dim=3 f=(32,49,19) p-vec 3^4 4^8 5^2 6^2 8^1 10^1 14^1 aut=1 W=2 nonsimple=2 cutoff_D2=9216 4rho2_G=7072/9 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 2.0s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=114 paired 1:1; disjointness G-ball D2=4rho2=7072/9 (coord bound (17, 17, 29)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.0s | audit re-derived 6 cells x 19 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 114 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 588 shared-vertex G-equidistance checks, 3648 vertex-side checks, 114 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 5.2s | tables T=6 nbrs=19 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 57, 770, 12018], free=[1, 14, 129, 2061]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 57, 770, 12018, 203934], free=[1, 14, 129, 2061, 33989], one-sided=[1, 14, 129, 2061, 33989], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 5s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #62 `dd3fb07fe11d73d3` — IT(179) P6_522, f=(31, 47, 18), p=3^4 4^7 6^3 7^2 10^1 12^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 2, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b). Candidate wall time 27.4s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.4s | IT(179) P6_522 p=(1/12, 3/8, 1/6) c/a=2 G=diag(2,2,8) period=24 n_conv=12 T=12 site=1 dim=3 f=(31,47,18) p-vec 3^4 4^7 6^3 7^2 10^1 12^1 aut=1 W=2 nonsimple=1 cutoff_D2=18432 4rho2_G=3848/3 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 4.2s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=216 paired 1:1; disjointness G-ball D2=4rho2=3848/3 (coord bound (30, 30, 13)), ball sizes 41..41 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 8.8s | audit re-derived 12 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 216 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1128 shared-vertex G-equidistance checks, 6696 vertex-side checks, 216 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 13.9s | tables T=12 nbrs=18 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 108, 1404, 21318], free=[1, 11, 117, 1802]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 108, 1404, 21318, 353136], free=[1, 11, 117, 1802, 29428], one-sided=[1, 11, 117, 1802, 29428], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 13s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #63 `36c92427e3d084dc` — IT(166) R-3m, f=(19, 30, 13), p=3^4 4^4 5^2 7^2 8^1, aut=2

Witness point (1/12, 1/6, 11/24), c/a = 5/4, site stabilizer 2, orbit 18 conventional / 6 primitive, stratum dim 2. Open/wall label (triage, carried): open-likely (triage, 16 b). Candidate wall time 4.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(166) R-3m p=(1/12, 1/6, 11/24) c/a=5/4 G=diag(16,16,25) period=24 n_conv=18 T=6 site=2 dim=2 f=(19,30,13) p-vec 3^4 4^4 5^2 7^2 8^1 aut=2 W=2 nonsimple=3 cutoff_D2=57600 4rho2_G=9412 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.1s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=78 paired 1:1; disjointness G-ball D2=4rho2=9412 (coord bound (29, 29, 20)), ball sizes 73..73 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.7s | audit re-derived 6 cells x 13 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 78 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 360 shared-vertex G-equidistance checks, 1482 vertex-side checks, 78 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=1, improper=1; solid achiral), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.1s | tables T=6 nbrs=13 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: inconsistent (achiral solid); banked enumerate n<=4: fixed=[6, 39, 364, 3924], free=[1, 6, 34, 353]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 39, 364, 3924, 45918], free=[1, 6, 34, 353, 3858], one-sided=[1, 9, 62, 675, 7653], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 1, solid achiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #64 `bc59e5d778f60d1f` — IT(178) P6_122, f=(29, 44, 17), p=3^3 4^6 5^3 6^2 9^2 10^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 3/4, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 7 b). Candidate wall time 20.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(178) P6_122 p=(1/8, 1/6, 5/12) c/a=3/4 G=diag(16,16,9) period=24 n_conv=12 T=12 site=1 dim=3 f=(29,44,17) p-vec 3^3 4^6 5^3 6^2 9^2 10^1 aut=1 W=2 nonsimple=1 cutoff_D2=36864 4rho2_G=194332/25 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.6s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=204 paired 1:1; disjointness G-ball D2=4rho2=194332/25 (coord bound (26, 26, 30)), ball sizes 50..50 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 6.5s | audit re-derived 12 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 204 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1056 shared-vertex G-equidistance checks, 5916 vertex-side checks, 204 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 12.2s | tables T=12 nbrs=17 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 102, 1248, 17808], free=[1, 13, 104, 1536]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 102, 1248, 17808, 276384], free=[1, 13, 104, 1536, 23032], one-sided=[1, 13, 104, 1536, 23032], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 11s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #65 `cbead3df2d2f1d0e` — IT(154) P3_221, f=(34, 51, 19), p=3^2 4^11 6^1 8^3 10^1 12^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1277/2000, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b; metric-thin: P5-only). Candidate wall time 16.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(154) P3_221 p=(1/8, 1/6, 5/12) c/a=1277/2000 G=diag(4000000,4000000,1630729) period=24 n_conv=6 T=6 site=1 dim=3 f=(34,51,19) p-vec 3^2 4^11 6^1 8^3 10^1 12^1 aut=1 W=2 nonsimple=0 cutoff_D2=9216000000 4rho2_G=165858173875374453021620416/77943775652015625 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.7s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=114 paired 1:1; disjointness G-ball D2=4rho2=165858173875374453021620416/77943775652015625 (coord bound (27, 27, 37)), ball sizes 32..32 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 9.7s | audit re-derived 6 cells x 19 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 114 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 612 shared-vertex G-equidistance checks, 3876 vertex-side checks, 114 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.3s | tables T=6 nbrs=19 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 57, 786, 12498], free=[1, 12, 131, 2115]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 57, 786, 12498, 215610], free=[1, 12, 131, 2115, 35935], one-sided=[1, 12, 131, 2115, 35935], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #66 `85244add8d1f2d55` — IT(169) P6_1, f=(32, 48, 18), p=3^2 4^6 5^6 6^2 12^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1/2, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 3 b). Candidate wall time 10.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(169) P6_1 p=(1/8, 1/6, 5/12) c/a=1/2 G=diag(4,4,1) period=24 n_conv=6 T=6 site=1 dim=3 f=(32,48,18) p-vec 3^2 4^6 5^6 6^2 12^2 aut=1 W=2 nonsimple=0 cutoff_D2=9216 4rho2_G=1957456/981 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.8s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=108 paired 1:1; disjointness G-ball D2=4rho2=1957456/981 (coord bound (26, 26, 45)), ball sizes 38..38 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.3s | audit re-derived 6 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 108 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 576 shared-vertex G-equidistance checks, 3456 vertex-side checks, 108 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 4.3s | tables T=6 nbrs=18 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 54, 654, 9162], free=[1, 9, 109, 1527]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 54, 654, 9162, 139686], free=[1, 9, 109, 1527, 23281], one-sided=[1, 9, 109, 1527, 23281], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #67 `2165f5c5260120de` — IT(152) P3_121, f=(30, 45, 17), p=3^4 4^3 5^4 6^1 7^2 8^2 10^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 527/1000, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b). Candidate wall time 9.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(152) P3_121 p=(1/8, 1/6, 5/12) c/a=527/1000 G=diag(1000000,1000000,277729) period=24 n_conv=6 T=6 site=1 dim=3 f=(30,45,17) p-vec 3^4 4^3 5^4 6^1 7^2 8^2 10^1 aut=1 W=2 nonsimple=0 cutoff_D2=2304000000 4rho2_G=1984834934279180142927088/3923803046671875 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.8s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=102 paired 1:1; disjointness G-ball D2=4rho2=1984834934279180142927088/3923803046671875 (coord bound (26, 26, 43)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.3s | audit re-derived 6 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 102 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 540 shared-vertex G-equidistance checks, 3060 vertex-side checks, 102 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.3s | tables T=6 nbrs=17 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 51, 612, 8496], free=[1, 11, 102, 1444]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 51, 612, 8496, 128004], free=[1, 11, 102, 1444, 21334], one-sided=[1, 11, 102, 1444, 21334], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #68 `437fbe758a6dd8e3` — IT(179) P6_522, f=(32, 48, 18), p=3^4 4^6 5^2 6^2 8^1 10^3, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1/2, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 3 b). Candidate wall time 25.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(179) P6_522 p=(1/8, 1/6, 5/12) c/a=1/2 G=diag(4,4,1) period=24 n_conv=12 T=12 site=1 dim=3 f=(32,48,18) p-vec 3^4 4^6 5^2 6^2 8^1 10^3 aut=1 W=2 nonsimple=0 cutoff_D2=9216 4rho2_G=1581424/867 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 2.8s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=216 paired 1:1; disjointness G-ball D2=4rho2=1581424/867 (coord bound (25, 25, 43)), ball sizes 64..64 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 9.7s | audit re-derived 12 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 216 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1152 shared-vertex G-equidistance checks, 6912 vertex-side checks, 216 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 12.8s | tables T=12 nbrs=18 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 108, 1380, 20418], free=[1, 14, 115, 1762]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 108, 1380, 20418, 328404], free=[1, 14, 115, 1762, 27367], one-sided=[1, 14, 115, 1762, 27367], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 12s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #69 `36ec4ad2f530e145` — IT(151) P3_112, f=(30, 45, 17), p=3^2 4^6 6^7 8^1 10^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 3/4, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 9 b). Candidate wall time 8.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(151) P3_112 p=(1/8, 1/6, 5/12) c/a=3/4 G=diag(16,16,9) period=24 n_conv=6 T=6 site=1 dim=3 f=(30,45,17) p-vec 3^2 4^6 6^7 8^1 10^1 aut=1 W=2 nonsimple=0 cutoff_D2=36864 4rho2_G=29680/3 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=102 paired 1:1; disjointness G-ball D2=4rho2=29680/3 (coord bound (29, 29, 34)), ball sizes 46..46 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 4.1s | audit re-derived 6 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 102 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 540 shared-vertex G-equidistance checks, 3060 vertex-side checks, 102 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.4s | tables T=6 nbrs=17 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 51, 612, 8520], free=[1, 12, 102, 1460]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 51, 612, 8520, 128952], free=[1, 12, 102, 1460, 21492], one-sided=[1, 12, 102, 1460, 21492], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #70 `fcffad0da2b5b62f` — IT(154) P3_221, f=(32, 48, 18), p=3^4 4^4 5^2 6^3 7^2 8^2 10^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 15/16, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 6 b; metric-thin: P5-only). Candidate wall time 10.5s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(154) P3_221 p=(1/8, 1/6, 5/12) c/a=15/16 G=diag(256,256,225) period=24 n_conv=6 T=6 site=1 dim=3 f=(32,48,18) p-vec 3^4 4^4 5^2 6^3 7^2 8^2 10^1 aut=1 W=2 nonsimple=0 cutoff_D2=589824 4rho2_G=49199131328/305809 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=108 paired 1:1; disjointness G-ball D2=4rho2=49199131328/305809 (coord bound (29, 29, 27)), ball sizes 40..40 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.6s | audit re-derived 6 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 108 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 576 shared-vertex G-equidistance checks, 3456 vertex-side checks, 108 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 4.2s | tables T=6 nbrs=18 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 54, 690, 10281], free=[1, 11, 115, 1737]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 54, 690, 10281, 166914], free=[1, 11, 115, 1737, 27819], one-sided=[1, 11, 115, 1737, 27819], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #71 `505a4911e298c933` — IT(181) P6_422, f=(28, 42, 16), p=3^2 4^6 6^6 8^1 10^1, aut=2

Witness point (1/8, 1/6, 5/12), c/a = 2, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 8 b). Candidate wall time 18.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.5s | IT(181) P6_422 p=(1/8, 1/6, 5/12) c/a=2 G=diag(2,2,8) period=24 n_conv=12 T=12 site=1 dim=3 f=(28,42,16) p-vec 3^2 4^6 6^6 8^1 10^1 aut=2 W=3 nonsimple=0 cutoff_D2=18432 4rho2_G=3578/3 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 3.8s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=192 paired 1:1; disjointness G-ball D2=4rho2=3578/3 (coord bound (29, 29, 13)), ball sizes 32..32 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.3s | audit re-derived 12 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 192 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1008 shared-vertex G-equidistance checks, 5376 vertex-side checks, 192 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 9.0s | tables T=12 nbrs=16 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 96, 1080, 14130], free=[1, 13, 90, 1231]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 96, 1080, 14130, 201240], free=[1, 13, 90, 1231, 16770], one-sided=[1, 13, 90, 1231, 16770], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 8s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #72 `24a6b511067d37b2` — IT(178) P6_122, f=(30, 45, 17), p=3^2 4^5 5^4 6^3 8^2 10^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 5/4, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b). Candidate wall time 21.5s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(178) P6_122 p=(1/8, 1/6, 5/12) c/a=5/4 G=diag(16,16,25) period=24 n_conv=12 T=12 site=1 dim=3 f=(30,45,17) p-vec 3^2 4^5 5^4 6^3 8^2 10^1 aut=1 W=2 nonsimple=0 cutoff_D2=57600 4rho2_G=11297728/1323 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.9s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=204 paired 1:1; disjointness G-ball D2=4rho2=11297728/1323 (coord bound (27, 27, 19)), ball sizes 35..35 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 7.5s | audit re-derived 12 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 204 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1080 shared-vertex G-equidistance checks, 6120 vertex-side checks, 204 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 11.8s | tables T=12 nbrs=17 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 102, 1248, 17676], free=[1, 12, 104, 1515]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 102, 1248, 17676, 271860], free=[1, 12, 104, 1515, 22655], one-sided=[1, 12, 104, 1515, 22655], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 11s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #73 `30f2a1e483babf55` — IT(178) P6_122, f=(29, 44, 17), p=3^4 4^5 5^2 6^1 7^2 8^1 9^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 11/4, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b). Candidate wall time 26.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.7s | IT(178) P6_122 p=(1/12, 3/8, 1/6) c/a=11/4 G=diag(16,16,121) period=24 n_conv=12 T=12 site=1 dim=3 f=(29,44,17) p-vec 3^4 4^5 5^2 6^1 7^2 8^1 9^2 aut=1 W=2 nonsimple=1 cutoff_D2=278784 4rho2_G=1404352/121 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 7.1s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=204 paired 1:1; disjointness G-ball D2=4rho2=1404352/121 (coord bound (32, 32, 10)), ball sizes 34..34 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 7.6s | audit re-derived 12 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 204 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1056 shared-vertex G-equidistance checks, 5916 vertex-side checks, 204 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 11.2s | tables T=12 nbrs=17 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 102, 1248, 17718], free=[1, 11, 104, 1507]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 102, 1248, 17718, 273444], free=[1, 11, 104, 1507, 22787], one-sided=[1, 11, 104, 1507, 22787], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 10s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #74 `37aa18e6e10583be` — IT(155) R32, f=(30, 47, 19), p=3^6 4^5 5^2 6^3 8^1 10^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 9/8, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 3 b; metric-thin: P5-only). Candidate wall time 11.5s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(155) R32 p=(1/8, 1/6, 5/12) c/a=9/8 G=diag(64,64,81) period=24 n_conv=18 T=6 site=1 dim=3 f=(30,47,19) p-vec 3^6 4^5 5^2 6^3 8^1 10^2 aut=1 W=2 nonsimple=4 cutoff_D2=186624 4rho2_G=35344 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.3s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=114 paired 1:1; disjointness G-ball D2=4rho2=35344 (coord bound (28, 28, 21)), ball sizes 77..77 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 3.8s | audit re-derived 6 cells x 19 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 114 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 564 shared-vertex G-equidistance checks, 3420 vertex-side checks, 114 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.0s | tables T=6 nbrs=19 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 57, 778, 12339], free=[1, 12, 131, 2089]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 57, 778, 12339, 213036], free=[1, 12, 131, 2089, 35506], one-sided=[1, 12, 131, 2089, 35506], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #75 `7715c7010e513b71` — IT(181) P6_422, f=(30, 45, 17), p=4^10 6^4 8^2 10^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 8 b). Candidate wall time 22.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(181) P6_422 p=(1/8, 1/6, 5/12) c/a=1 G=diag(2,2,2) period=24 n_conv=12 T=12 site=1 dim=3 f=(30,45,17) p-vec 4^10 6^4 8^2 10^1 aut=1 W=2 nonsimple=0 cutoff_D2=4608 4rho2_G=1054 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.6s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=204 paired 1:1; disjointness G-ball D2=4rho2=1054 (coord bound (27, 27, 23)), ball sizes 39..39 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 7.8s | audit re-derived 12 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 204 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1080 shared-vertex G-equidistance checks, 6120 vertex-side checks, 204 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 12.3s | tables T=12 nbrs=17 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 102, 1272, 18408], free=[1, 14, 106, 1597]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 102, 1272, 18408, 289800], free=[1, 14, 106, 1597, 24150], one-sided=[1, 14, 106, 1597, 24150], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 11s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #76 `0b5d9beb0fc972f6` — IT(179) P6_522, f=(32, 48, 18), p=3^2 4^5 5^6 6^1 8^3 10^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 13/8, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b; metric-thin: P5-only). Candidate wall time 28.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(179) P6_522 p=(1/12, 3/8, 1/6) c/a=13/8 G=diag(64,64,169) period=24 n_conv=12 T=12 site=1 dim=3 f=(32,48,18) p-vec 3^2 4^5 5^6 6^1 8^3 10^1 aut=1 W=2 nonsimple=0 cutoff_D2=389376 4rho2_G=118960/3 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 3.1s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=216 paired 1:1; disjointness G-ball D2=4rho2=118960/3 (coord bound (29, 29, 16)), ball sizes 43..43 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 10.4s | audit re-derived 12 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 216 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1152 shared-vertex G-equidistance checks, 6912 vertex-side checks, 216 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 14.9s | tables T=12 nbrs=18 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 108, 1428, 21984], free=[1, 12, 119, 1870]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 108, 1428, 21984, 368604], free=[1, 12, 119, 1870, 30717], one-sided=[1, 12, 119, 1870, 30717], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 14s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #77 `322d5ff451e4101d` — IT(169) P6_1, f=(32, 48, 18), p=3^2 4^6 5^4 6^2 7^2 10^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 11/8, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): indeterminate (triage, 3 b; metric-thin: P5-only). Candidate wall time 11.1s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(169) P6_1 p=(1/8, 1/6, 5/12) c/a=11/8 G=diag(64,64,121) period=24 n_conv=6 T=6 site=1 dim=3 f=(32,48,18) p-vec 3^2 4^6 5^4 6^2 7^2 10^2 aut=1 W=2 nonsimple=0 cutoff_D2=278784 4rho2_G=148084336/3267 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.8s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=108 paired 1:1; disjointness G-ball D2=4rho2=148084336/3267 (coord bound (31, 31, 20)), ball sizes 32..32 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 6.0s | audit re-derived 6 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 108 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 576 shared-vertex G-equidistance checks, 3456 vertex-side checks, 108 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 4.1s | tables T=6 nbrs=18 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 54, 678, 9816], free=[1, 9, 113, 1636]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 54, 678, 9816, 154116], free=[1, 9, 113, 1636, 25686], one-sided=[1, 9, 113, 1636, 25686], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #78 `34351050a4f29035` — IT(178) P6_122, f=(28, 42, 16), p=3^2 4^5 5^2 6^4 8^3, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 11 b). Candidate wall time 16.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(178) P6_122 p=(1/8, 1/6, 5/12) c/a=1 G=diag(2,2,2) period=24 n_conv=12 T=12 site=1 dim=3 f=(28,42,16) p-vec 3^2 4^5 5^2 6^4 8^3 aut=1 W=2 nonsimple=0 cutoff_D2=4608 4rho2_G=1000 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.4s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=192 paired 1:1; disjointness G-ball D2=4rho2=1000 (coord bound (26, 26, 23)), ball sizes 39..39 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.8s | audit re-derived 12 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 192 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1008 shared-vertex G-equidistance checks, 5376 vertex-side checks, 192 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 9.1s | tables T=12 nbrs=16 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 96, 1080, 14130], free=[1, 12, 90, 1220]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 96, 1080, 14130, 201048], free=[1, 12, 90, 1220, 16754], one-sided=[1, 12, 90, 1220, 16754], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 8s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #79 `c0071756347c5a8a` — IT(144) P3_1, f=(28, 42, 16), p=3^2 4^4 5^4 7^6, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 1, site stabilizer 1, orbit 3 conventional / 3 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 9 b). Candidate wall time 2.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.0s | IT(144) P3_1 p=(1/12, 3/8, 1/6) c/a=1 G=diag(2,2,2) period=24 n_conv=3 T=3 site=1 dim=3 f=(28,42,16) p-vec 3^2 4^4 5^4 7^6 aut=1 W=2 nonsimple=0 cutoff_D2=4608 4rho2_G=32401/24 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.2s | detL=13824 T=3 vol=4608 T*vol=13824 (crystal-basis measure) slots=48 paired 1:1; disjointness G-ball D2=4rho2=32401/24 (coord bound (31, 31, 26)), ball sizes 20..20 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.5s | audit re-derived 3 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 4608 each, T*vol == |det|; all 48 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 252 shared-vertex G-equidistance checks, 1344 vertex-side checks, 48 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=3 (0 improper) vs T*|site|=3: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.0s | tables T=3 nbrs=16 |ops|=3 (3 proper, 0 improper; T*|site|=3), identity+closure exact; hands: 0 of 3 classes of the other hand; banked enumerate n<=4: fixed=[3, 24, 264, 3354], free=[1, 8, 88, 1118]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[3, 24, 264, 3354, 46299], free=[1, 8, 88, 1118, 15433], one-sided=[1, 8, 88, 1118, 15433], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 3 (0 improper) vs T*|site| = 3: the full symmetry group of the honeycomb IS exactly the generating group G.

### #80 `d9bf7fb7a80eaa38` — IT(155) R32, f=(30, 47, 19), p=3^4 4^6 5^4 6^3 10^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 5/4, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): indeterminate (triage, 2 b). Candidate wall time 12.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(155) R32 p=(1/8, 1/6, 5/12) c/a=5/4 G=diag(16,16,25) period=24 n_conv=18 T=6 site=1 dim=3 f=(30,47,19) p-vec 3^4 4^6 5^4 6^3 10^2 aut=1 W=2 nonsimple=4 cutoff_D2=57600 4rho2_G=8912 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.5s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=114 paired 1:1; disjointness G-ball D2=4rho2=8912 (coord bound (28, 28, 19)), ball sizes 65..65 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 4.2s | audit re-derived 6 cells x 19 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 114 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 564 shared-vertex G-equidistance checks, 3420 vertex-side checks, 114 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.7s | tables T=6 nbrs=19 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 57, 802, 13248], free=[1, 12, 135, 2241]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 57, 802, 13248, 238860], free=[1, 12, 135, 2241, 39810], one-sided=[1, 12, 135, 2241, 39810], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #81 `847d2695a14ae424` — IT(152) P3_121, f=(29, 44, 17), p=3^4 4^4 5^4 6^1 8^2 9^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 5/4, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b). Candidate wall time 8.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(152) P3_121 p=(1/8, 1/6, 5/12) c/a=5/4 G=diag(16,16,25) period=24 n_conv=6 T=6 site=1 dim=3 f=(29,44,17) p-vec 3^4 4^4 5^4 6^1 8^2 9^2 aut=1 W=2 nonsimple=1 cutoff_D2=57600 4rho2_G=234706288/21675 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=102 paired 1:1; disjointness G-ball D2=4rho2=234706288/21675 (coord bound (31, 31, 21)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 3.9s | audit re-derived 6 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 102 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 528 shared-vertex G-equidistance checks, 2958 vertex-side checks, 102 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 4.0s | tables T=6 nbrs=17 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 51, 624, 8871], free=[1, 10, 104, 1497]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 51, 624, 8871, 137076], free=[1, 10, 104, 1497, 22846], one-sided=[1, 10, 104, 1497, 22846], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #82 `090dcafb7ce9cb08` — IT(166) R-3m, f=(20, 32, 14), p=3^2 4^9 7^2 8^1, aut=2

Witness point (1/24, 1/12, 11/24), c/a = 1/2, site stabilizer 2, orbit 18 conventional / 6 primitive, stratum dim 2. Open/wall label (triage, carried): open-likely (triage, 6 b). Candidate wall time 6.1s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(166) R-3m p=(1/24, 1/12, 11/24) c/a=1/2 G=diag(4,4,1) period=24 n_conv=18 T=6 site=2 dim=2 f=(20,32,14) p-vec 3^2 4^9 7^2 8^1 aut=2 W=2 nonsimple=4 cutoff_D2=9216 4rho2_G=8308/9 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.5s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=84 paired 1:1; disjointness G-ball D2=4rho2=8308/9 (coord bound (18, 18, 31)), ball sizes 49..49 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.8s | audit re-derived 6 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 84 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 384 shared-vertex G-equidistance checks, 1680 vertex-side checks, 84 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=1, improper=1; solid achiral), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.3s | tables T=6 nbrs=14 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: inconsistent (achiral solid); banked enumerate n<=4: fixed=[6, 42, 434, 5313], free=[1, 7, 40, 481]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 42, 434, 5313, 71310], free=[1, 7, 40, 481, 5988], one-sided=[1, 11, 73, 925, 11885], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 1, solid achiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #83 `9bc4922a7b574aa6` — IT(166) R-3m, f=(17, 28, 13), p=3^4 4^4 5^4 8^1, aut=2

Witness point (1/24, 1/12, 11/24), c/a = 3/4, site stabilizer 2, orbit 18 conventional / 6 primitive, stratum dim 2. Open/wall label (triage, carried): open-likely (triage, 10 b). Candidate wall time 4.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(166) R-3m p=(1/24, 1/12, 11/24) c/a=3/4 G=diag(16,16,9) period=24 n_conv=18 T=6 site=2 dim=2 f=(17,28,13) p-vec 3^4 4^4 5^4 8^1 aut=2 W=2 nonsimple=5 cutoff_D2=36864 4rho2_G=5188 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.1s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=78 paired 1:1; disjointness G-ball D2=4rho2=5188 (coord bound (21, 21, 25)), ball sizes 54..54 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.4s | audit re-derived 6 cells x 13 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 78 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 336 shared-vertex G-equidistance checks, 1326 vertex-side checks, 78 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=1, improper=1; solid achiral), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.9s | tables T=6 nbrs=13 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: inconsistent (achiral solid); banked enumerate n<=4: fixed=[6, 39, 380, 4365], free=[1, 6, 35, 393]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 39, 380, 4365, 54822], free=[1, 6, 35, 393, 4602], one-sided=[1, 10, 64, 760, 9137], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 1, solid achiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #84 `43e4e46001b4d8b9` — IT(181) P6_422, f=(32, 48, 18), p=3^6 4^3 5^2 6^2 8^3 10^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 31/16, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b; metric-thin: P5-only). Candidate wall time 29.1s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.7s | IT(181) P6_422 p=(1/8, 1/6, 5/12) c/a=31/16 G=diag(256,256,961) period=24 n_conv=12 T=12 site=1 dim=3 f=(32,48,18) p-vec 3^6 4^3 5^2 6^2 8^3 10^2 aut=1 W=3 nonsimple=0 cutoff_D2=2214144 4rho2_G=438680176/2883 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 4.6s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=216 paired 1:1; disjointness G-ball D2=4rho2=438680176/2883 (coord bound (29, 29, 13)), ball sizes 34..34 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 10.0s | audit re-derived 12 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 216 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1152 shared-vertex G-equidistance checks, 6912 vertex-side checks, 216 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 13.7s | tables T=12 nbrs=18 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 108, 1380, 20508], free=[1, 14, 115, 1768]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 108, 1380, 20508, 331836], free=[1, 14, 115, 1768, 27653], one-sided=[1, 14, 115, 1768, 27653], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 13s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #85 `af8b2135c913b13b` — IT(181) P6_422, f=(32, 48, 18), p=3^6 4^4 6^4 8^1 10^3, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 7/8, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 3 b). Candidate wall time 26.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(181) P6_422 p=(1/8, 1/6, 5/12) c/a=7/8 G=diag(64,64,49) period=24 n_conv=12 T=12 site=1 dim=3 f=(32,48,18) p-vec 3^6 4^4 6^4 8^1 10^3 aut=1 W=2 nonsimple=0 cutoff_D2=147456 4rho2_G=35512816/1083 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.9s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=216 paired 1:1; disjointness G-ball D2=4rho2=35512816/1083 (coord bound (27, 27, 26)), ball sizes 43..43 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 10.6s | audit re-derived 12 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 216 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1152 shared-vertex G-equidistance checks, 6912 vertex-side checks, 216 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 14.0s | tables T=12 nbrs=18 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 108, 1356, 19737], free=[1, 14, 113, 1704]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 108, 1356, 19737, 312060], free=[1, 14, 113, 1704, 26005], one-sided=[1, 14, 113, 1704, 26005], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 13s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #86 `74a69fba4266de3b` — IT(167) R-3c, f=(28, 43, 17), p=3^10 6^1 8^5 10^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 527/1000, site stabilizer 1, orbit 36 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 6 b). Candidate wall time 25.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.8s | IT(167) R-3c p=(1/8, 1/6, 5/12) c/a=527/1000 G=diag(1000000,1000000,277729) period=24 n_conv=36 T=12 site=1 dim=3 f=(28,43,17) p-vec 3^10 6^1 8^5 10^1 aut=1 W=2 nonsimple=2 cutoff_D2=2304000000 4rho2_G=84259020089764/765625 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 5.6s | detL=4608 T=12 vol=384 T*vol=4608 (crystal-basis measure) slots=204 paired 1:1; disjointness G-ball D2=4rho2=84259020089764/765625 (coord bound (13, 13, 20)), ball sizes 25..25 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 7.9s | audit re-derived 12 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 384 each, T*vol == |det|; all 204 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1032 shared-vertex G-equidistance checks, 5712 vertex-side checks, 204 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 11.2s | tables T=12 nbrs=17 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: 6 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 102, 1192, 16086], free=[1, 11, 100, 1369]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 102, 1192, 16086, 235656], free=[1, 11, 100, 1369, 19638], one-sided=[2, 21, 200, 2726, 39276], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 10s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #87 `c3b4b14633c9d4d5` — IT(155) R32, f=(28, 43, 17), p=4^9 5^2 6^4 8^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 6 b). Candidate wall time 7.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(155) R32 p=(1/8, 1/6, 5/12) c/a=1 G=diag(2,2,2) period=24 n_conv=18 T=6 site=1 dim=3 f=(28,43,17) p-vec 4^9 5^2 6^4 8^2 aut=1 W=2 nonsimple=2 cutoff_D2=4608 4rho2_G=904 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.1s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=102 paired 1:1; disjointness G-ball D2=4rho2=904 (coord bound (25, 25, 22)), ball sizes 70..70 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 2.6s | audit re-derived 6 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 102 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 516 shared-vertex G-equidistance checks, 2856 vertex-side checks, 102 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.7s | tables T=6 nbrs=17 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 51, 644, 9456], free=[1, 12, 108, 1619]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 51, 644, 9456, 150948], free=[1, 12, 108, 1619, 25158], one-sided=[1, 12, 108, 1619, 25158], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #88 `e19babba732f5fd4` — IT(179) P6_522, f=(29, 44, 17), p=4^11 5^2 7^2 10^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 7/4, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 3 b). Candidate wall time 24.1s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(179) P6_522 p=(1/12, 3/8, 1/6) c/a=7/4 G=diag(16,16,49) period=24 n_conv=12 T=12 site=1 dim=3 f=(29,44,17) p-vec 4^11 5^2 7^2 10^2 aut=1 W=2 nonsimple=1 cutoff_D2=112896 4rho2_G=30064/3 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 3.1s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=204 paired 1:1; disjointness G-ball D2=4rho2=30064/3 (coord bound (29, 29, 15)), ball sizes 43..43 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 6.7s | audit re-derived 12 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 204 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1056 shared-vertex G-equidistance checks, 5916 vertex-side checks, 204 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 13.9s | tables T=12 nbrs=17 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 102, 1296, 19278], free=[1, 11, 108, 1637]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 102, 1296, 19278, 312864], free=[1, 11, 108, 1637, 26072], one-sided=[1, 11, 108, 1637, 26072], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 13s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #89 `7472d8ba000c8056` — IT(152) P3_121, f=(22, 36, 16), p=3^8 4^2 6^2 7^4, aut=2

Witness point (0, 1/4, 1/6), c/a = 9/8, site stabilizer 2, orbit 3 conventional / 3 primitive, stratum dim 1. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b,P5-only). Candidate wall time 2.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.0s | IT(152) P3_121 p=(0, 1/4, 1/6) c/a=9/8 G=diag(64,64,81) period=12 n_conv=3 T=3 site=2 dim=1 f=(22,36,16) p-vec 3^8 4^2 6^2 7^4 aut=2 W=2 nonsimple=6 cutoff_D2=46656 4rho2_G=12240 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.1s | detL=1728 T=3 vol=576 T*vol=1728 (crystal-basis measure) slots=48 paired 1:1; disjointness G-ball D2=4rho2=12240 (coord bound (16, 16, 13)), ball sizes 24..24 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.5s | audit re-derived 3 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 576 each, T*vol == |det|; all 48 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 216 shared-vertex G-equidistance checks, 1056 vertex-side checks, 48 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.5s | tables T=3 nbrs=16 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 3 classes of the other hand; banked enumerate n<=4: fixed=[3, 24, 276, 3648], free=[1, 5, 50, 621]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[3, 24, 276, 3648, 52275], free=[1, 5, 50, 621, 8762], one-sided=[1, 5, 50, 621, 8762], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #90 `d0c5a15c25ab6413` — IT(152) P3_121, f=(32, 48, 18), p=3^2 4^7 5^2 6^3 8^2 9^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 17/16, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 3 b; metric-thin: P5-only). Candidate wall time 11.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(152) P3_121 p=(1/8, 1/6, 5/12) c/a=17/16 G=diag(256,256,289) period=24 n_conv=6 T=6 site=1 dim=3 f=(32,48,18) p-vec 3^2 4^7 5^2 6^3 8^2 9^2 aut=1 W=2 nonsimple=0 cutoff_D2=665856 4rho2_G=329674144/2025 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.5s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=108 paired 1:1; disjointness G-ball D2=4rho2=329674144/2025 (coord bound (30, 30, 24)), ball sizes 34..34 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.5s | audit re-derived 6 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 108 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 576 shared-vertex G-equidistance checks, 3456 vertex-side checks, 108 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 5.1s | tables T=6 nbrs=18 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 54, 690, 10254], free=[1, 11, 115, 1734]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 54, 690, 10254, 165906], free=[1, 11, 115, 1734, 27651], one-sided=[1, 11, 115, 1734, 27651], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 5s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #91 `d770abfcee4deb90` — IT(153) P3_212, f=(32, 48, 18), p=3^6 4^3 5^2 6^2 8^4 12^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 19/16, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 3 b; metric-thin: P5-only). Candidate wall time 10.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(153) P3_212 p=(1/8, 1/6, 5/12) c/a=19/16 G=diag(256,256,361) period=24 n_conv=6 T=6 site=1 dim=3 f=(32,48,18) p-vec 3^6 4^3 5^2 6^2 8^4 12^1 aut=1 W=2 nonsimple=0 cutoff_D2=831744 4rho2_G=184373824/1083 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.7s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=108 paired 1:1; disjointness G-ball D2=4rho2=184373824/1083 (coord bound (30, 30, 22)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.8s | audit re-derived 6 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 108 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 576 shared-vertex G-equidistance checks, 3456 vertex-side checks, 108 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 4.2s | tables T=6 nbrs=18 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 54, 678, 9864], free=[1, 12, 113, 1679]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 54, 678, 9864, 155994], free=[1, 12, 113, 1679, 25999], one-sided=[1, 12, 113, 1679, 25999], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #92 `4a560e459032166a` — IT(154) P3_221, f=(28, 42, 16), p=3^4 5^8 8^4, aut=2

Witness point (1/8, 1/6, 5/12), c/a = 7/8, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b). Candidate wall time 6.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(154) P3_221 p=(1/8, 1/6, 5/12) c/a=7/8 G=diag(64,64,49) period=24 n_conv=6 T=6 site=1 dim=3 f=(28,42,16) p-vec 3^4 5^8 8^4 aut=2 W=2 nonsimple=0 cutoff_D2=147456 4rho2_G=2762378557/70756 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=96 paired 1:1; disjointness G-ball D2=4rho2=2762378557/70756 (coord bound (29, 29, 29)), ball sizes 39..39 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 3.3s | audit re-derived 6 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 96 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 504 shared-vertex G-equidistance checks, 2688 vertex-side checks, 96 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.6s | tables T=6 nbrs=16 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 48, 528, 6732], free=[1, 10, 88, 1142]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 48, 528, 6732, 93414], free=[1, 10, 88, 1142, 15569], one-sided=[1, 10, 88, 1142, 15569], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #93 `5beb94b61eb66eb1` — IT(178) P6_122, f=(27, 41, 16), p=3^3 4^7 6^2 7^1 8^1 9^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1/2, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b). Candidate wall time 16.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(178) P6_122 p=(1/8, 1/6, 5/12) c/a=1/2 G=diag(4,4,1) period=24 n_conv=12 T=12 site=1 dim=3 f=(27,41,16) p-vec 3^3 4^7 6^2 7^1 8^1 9^2 aut=1 W=2 nonsimple=1 cutoff_D2=9216 4rho2_G=1994992/1083 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 2.2s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=192 paired 1:1; disjointness G-ball D2=4rho2=1994992/1083 (coord bound (25, 25, 43)), ball sizes 66..66 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.1s | audit re-derived 12 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 192 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 984 shared-vertex G-equidistance checks, 5184 vertex-side checks, 192 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 9.1s | tables T=12 nbrs=16 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 96, 1104, 14658], free=[1, 13, 92, 1275]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 96, 1104, 14658, 211332], free=[1, 13, 92, 1275, 17611], one-sided=[1, 13, 92, 1275, 17611], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 8s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #94 `95934e84555dc2ea` — IT(179) P6_522, f=(26, 40, 16), p=3^2 4^7 5^1 6^3 7^1 8^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 1/2, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b). Candidate wall time 16.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(179) P6_522 p=(1/12, 3/8, 1/6) c/a=1/2 G=diag(4,4,1) period=24 n_conv=12 T=12 site=1 dim=3 f=(26,40,16) p-vec 3^2 4^7 5^1 6^3 7^1 8^2 aut=1 W=2 nonsimple=2 cutoff_D2=9216 4rho2_G=1205 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 2.0s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=192 paired 1:1; disjointness G-ball D2=4rho2=1205 (coord bound (21, 21, 35)), ball sizes 47..47 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 4.2s | audit re-derived 12 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 192 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 960 shared-vertex G-equidistance checks, 4992 vertex-side checks, 192 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 10.3s | tables T=12 nbrs=16 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 96, 1152, 16152], free=[1, 13, 96, 1404]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 96, 1152, 16152, 246444], free=[1, 13, 96, 1404, 20537], one-sided=[1, 13, 96, 1404, 20537], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 9s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #95 `d0ed9179c6947b5f` — IT(155) R32, f=(16, 26, 12), p=3^2 4^6 5^2 6^2, aut=2

Witness point (1/12, 3/8, 1/6), c/a = 1/2, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 25 b). Candidate wall time 2.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(155) R32 p=(1/12, 3/8, 1/6) c/a=1/2 G=diag(4,4,1) period=24 n_conv=18 T=6 site=1 dim=3 f=(16,26,12) p-vec 3^2 4^6 5^2 6^2 aut=2 W=2 nonsimple=3 cutoff_D2=9216 4rho2_G=1136 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.1s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=72 paired 1:1; disjointness G-ball D2=4rho2=1136 (coord bound (20, 20, 34)), ball sizes 75..75 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.3s | audit re-derived 6 cells x 12 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 72 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 312 shared-vertex G-equidistance checks, 1152 vertex-side checks, 72 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.0s | tables T=6 nbrs=12 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 36, 296, 2814], free=[1, 9, 50, 492]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 36, 296, 2814, 29130], free=[1, 9, 50, 492, 4855], one-sided=[1, 9, 50, 492, 4855], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #96 `0948aa6184f13a8a` — IT(179) P6_522, f=(30, 45, 17), p=3^4 4^4 6^4 7^2 8^3, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 5/4, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b). Candidate wall time 20.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(179) P6_522 p=(1/8, 1/6, 5/12) c/a=5/4 G=diag(16,16,25) period=24 n_conv=12 T=12 site=1 dim=3 f=(30,45,17) p-vec 3^4 4^4 6^4 7^2 8^3 aut=1 W=2 nonsimple=0 cutoff_D2=57600 4rho2_G=677236/75 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 2.0s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=204 paired 1:1; disjointness G-ball D2=4rho2=677236/75 (coord bound (28, 28, 20)), ball sizes 37..37 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 7.8s | audit re-derived 12 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 204 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1080 shared-vertex G-equidistance checks, 6120 vertex-side checks, 204 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 10.6s | tables T=12 nbrs=17 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 102, 1200, 16368], free=[1, 12, 100, 1404]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 102, 1200, 16368, 242700], free=[1, 12, 100, 1404, 20225], one-sided=[1, 12, 100, 1404, 20225], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 10s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #97 `272aefcd5e48ba49` — IT(179) P6_522, f=(29, 44, 17), p=3^3 4^3 5^3 6^5 7^2 8^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 9/8, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b; metric-thin: P5-only). Candidate wall time 21.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(179) P6_522 p=(1/12, 3/8, 1/6) c/a=9/8 G=diag(64,64,81) period=24 n_conv=12 T=12 site=1 dim=3 f=(29,44,17) p-vec 3^3 4^3 5^3 6^5 7^2 8^1 aut=1 W=2 nonsimple=1 cutoff_D2=186624 4rho2_G=2426224/75 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.8s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=204 paired 1:1; disjointness G-ball D2=4rho2=2426224/75 (coord bound (26, 26, 20)), ball sizes 44..44 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 7.5s | audit re-derived 12 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 204 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1056 shared-vertex G-equidistance checks, 5916 vertex-side checks, 204 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 12.1s | tables T=12 nbrs=17 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 102, 1248, 17952], free=[1, 13, 104, 1549]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 102, 1248, 17952, 282288], free=[1, 13, 104, 1549, 23524], one-sided=[1, 13, 104, 1549, 23524], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 11s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #98 `466b12546dd936c3` — IT(161) R3c, f=(26, 40, 16), p=3^6 5^4 6^2 7^2 8^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 527/1000, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b). Candidate wall time 8.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(161) R3c p=(1/8, 1/6, 5/12) c/a=527/1000 G=diag(1000000,1000000,277729) period=24 n_conv=18 T=6 site=1 dim=3 f=(26,40,16) p-vec 3^6 5^4 6^2 7^2 8^2 aut=1 W=2 nonsimple=2 cutoff_D2=2304000000 4rho2_G=111928479525725601113968/807162924796875 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.5s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=96 paired 1:1; disjointness G-ball D2=4rho2=111928479525725601113968/807162924796875 (coord bound (14, 14, 23)), ball sizes 18..18 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 3.5s | audit re-derived 6 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 96 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 480 shared-vertex G-equidistance checks, 2496 vertex-side checks, 96 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (3 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.9s | tables T=6 nbrs=16 |ops|=6 (3 proper, 3 improper; T*|site|=6), identity+closure exact; hands: 3 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 48, 536, 6948], free=[1, 8, 90, 1158]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 48, 536, 6948, 97998], free=[1, 8, 90, 1158, 16333], one-sided=[2, 16, 180, 2316, 32666], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (3 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #99 `4885ce1e70fa9713` — IT(179) P6_522, f=(27, 41, 16), p=3^3 4^5 6^4 7^3 8^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 3/4, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 7 b). Candidate wall time 16.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(179) P6_522 p=(1/12, 3/8, 1/6) c/a=3/4 G=diag(16,16,9) period=24 n_conv=12 T=12 site=1 dim=3 f=(27,41,16) p-vec 3^3 4^5 6^4 7^3 8^1 aut=1 W=2 nonsimple=1 cutoff_D2=36864 4rho2_G=22345/4 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.7s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=192 paired 1:1; disjointness G-ball D2=4rho2=22345/4 (coord bound (22, 22, 25)), ball sizes 43..43 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.2s | audit re-derived 12 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 192 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 984 shared-vertex G-equidistance checks, 5184 vertex-side checks, 192 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 9.7s | tables T=12 nbrs=16 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 96, 1104, 14820], free=[1, 13, 92, 1289]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 96, 1104, 14820, 217392], free=[1, 13, 92, 1289, 18116], one-sided=[1, 13, 92, 1289, 18116], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 9s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #100 `3d6b109f392fda19` — IT(154) P3_221, f=(33, 50, 19), p=3^6 4^4 5^2 6^3 8^2 10^1 12^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 3/2, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 12.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(154) P3_221 p=(1/8, 1/6, 5/12) c/a=3/2 G=diag(4,4,9) period=24 n_conv=6 T=6 site=1 dim=3 f=(33,50,19) p-vec 3^6 4^4 5^2 6^3 8^2 10^1 12^1 aut=1 W=2 nonsimple=1 cutoff_D2=20736 4rho2_G=2578512/841 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.8s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=114 paired 1:1; disjointness G-ball D2=4rho2=2578512/841 (coord bound (32, 32, 19)), ball sizes 34..34 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 5.9s | audit re-derived 6 cells x 19 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 114 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 600 shared-vertex G-equidistance checks, 3762 vertex-side checks, 114 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 5.8s | tables T=6 nbrs=19 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 57, 774, 12156], free=[1, 11, 129, 2045]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 57, 774, 12156, 207126], free=[1, 11, 129, 2045, 34521], one-sided=[1, 11, 129, 2045, 34521], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 5s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #101 `e598ffd8a1cac138` — IT(144) P3_1, f=(32, 48, 18), p=3^4 4^4 5^4 6^2 9^4, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 29/32, site stabilizer 1, orbit 3 conventional / 3 primitive, stratum dim 3. Open/wall label (triage, carried): indeterminate (triage, 2 b; metric-thin: P5-only). Candidate wall time 5.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(144) P3_1 p=(1/8, 1/6, 5/12) c/a=29/32 G=diag(1024,1024,841) period=24 n_conv=3 T=3 site=1 dim=3 f=(32,48,18) p-vec 3^4 4^4 5^4 6^2 9^4 aut=1 W=2 nonsimple=0 cutoff_D2=2359296 4rho2_G=146460935956/204363 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.2s | detL=13824 T=3 vol=4608 T*vol=13824 (crystal-basis measure) slots=54 paired 1:1; disjointness G-ball D2=4rho2=146460935956/204363 (coord bound (31, 31, 30)), ball sizes 22..22 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 2.9s | audit re-derived 3 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 4608 each, T*vol == |det|; all 54 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 288 shared-vertex G-equidistance checks, 1728 vertex-side checks, 54 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=3 (0 improper) vs T*|site|=3: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.8s | tables T=3 nbrs=18 |ops|=3 (3 proper, 0 improper; T*|site|=3), identity+closure exact; hands: 0 of 3 classes of the other hand; banked enumerate n<=4: fixed=[3, 27, 351, 5289], free=[1, 9, 117, 1763]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[3, 27, 351, 5289, 86460], free=[1, 9, 117, 1763, 28820], one-sided=[1, 9, 117, 1763, 28820], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 3 (0 improper) vs T*|site| = 3: the full symmetry group of the honeycomb IS exactly the generating group G.

### #102 `a93f8fe7ecdc5851` — IT(144) P3_1, f=(32, 48, 18), p=3^2 4^8 5^2 7^2 8^2 9^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 9/8, site stabilizer 1, orbit 3 conventional / 3 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b,P5-only). Candidate wall time 4.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(144) P3_1 p=(1/12, 3/8, 1/6) c/a=9/8 G=diag(64,64,81) period=24 n_conv=3 T=3 site=1 dim=3 f=(32,48,18) p-vec 3^2 4^8 5^2 7^2 8^2 9^2 aut=1 W=2 nonsimple=0 cutoff_D2=186624 4rho2_G=34310992/729 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.2s | detL=13824 T=3 vol=4608 T*vol=13824 (crystal-basis measure) slots=54 paired 1:1; disjointness G-ball D2=4rho2=34310992/729 (coord bound (32, 32, 25)), ball sizes 22..22 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 2.6s | audit re-derived 3 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 4608 each, T*vol == |det|; all 54 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 288 shared-vertex G-equidistance checks, 1728 vertex-side checks, 54 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=3 (0 improper) vs T*|site|=3: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.7s | tables T=3 nbrs=18 |ops|=3 (3 proper, 0 improper; T*|site|=3), identity+closure exact; hands: 0 of 3 classes of the other hand; banked enumerate n<=4: fixed=[3, 27, 345, 5097], free=[1, 9, 115, 1699]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[3, 27, 345, 5097, 81780], free=[1, 9, 115, 1699, 27260], one-sided=[1, 9, 115, 1699, 27260], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 3 (0 improper) vs T*|site| = 3: the full symmetry group of the honeycomb IS exactly the generating group G.

### #103 `aef8972953d53d20` — IT(171) P6_2, f=(32, 48, 18), p=3^4 4^3 5^2 6^6 8^1 9^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 81/64, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b,P5-only). Candidate wall time 11.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(171) P6_2 p=(1/12, 3/8, 1/6) c/a=81/64 G=diag(4096,4096,6561) period=24 n_conv=6 T=6 site=1 dim=3 f=(32,48,18) p-vec 3^4 4^3 5^2 6^6 8^1 9^2 aut=1 W=3 nonsimple=0 cutoff_D2=15116544 4rho2_G=203406400/81 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=108 paired 1:1; disjointness G-ball D2=4rho2=203406400/81 (coord bound (29, 29, 20)), ball sizes 28..28 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 6.2s | audit re-derived 6 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 108 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 576 shared-vertex G-equidistance checks, 3456 vertex-side checks, 108 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 4.6s | tables T=6 nbrs=18 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 54, 690, 10245], free=[1, 11, 115, 1732]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 54, 690, 10245, 165438], free=[1, 11, 115, 1732, 27573], one-sided=[1, 11, 115, 1732, 27573], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #104 `72bcd959be4ab7dd` — IT(152) P3_121, f=(28, 42, 16), p=3^4 4^1 5^4 6^4 8^3, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 5/4, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b). Candidate wall time 6.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(152) P3_121 p=(1/12, 3/8, 1/6) c/a=5/4 G=diag(16,16,25) period=24 n_conv=6 T=6 site=1 dim=3 f=(28,42,16) p-vec 3^4 4^1 5^4 6^4 8^3 aut=1 W=2 nonsimple=0 cutoff_D2=57600 4rho2_G=578048/49 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.7s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=96 paired 1:1; disjointness G-ball D2=4rho2=578048/49 (coord bound (32, 32, 22)), ball sizes 39..39 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 3.1s | audit re-derived 6 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 96 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 504 shared-vertex G-equidistance checks, 2688 vertex-side checks, 96 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.8s | tables T=6 nbrs=16 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 48, 528, 6720], free=[1, 10, 88, 1141]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 48, 528, 6720, 93000], free=[1, 10, 88, 1141, 15500], one-sided=[1, 10, 88, 1141, 15500], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #105 `ab801b11bead62ef` — IT(166) R-3m, f=(19, 30, 13), p=3^6 4^2 5^2 6^2 12^1, aut=2

Witness point (1/12, 1/6, 7/24), c/a = 7/4, site stabilizer 2, orbit 18 conventional / 6 primitive, stratum dim 2. Open/wall label (triage, carried): open-likely (triage, 6 b). Candidate wall time 5.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.4s | IT(166) R-3m p=(1/12, 1/6, 7/24) c/a=7/4 G=diag(16,16,49) period=24 n_conv=18 T=6 site=2 dim=2 f=(19,30,13) p-vec 3^6 4^2 5^2 6^2 12^1 aut=2 W=2 nonsimple=3 cutoff_D2=112896 4rho2_G=10180 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.9s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=78 paired 1:1; disjointness G-ball D2=4rho2=10180 (coord bound (30, 30, 15)), ball sizes 60..60 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.8s | audit re-derived 6 cells x 13 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 78 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 360 shared-vertex G-equidistance checks, 1482 vertex-side checks, 78 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=1, improper=1; solid achiral), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.5s | tables T=6 nbrs=13 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: inconsistent (achiral solid); banked enumerate n<=4: fixed=[6, 39, 364, 3972], free=[1, 6, 34, 355]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 39, 364, 3972, 47154], free=[1, 6, 34, 355, 3961], one-sided=[1, 9, 62, 683, 7859], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 1, solid achiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #106 `2c121297dbaa80af` — IT(154) P3_221, f=(28, 42, 16), p=3^4 4^2 6^8 8^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 1, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 7 b). Candidate wall time 6.4s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(154) P3_221 p=(1/12, 3/8, 1/6) c/a=1 G=diag(2,2,2) period=24 n_conv=6 T=6 site=1 dim=3 f=(28,42,16) p-vec 3^4 4^2 6^8 8^2 aut=1 W=2 nonsimple=0 cutoff_D2=4608 4rho2_G=638552/729 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.5s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=96 paired 1:1; disjointness G-ball D2=4rho2=638552/729 (coord bound (25, 25, 21)), ball sizes 17..17 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 3.2s | audit re-derived 6 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 96 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 504 shared-vertex G-equidistance checks, 2688 vertex-side checks, 96 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.6s | tables T=6 nbrs=16 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 48, 528, 6708], free=[1, 10, 88, 1139]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 48, 528, 6708, 92604], free=[1, 10, 88, 1139, 15434], one-sided=[1, 10, 88, 1139, 15434], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #107 `9d0b36ad5caceb2e` — IT(167) R-3c, f=(22, 35, 15), p=3^6 4^2 5^4 6^1 8^1 10^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 7/8, site stabilizer 1, orbit 36 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 5 b). Candidate wall time 12.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.5s | IT(167) R-3c p=(1/12, 3/8, 1/6) c/a=7/8 G=diag(64,64,49) period=24 n_conv=36 T=12 site=1 dim=3 f=(22,35,15) p-vec 3^6 4^2 5^4 6^1 8^1 10^1 aut=1 W=2 nonsimple=3 cutoff_D2=147456 4rho2_G=17936 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 3.5s | detL=4608 T=12 vol=384 T*vol=4608 (crystal-basis measure) slots=180 paired 1:1; disjointness G-ball D2=4rho2=17936 (coord bound (20, 20, 20)), ball sizes 73..73 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 2.3s | audit re-derived 12 cells x 15 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 384 each, T*vol == |det|; all 180 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 840 shared-vertex G-equidistance checks, 3960 vertex-side checks, 180 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.5s | tables T=12 nbrs=15 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: 6 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 90, 940, 11466], free=[1, 10, 79, 980]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 90, 940, 11466, 152952], free=[1, 10, 79, 980, 12746], one-sided=[2, 19, 158, 1949, 25492], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #108 `d176b8d859dd651a` — IT(178) P6_122, f=(32, 48, 18), p=3^2 4^8 5^2 6^1 8^3 9^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 5/2, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 30.4s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.6s | IT(178) P6_122 p=(1/12, 3/8, 1/6) c/a=5/2 G=diag(4,4,25) period=24 n_conv=12 T=12 site=1 dim=3 f=(32,48,18) p-vec 3^2 4^8 5^2 6^1 8^3 9^2 aut=1 W=2 nonsimple=0 cutoff_D2=57600 4rho2_G=11377/4 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 6.3s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=216 paired 1:1; disjointness G-ball D2=4rho2=11377/4 (coord bound (31, 31, 11)), ball sizes 35..35 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 10.2s | audit re-derived 12 cells x 18 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 216 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1152 shared-vertex G-equidistance checks, 6912 vertex-side checks, 216 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 13.1s | tables T=12 nbrs=18 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 108, 1380, 20454], free=[1, 12, 115, 1742]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 108, 1380, 20454, 329736], free=[1, 12, 115, 1742, 27478], one-sided=[1, 12, 115, 1742, 27478], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 12s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #109 `60eb4282db04fca2` — IT(179) P6_522, f=(30, 45, 17), p=3^2 4^6 5^2 6^3 8^4, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 11/8, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b; metric-thin: P5-only). Candidate wall time 23.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(179) P6_522 p=(1/12, 3/8, 1/6) c/a=11/8 G=diag(64,64,121) period=24 n_conv=12 T=12 site=1 dim=3 f=(30,45,17) p-vec 3^2 4^6 5^2 6^3 8^4 aut=1 W=2 nonsimple=0 cutoff_D2=278784 4rho2_G=24735856/675 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 2.5s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=204 paired 1:1; disjointness G-ball D2=4rho2=24735856/675 (coord bound (28, 28, 18)), ball sizes 39..39 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 8.6s | audit re-derived 12 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 204 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 1080 shared-vertex G-equidistance checks, 6120 vertex-side checks, 204 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 11.6s | tables T=12 nbrs=17 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 102, 1248, 17742], free=[1, 12, 104, 1519]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 102, 1248, 17742, 274212], free=[1, 12, 104, 1519, 22851], one-sided=[1, 12, 104, 1519, 22851], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 11s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #110 `f43b45fd6383b36b` — IT(155) R32, f=(26, 41, 17), p=3^4 4^5 5^4 6^1 8^3, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 19/16, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 3 b; metric-thin: P5-only). Candidate wall time 7.5s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(155) R32 p=(1/8, 1/6, 5/12) c/a=19/16 G=diag(256,256,361) period=24 n_conv=18 T=6 site=1 dim=3 f=(26,41,17) p-vec 3^4 4^5 5^4 6^1 8^3 aut=1 W=2 nonsimple=4 cutoff_D2=831744 4rho2_G=141968 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.2s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=102 paired 1:1; disjointness G-ball D2=4rho2=141968 (coord bound (28, 28, 20)), ball sizes 73..73 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 2.3s | audit re-derived 6 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 102 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 492 shared-vertex G-equidistance checks, 2652 vertex-side checks, 102 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.6s | tables T=6 nbrs=17 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 51, 628, 8994], free=[1, 11, 106, 1528]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 51, 628, 8994, 140148], free=[1, 11, 106, 1528, 23358], one-sided=[1, 11, 106, 1528, 23358], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #111 `4ff9d77aa9f8194a` — IT(167) R-3c, f=(24, 37, 15), p=3^2 4^7 6^4 8^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 3/4, site stabilizer 1, orbit 36 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 8 b). Candidate wall time 14.1s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.5s | IT(167) R-3c p=(1/8, 1/6, 5/12) c/a=3/4 G=diag(16,16,9) period=24 n_conv=36 T=12 site=1 dim=3 f=(24,37,15) p-vec 3^2 4^7 6^4 8^2 aut=1 W=2 nonsimple=2 cutoff_D2=36864 4rho2_G=1920 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 3.7s | detL=4608 T=12 vol=384 T*vol=4608 (crystal-basis measure) slots=180 paired 1:1; disjointness G-ball D2=4rho2=1920 (coord bound (13, 13, 15)), ball sizes 21..21 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 3.3s | audit re-derived 12 cells x 15 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 384 each, T*vol == |det|; all 180 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 888 shared-vertex G-equidistance checks, 4320 vertex-side checks, 180 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.5s | tables T=12 nbrs=15 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: 6 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 90, 940, 11346], free=[1, 10, 79, 971]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 90, 940, 11346, 148812], free=[1, 10, 79, 971, 12401], one-sided=[2, 19, 158, 1931, 24802], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #112 `6de3dac5f334cfed` — IT(167) R-3c, f=(26, 40, 16), p=3^4 4^6 6^2 8^4, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1/2, site stabilizer 1, orbit 36 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b). Candidate wall time 20.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.7s | IT(167) R-3c p=(1/8, 1/6, 5/12) c/a=1/2 G=diag(4,4,1) period=24 n_conv=36 T=12 site=1 dim=3 f=(26,40,16) p-vec 3^4 4^6 6^2 8^4 aut=1 W=2 nonsimple=2 cutoff_D2=9216 4rho2_G=3856/9 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 5.9s | detL=4608 T=12 vol=384 T*vol=4608 (crystal-basis measure) slots=192 paired 1:1; disjointness G-ball D2=4rho2=3856/9 (coord bound (12, 12, 21)), ball sizes 25..25 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 4.6s | audit re-derived 12 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 384 each, T*vol == |det|; all 192 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 960 shared-vertex G-equidistance checks, 4992 vertex-side checks, 192 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 9.5s | tables T=12 nbrs=16 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: 6 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 96, 1096, 14538], free=[1, 11, 92, 1246]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 96, 1096, 14538, 209316], free=[1, 11, 92, 1246, 17443], one-sided=[2, 21, 184, 2478, 34886], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 9s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #113 `105e41c2798e6180` — IT(148) R-3, f=(16, 27, 13), p=3^6 4^3 6^4, aut=6

Witness point (0, 0, 5/24), c/a = 2, site stabilizer 3, orbit 6 conventional / 2 primitive, stratum dim 1. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 1.5s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(148) R-3 p=(0, 0, 5/24) c/a=2 G=diag(2,2,8) period=24 n_conv=6 T=2 site=3 dim=1 f=(16,27,13) p-vec 3^6 4^3 6^4 aut=6 W=2 nonsimple=4 cutoff_D2=18432 4rho2_G=1568 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.3s | detL=4608 T=2 vol=2304 T*vol=4608 (crystal-basis measure) slots=26 paired 1:1; disjointness G-ball D2=4rho2=1568 (coord bound (33, 33, 14)), ball sizes 23..23 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.1s | audit re-derived 2 cells x 13 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 26 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 108 shared-vertex G-equidistance checks, 416 vertex-side checks, 26 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=3, Isom_fix_site=6, Isom(solid)=6 (Isom+=3, improper=3; solid achiral), aut_comb=6; chain site<=Isom_fix (linear parts) contained, divisibility 3|6|6|6 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=6: full symmetry group of the honeycomb is LARGER than G (|H_cell|=6) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.0s | tables T=2 nbrs=13 |ops|=12 (6 proper, 6 improper; T*|site|=6), identity+closure exact; hands: inconsistent (achiral solid); banked enumerate n<=4: fixed=[2, 13, 120, 1271], free=[1, 4, 16, 143]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[2, 13, 120, 1271, 14576], free=[1, 4, 16, 143, 1327], one-sided=[1, 4, 20, 228, 2432], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 3 <= Isom_fix_site 6 <= Isom(solid) 6 (Isom+ 3, solid achiral) <= combinatorial aut 6 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 6: the full symmetry group of the honeycomb is LARGER than G.

### #114 `542cbe76934b484b` — IT(154) P3_221, f=(29, 44, 17), p=3^6 4^2 5^2 6^3 8^3 10^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 5/4, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 8.4s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(154) P3_221 p=(1/8, 1/6, 5/12) c/a=5/4 G=diag(16,16,25) period=24 n_conv=6 T=6 site=1 dim=3 f=(29,44,17) p-vec 3^6 4^2 5^2 6^3 8^3 10^1 aut=1 W=2 nonsimple=1 cutoff_D2=57600 4rho2_G=233404096/21025 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=102 paired 1:1; disjointness G-ball D2=4rho2=233404096/21025 (coord bound (31, 31, 22)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 3.8s | audit re-derived 6 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 102 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 528 shared-vertex G-equidistance checks, 2958 vertex-side checks, 102 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.8s | tables T=6 nbrs=17 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 51, 624, 8883], free=[1, 10, 104, 1498]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 51, 624, 8883, 137544], free=[1, 10, 104, 1498, 22924], one-sided=[1, 10, 104, 1498, 22924], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 4s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #115 `75bbbcb4a37e70e8` — IT(146) R3, f=(27, 41, 16), p=3^2 4^4 5^4 6^2 7^4, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 67/80, site stabilizer 1, orbit 9 conventional / 3 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b; metric-thin: P5-only). Candidate wall time 3.4s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(146) R3 p=(1/8, 1/6, 5/12) c/a=67/80 G=diag(6400,6400,4489) period=24 n_conv=9 T=3 site=1 dim=3 f=(27,41,16) p-vec 3^2 4^4 5^4 6^2 7^4 aut=1 W=2 nonsimple=1 cutoff_D2=14745600 4rho2_G=2918464 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.4s | detL=4608 T=3 vol=1536 T*vol=4608 (crystal-basis measure) slots=48 paired 1:1; disjointness G-ball D2=4rho2=2918464 (coord bound (25, 25, 26)), ball sizes 42..42 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.6s | audit re-derived 3 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1536 each, T*vol == |det|; all 48 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 246 shared-vertex G-equidistance checks, 1296 vertex-side checks, 48 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=3 (0 improper) vs T*|site|=3: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.2s | tables T=3 nbrs=16 |ops|=3 (3 proper, 0 improper; T*|site|=3), identity+closure exact; hands: 0 of 3 classes of the other hand; banked enumerate n<=4: fixed=[3, 24, 272, 3591], free=[1, 8, 92, 1197]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[3, 24, 272, 3591, 51594], free=[1, 8, 92, 1197, 17198], one-sided=[1, 8, 92, 1197, 17198], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 3 (0 improper) vs T*|site| = 3: the full symmetry group of the honeycomb IS exactly the generating group G.

### #116 `cff2d5fb5e0d4149` — IT(171) P6_2, f=(23, 35, 14), p=4^5 5^6 6^1 7^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 1/2, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b). Candidate wall time 4.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(171) P6_2 p=(1/12, 3/8, 1/6) c/a=1/2 G=diag(4,4,1) period=24 n_conv=6 T=6 site=1 dim=3 f=(23,35,14) p-vec 4^5 5^6 6^1 7^2 aut=1 W=2 nonsimple=1 cutoff_D2=9216 4rho2_G=1136 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=84 paired 1:1; disjointness G-ball D2=4rho2=1136 (coord bound (20, 20, 34)), ball sizes 20..20 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.6s | audit re-derived 6 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 84 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 420 shared-vertex G-equidistance checks, 1932 vertex-side checks, 84 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.9s | tables T=6 nbrs=14 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 42, 414, 4686], free=[1, 8, 69, 790]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 42, 414, 4686, 57600], free=[1, 8, 69, 790, 9600], one-sided=[1, 8, 69, 790, 9600], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #117 `4b6055c7aa3d341b` — IT(178) P6_122, f=(25, 38, 15), p=3^2 4^4 5^5 6^1 7^2 9^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 17/8, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b; metric-thin: P5-only). Candidate wall time 16.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.5s | IT(178) P6_122 p=(1/8, 1/6, 5/12) c/a=17/8 G=diag(64,64,289) period=24 n_conv=12 T=12 site=1 dim=3 f=(25,38,15) p-vec 3^2 4^4 5^5 6^1 7^2 9^1 aut=1 W=2 nonsimple=1 cutoff_D2=665856 4rho2_G=33840688/867 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 4.1s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=180 paired 1:1; disjointness G-ball D2=4rho2=33840688/867 (coord bound (29, 29, 12)), ball sizes 26..26 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 4.2s | audit re-derived 12 cells x 15 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 180 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 912 shared-vertex G-equidistance checks, 4500 vertex-side checks, 180 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 7.2s | tables T=12 nbrs=15 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 90, 972, 12210], free=[1, 10, 81, 1043]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 90, 972, 12210, 166920], free=[1, 10, 81, 1043, 13910], one-sided=[1, 10, 81, 1043, 13910], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #118 `7e79f1c38b5516bf` — IT(178) P6_122, f=(22, 34, 14), p=3^4 4^2 5^4 6^2 8^2, aut=2

Witness point (0, 1/4, 1/3), c/a = 3/2, site stabilizer 2, orbit 6 conventional / 6 primitive, stratum dim 1. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 4.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(178) P6_122 p=(0, 1/4, 1/3) c/a=3/2 G=diag(4,4,9) period=12 n_conv=6 T=6 site=2 dim=1 f=(22,34,14) p-vec 3^4 4^2 5^4 6^2 8^2 aut=2 W=2 nonsimple=2 cutoff_D2=5184 4rho2_G=660 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.5s | detL=1728 T=6 vol=288 T*vol=1728 (crystal-basis measure) slots=84 paired 1:1; disjointness G-ball D2=4rho2=660 (coord bound (15, 15, 9)), ball sizes 24..24 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.2s | audit re-derived 6 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 288 each, T*vol == |det|; all 84 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 408 shared-vertex G-equidistance checks, 1848 vertex-side checks, 84 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.1s | tables T=6 nbrs=14 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 42, 426, 5058], free=[1, 5, 39, 437]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 42, 426, 5058, 65364], free=[1, 5, 39, 437, 5485], one-sided=[1, 5, 39, 437, 5485], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #119 `d7c638d7fa23127e` — IT(169) P6_1, f=(25, 39, 16), p=3^4 4^4 5^4 7^2 8^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 3/2, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 6.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(169) P6_1 p=(1/12, 3/8, 1/6) c/a=3/2 G=diag(4,4,9) period=24 n_conv=6 T=6 site=1 dim=3 f=(25,39,16) p-vec 3^4 4^4 5^4 7^2 8^2 aut=1 W=2 nonsimple=3 cutoff_D2=20736 4rho2_G=23488/9 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.7s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=96 paired 1:1; disjointness G-ball D2=4rho2=23488/9 (coord bound (30, 30, 18)), ball sizes 26..26 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 2.4s | audit re-derived 6 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 96 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 468 shared-vertex G-equidistance checks, 2400 vertex-side checks, 96 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.0s | tables T=6 nbrs=16 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 48, 552, 7380], free=[1, 8, 92, 1230]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 48, 552, 7380, 107100], free=[1, 8, 92, 1230, 17850], one-sided=[1, 8, 92, 1230, 17850], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #120 `0417061f8f56488e` — IT(152) P3_121, f=(20, 32, 14), p=3^4 4^5 6^4 8^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 1/2, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 9 b). Candidate wall time 3.5s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(152) P3_121 p=(1/12, 3/8, 1/6) c/a=1/2 G=diag(4,4,1) period=24 n_conv=6 T=6 site=1 dim=3 f=(20,32,14) p-vec 3^4 4^5 6^4 8^1 aut=1 W=2 nonsimple=4 cutoff_D2=9216 4rho2_G=571120/441 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=84 paired 1:1; disjointness G-ball D2=4rho2=571120/441 (coord bound (21, 21, 36)), ball sizes 27..27 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.9s | audit re-derived 6 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 84 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 384 shared-vertex G-equidistance checks, 1680 vertex-side checks, 84 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.9s | tables T=6 nbrs=14 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 42, 426, 4998], free=[1, 9, 71, 853]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 42, 426, 4998, 63630], free=[1, 9, 71, 853, 10605], one-sided=[1, 9, 71, 853, 10605], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #121 `6cc34ed38aa354e1` — IT(181) P6_422, f=(22, 34, 14), p=3^2 4^4 5^4 6^3 8^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 1/2, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b). Candidate wall time 9.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(181) P6_422 p=(1/12, 3/8, 1/6) c/a=1/2 G=diag(4,4,1) period=24 n_conv=12 T=12 site=1 dim=3 f=(22,34,14) p-vec 3^2 4^4 5^4 6^3 8^1 aut=1 W=2 nonsimple=2 cutoff_D2=9216 4rho2_G=1136 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.8s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=168 paired 1:1; disjointness G-ball D2=4rho2=1136 (coord bound (20, 20, 34)), ball sizes 41..41 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 2.3s | audit re-derived 12 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 168 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 816 shared-vertex G-equidistance checks, 3696 vertex-side checks, 168 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 5.4s | tables T=12 nbrs=14 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 84, 828, 9516], free=[1, 12, 69, 840]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 84, 828, 9516, 119112], free=[1, 12, 69, 840, 9926], one-sided=[1, 12, 69, 840, 9926], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 5s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #122 `5838282f46223111` — IT(152) P3_121, f=(29, 44, 17), p=3^2 4^9 6^2 8^3 10^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 7/4, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 8.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(152) P3_121 p=(1/8, 1/6, 5/12) c/a=7/4 G=diag(16,16,49) period=24 n_conv=6 T=6 site=1 dim=3 f=(29,44,17) p-vec 3^2 4^9 6^2 8^3 10^1 aut=1 W=2 nonsimple=1 cutoff_D2=112896 4rho2_G=602368/49 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.9s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=102 paired 1:1; disjointness G-ball D2=4rho2=602368/49 (coord bound (33, 33, 16)), ball sizes 28..28 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 3.4s | audit re-derived 6 cells x 17 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 102 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 528 shared-vertex G-equidistance checks, 2958 vertex-side checks, 102 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.8s | tables T=6 nbrs=17 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 51, 624, 8766], free=[1, 10, 104, 1478]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 51, 624, 8766, 133446], free=[1, 10, 104, 1478, 22241], one-sided=[1, 10, 104, 1478, 22241], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #123 `cda1d1c03659b67d` — IT(148) R-3, f=(22, 34, 14), p=4^6 5^4 6^4, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 527/1000, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 7 b). Candidate wall time 5.4s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(148) R-3 p=(1/8, 1/6, 5/12) c/a=527/1000 G=diag(1000000,1000000,277729) period=24 n_conv=18 T=6 site=1 dim=3 f=(22,34,14) p-vec 4^6 5^4 6^4 aut=1 W=2 nonsimple=2 cutoff_D2=2304000000 4rho2_G=2796440612815295559632/16788891630625 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.4s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=84 paired 1:1; disjointness G-ball D2=4rho2=2796440612815295559632/16788891630625 (coord bound (15, 15, 25)), ball sizes 26..26 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.8s | audit re-derived 6 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 84 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 408 shared-vertex G-equidistance checks, 1848 vertex-side checks, 84 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (3 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.8s | tables T=6 nbrs=14 |ops|=6 (3 proper, 3 improper; T*|site|=6), identity+closure exact; hands: 3 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 42, 410, 4599], free=[1, 8, 69, 778]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 42, 410, 4599, 56052], free=[1, 8, 69, 778, 9342], one-sided=[2, 14, 138, 1533, 18684], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (3 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #124 `161b09808f4c1863` — IT(178) P6_122, f=(18, 30, 14), p=3^4 4^6 6^4, aut=4

Witness point (0, 1/3, 1/3), c/a = 2, site stabilizer 2, orbit 6 conventional / 6 primitive, stratum dim 1. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 4.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(178) P6_122 p=(0, 1/3, 1/3) c/a=2 G=diag(2,2,8) period=12 n_conv=6 T=6 site=2 dim=1 f=(18,30,14) p-vec 3^4 4^6 6^4 aut=4 W=2 nonsimple=6 cutoff_D2=4608 4rho2_G=992/3 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=1728 T=6 vol=288 T*vol=1728 (crystal-basis measure) slots=84 paired 1:1; disjointness G-ball D2=4rho2=992/3 (coord bound (15, 15, 7)), ball sizes 22..22 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.5s | audit re-derived 6 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 288 each, T*vol == |det|; all 84 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 360 shared-vertex G-equidistance checks, 1512 vertex-side checks, 84 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=4; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|4 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.0s | tables T=6 nbrs=14 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 42, 426, 5088], free=[1, 5, 39, 439]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 42, 426, 5088, 66312], free=[1, 5, 39, 439, 5567], one-sided=[1, 5, 39, 439, 5567], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 4 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #125 `c92eef8763d02d8a` — IT(179) P6_522, f=(25, 39, 16), p=3^2 4^8 5^2 7^2 8^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 3/2, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 16.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(179) P6_522 p=(1/12, 3/8, 1/6) c/a=3/2 G=diag(4,4,9) period=24 n_conv=12 T=12 site=1 dim=3 f=(25,39,16) p-vec 3^2 4^8 5^2 7^2 8^2 aut=1 W=2 nonsimple=3 cutoff_D2=20736 4rho2_G=7360/3 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 2.5s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=192 paired 1:1; disjointness G-ball D2=4rho2=7360/3 (coord bound (29, 29, 17)), ball sizes 47..47 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 3.7s | audit re-derived 12 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 192 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 936 shared-vertex G-equidistance checks, 4800 vertex-side checks, 192 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 9.6s | tables T=12 nbrs=16 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 96, 1128, 15474], free=[1, 11, 94, 1323]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 96, 1128, 15474, 231060], free=[1, 11, 94, 1323, 19255], one-sided=[1, 11, 94, 1323, 19255], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 9s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #126 `3a491fd6426d90b2` — IT(146) R3, f=(24, 38, 16), p=3^4 4^4 5^2 6^4 7^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 33/32, site stabilizer 1, orbit 9 conventional / 3 primitive, stratum dim 3. Open/wall label (triage, carried): indeterminate (triage, 2 b; metric-thin: P5-only). Candidate wall time 2.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(146) R3 p=(1/8, 1/6, 5/12) c/a=33/32 G=diag(1024,1024,1089) period=24 n_conv=9 T=3 site=1 dim=3 f=(24,38,16) p-vec 3^4 4^4 5^2 6^4 7^2 aut=1 W=2 nonsimple=4 cutoff_D2=2509056 4rho2_G=68159744/121 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.4s | detL=4608 T=3 vol=1536 T*vol=4608 (crystal-basis measure) slots=48 paired 1:1; disjointness G-ball D2=4rho2=68159744/121 (coord bound (28, 28, 23)), ball sizes 40..40 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.0s | audit re-derived 3 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1536 each, T*vol == |det|; all 48 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 228 shared-vertex G-equidistance checks, 1152 vertex-side checks, 48 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=3 (0 improper) vs T*|site|=3: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.2s | tables T=3 nbrs=16 |ops|=3 (3 proper, 0 improper; T*|site|=3), identity+closure exact; hands: 0 of 3 classes of the other hand; banked enumerate n<=4: fixed=[3, 24, 278, 3759], free=[1, 8, 94, 1253]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[3, 24, 278, 3759, 55368], free=[1, 8, 94, 1253, 18456], one-sided=[1, 8, 94, 1253, 18456], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 3 (0 improper) vs T*|site| = 3: the full symmetry group of the honeycomb IS exactly the generating group G.

### #127 `5b679d8b0a3147c3` — IT(152) P3_121, f=(24, 38, 16), p=3^6 4^5 7^2 8^3, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 17/16, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): indeterminate (triage, 2 b; metric-thin: P5-only). Candidate wall time 5.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(152) P3_121 p=(1/12, 3/8, 1/6) c/a=17/16 G=diag(256,256,289) period=24 n_conv=6 T=6 site=1 dim=3 f=(24,38,16) p-vec 3^6 4^5 7^2 8^3 aut=1 W=2 nonsimple=4 cutoff_D2=665856 4rho2_G=75330880/441 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.5s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=96 paired 1:1; disjointness G-ball D2=4rho2=75330880/441 (coord bound (30, 30, 25)), ball sizes 39..39 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.7s | audit re-derived 6 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 96 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 456 shared-vertex G-equidistance checks, 2304 vertex-side checks, 96 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.7s | tables T=6 nbrs=16 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 48, 552, 7353], free=[1, 10, 92, 1248]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 48, 552, 7353, 106230], free=[1, 10, 92, 1248, 17705], one-sided=[1, 10, 92, 1248, 17705], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #128 `fac4317d5a65b959` — IT(148) R-3, f=(24, 38, 16), p=3^6 4^2 5^2 6^2 7^4, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 9/8, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): indeterminate (triage, 2 b; metric-thin: P5-only). Candidate wall time 6.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(148) R-3 p=(1/8, 1/6, 5/12) c/a=9/8 G=diag(64,64,81) period=24 n_conv=18 T=6 site=1 dim=3 f=(24,38,16) p-vec 3^6 4^2 5^2 6^2 7^4 aut=1 W=2 nonsimple=4 cutoff_D2=186624 4rho2_G=35344 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.2s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=96 paired 1:1; disjointness G-ball D2=4rho2=35344 (coord bound (28, 28, 21)), ball sizes 78..78 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.7s | audit re-derived 6 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 96 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 456 shared-vertex G-equidistance checks, 2304 vertex-side checks, 96 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (3 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.8s | tables T=6 nbrs=16 |ops|=6 (3 proper, 3 improper; T*|site|=6), identity+closure exact; hands: 3 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 48, 544, 7146], free=[1, 9, 92, 1205]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 48, 544, 7146, 102126], free=[1, 9, 92, 1205, 17021], one-sided=[2, 16, 184, 2382, 34042], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (3 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #129 `27d463eac6cda5ea` — IT(171) P6_2, f=(27, 41, 16), p=3^2 4^7 6^4 8^3, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 5331/8000, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): indeterminate (triage, 2 b; metric-thin: P5-only). Candidate wall time 7.1s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(171) P6_2 p=(1/12, 3/8, 1/6) c/a=5331/8000 G=diag(64000000,64000000,28419561) period=24 n_conv=6 T=6 site=1 dim=3 f=(27,41,16) p-vec 3^2 4^7 6^4 8^3 aut=1 W=2 nonsimple=1 cutoff_D2=147456000000 4rho2_G=557968647495515728/26265625 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=96 paired 1:1; disjointness G-ball D2=4rho2=557968647495515728/26265625 (coord bound (22, 22, 28)), ball sizes 23..23 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 3.4s | audit re-derived 6 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 96 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 492 shared-vertex G-equidistance checks, 2592 vertex-side checks, 96 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.0s | tables T=6 nbrs=16 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 48, 552, 7350], free=[1, 9, 92, 1236]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 48, 552, 7350, 106446], free=[1, 9, 92, 1236, 17741], one-sided=[1, 9, 92, 1236, 17741], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #130 `919d30fd9021b5ee` — IT(154) P3_221, f=(25, 38, 15), p=3^3 4^3 5^2 6^4 7^3, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 51/32, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 3 b; metric-thin: P5-only). Candidate wall time 4.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(154) P3_221 p=(1/12, 3/8, 1/6) c/a=51/32 G=diag(1024,1024,2601) period=24 n_conv=6 T=6 site=1 dim=3 f=(25,38,15) p-vec 3^3 4^3 5^2 6^4 7^3 aut=1 W=2 nonsimple=1 cutoff_D2=5992704 4rho2_G=202443328/289 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.6s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=90 paired 1:1; disjointness G-ball D2=4rho2=202443328/289 (coord bound (31, 31, 17)), ball sizes 23..23 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.9s | audit re-derived 6 cells x 15 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 90 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 456 shared-vertex G-equidistance checks, 2250 vertex-side checks, 90 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.2s | tables T=6 nbrs=15 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 45, 474, 5772], free=[1, 10, 79, 987]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 45, 474, 5772, 76500], free=[1, 10, 79, 987, 12750], one-sided=[1, 10, 79, 987, 12750], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #131 `6074c5fa5d2dffc5` — IT(148) R-3, f=(16, 26, 12), p=3^2 4^5 5^4 6^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 3/4, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 19 b). Candidate wall time 2.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(148) R-3 p=(1/12, 3/8, 1/6) c/a=3/4 G=diag(16,16,9) period=24 n_conv=18 T=6 site=1 dim=3 f=(16,26,12) p-vec 3^2 4^5 5^4 6^1 aut=1 W=2 nonsimple=3 cutoff_D2=36864 4rho2_G=4864 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.0s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=72 paired 1:1; disjointness G-ball D2=4rho2=4864 (coord bound (21, 21, 24)), ball sizes 43..43 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.4s | audit re-derived 6 cells x 12 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 72 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 312 shared-vertex G-equidistance checks, 1152 vertex-side checks, 72 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (3 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.0s | tables T=6 nbrs=12 |ops|=6 (3 proper, 3 improper; T*|site|=6), identity+closure exact; hands: 3 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 36, 296, 2820], free=[1, 7, 50, 479]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 36, 296, 2820, 29244], free=[1, 7, 50, 479, 4874], one-sided=[2, 12, 100, 940, 9748], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (3 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #132 `5e68ffe7582a0657` — IT(167) R-3c, f=(20, 31, 13), p=3^4 4^3 6^5 8^1, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 1/2, site stabilizer 1, orbit 36 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 8 b). Candidate wall time 10.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.6s | IT(167) R-3c p=(1/12, 3/8, 1/6) c/a=1/2 G=diag(4,4,1) period=24 n_conv=36 T=12 site=1 dim=3 f=(20,31,13) p-vec 3^4 4^3 6^5 8^1 aut=1 W=2 nonsimple=2 cutoff_D2=9216 4rho2_G=832 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 5.0s | detL=4608 T=12 vol=384 T*vol=4608 (crystal-basis measure) slots=156 paired 1:1; disjointness G-ball D2=4rho2=832 (coord bound (17, 17, 29)), ball sizes 79..79 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.7s | audit re-derived 12 cells x 13 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 384 each, T*vol == |det|; all 156 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 744 shared-vertex G-equidistance checks, 3120 vertex-side checks, 156 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.3s | tables T=12 nbrs=13 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: 6 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 78, 672, 6594], free=[1, 9, 56, 571]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 78, 672, 6594, 69876], free=[1, 9, 56, 571, 5823], one-sided=[2, 17, 112, 1132, 11646], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #133 `1ba26ab2c0999b93` — IT(148) R-3, f=(20, 32, 14), p=3^4 4^3 5^2 6^5, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 1/2, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b). Candidate wall time 4.6s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(148) R-3 p=(1/12, 3/8, 1/6) c/a=1/2 G=diag(4,4,1) period=24 n_conv=18 T=6 site=1 dim=3 f=(20,32,14) p-vec 3^4 4^3 5^2 6^5 aut=1 W=2 nonsimple=3 cutoff_D2=9216 4rho2_G=1136 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.5s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=84 paired 1:1; disjointness G-ball D2=4rho2=1136 (coord bound (20, 20, 34)), ball sizes 68..68 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.8s | audit re-derived 6 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 84 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 384 shared-vertex G-equidistance checks, 1680 vertex-side checks, 84 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (3 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.9s | tables T=6 nbrs=14 |ops|=6 (3 proper, 3 improper; T*|site|=6), identity+closure exact; hands: 3 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 42, 422, 4947], free=[1, 8, 71, 837]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 42, 422, 4947, 63366], free=[1, 8, 71, 837, 10561], one-sided=[2, 14, 142, 1649, 21122], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (3 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #134 `27dbb77012555d28` — IT(161) R3c, f=(26, 40, 16), p=3^4 4^2 5^6 6^2 9^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 4439/8000, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b,P5-only). Candidate wall time 8.4s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.4s | IT(161) R3c p=(1/12, 3/8, 1/6) c/a=4439/8000 G=diag(64000000,64000000,19704721) period=24 n_conv=18 T=6 site=1 dim=3 f=(26,40,16) p-vec 3^4 4^2 5^6 6^2 9^2 aut=1 W=2 nonsimple=2 cutoff_D2=147456000000 4rho2_G=13845479824 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.6s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=96 paired 1:1; disjointness G-ball D2=4rho2=13845479824 (coord bound (17, 17, 27)), ball sizes 38..38 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 3.7s | audit re-derived 6 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 96 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 480 shared-vertex G-equidistance checks, 2496 vertex-side checks, 96 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (3 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.6s | tables T=6 nbrs=16 |ops|=6 (3 proper, 3 improper; T*|site|=6), identity+closure exact; hands: 3 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 48, 524, 6618], free=[1, 8, 88, 1103]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 48, 524, 6618, 90924], free=[1, 8, 88, 1103, 15154], one-sided=[2, 16, 176, 2206, 30308], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (3 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #135 `c18a9b1cb2a5d168` — IT(148) R-3, f=(26, 40, 16), p=3^6 4^1 5^2 6^1 7^6, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1/2, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 7.1s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.4s | IT(148) R-3 p=(1/8, 1/6, 5/12) c/a=1/2 G=diag(4,4,1) period=24 n_conv=18 T=6 site=1 dim=3 f=(26,40,16) p-vec 3^6 4^1 5^2 6^1 7^6 aut=1 W=2 nonsimple=2 cutoff_D2=9216 4rho2_G=1394416/2187 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.6s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=96 paired 1:1; disjointness G-ball D2=4rho2=1394416/2187 (coord bound (15, 15, 26)), ball sizes 26..26 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 2.3s | audit re-derived 6 cells x 16 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 96 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 480 shared-vertex G-equidistance checks, 2496 vertex-side checks, 96 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (3 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.7s | tables T=6 nbrs=16 |ops|=6 (3 proper, 3 improper; T*|site|=6), identity+closure exact; hands: 3 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 48, 536, 6909], free=[1, 9, 90, 1166]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 48, 536, 6909, 96756], free=[1, 9, 90, 1166, 16126], one-sided=[2, 16, 180, 2303, 32252], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (3 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #136 `d1f1121757598de0` — IT(154) P3_221, f=(15, 25, 12), p=3^2 4^8 6^2, aut=2

Witness point (1/8, 1/6, 5/12), c/a = 9/4, site stabilizer 1, orbit 6 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): indeterminate (triage, 2 b). Candidate wall time 2.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(154) P3_221 p=(1/8, 1/6, 5/12) c/a=9/4 G=diag(16,16,81) period=24 n_conv=6 T=6 site=1 dim=3 f=(15,25,12) p-vec 3^2 4^8 6^2 aut=2 W=2 nonsimple=5 cutoff_D2=186624 4rho2_G=116992/9 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.8s | detL=13824 T=6 vol=2304 T*vol=13824 (crystal-basis measure) slots=72 paired 1:1; disjointness G-ball D2=4rho2=116992/9 (coord bound (33, 33, 13)), ball sizes 26..26 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.3s | audit re-derived 6 cells x 12 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 2304 each, T*vol == |det|; all 72 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 300 shared-vertex G-equidistance checks, 1080 vertex-side checks, 72 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.0s | tables T=6 nbrs=12 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 36, 300, 2850], free=[1, 7, 50, 483]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 36, 300, 2850, 29292], free=[1, 7, 50, 483, 4882], one-sided=[1, 7, 50, 483, 4882], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #137 `b27ba8dbcbc2891a` — IT(161) R3c, f=(22, 34, 14), p=4^8 6^6, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1/2, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): open-likely (triage, 4 b). Candidate wall time 5.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(161) R3c p=(1/8, 1/6, 5/12) c/a=1/2 G=diag(4,4,1) period=24 n_conv=18 T=6 site=1 dim=3 f=(22,34,14) p-vec 4^8 6^6 aut=1 W=2 nonsimple=2 cutoff_D2=9216 4rho2_G=99004960/186003 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.6s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=84 paired 1:1; disjointness G-ball D2=4rho2=99004960/186003 (coord bound (14, 14, 24)), ball sizes 18..18 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.4s | audit re-derived 6 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 84 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 408 shared-vertex G-equidistance checks, 1848 vertex-side checks, 84 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (3 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.6s | tables T=6 nbrs=14 |ops|=6 (3 proper, 3 improper; T*|site|=6), identity+closure exact; hands: 3 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 42, 410, 4614], free=[1, 7, 69, 769]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 42, 410, 4614, 56418], free=[1, 7, 69, 769, 9403], one-sided=[2, 14, 138, 1538, 18806], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (3 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #138 `457c20cf036ae496` — IT(180) P6_222, f=(11, 20, 11), p=3^6 4^3 5^2, aut=2

Witness point (0, 1/2, 0), c/a = 3/2, site stabilizer 2, orbit 6 conventional / 6 primitive, stratum dim 1. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 1.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(180) P6_222 p=(0, 1/2, 0) c/a=3/2 G=diag(4,4,9) period=12 n_conv=6 T=6 site=2 dim=1 f=(11,20,11) p-vec 3^6 4^3 5^2 aut=2 W=2 nonsimple=7 cutoff_D2=5184 4rho2_G=720 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.3s | detL=1728 T=6 vol=288 T*vol=1728 (crystal-basis measure) slots=66 paired 1:1; disjointness G-ball D2=4rho2=720 (coord bound (16, 16, 9)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.1s | audit re-derived 6 cells x 11 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 288 each, T*vol == |det|; all 66 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 240 shared-vertex G-equidistance checks, 726 vertex-side checks, 66 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.5s | tables T=6 nbrs=11 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 33, 258, 2352], free=[1, 5, 24, 214]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 33, 258, 2352, 23412], free=[1, 5, 24, 214, 1973], one-sided=[1, 5, 24, 214, 1973], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #139 `11a9fe078850b5cd` — IT(179) P6_522, f=(25, 38, 15), p=3^2 4^3 5^4 6^4 7^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 65/32, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b,P5-only). Candidate wall time 14.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.4s | IT(179) P6_522 p=(1/8, 1/6, 5/12) c/a=65/32 G=diag(1024,1024,4225) period=24 n_conv=12 T=12 site=1 dim=3 f=(25,38,15) p-vec 3^2 4^3 5^4 6^4 7^2 aut=1 W=2 nonsimple=1 cutoff_D2=9734400 4rho2_G=8324792368/12675 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 3.6s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=180 paired 1:1; disjointness G-ball D2=4rho2=8324792368/12675 (coord bound (30, 30, 13)), ball sizes 33..33 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 4.1s | audit re-derived 12 cells x 15 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 180 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 912 shared-vertex G-equidistance checks, 4500 vertex-side checks, 180 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.6s | tables T=12 nbrs=15 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 90, 972, 12168], free=[1, 10, 81, 1039]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 90, 972, 12168, 165612], free=[1, 10, 81, 1039, 13801], one-sided=[1, 10, 81, 1039, 13801], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #140 `5f812747976b224a` — IT(148) R-3, f=(20, 32, 14), p=3^2 4^6 5^4 7^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 39/32, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): indeterminate (triage, 2 b; metric-thin: P5-only). Candidate wall time 4.3s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(148) R-3 p=(1/8, 1/6, 5/12) c/a=39/32 G=diag(1024,1024,1521) period=24 n_conv=18 T=6 site=1 dim=3 f=(20,32,14) p-vec 3^2 4^6 5^4 7^2 aut=1 W=2 nonsimple=4 cutoff_D2=3504384 4rho2_G=569104 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.2s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=84 paired 1:1; disjointness G-ball D2=4rho2=569104 (coord bound (28, 28, 20)), ball sizes 66..66 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.0s | audit re-derived 6 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 84 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 384 shared-vertex G-equidistance checks, 1680 vertex-side checks, 84 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (3 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.8s | tables T=6 nbrs=14 |ops|=6 (3 proper, 3 improper; T*|site|=6), identity+closure exact; hands: 3 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 42, 418, 4818], free=[1, 8, 71, 816]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 42, 418, 4818, 60288], free=[1, 8, 71, 816, 10048], one-sided=[2, 14, 142, 1606, 20096], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (3 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #141 `c95a5fcf4d681568` — IT(166) R-3m, f=(12, 21, 11), p=3^4 4^5 5^2, aut=2

Witness point (1/24, 1/12, 1/6), c/a = 3/2, site stabilizer 2, orbit 18 conventional / 6 primitive, stratum dim 2. Open/wall label (triage, carried): indeterminate (triage, 2 b). Candidate wall time 2.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(166) R-3m p=(1/24, 1/12, 1/6) c/a=3/2 G=diag(4,4,9) period=24 n_conv=18 T=6 site=2 dim=2 f=(12,21,11) p-vec 3^4 4^5 5^2 aut=2 W=2 nonsimple=4 cutoff_D2=20736 4rho2_G=2352 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.1s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=66 paired 1:1; disjointness G-ball D2=4rho2=2352 (coord bound (28, 28, 17)), ball sizes 59..59 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.1s | audit re-derived 6 cells x 11 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 66 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 252 shared-vertex G-equidistance checks, 792 vertex-side checks, 66 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=1, improper=1; solid achiral), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.3s | tables T=6 nbrs=11 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: inconsistent (achiral solid); banked enumerate n<=4: fixed=[6, 33, 254, 2250], free=[1, 5, 24, 206]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 33, 254, 2250, 21660], free=[1, 5, 24, 206, 1827], one-sided=[1, 8, 43, 393, 3610], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 1, solid achiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #142 `f7bd7cd9eae6436b` — IT(166) R-3m, f=(16, 27, 13), p=3^6 4^4 6^2 8^1, aut=2

Witness point (1/12, 1/6, 11/24), c/a = 1, site stabilizer 2, orbit 18 conventional / 6 primitive, stratum dim 2. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 3.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(166) R-3m p=(1/12, 1/6, 11/24) c/a=1 G=diag(2,2,2) period=24 n_conv=18 T=6 site=2 dim=2 f=(16,27,13) p-vec 3^6 4^4 6^2 8^1 aut=2 W=2 nonsimple=5 cutoff_D2=4608 4rho2_G=1064 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.9s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=78 paired 1:1; disjointness G-ball D2=4rho2=1064 (coord bound (27, 27, 24)), ball sizes 84..84 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.3s | audit re-derived 6 cells x 13 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 78 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 324 shared-vertex G-equidistance checks, 1248 vertex-side checks, 78 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=1, improper=1; solid achiral), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 2.3s | tables T=6 nbrs=13 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: inconsistent (achiral solid); banked enumerate n<=4: fixed=[6, 39, 364, 3924], free=[1, 6, 34, 353]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 39, 364, 3924, 45918], free=[1, 6, 34, 353, 3858], one-sided=[1, 9, 62, 675, 7653], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 1, solid achiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #143 `75c9be976d704515` — IT(152) P3_121, f=(18, 28, 12), p=4^8 6^4, aut=2

Witness point (0, 3/8, 1/6), c/a = 9/8, site stabilizer 2, orbit 3 conventional / 3 primitive, stratum dim 1. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b,P5-only). Candidate wall time 1.1s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.0s | IT(152) P3_121 p=(0, 3/8, 1/6) c/a=9/8 G=diag(64,64,81) period=24 n_conv=3 T=3 site=2 dim=1 f=(18,28,12) p-vec 4^8 6^4 aut=2 W=2 nonsimple=2 cutoff_D2=186624 4rho2_G=48960 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.2s | detL=13824 T=3 vol=4608 T*vol=13824 (crystal-basis measure) slots=36 paired 1:1; disjointness G-ball D2=4rho2=48960 (coord bound (32, 32, 25)), ball sizes 22..22 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.3s | audit re-derived 3 cells x 12 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 4608 each, T*vol == |det|; all 36 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 168 shared-vertex G-equidistance checks, 648 vertex-side checks, 36 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 0.6s | tables T=3 nbrs=12 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 3 classes of the other hand; banked enumerate n<=4: fixed=[3, 18, 150, 1443], free=[1, 4, 28, 250]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[3, 18, 150, 1443, 15060], free=[1, 4, 28, 250, 2537], one-sided=[1, 4, 28, 250, 2537], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 0s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #144 `8463196a30c6643f` — IT(179) P6_522, f=(23, 36, 15), p=3^2 4^5 5^2 6^6, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 2, site stabilizer 1, orbit 12 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 12.7s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(179) P6_522 p=(1/8, 1/6, 5/12) c/a=2 G=diag(2,2,8) period=24 n_conv=12 T=12 site=1 dim=3 f=(23,36,15) p-vec 3^2 4^5 5^2 6^6 aut=1 W=2 nonsimple=3 cutoff_D2=18432 4rho2_G=3848/3 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 3.4s | detL=13824 T=12 vol=1152 T*vol=13824 (crystal-basis measure) slots=180 paired 1:1; disjointness G-ball D2=4rho2=3848/3 (coord bound (30, 30, 13)), ball sizes 35..35 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 2.7s | audit re-derived 12 cells x 15 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1152 each, T*vol == |det|; all 180 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 864 shared-vertex G-equidistance checks, 4140 vertex-side checks, 180 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 6.3s | tables T=12 nbrs=15 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 90, 972, 12168], free=[1, 10, 81, 1039]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 90, 972, 12168, 165612], free=[1, 10, 81, 1039, 13801], one-sided=[1, 10, 81, 1039, 13801], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 6s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #145 `487490cdf474e568` — IT(148) R-3, f=(20, 32, 14), p=3^4 4^5 6^3 7^2, aut=1

Witness point (1/12, 3/8, 1/6), c/a = 1277/2000, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): indeterminate (triage, 2 b; metric-thin: P5-only). Candidate wall time 4.5s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(148) R-3 p=(1/12, 3/8, 1/6) c/a=1277/2000 G=diag(4000000,4000000,1630729) period=24 n_conv=18 T=6 site=1 dim=3 f=(20,32,14) p-vec 3^4 4^5 6^3 7^2 aut=1 W=2 nonsimple=3 cutoff_D2=9216000000 4rho2_G=1176366656 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.3s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=84 paired 1:1; disjointness G-ball D2=4rho2=1176366656 (coord bound (20, 20, 27)), ball sizes 49..49 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 1.1s | audit re-derived 6 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 84 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 384 shared-vertex G-equidistance checks, 1680 vertex-side checks, 84 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (3 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.7s | tables T=6 nbrs=14 |ops|=6 (3 proper, 3 improper; T*|site|=6), identity+closure exact; hands: 3 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 42, 410, 4659], free=[1, 8, 69, 788]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 42, 410, 4659, 57768], free=[1, 8, 69, 788, 9628], one-sided=[2, 14, 138, 1553, 19256], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (3 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #146 `f0e2036d295195b4` — IT(152) P3_121, f=(12, 20, 10), p=3^4 4^4 6^2, aut=2

Witness point (0, 1/8, 1/6), c/a = 9/8, site stabilizer 2, orbit 3 conventional / 3 primitive, stratum dim 1. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b,P5-only). Candidate wall time 0.8s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.0s | IT(152) P3_121 p=(0, 1/8, 1/6) c/a=9/8 G=diag(64,64,81) period=24 n_conv=3 T=3 site=2 dim=1 f=(12,20,10) p-vec 3^4 4^4 6^2 aut=2 W=2 nonsimple=4 cutoff_D2=186624 4rho2_G=50176 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.1s | detL=13824 T=3 vol=4608 T*vol=13824 (crystal-basis measure) slots=30 paired 1:1; disjointness G-ball D2=4rho2=50176 (coord bound (33, 33, 25)), ball sizes 24..24 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.1s | audit re-derived 3 cells x 10 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 4608 each, T*vol == |det|; all 30 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 120 shared-vertex G-equidistance checks, 360 vertex-side checks, 30 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 0.5s | tables T=3 nbrs=10 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 3 classes of the other hand; banked enumerate n<=4: fixed=[3, 15, 111, 945], free=[1, 3, 21, 162]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[3, 15, 111, 945, 8691], free=[1, 3, 21, 162, 1468], one-sided=[1, 3, 21, 162, 1468], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 0s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #147 `67b1ede4b021a4fc` — IT(155) R32, f=(17, 29, 14), p=3^4 4^6 5^2 6^2, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 3/2, site stabilizer 1, orbit 18 conventional / 6 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 3.9s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.3s | IT(155) R32 p=(1/8, 1/6, 5/12) c/a=3/2 G=diag(4,4,9) period=24 n_conv=18 T=6 site=1 dim=3 f=(17,29,14) p-vec 3^4 4^6 5^2 6^2 aut=1 W=2 nonsimple=5 cutoff_D2=20736 4rho2_G=2272 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.2s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=84 paired 1:1; disjointness G-ball D2=4rho2=2272 (coord bound (28, 28, 16)), ball sizes 57..57 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.4s | audit re-derived 6 cells x 14 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 84 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 348 shared-vertex G-equidistance checks, 1428 vertex-side checks, 84 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=6 (0 improper) vs T*|site|=6: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.8s | tables T=6 nbrs=14 |ops|=6 (6 proper, 0 improper; T*|site|=6), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 42, 426, 5028], free=[1, 9, 73, 857]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 42, 426, 5028, 64590], free=[1, 9, 73, 857, 10765], one-sided=[1, 9, 73, 857, 10765], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 2s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 6 (0 improper) vs T*|site| = 6: the full symmetry group of the honeycomb IS exactly the generating group G.

### #148 `34e5e7acce18b5cd` — IT(166) R-3m, f=(14, 23, 11), p=3^6 4^2 6^2 8^1, aut=2

Witness point (1/24, 1/12, 5/12), c/a = 3/2, site stabilizer 2, orbit 18 conventional / 6 primitive, stratum dim 2. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 3.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.2s | IT(166) R-3m p=(1/24, 1/12, 5/12) c/a=3/2 G=diag(4,4,9) period=24 n_conv=18 T=6 site=2 dim=2 f=(14,23,11) p-vec 3^6 4^2 6^2 8^1 aut=2 W=2 nonsimple=4 cutoff_D2=20736 4rho2_G=2880 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 1.1s | detL=4608 T=6 vol=768 T*vol=4608 (crystal-basis measure) slots=66 paired 1:1; disjointness G-ball D2=4rho2=2880 (coord bound (31, 31, 18)), ball sizes 90..90 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.2s | audit re-derived 6 cells x 11 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 768 each, T*vol == |det|; all 66 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 276 shared-vertex G-equidistance checks, 924 vertex-side checks, 66 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=1, improper=1; solid achiral), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 1.4s | tables T=6 nbrs=11 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: inconsistent (achiral solid); banked enumerate n<=4: fixed=[6, 33, 262, 2412], free=[1, 5, 25, 218]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 33, 262, 2412, 24120], free=[1, 5, 25, 218, 2032], one-sided=[1, 7, 45, 413, 4020], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 1s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 1, solid achiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #149 `fa9c370d30741970` — IT(180) P6_222, f=(9, 16, 9), p=3^4 4^5, aut=2

Witness point (1/6, 1/3, 0), c/a = 3/2, site stabilizer 2, orbit 6 conventional / 6 primitive, stratum dim 1. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 1.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(180) P6_222 p=(1/6, 1/3, 0) c/a=3/2 G=diag(4,4,9) period=12 n_conv=6 T=6 site=2 dim=1 f=(9,16,9) p-vec 3^4 4^5 aut=2 W=2 nonsimple=5 cutoff_D2=5184 4rho2_G=768 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.2s | detL=1728 T=6 vol=288 T*vol=1728 (crystal-basis measure) slots=54 paired 1:1; disjointness G-ball D2=4rho2=768 (coord bound (16, 16, 10)), ball sizes 36..36 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.1s | audit re-derived 6 cells x 9 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 288 each, T*vol == |det|; all 54 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 192 shared-vertex G-equidistance checks, 486 vertex-side checks, 54 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=2, Isom_fix_site=2, Isom(solid)=2 (Isom+=2, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 2|2|2|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 24 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (0 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=2) |
| V3 Burnside identity (banked + independent) | **PASS** | 0.6s | tables T=6 nbrs=9 |ops|=12 (12 proper, 0 improper; T*|site|=12), identity+closure exact; hands: 0 of 6 classes of the other hand; banked enumerate n<=4: fixed=[6, 27, 168, 1224], free=[1, 5, 16, 118]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[6, 27, 168, 1224, 9744], free=[1, 5, 16, 118, 826], one-sided=[1, 5, 16, 118, 826], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 0s |

Symmetry reconciliation: site symmetry 2 <= Isom_fix_site 2 <= Isom(solid) 2 (Isom+ 2, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 24. Honeycomb point group |H/L| = 12 (0 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #150 `400cba5c78326d1d` — IT(167) R-3c, f=(17, 28, 13), p=4^10 5^2 6^1, aut=1

Witness point (1/8, 1/6, 5/12), c/a = 1, site stabilizer 1, orbit 36 conventional / 12 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 7.2s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.4s | IT(167) R-3c p=(1/8, 1/6, 5/12) c/a=1 G=diag(2,2,2) period=24 n_conv=36 T=12 site=1 dim=3 f=(17,28,13) p-vec 4^10 5^2 6^1 aut=1 W=2 nonsimple=5 cutoff_D2=4608 4rho2_G=296 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 2.4s | detL=4608 T=12 vol=384 T*vol=4608 (crystal-basis measure) slots=156 paired 1:1; disjointness G-ball D2=4rho2=296 (coord bound (15, 15, 13)), ball sizes 22..22 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.8s | audit re-derived 12 cells x 13 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 384 each, T*vol == |det|; all 156 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 672 shared-vertex G-equidistance checks, 2652 vertex-side checks, 156 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.1s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=1; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|1 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=12 (6 improper) vs T*|site|=12: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 3.5s | tables T=12 nbrs=13 |ops|=12 (6 proper, 6 improper; T*|site|=12), identity+closure exact; hands: 6 of 12 classes of the other hand; banked enumerate n<=4: fixed=[12, 78, 712, 7524], free=[1, 9, 60, 650]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[12, 78, 712, 7524, 86532], free=[1, 9, 60, 650, 7211], one-sided=[2, 17, 120, 1290, 14422], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 3s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 1 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 12 (6 improper) vs T*|site| = 12: the full symmetry group of the honeycomb IS exactly the generating group G.

### #151 `78e755ffdff3a2f5` — IT(146) R3, f=(14, 24, 12), p=3^4 4^6 6^2, aut=2

Witness point (1/12, 3/8, 1/6), c/a = 3/4, site stabilizer 1, orbit 9 conventional / 3 primitive, stratum dim 3. Open/wall label (triage, carried): wall-suspect (triage, 1 b; metric-thin: 1b). Candidate wall time 1.0s.

| stage | verdict | wall | key numbers |
|---|---|---|---|
| V0 exact re-derivation (Gram chain) | **PASS** | 0.1s | IT(146) R3 p=(1/12, 3/8, 1/6) c/a=3/4 G=diag(16,16,9) period=24 n_conv=9 T=3 site=1 dim=3 f=(14,24,12) p-vec 3^4 4^6 6^2 aut=2 W=2 nonsimple=6 cutoff_D2=36864 4rho2_G=5888 |
| V1 tiling certificate in the G-norm (generator) | **PASS** | 0.3s | detL=4608 T=3 vol=1536 T*vol=4608 (crystal-basis measure) slots=36 paired 1:1; disjointness G-ball D2=4rho2=5888 (coord bound (23, 23, 26)), ball sizes 34..34 sites/rep, all G-bisectors weakly satisfied, no unlisted 2-face contact |
| V1 independent adapted audit (affine + Gram layer) | **PASS** | 0.1s | audit re-derived 3 cells x 12 facets (supporting-plane scan), closed surfaces, Euler ok; volumes 1536 each, T*vol == |det|; all 36 pairing claims verified full-facet both sides, slots covered exactly once; Gram layer: 144 shared-vertex G-equidistance checks, 504 vertex-side checks, 36 facet normals parallel to G(r-c) — all exact |
| V2 symmetry certification (G-isometries) | **PASS** | 0.0s | site=1, Isom_fix_site=1, Isom(solid)=1 (Isom+=1, improper=0; solid CHIRAL), aut_comb=2; chain site<=Isom_fix (linear parts) contained, divisibility 1|1|1|2 holds; Gram-triple re-derivation agrees; Bravais point group of L in G: order 12 (embedded ops NOT all signed perms); honeycomb point group |H/L|=3 (0 improper) vs T*|site|=3: full symmetry group of the honeycomb IS exactly G (|H_cell|=1) |
| V3 Burnside identity (banked + independent) | **PASS** | 0.5s | tables T=3 nbrs=12 |ops|=3 (3 proper, 0 improper; T*|site|=3), identity+closure exact; hands: 0 of 3 classes of the other hand; banked enumerate n<=4: fixed=[3, 18, 158, 1611], free=[1, 6, 54, 537]; burnside_generic ALL PASS n<=4; INDEPENDENT enumerator (verify_counts_independent.py) reached n=5: fixed=[3, 18, 158, 1611, 17811], free=[1, 6, 54, 537, 5937], one-sided=[1, 6, 54, 537, 5937], n<=4 identical to banked, its own Burnside (all + proper) ok at every n, 0s |

Symmetry reconciliation: site symmetry 1 <= Isom_fix_site 1 <= Isom(solid) 1 (Isom+ 1, solid chiral) <= combinatorial aut 2 (containment + divisibility verified exactly; Gram-triple re-derivation agrees). Bravais point group of the actual lattice in G: order 12. Honeycomb point group |H/L| = 3 (0 improper) vs T*|site| = 3: the full symmetry group of the honeycomb IS exactly the generating group G.

## Deferrals / failures

- none

Total wall time 26s. Deterministic except the timing columns (`--mask-timings` writes them as `<t>`; the md5 of the masked text is printed by the driver). Artifacts: `g4p2hex_tables_<id>.json` (+ `.txt` enumerator input, `_indep.json` independent-enumerator record) per cell; `g4p2hex_cells/<id>.json` per-cell records (resume boundary); `g4p2hex_control_*` for the sanity gates.

Re-run for acceptance (see the docstring of `g4_certify_hex.py`): `PY=python3; cd <repo>/harness; $PY g4_certify_hex.py --fresh --budget-s 420; rc=$?; while [ $rc -eq 3 ]; do $PY g4_certify_hex.py --resume --budget-s 420; rc=$?; done; echo exit $rc` (exit 0 required).

