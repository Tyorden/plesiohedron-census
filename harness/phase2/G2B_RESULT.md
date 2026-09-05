# G2b result — metric controls (2026-09-03)

Gate: `../../ANCHORS.md` block "G2b - METRIC CONTROLS" (pre-registered before this run). Pipeline under test: `orbit.py` -> `phase2/sweep_voronoi_gram.py` (float proposal; delegates to the accepted `sweep_voronoi.sweep` Gram hook after exact PD / R^T G R = G validation) -> `phase2/exact_cell_gram.py` (exact Fractions, G-norm certificate 4*rho^2 <= D^2 with the coordinate-bound-complete candidate block) -> `canon_code.py`, compared against `seed_catalog.json` (G2, independent).

Verdict: **G2b ALL ASSERTIONS PASS** (wall 1.5 s, single process)

## Basis decision (recorded)

Trigonal/hexagonal groups run in the ITA hexagonal basis of the frozen ops with the rational Gram [[1,-1/2,0],[-1/2,1,0],[0,0,(c/a)^2]] (cleared to integers). Schmitt's orthohexagonal C-centered basis (his App. B, printed pp. 171-172) is not needed under the Gram form and would require half-integer R (a re-freeze of G1 data). b-ratio = c/a = ||b3'||/||b1'|| (his p. 27).

## Elongated-dodecahedron lattice (source)

Body-centered tetragonal lattice with c/a > sqrt 2. Primary source: Schmitt 2016, printed p. 29 (PDF p. 34), IT(79) = I4 table rows "(18, 28, 12) | 7/2 | (0, 0, 0)" and "(24, 36, 14) | 1/2 | (0, 0, 0)" (the origin orbit of I4 is the BCT lattice); he lists the (18,28,12) lattice cell as the "hexarhombic dodecahedron" in his IT(1) table (p. 27). Corroborated by Wikipedia "Elongated dodecahedron" (Wigner-Seitz cell of BCT for c/a > sqrt 2; retrieved 2026-09-03) and by the analytic threshold derived here: the (0,0,+-c) facet exists iff a^2/(2c) + c/4 > c/2, i.e. iff c/a < sqrt 2 (c/a = sqrt 2 is FCC).

## Assertions (with per-assertion wall time)

- **PASS** (a) P6/mmm #191 origin orbit (hexagonal lattice), c/a=1/2: code == seed hexagonal_prism, aut 24, f=(12,18,8), simple, R^T G R = G, float/exact agree, G-norm certificate — orbit=1, f=(12, 18, 8), p=(4, 4, 4, 4, 4, 4, 6, 6), aut=24, nonsimple=0, flags=[True], W=2, D2=2304, rho2=228 — 0.01 s
- **PASS** (a) P6/mmm #191 origin orbit (hexagonal lattice), c/a=1: code == seed hexagonal_prism, aut 24, f=(12,18,8), simple, R^T G R = G, float/exact agree, G-norm certificate — orbit=1, f=(12, 18, 8), p=(4, 4, 4, 4, 4, 4, 6, 6), aut=24, nonsimple=0, flags=[True], W=2, D2=1152, rho2=168 — 0.01 s
- **PASS** (a) P6/mmm #191 origin orbit (hexagonal lattice), c/a=2: code == seed hexagonal_prism, aut 24, f=(12,18,8), simple, R^T G R = G, float/exact agree, G-norm certificate — orbit=1, f=(12, 18, 8), p=(4, 4, 4, 4, 4, 4, 6, 6), aut=24, nonsimple=0, flags=[True], W=2, D2=4608, rho2=384 — 0.01 s
- **PASS** (b) I4/mmm #139 origin orbit (BCT lattice), c/a=7/2: code == seed elongated_dodecahedron, aut 16, 2 non-simple vertices, R^T G R = G, agree, certificate — orbit=2, f=(18, 28, 12), p=(4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6), aut=16, nonsimple=2, flags=[True, True], superseded=0, W=2 — 0.15 s
- **PASS** (b) I4/mmm #139 origin orbit (BCT lattice), c/a=2: code == seed elongated_dodecahedron, aut 16, 2 non-simple vertices, R^T G R = G, agree, certificate — orbit=2, f=(18, 28, 12), p=(4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6), aut=16, nonsimple=2, flags=[True, True], superseded=0, W=2 — 0.06 s
- **PASS** (b) I4/mmm #139 origin orbit (BCT lattice), c/a=3/2: code == seed elongated_dodecahedron, aut 16, 2 non-simple vertices, R^T G R = G, agree, certificate — orbit=2, f=(18, 28, 12), p=(4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6), aut=16, nonsimple=2, flags=[True, True], superseded=0, W=2 — 0.04 s
- **PASS** (b) I4/mmm #139 origin orbit (BCT lattice), c/a=1/2: code == seed truncated_octahedron, aut 48, 0 non-simple vertices, R^T G R = G, agree, certificate — orbit=2, f=(24, 36, 14), p=(4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6), aut=48, nonsimple=0, flags=[False, False], superseded=0, W=2 — 0.05 s
- **PASS** (b) I4/mmm #139 origin orbit (BCT lattice), c/a=1: code == seed truncated_octahedron, aut 48, 0 non-simple vertices, R^T G R = G, agree, certificate — orbit=2, f=(24, 36, 14), p=(4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6), aut=48, nonsimple=0, flags=[False, False], superseded=0, W=2 — 0.03 s
- **PASS** (b) I4/mmm #139 origin orbit (BCT lattice), c/a=7/5: code == seed truncated_octahedron, aut 48, 0 non-simple vertices, R^T G R = G, agree, certificate — orbit=2, f=(24, 36, 14), p=(4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6), aut=48, nonsimple=0, flags=[False, False], superseded=0, W=2 — 0.05 s
- **PASS** (b) I4 #79 origin orbit (BCT lattice), c/a=7/2: code == seed elongated_dodecahedron, aut 16, 2 non-simple vertices, R^T G R = G, agree, certificate — orbit=2, f=(18, 28, 12), p=(4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6), aut=16, nonsimple=2, flags=[True, True], superseded=0, W=2 — 0.15 s
- **PASS** (b) I4 #79 origin orbit (BCT lattice), c/a=2: code == seed elongated_dodecahedron, aut 16, 2 non-simple vertices, R^T G R = G, agree, certificate — orbit=2, f=(18, 28, 12), p=(4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6), aut=16, nonsimple=2, flags=[True, True], superseded=0, W=2 — 0.06 s
- **PASS** (b) I4 #79 origin orbit (BCT lattice), c/a=3/2: code == seed elongated_dodecahedron, aut 16, 2 non-simple vertices, R^T G R = G, agree, certificate — orbit=2, f=(18, 28, 12), p=(4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6), aut=16, nonsimple=2, flags=[True, True], superseded=0, W=2 — 0.04 s
- **PASS** (b) I4 #79 origin orbit (BCT lattice), c/a=1/2: code == seed truncated_octahedron, aut 48, 0 non-simple vertices, R^T G R = G, agree, certificate — orbit=2, f=(24, 36, 14), p=(4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6), aut=48, nonsimple=0, flags=[False, False], superseded=0, W=2 — 0.04 s
- **PASS** (b) I4 #79 origin orbit (BCT lattice), c/a=1: code == seed truncated_octahedron, aut 48, 0 non-simple vertices, R^T G R = G, agree, certificate — orbit=2, f=(24, 36, 14), p=(4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6), aut=48, nonsimple=0, flags=[False, False], superseded=0, W=2 — 0.03 s
- **PASS** (b) I4 #79 origin orbit (BCT lattice), c/a=7/5: code == seed truncated_octahedron, aut 48, 0 non-simple vertices, R^T G R = G, agree, certificate — orbit=2, f=(24, 36, 14), p=(4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6), aut=48, nonsimple=0, flags=[False, False], superseded=0, W=2 — 0.04 s
- **PASS** (c) Pm-3m #221 origin orbit via Gram path (G=I): vertices/neighbors/p-vector/code IDENTICAL to exact_cell.clip_cell and == seed cube — f=(8, 12, 6), aut=48, nonsimple=0, flags=[True], superseded=0 — 0.01 s
- **PASS** (c) Fm-3m #225 origin orbit via Gram path (G=I): vertices/neighbors/p-vector/code IDENTICAL to exact_cell.clip_cell and == seed rhombic_dodecahedron — f=(14, 24, 12), aut=48, nonsimple=6, flags=[True, True, True, True], superseded=0 — 0.12 s
- **PASS** (c) Im-3m #229 origin orbit via Gram path (G=I): vertices/neighbors/p-vector/code IDENTICAL to exact_cell.clip_cell and == seed truncated_octahedron — f=(24, 36, 14), aut=48, nonsimple=0, flags=[False, False], superseded=0 — 0.06 s
- **PASS** (d) S75 Schmitt P4 IT(75) printed p.28 (PDF 33): f=(10, 15, 7) at b-ratio 1/2, x=('2825/5652', '-1/5652', '0') -> exact f-vector == printed, R^T G R = G, agree, certificate — exact f=(10, 15, 7), p=(4, 4, 4, 4, 4, 5, 5), aut=20, general_position=True, orbit=4, PERIOD=5652, nonsimple=0, flags=[True, True, True, True], superseded=0, W=2, D2=511121664 — 0.08 s
- **PASS** (d) S76 Schmitt P4_1 IT(76) printed p.28 (PDF 33): f=(44, 66, 24) at b-ratio 797/1000, x=('20/333', '44/999', '0') -> exact f-vector == printed, R^T G R = G, agree, certificate — exact f=(44, 66, 24), p=(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 11, 11, 13, 13), aut=1, general_position=True, orbit=4, PERIOD=3996, nonsimple=0, flags=[False, False, False, False], superseded=0, W=2, D2=63872064000000 — 0.22 s
- **PASS** (d) S77 Schmitt P4_2 IT(77) printed p.29 (PDF 34): f=(28, 42, 16) at b-ratio 1/2, x=('539/5652', '-187/5652', '0') -> exact f-vector == printed, R^T G R = G, agree, certificate — exact f=(28, 42, 16), p=(3, 3, 3, 3, 4, 4, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7), aut=2, general_position=True, orbit=4, PERIOD=5652, nonsimple=0, flags=[False, False, False, False], superseded=0, W=2, D2=511121664 — 0.18 s

## Honest limits / deferrals

- Aut orders are COMBINATORIAL map automorphism counts; geometric stabilizers (C6) remain the G4/V2 ladder.
- c/a = sqrt 2 (the BCT -> FCC transition) is irrational and untested; the rationals 7/5 and 3/2 bracket it.
- Schmitt rows are f-vector-level checks (his tables print f-vectors, not types); the exact cell's p-vector/aut are recorded but have no printed counterpart to compare with.
- Orthorhombic Gram is provided (metric.gram_orthorhombic) but not gated; monoclinic/triclinic raise NotImplementedError by design (§2.1 deferral).
- No hunt sweep was run in this step.

## Commands run

```
PY=python3
cd <repo>/harness/phase2
$PY metric.py && $PY exact_cell_gram.py && $PY sweep_voronoi_gram.py  # selftests
$PY g2b_controls.py      # this gate; writes G2B_RESULT.md
```
