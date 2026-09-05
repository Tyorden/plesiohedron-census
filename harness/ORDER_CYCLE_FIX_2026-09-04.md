# order_cycle fix — exact fallback for facet-cycle ordering (2026-09-04)

Open item from `PHASE2_RESULT.md` addendum / `../STATUS.md` 2026-09-04 (early):
two P2 rows (Schmitt's printed tetragonal tables, b = 3497/1000, PERIOD 5652)
crashed the accepted `exact_cell.order_cycle` with
`AssertionError: facet ordering failed exact convexity check`. House invariant
(`../ANCHORS.md`): floats propose, exact decides; a failing float proposal
must fall back to an EXACT method, never crash and never be accepted.

## Cause

`order_cycle(pts, normal)` proposes the cyclic order of a facet's exact
vertices by float `atan2` of the projections onto the in-plane frame
`u = pts[1]-pts[0]`, `w = normal x u`. On the two rows the facet normals are
Gram bisector normals with entries of very different size (IT(80):
`(8000000, 4000000, 34559179434)`; IT(110): `(-5648000000, 4000000,
-34559179434)` and `(4000000, 5648000000, -34559179434)`), so `|w| / |u|` is
~10^10 and the projected coordinates are ~10^12-10^14 in `y` against ~10^0
in `x`. Every float angle collapses to +-pi/2 (recorded values:
`-1.5707963267948966`, `1.5707963267948966`, ... differing in the 11th-16th
digit or exactly tied), the sort order is arbitrary, and the exact
convexity verifier correctly refuses it. Diagnostic (scratch run, 2026-09-04)
on all four failing facets (IT(80): two 9-gons; IT(110): two pentagons): the
EXACT angular order passes the strict convexity check with zero collinear
triples, i.e. the facets are fine convex polygons and the failure is purely
the float proposal.

## Fix (`exact_cell.py`, 50 lines added, 5 replaced; nothing else touched)

- `_convex_cycle_ok(poly, normal)`: the existing strict test (every
  consecutive triple turns left as seen from the outward normal) factored
  into a boolean; strength unchanged.
- `order_cycle_exact(pts, normal)` (sibling helper, all rational): exact
  centroid `c`; the same oriented frame `(u, w)`; 2-D projections
  `x = (p-c).u`, `y = (p-c).w` as Fractions; comparator = half-plane first
  (`y > 0 or (y == 0 and x > 0)` before the rest), then the sign of
  `x_a y_b - y_a x_b`. `u x w = normal |u|^2` (u in the plane), so CCW in
  `(x, y)` is CCW from outside. For a convex facet the vertex centroid is
  interior and no two vertices share a direction from it, so the comparator
  is a strict total order. No floating point anywhere.
- `order_cycle`: unchanged float proposal; if `_convex_cycle_ok` fails, the
  order is replaced by `order_cycle_exact` and the SAME assertion is applied
  to the result. Whenever the float order passes, it is returned unchanged,
  so every previously accepted output is byte-identical by construction.
- `phase2/exact_cell_gram.py` imports `order_cycle` from `exact_cell` and is
  untouched; it inherits the fallback.
- Cross-check (scratch run): on all 78 facets of the module selftests
  (SC/BCC/FCC via both clippers, tetragonal box, hexagonal prism)
  `order_cycle_exact` equals the accepted float order up to rotation.

## Non-regression (battery run 2026-09-04, python = paper_prep_venv)

Result files compared to git HEAD (`1e8d992`) after each run.

| gate | exit | wall | result file(s) vs HEAD |
|---|---|---|---|
| `g0_regression.py` | 0 | 1 s | `G0_RESULT.md` byte-identical |
| `g2_controls.py` | 0 | 1 s | `G2_RESULT.md` byte-identical |
| `mint_tables.py` | 0 | 1 s | `MINT_TABLES_RESULT.md`, `mint_tables_{mine,banked}[_proper].txt` byte-identical |
| `g4_certify.py` (all 11) | 0 | 179 s | all 11 `g4_tables_<id>.txt` byte-identical; `G4_RESULTS.md` identical except timing tokens (per-step seconds, "Total wall time 113s" -> 178s; the file states "Deterministic except the timing decimals") |
| `schmitt_220_check.py` | 0 | 8 s | `SCHMITT_220_CHECK_RESULT.md` byte-identical |
| `schmitt_collision_check.py` (all 21 pairs) | 0 | 158 s | `SCHMITT_COLLISION_RESULTS.md` identical except the per-pair seconds column (proved by masking decimal tokens: md5 equal) |
| `phase2/g2b_controls.py` | 0 | 2 s | `phase2/G2B_RESULT.md` identical except per-assertion seconds and the wall line (md5 equal after masking) |

Module selftests: `exact_cell.py` PASS, `phase2/exact_cell_gram.py` PASS.
The three timing-only-churned report files were restored to HEAD after the
comparison so the working-tree diff is exactly the fix; the main session's
acceptance re-run regenerates them.

## The two rows (`repro_crash.py`, exit 0; before the fix both crash)

| row | point | printed f | exact f now | p-vector | aut | period | certificate |
|---|---|---|---|---|---|---|---|
| IT(80) I4_1, b = 3497/1000 | (353/1413, 235/942, 0) | (32, 48, 18) | (32, 48, 18) | 3^4 4^6 5^2 6^1 8^2 9^2 10^1 | 1 | 5652 | 4 rho^2 <= D^2 held; orbit congruence (2nd cell) checked |
| IT(110) I4_1cd, b = 3497/1000 | (1/4, 1411/5652, 0) | (24, 36, 14) | (24, 36, 14) | 4^4 5^4 6^6 | 4 | 5652 | 4 rho^2 <= D^2 held; orbit congruence checked |

Fallback engaged on 2 facets per row (the four diagnosed above); every other
facet took the float order. Schmitt screen bookkeeping: with these two rows
the printed tetragonal rows reproducing at f-vector level become 1,476 of
1,476 (1,215 direct + 348 origin-shift/enantiomorph re-runs of
`PHASE2_SCHMITT_ORIGIN_CHECK.md` + 107 + these 2). `phase2_types.json` and
`PHASE2_RESULT.md` are NOT rewritten (the run's record stands; the two rows
remain listed there as crash quarantines, resolved by this note). The two
cells were not added to the store.

## Files

`exact_cell.py` (modified), `repro_crash.py` (new; reproduces both rows
through `sweep_phase2_tetragonal.evaluate`, exit 0 iff both match printed),
this note. Gate logs of the battery were in the session scratchpad; the
table above is the record. Main session re-runs the battery before
acceptance (rule).
