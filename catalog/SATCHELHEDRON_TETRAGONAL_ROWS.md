# Satchelhedron vs Schmitt's two tetragonal (16,25,11) rows - type-level check

Raised by RECONCILIATION.md. Accepted phase-2 exact chain (`harness/sweep_phase2_tetragonal.evaluate`: exact orbit, Gram metric, float proposal, exact clip with the 4*rho^2 <= D^2 certificate asserted, orbit congruence, canonical code); origin-choice-2 -> origin-choice-1 shifts from `harness/phase2_schmitt_origin_check.json` (all shifts that reproduced every printed row of the group are run and must agree).

Satchelhedron stored code sha1[:16] = `8cf50403cf88c455`, f=(16,25,11), p=3^2 4^1 5^8, aut 4.

| IT | symbol | printed c/a | printed point (his coords) | shift | our point | exact f | p-vector | aut | code == Satchelhedron? | stored id (any) | secs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 134 | P4_2/nnm | 4/5 | (43/125,-1/10,11/50) | +(1/4,3/4,1/4) | (297/500,13/20,47/100) | (16, 25, 11) | 3^2 4^6 5^1 7^1 8^1 | 1 | DIFFERENT | not stored | 0.2 |
| 134 | P4_2/nnm | 4/5 | (43/125,-1/10,11/50) | +(1/4,3/4,3/4) | (297/500,13/20,97/100) | (16, 25, 11) | 3^2 4^6 5^1 7^1 8^1 | 1 | DIFFERENT | not stored | 0.1 |
| 134 | P4_2/nnm | 4/5 | (43/125,-1/10,11/50) | +(3/4,1/4,1/4) | (547/500,3/20,47/100) | (16, 25, 11) | 3^2 4^6 5^1 7^1 8^1 | 1 | DIFFERENT | not stored | 0.1 |
| 134 | P4_2/nnm | 4/5 | (43/125,-1/10,11/50) | +(3/4,1/4,3/4) | (547/500,3/20,97/100) | (16, 25, 11) | 3^2 4^6 5^1 7^1 8^1 | 1 | DIFFERENT | not stored | 0.1 |
| 141 | I4_1/amd | 797/1000 | (62/125,62/125,0) | +(0,3/4,1/8) | (62/125,623/500,1/8) | (16, 25, 11) | 3^3 4^4 6^3 7^1 | 1 | DIFFERENT | not stored | 0.3 |
| 141 | I4_1/amd | 797/1000 | (62/125,62/125,0) | +(0,3/4,5/8) | (62/125,623/500,5/8) | (16, 25, 11) | 3^3 4^4 6^3 7^1 | 1 | DIFFERENT | not stored | 0.2 |
| 141 | I4_1/amd | 797/1000 | (62/125,62/125,0) | +(1/2,1/4,1/8) | (249/250,373/500,1/8) | (16, 25, 11) | 3^3 4^4 6^3 7^1 | 1 | DIFFERENT | not stored | 0.2 |
| 141 | I4_1/amd | 797/1000 | (62/125,62/125,0) | +(1/2,1/4,5/8) | (249/250,373/500,5/8) | (16, 25, 11) | 3^3 4^4 6^3 7^1 | 1 | DIFFERENT | not stored | 0.2 |

**Verdict: both printed (16,25,11) cells reproduce their printed f-vector under every documented shift and are DIFFERENT combinatorial types from the Satchelhedron** (and, per the last column, whether either is any stored type). This is not a novelty claim: his tables print one representative per (group, f-vector) from a grid sampling; the Satchelhedron remains 'not matched against the records checked as of 2026-09-04'. New micro-fact of the Josehedron/Schmitt-220 class: f = (16,25,11) is realised by at least 3 distinct combinatorial types across the survey (the Satchelhedron plus one per printed row; codes pairwise distinct).

Provenance: script `catalog/check_satchelhedron_tetragonal_rows.py`, exact arithmetic throughout, deterministic; main-session re-run required before acceptance. Computed with the assistance of Claude (Anthropic).
