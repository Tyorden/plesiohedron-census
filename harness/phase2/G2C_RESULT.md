# G2c result — hexagonal-family controls (2026-09-04)

Gate: `../../ANCHORS.md` block "G2c - HEXAGONAL-FAMILY CONTROLS" (pre-registered before this run). Pipeline under test: `orbit.py` -> `phase2/metric.py` (gram_hexagonal, R^T G R = G) -> `phase2/sweep_voronoi_gram.py` (float proposal) -> `phase2/exact_cell_gram.py` (exact Fractions, G-norm certificate 4*rho^2 <= D^2) -> `canon_code.py`, compared against `seed_catalog.json` (G2, independent) and Schmitt's printed trigonal/hexagonal rows (`schmitt_hexagonal_tables.json`). Accepted modules unmodified.

Verdict: **G2c ALL REQUIRED ASSERTIONS PASS** (wall 5.6 s, single process)

## Convention confirmed (recorded)

Per required Schmitt row, the first documented convention under which the exact chain reproduced the printed f-vector:

- S143: H1 (B'' -> ITA: x'=2x'', y'=x''+y'', z'=z''), b = c/a
- S147: H1 (B'' -> ITA: x'=2x'', y'=x''+y'', z'=z''), b = c/a
- S155: H1 (B'' -> ITA: x'=2x'', y'=x''+y'', z'=z''), b = c/a
- S166: H1 (B'' -> ITA: x'=2x'', y'=x''+y'', z'=z''), b = c/a
- S178: H1 (B'' -> ITA: x'=2x'', y'=x''+y'', z'=z''), b = c/a
- S194: H1 (B'' -> ITA: x'=2x'', y'=x''+y'', z'=z''), b = c/a

Notes:

- bracket FCC c/a=sqrt6~2.4495: 12/5 -> rhombic_dodecahedron, 5/2 -> rhombic_dodecahedron
- bracket SC c/a=sqrt6/2~1.2247: 6/5 -> truncated_octahedron, 5/4 -> rhombic_dodecahedron
- bracket BCC c/a=sqrt6/4~0.6124: 3/5 -> truncated_octahedron, 5/8 -> truncated_octahedron
- IT(179) enantiomorph conversion for the S178 row: z -> -z (tried [('verbatim', (36, 54, 20), 1), ('z -> -z', (64, 96, 34), 1)])

## Assertions (with per-assertion wall time)

- **PASS** (a) P6/mmm #191 origin orbit (hexagonal lattice), c/a=1/2: code == seed hexagonal_prism, aut 24, f=(12,18,8), simple, invariants (d) — orbit=1, f=(12, 18, 8), p=(4, 4, 4, 4, 4, 4, 6, 6), aut=24, nonsimple=0, flags=[True], W=2, D2=2304, rho2=228 — 0.01 s
- **PASS** (a) P6/mmm #191 origin orbit (hexagonal lattice), c/a=1: code == seed hexagonal_prism, aut 24, f=(12,18,8), simple, invariants (d) — orbit=1, f=(12, 18, 8), p=(4, 4, 4, 4, 4, 4, 6, 6), aut=24, nonsimple=0, flags=[True], W=2, D2=1152, rho2=168 — 0.01 s
- **PASS** (a) P6/mmm #191 origin orbit (hexagonal lattice), c/a=2: code == seed hexagonal_prism, aut 24, f=(12,18,8), simple, invariants (d) — orbit=1, f=(12, 18, 8), p=(4, 4, 4, 4, 4, 4, 6, 6), aut=24, nonsimple=0, flags=[True], W=2, D2=4608, rho2=384 — 0.01 s
- **PASS** (b) R-3m #166 origin orbit is a LATTICE with 3 points per conventional cell (rhombohedral, hexagonal axes) — is_lattice=True, orbit=3, points=[(Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)), (Fraction(1, 3), Fraction(2, 3), Fraction(2, 3)), (Fraction(2, 3), Fraction(1, 3), Fraction(1, 3))] — 0.07 s
- **PASS** (b) R-3m #166 lattice, bracket FCC c/a=sqrt6~2.4495, side c/a=12/5: seed-catalog parallelohedron with the seed's aut, invariants (d) — code -> rhombic_dodecahedron, f=(14, 24, 12), p=(4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4), aut=48, nonsimple=6, flags=[True, True, True], superseded=0, W=2 — 0.15 s
- **PASS** (b) R-3m #166 lattice, bracket FCC c/a=sqrt6~2.4495, side c/a=5/2: seed-catalog parallelohedron with the seed's aut, invariants (d) — code -> rhombic_dodecahedron, f=(14, 24, 12), p=(4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4), aut=48, nonsimple=6, flags=[True, True, True], superseded=0, W=2 — 0.16 s
- **PASS** (b) bracket FCC c/a=sqrt6~2.4495: RECORDED sides 12/5 -> rhombic_dodecahedron, 5/2 -> rhombic_dodecahedron (same code both sides) — prediction check only, recorded not required
- **PASS** (b) R-3m #166 lattice, bracket SC c/a=sqrt6/2~1.2247, side c/a=6/5: seed-catalog parallelohedron with the seed's aut, invariants (d) — code -> truncated_octahedron, f=(24, 36, 14), p=(4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6), aut=48, nonsimple=0, flags=[False, False, False], superseded=0, W=2 — 0.08 s
- **PASS** (b) R-3m #166 lattice, bracket SC c/a=sqrt6/2~1.2247, side c/a=5/4: seed-catalog parallelohedron with the seed's aut, invariants (d) — code -> rhombic_dodecahedron, f=(14, 24, 12), p=(4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4), aut=48, nonsimple=6, flags=[True, True, True], superseded=0, W=2 — 0.06 s
- **PASS** (b) bracket SC c/a=sqrt6/2~1.2247: RECORDED sides 6/5 -> truncated_octahedron, 5/4 -> rhombic_dodecahedron (DIFFERENT codes on the two sides) — prediction check only, recorded not required
- **PASS** (b) R-3m #166 lattice, bracket BCC c/a=sqrt6/4~0.6124, side c/a=3/5: seed-catalog parallelohedron with the seed's aut, invariants (d) — code -> truncated_octahedron, f=(24, 36, 14), p=(4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6), aut=48, nonsimple=0, flags=[False, False, False], superseded=0, W=2 — 0.09 s
- **PASS** (b) R-3m #166 lattice, bracket BCC c/a=sqrt6/4~0.6124, side c/a=5/8: seed-catalog parallelohedron with the seed's aut, invariants (d) — code -> truncated_octahedron, f=(24, 36, 14), p=(4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6), aut=48, nonsimple=0, flags=[False, False, False], superseded=0, W=2 — 0.09 s
- **PASS** (b) bracket BCC c/a=sqrt6/4~0.6124: RECORDED sides 3/5 -> truncated_octahedron, 5/8 -> truncated_octahedron (same code both sides) — prediction check only, recorded not required
- **PASS** (b) R-3m #166 lattice, generic c/a=1: seed-catalog parallelohedron (identified: truncated_octahedron), seed aut, STABLE at c/a +- 1/24, invariants (d) — f=(24, 36, 14), p=(4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6), aut=48, nonsimple=0, stable=True (codes at -1/24: truncated_octahedron, +1/24: truncated_octahedron), flags=[False, False, False], superseded=0 — 0.21 s
- **PASS** (b) R-3m #166 lattice, generic c/a=2: seed-catalog parallelohedron (identified: rhombic_dodecahedron), seed aut, STABLE at c/a +- 1/24, invariants (d) — f=(14, 24, 12), p=(4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4), aut=48, nonsimple=6, stable=True (codes at -1/24: rhombic_dodecahedron, +1/24: rhombic_dodecahedron), flags=[True, True, True], superseded=0 — 0.33 s
- **PASS** (b) R-3m #166 lattice, generic c/a=3: seed-catalog parallelohedron (identified: rhombic_dodecahedron), seed aut, STABLE at c/a +- 1/24, invariants (d) — f=(14, 24, 12), p=(4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4), aut=48, nonsimple=6, stable=True (codes at -1/24: rhombic_dodecahedron, +1/24: rhombic_dodecahedron), flags=[True, True, True], superseded=0 — 0.68 s
- **PASS** (c) S143 row present verbatim in schmitt_hexagonal_tables.json (PDF 88)
- **PASS** (c) S143 Schmitt P3 IT(143) PDF 88: f=(8, 12, 6) at b-ratio 3497/1000, printed point ('1/6', '0', '0') -> exact f-vector == printed under a documented convention, invariants (d) — tried H1 (B'' -> ITA: x'=2x'', y'=x''+y'', z'=z''), b = c/a: f=(8, 12, 6) | exact f=(8, 12, 6), p=(4, 4, 4, 4, 4, 4), aut=48, stab=1, orbit=3, PERIOD=12, nonsimple=0, flags=[True, True, True], superseded=0, W=2, D2=7043909184, point_ITA=('1/3', '1/6', '0') — 0.18 s
- **PASS** (c) S147 row present verbatim in schmitt_hexagonal_tables.json (PDF 89)
- **PASS** (c) S147 Schmitt P-3 IT(147) PDF 89: f=(10, 15, 7) at b-ratio 3497/1000, printed point ('33/100', '-1/500', '0') -> exact f-vector == printed under a documented convention, invariants (d) — tried H1 (B'' -> ITA: x'=2x'', y'=x''+y'', z'=z''), b = c/a: f=(10, 15, 7) | exact f=(10, 15, 7), p=(4, 4, 4, 4, 4, 5, 5), aut=20, stab=1, orbit=6, PERIOD=1500, nonsimple=0, flags=[True, True, True, True, True, True], superseded=0, W=2, D2=110061081000000, point_ITA=('33/50', '41/125', '0') — 0.88 s
- **PASS** (c) S155 row present verbatim in schmitt_hexagonal_tables.json (PDF 97)
- **PASS** (c) S155 Schmitt R32 IT(155) PDF 97: f=(48, 73, 27) at b-ratio 797/1000, printed point ('-193/750', '-53/250', '6/125') -> exact f-vector == printed under a documented convention, invariants (d) — tried H1 (B'' -> ITA: x'=2x'', y'=x''+y'', z'=z''), b = c/a: f=(48, 73, 27) | exact f=(48, 73, 27), p=(3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 6, 6, 6, 8, 8, 8, 10, 22), aut=1, stab=1, orbit=18, PERIOD=1500, nonsimple=2, flags=[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], superseded=0, W=2, D2=9000000000000, point_ITA=('-193/375', '-176/375', '6/125') — 0.58 s
- **PASS** (c) S166 row present verbatim in schmitt_hexagonal_tables.json (PDF 105)
- **PASS** (c) S166 Schmitt R-3m IT(166) PDF 105: f=(38, 58, 22) at b-ratio 527/1000, printed point ('-16/375', '-16/125', '31/500') -> exact f-vector == printed under a documented convention, invariants (d) — tried H1 (B'' -> ITA: x'=2x'', y'=x''+y'', z'=z''), b = c/a: f=(38, 58, 22) | exact f=(38, 58, 22), p=(3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 12, 12, 18), aut=2, stab=2, orbit=18, PERIOD=1500, nonsimple=2, flags=[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], superseded=0, W=2, D2=9000000000000, point_ITA=('-32/375', '-64/375', '31/500') — 0.59 s
- **PASS** (c) S178 row present verbatim in schmitt_hexagonal_tables.json (PDF 114)
- **PASS** (c) S178 Schmitt P6_122 IT(178) PDF 114: f=(64, 96, 34) at b-ratio 163/200, printed point ('32/125', '-19/125', '43/1500') -> exact f-vector == printed under a documented convention, invariants (d) — tried H1 (B'' -> ITA: x'=2x'', y'=x''+y'', z'=z''), b = c/a: f=(64, 96, 34) | exact f=(64, 96, 34), p=(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 12, 18, 26), aut=1, stab=1, orbit=12, PERIOD=1500, nonsimple=0, flags=[False, False, False, False, False, False, False, False, False, False, False, False], superseded=0, W=2, D2=360000000000, point_ITA=('64/125', '13/125', '43/1500') — 0.52 s
- **PASS** (c) S194 row present verbatim in schmitt_hexagonal_tables.json (PDF 123)
- **PASS** (c) S194 Schmitt P6_3/mmc IT(194) PDF 123: f=(18, 30, 14) at b-ratio 797/1000, printed point ('1/3', '0', '1/4') -> exact f-vector == printed under a documented convention, invariants (d) — tried H1 (B'' -> ITA: x'=2x'', y'=x''+y'', z'=z''), b = c/a: f=(18, 30, 14) | exact f=(18, 30, 14), p=(3, 3, 3, 3, 3, 3, 3, 3, 6, 6, 6, 6, 6, 6), aut=12, stab=12, orbit=2, PERIOD=12, nonsimple=6, flags=[True, True], superseded=0, W=2, D2=576000000, point_ITA=('2/3', '1/3', '1/4') — 0.03 s
- **PASS** (c) ONE convention reproduces all six required rows — conventions used: ["H1 (B'' -> ITA: x'=2x'', y'=x''+y'', z'=z''), b = c/a"]
- **PASS** (c) S178 row run in the second enantiomorph IT(179) P6_522: reproduces under 'verbatim' or 'z -> -z' (conversion recorded) — used: z -> -z; tried [('verbatim', (36, 54, 20), 1), ('z -> -z', (64, 96, 34), 1)]

## Honest limits / deferrals

- Aut orders are COMBINATORIAL map automorphism counts; geometric stabilizers remain G4/V2.
- The transition values c/a = sqrt6, sqrt6/2, sqrt6/4 are irrational and untested; the rational brackets record the code on each side only.
- Schmitt rows are f-vector-level checks (his tables print f-vectors, not types).
- Convention evidence: six printed rows (plus one enantiomorph re-run) — the P2 pass of the sweep runs every printed row and counts mismatches, which is the full-table test.
- No hunt sweep runs in this step.

## Commands run

```
PY=python3
cd <repo>/harness/phase2
$PY g2c_controls.py      # this gate; writes G2C_RESULT.md; exit 0 required
```
