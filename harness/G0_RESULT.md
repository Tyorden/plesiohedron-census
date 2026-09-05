# G0 result — regression gate on the Josehedron generating orbit (2026-08-28)

Gate: `../ANCHORS.md` G0. Spec: `../HARNESS_DESIGN_FABLE5_2026-08-27.md` §1.2-§1.4. Pipeline under test: `orbit.py` -> `sweep_voronoi.py` (float, W=2) -> `exact_cell.py` (exact Fractions) -> `canon_code.py`.

Verdict: **G0 IN-SCOPE ASSERTIONS: ALL PASS**

Input: the 12 FKS extremal centre points, VERBATIM from `build_josehedron.py:33-35` (Bernhard Table 4 minima), integers mod 8, fed to the pipeline as fractions p/8 (scaled by orbit.scale_orbit to integers mod PERIOD=lcm(8,12)=24).

## T reconciliation (per the pre-build instruction)

`josehedron_tables.json` has **T=6**: translation-orbit *types* in the PRIMITIVE lattice (12*detL/8^3 = 12*256/512 = 6). The generating orbit has **12 points per conventional period-8 cell** (ANCHORS' "T=12"). Both are asserted below (A1 conventional count, A2 primitive count against the banked tables); the per-cell facet count and p-vector are the regression targets.

## Assertions

- **PASS** A1 orbit: 12 points per conventional cell, scaling exact — PERIOD=24, scale=3
- **PASS** A2 reconciliation: detL=256, T_primitive=6 == tables T (tables count PRIMITIVE translation types; orbit has 12/conv. cell) — detL=256, T_prim=6, tables.T=6
- **PASS** A3 float: every cell has 12 facets with p-vector {4x3, 8x4} (guards: no unbounded ridge, no outer-shell neighbor) — p_vectors=[(3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4)], degenerate_flags=12/12
- **PASS** A4 exact: every cell 12 facets, p-vector {4x3, 8x4}, matches float; provable cutoff held, no box facet survived — cutoff_D=[48], max rho2=69, V=[12], nonsimple=[8]
- **PASS** A5 float/exact neighbor site sets identical for all 12 cells
- **PASS** A6 canon: canonical planar code identical for all 12 cells — aut_order=4, code_len=163 bytes
- **PASS** A7 tables facet_signature == [3,3,3,3,4*8] == exact p-vector

## Out of scope for this build step (recorded as NOT YET RUN, not as passed)

- ANCHORS G0 clause |ops|=24 (12 proper) — belongs to the ops/tables step (`mint_tables.py`, design §V2), not built in steps 2-4.
- ANCHORS G0 clause tables semantic equality (nbr multiset per type up to relabeling) — same step.
- ANCHORS G0 clause enumerator fixed/free n<=6 identity — same step (V3 back end).

## Commands run (in order)

```
PY=python3
cd <repo>/harness
$PY orbit.py          # selftest PASS (P23/Fm-3m orbits, stabilizer gate incl. glide-mirror catch)
$PY canon_code.py     # smoke PASS (tetrahedron aut 24)
$PY exact_cell.py     # selftest PASS (cube / trunc. octahedron / rhombic dodecahedron)
$PY sweep_voronoi.py  # selftest PASS (cube flagged-degenerate / BCC clean; FCC informational)
$PY test_canon.py     # ALL PASS (20 relabelings x3 solids, mirrors, cube!=octa, aut orders)
$PY g0_regression.py  # this gate; writes G0_RESULT.md
```

## Notes

- House invariant held: the float phase (scipy Voronoi) only PROPOSES; every G0 decision above is exact-Fraction (exact_cell, canon over exact facet cycles) or exact-integer (lattice det, scaling).
- The Josehedron cell is NOT simple (12 vertices, 22 edges: eight 4-valent vertices), so the float degeneracy flag fires by design on this configuration — logged in A3's detail; the exact clipper decides.
- Combinatorial automorphism order of the cell (canon traversal count, reflections included): 4. Consistency remark (not an assertion): the banked tables imply a geometric site symmetry of order 24 ops / 6 types = 4 — equal to the combinatorial order, so no combinatorial-vs-geometric symmetry gap here (design §4 fingerprint item 4).
