# G2 result — cubic controls (2026-08-28)

Gate: `../ANCHORS.md` G2. Spec: `../HARNESS_DESIGN_FABLE5_2026-08-27.md` §1.3-§1.4, §4. Pipeline under test: `orbit.py` -> `sweep_voronoi.py` (float, W=2) -> `exact_cell.py` (exact Fractions) -> `canon_code.py`, compared against `seed_catalog.json` built independently by `g2_seed_catalog.py`.

Verdict: **G2 IN-SCOPE ASSERTIONS: ALL PASS**

## Reading of the Pm-3m clause (recorded)

A general-position Pm-3m orbit has 48 points/cell and its Voronoi cells are not cubes — the "P1-like orbit degeneration" ANCHORS excludes. The honest control is the lattice Voronoi cell: the ORIGIN orbit (Wyckoff 1a) of Pm-3m under the frozen G1-audited group data is exactly one point per cell, i.e. the simple-cubic lattice; likewise Fm-3m 4a -> FCC and Im-3m 2a -> BCC. All three control point sets are DERIVED from spacegroups.json via orbit.py (assertion B2), not typed in.

## Seeded catalog (independent side)

`g2_seed_catalog.py` builds all 5 parallelohedra from published exact integer vertex data (sources in its docstring: Coxeter standard coordinates for cube / rhombic dodecahedron / truncated octahedron; exact rational affine image of the regular hexagonal prism; Fedorov elongation construction for the elongated dodecahedron) via an exact all-integer hull-free face enumeration — scipy unused, sweep_voronoi/exact_cell not imported (audited in B1c). Catalog: 5 entries, codes pairwise distinct, aut orders 48/24/48/16/48.

## Assertions

- **PASS** B1a catalog: 5 parallelohedra present with published f-vectors and p-vectors — entries=['cube', 'elongated_dodecahedron', 'hexagonal_prism', 'rhombic_dodecahedron', 'truncated_octahedron']
- **PASS** B1b catalog: 5 canonical codes pairwise distinct
- **PASS** B1c catalog independence: g2_seed_catalog.py imports neither sweep_voronoi nor exact_cell nor scipy (G1-style no-shared-code audit, via ast on the actual import statements) — imports=['canon_code', 'itertools', 'json', 'math', 'os', 'sys']
- **PASS** B2 orbits: origin orbits of #221/#225/#229 are exactly the SC/FCC/BCC lattices (1/4/2 points per cell, stabilizer 48, special-position flagged, PERIOD 12) — SC=Pm-3m#221: orbit 1, stab 48; FCC=Fm-3m#225: orbit 4, stab 48; BCC=Im-3m#229: orbit 2, stab 48
- **PASS** B3 SC (Pm-3m origin orbit -> cube): float degeneracy flag == True on all cells (SC/FCC vertices are permanently >4-equidistant — flag routes to exact, which decides) — flags=[True]
- **PASS** B3 SC (Pm-3m origin orbit -> cube): float/exact agreement (facet count, p-vector, neighbor site sets) + provable cutoff 4*rho2 <= D^2 held — p=(4, 4, 4, 4, 4, 4), D=24, rho2=108
- **PASS** B3 SC (Pm-3m origin orbit -> cube): exact cell has V=8, 0 non-simple vertices (flagged, not fatal — G0 amendment) — V=[8], nonsimple=[0]
- **PASS** B3 SC (Pm-3m origin orbit -> cube): ONE canonical code across the orbit, MATCHING the seeded catalog code (MATCH REQUIRED) — aut=48, code_len=88, orbit_cells=1
- **PASS** B4 FCC (Fm-3m origin orbit -> rhombic_dodecahedron): float degeneracy flag == True on all cells (SC/FCC vertices are permanently >4-equidistant — flag routes to exact, which decides) — flags=[True, True, True, True]
- **PASS** B4 FCC (Fm-3m origin orbit -> rhombic_dodecahedron): float/exact agreement (facet count, p-vector, neighbor site sets) + provable cutoff 4*rho2 <= D^2 held — p=(4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4), D=24, rho2=36
- **PASS** B4 FCC (Fm-3m origin orbit -> rhombic_dodecahedron): exact cell has V=14, 6 non-simple vertices (flagged, not fatal — G0 amendment) — V=[14], nonsimple=[6]
- **PASS** B4 FCC (Fm-3m origin orbit -> rhombic_dodecahedron): ONE canonical code across the orbit, MATCHING the seeded catalog code (MATCH REQUIRED) — aut=48, code_len=187, orbit_cells=4
- **PASS** B5 BCC (Im-3m origin orbit -> truncated_octahedron): float degeneracy flag == False on all cells (SC/FCC vertices are permanently >4-equidistant — flag routes to exact, which decides) — flags=[False, False]
- **PASS** B5 BCC (Im-3m origin orbit -> truncated_octahedron): float/exact agreement (facet count, p-vector, neighbor site sets) + provable cutoff 4*rho2 <= D^2 held — p=(4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6), D=24, rho2=45
- **PASS** B5 BCC (Im-3m origin orbit -> truncated_octahedron): exact cell has V=24, 0 non-simple vertices (flagged, not fatal — G0 amendment) — V=[24], nonsimple=[0]
- **PASS** B5 BCC (Im-3m origin orbit -> truncated_octahedron): ONE canonical code across the orbit, MATCHING the seeded catalog code (MATCH REQUIRED) — aut=48, code_len=306, orbit_cells=2
- **PASS** B6a the three pipeline codes are pairwise distinct
- **PASS** B6b aut orders: pipeline (SC, FCC, BCC) == catalog (cube, rhombic dodeca, trunc octa) == (48, 48, 48) — pipeline={'SC': 48, 'FCC': 48, 'BCC': 48}, catalog=(48, 48, 48)

## Scope notes (honest limits — what G2 does NOT claim)

- The hexagonal prism and elongated dodecahedron are catalog-only here: no cubic-lattice control produces them (they are hex / tetragonal-ish lattice cells). They enter as seeded entries (with the same exact verification) and await the Phase-2 metric sweeps.
- G2 does not test the Gram-metric path (exact_cell still raises NotImplementedError for gram != None); all three controls are cubic, integer, Euclidean — exactly the anchor's scope.
- Aut orders asserted are COMBINATORIAL map automorphism counts from the canon traversal; geometric stabilizer certification (all orthogonal maps, C6) is the G4/V2 ladder, not claimed here.
- The catalog shares exactly one module with the pipeline: canon_code.py, the type-identity function itself — codes must be comparable by construction. Its independent unit suite is test_canon.py (rerun below).

## Commands run (in order)

```
PY=python3
cd <repo>/harness
$PY g2_seed_catalog.py  # writes seed_catalog.json; ALL PASS
$PY test_canon.py       # canon unit suite: ALL PASS
$PY g2_controls.py      # this gate; writes G2_RESULT.md
```

## Notes

- House invariant held: scipy Voronoi only PROPOSES (and its degeneracy flag fires on SC/FCC, whose Voronoi vertices are permanently 8-/6-site-equidistant); every decision above is exact — integer face enumeration on the catalog side, Fraction clipping with the provable 4*rho2 <= D^2 cutoff on the pipeline side, canonical codes over exact facet cycles on both.
- The rhombic dodecahedron control also exercises the G0 amendment path end-to-end: its 6 degree-4 vertices are flagged non-simple and the type still canonicalizes and matches.
