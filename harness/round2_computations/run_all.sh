#!/bin/sh
# Round-2 computations (2026-09-03): deterministic, exact; regenerates RESULTS.md whole.
set -e
PY=python3
cd "$(dirname "$0")"
$PY r1_roundness_classical.py   > r1_run.log 2>&1
$PY r2_schmitt_grid.py          > r2_run.log 2>&1
$PY r3_neighbour_identity.py    > r3_run.log 2>&1
$PY r4_orden_vertex_stabilizers.py > r4_run.log 2>&1
$PY r5_orden_region.py          > r5_run.log 2>&1
$PY r6_laves_wyckoff.py         > r6_run.log 2>&1
$PY r7_schmitt_table_sums.py    > r7_run.log 2>&1
$PY r8_schmitt_grid_201_224.py  > r8_run.log 2>&1
{
  echo "# Round-2 computations for the seven-shape paper (2026-09-03)"
  echo
  echo "Scripts r1-r8 in this directory; all exact (fractions.Fraction) on the frozen harness (orbit.py, exact_cell.py, canon_code.py, phase1_types.json) and the round-1 helpers (round1_computations/common.py). Regenerate with run_all.sh; each script's stdout is in r*_run.log. Written by Claude (Fable 5.1) in a Claude Code session as the round-2 fix-editor task, in answer to paper/REVIEW_COLD_R2_2026-09-03.md (W2, W3(f), W5, W7, W9, Q2-Q6; r7 checks the printed frequency sums, r8 the reduced domains of IT(201)/IT(224)); machine results, not AI-generated numbers. Acceptance: main-session re-run of run_all.sh, exit 0."
  echo
  cat r1_roundness_classical.md; echo; cat r2_schmitt_grid.md; echo; cat r3_neighbour_identity.md; echo; cat r4_orden_vertex_stabilizers.md; echo; cat r5_orden_region.md; echo; cat r6_laves_wyckoff.md; echo; cat r7_schmitt_table_sums.md; echo; cat r8_schmitt_grid_201_224.md
} > RESULTS.md
echo "RESULTS.md written"
