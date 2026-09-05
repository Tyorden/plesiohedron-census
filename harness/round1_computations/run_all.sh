#!/bin/sh
# Round-1 computations (2026-09-03): deterministic, exact; regenerates RESULTS.md whole.
set -e
PY=python3
cd "$(dirname "$0")"
$PY c1_wall_open.py > c1_run.log 2>&1
$PY c2_isometry.py  > c2_run.log 2>&1
$PY c3_laves.py     > c3_run.log 2>&1
$PY c4_roundness.py > c4_run.log 2>&1
$PY c5_josehedron_wyckoff.py > c5_run.log 2>&1
{
  echo "# Round-1 computations for the seven-shape paper (2026-09-03)"
  echo
  echo "Scripts c1-c5 in this directory; all exact (fractions.Fraction) on the frozen harness (orbit.py, exact_cell.py, canon_code.py, phase1_types.json, the banked g4 tables). Regenerate with run_all.sh; each script's stdout is in c*_run.log. Written by Claude (Fable 5.1) in a Claude Code session as the round-1 fix-editor task; machine results, not AI-generated numbers. Acceptance: main-session re-run of run_all.sh, exit 0."
  echo
  cat c1_wall_open.md; echo; cat c2_isometry.md; echo; cat c3_laves.md; echo; cat c4_roundness.md; echo; cat c5_josehedron_wyckoff.md
} > RESULTS.md
echo "RESULTS.md written"
