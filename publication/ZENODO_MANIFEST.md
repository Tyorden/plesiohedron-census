# ZENODO_MANIFEST — what a MINT deposit contains (staged 2026-09-01)

One Zenodo record (DOI) for the whole hunt, the Josehedron-family playbook
(precedent: Bernhard's own record 10.5281/zenodo.19471917). Tyler creates the
record and pushes the button; this manifest is the packing list. Everything
listed is already on disk under `paper_prep/MINT_plesiohedron/`.

## Contents

1. **Harness code** (`harness/`): `spacegroup_ops.py`, `orbit.py`,
   `sweep_voronoi.py`, `exact_cell.py`, `canon_code.py`, `sweep_phase1.py`,
   `triage_phase1.py`, `mint_tables.py`, `g0_regression.py`, `audit_g1.py`,
   `g2_seed_catalog.py`, `g2_controls.py`, `g4_certify.py`,
   `g5_rekey_check.py`, `schmitt_220_check.py`, `schmitt_collision_check.py`,
   `schmitt_crossgroup_check.py`, `xcheck_schmitt_ops.py`, `test_canon.py`.
2. **The frozen group data**: `harness/spacegroups.json` (230 groups, 4,425
   ops, exact rationals; G1-audited; independently confirmed op-by-op against
   Schmitt's 2016 pre-LLM derivation — zero discrepancies on all 229
   comparable groups).
3. **Certificates and result documents**: `harness/G0_RESULT.md` …
   `G4_RESULTS.md`, `MINT_TABLES_RESULT.md`, `PHASE1_RESULT.md`,
   `TRIAGE_RESULT.md`, `SCHMITT_220_CHECK_RESULT.md`,
   `SCHMITT_COLLISION_RESULTS.md`, `CROSS_GROUP_RESULTS.md`,
   `G5_DILIGENCE_2026-08-30.md`, `ANCHORS.md` (the pre-registered gates),
   plus the type store `harness/phase1_types.json` (all 102 stored types with
   witnesses) and `harness/rekey_tables.json` (the independent re-key).
4. **Per-shape publication packages**: this `publication/` tree — per
   finalist: `COORDS.md` (exact coordinates), `render.png`, banked
   `g4_tables_<id>.json/.txt` (+ proper-ops export), `counts.md`; for the
   four publishable-now shapes the OEIS draft texts and a-files;
   `ROUNDNESS.md`; `build_packages.py` (regenerates all of it,
   deterministic).
5. **Recovery provenance referenced, NOT re-deposited**: the Schmitt
   repository recovery tarballs stay out of the deposit; the record cites
   their durable Software Heritage identifiers instead
   (`SCHMITT_DATA_RECOVERY_2026-08-28.md`):
   - directory `swh:1:dir:d812ef736b08ffd6072dfd59725f1ba5ff4194ec`
   - revision  `swh:1:rev:97cb86b649d5bf9df82f9e9895150f2dfbb93616`
   - snapshot  `swh:1:snp:8978d77b0000297a95f6a42926a3fa48c59f973b`
   Likewise NOT deposited: `references/` PDFs (Schmitt's dissertation is
   doi:10.17169/refubium-14374; Bernhard is arXiv:2604.07160 — cite, don't
   re-host).

## License note

Code: MIT (consistent with the program's prior deposits). Data/tables/text:
CC-BY-4.0. The compiled `enumerate` binary is excluded (source is already
public as the A398957 a-file; cite it). Tyler confirms license lines at
deposit time.

## Wall / sensitivity check

Performed 2026-09-01: this tree contains NO wall-sensitive content — no
track_h/market material, no employer-adjacent material, no personal data
beyond Tyler's own name (which he places on the record deliberately). The
Schmitt recovery tarballs (third-party code) are excluded from the deposit
itself per item 5. The two manuscripts under `papers/` (SVU program) are a
DIFFERENT project and are not part of this tree.

## Deposit metadata (suggested)

- Title: "Certified space-filling polyhedra from a gated agentic search:
  code, certificates, and per-shape data (MINT)"
- Creators: Tyler Satchel Orden (independent researcher)
- Description: includes the house AI-disclosure sentence and the snapshot
  wording ("not matched against the records checked as of 2026-09-01");
  NEVER "new to science".
- Related identifiers: arXiv:2604.07160 (cites), doi:10.17169/refubium-14374
  (cites), the three SWHIDs above (references), A398957/A398958/A398959
  (is-supplemented-by), plus the four shapes' new A-numbers when assigned.

## Sequencing (Tyler's call, per the two-track decision)

The deposit can go out with the four publishable-now shapes fully presented
and the three HELD shapes included as certified-but-diligence-pending (their
packages already say so); or wait for the ILL check and deposit once. Either
is honest — the per-shape status lines carry the difference.

## v2 section (2026-09-04 22:48 PDT, subagent #165): the refreshed deposit after phase 2 and the catalog

Scope of the refreshed record: the cubic seven-shape paper (draft_v4) AND the census beyond the
cubic system (tetragonal + hexagonal families, 165 certified cells, the 1,583-type catalog v5).
This section lists what the refreshed zip MUST contain; the zip itself is NOT built here (the
public repository is #166's task; the wall re-sweep of every artifact precedes any upload, and
the export is built from the scanned folder, never from the MathProofs repo: RULES_BANK 28).
Everything listed is on disk under paper_prep/MINT_plesiohedron/. Items 1-5 of the 2026-09-01
list stay in the record unchanged; the following are ADDED.

6. Round-1 and round-2 computations of the paper's revision: harness/round1_computations/
   (c1-c5 scripts, JSON, RESULTS.md, run_all.sh, c*_run.log) and harness/round2_computations/
   (r1-r8 scripts, JSON, RESULTS.md, run_all.sh, r*_run.log); the paper's generated tables
   paper/{master_table_v2,cert_table_v2,counts_table_v2,roundness_table_v3,appendix_coords_v2}.tex
   with paper/{make_tables.py,make_roundness_v3.py,wyckoff_check.py,wyckoff_check.txt}.
7. Phase-2 code: harness/{sweep_phase2_tetragonal.py, sweep_phase2_hexagonal.py, triage_phase2.py,
   triage_phase2_hexagonal.py, collision_phase2_check.py, collision_phase2_hex_check.py,
   collision_phase2_tetragonal_storeside.py, collision_phase2_tetragonal_rows_recompute.py,
   g4_certify_gram.py, g4_certify_hex.py, digitize_schmitt_hexagonal.py, rekey_hexagonal_diff.py,
   phase2_schmitt_origin_check.py, phase2_hex_schmitt_180_check.py} and harness/phase2/{metric.py,
   sweep_voronoi_gram.py, exact_cell_gram.py, g2b_controls.py, g2c_controls.py, plan_counts.py,
   wall_open_phase2.py, pool_ranking_2026-09-04.py, nice_points_2026-09-04.py}.
8. Phase-2 stores and hashes: harness/phase2_types.json.gz + phase2_types.SHA256SUMS;
   harness/phase2_hexagonal_types.json.gz + phase2_hexagonal_types.SHA256SUMS (the raw JSON
   files and the resume log phase2_hexagonal_records.jsonl are EXCLUDED: regenerable, ignored).
9. Digitizations and re-keys of Schmitt's printed tables: harness/{rekey_tables.json,
   schmitt_tetragonal_tables.json, schmitt_tetragonal_rows_harvested.json,
   schmitt_hexagonal_tables.json, schmitt_hexagonal_rekey.json}; the documents
   SCHMITT_TETRAGONAL_DIGITIZATION_2026-09-04.md, SCHMITT_HEXAGONAL_DIGITIZATION_2026-09-04.md,
   SCHMITT_HEXAGONAL_REKEY_2026-09-04.md.
10. Phase-2 results and certificates: harness/{PHASE2_RESULT.md, PHASE2_HEX_RESULT.md,
    TRIAGE_PHASE2_RESULT.md, TRIAGE_PHASE2_HEX_RESULT.md, triage_phase2_hex_shortlist.json,
    COLLISION_PHASE2_RESULTS.md, collision_phase2_results.json, collision_phase2_tetragonal_storeside.json,
    collision_phase2_tetragonal_rows_recomputed.json, collision_phase2_tetragonal_unresolved_overlay.json,
    COLLISION_PHASE2_HEX_RESULTS.md, collision_phase2_hex_results.json, PHASE2_SCHMITT_ORIGIN_CHECK.md,
    phase2_schmitt_origin_check.json, PHASE2_HEX_SCHMITT_180_CHECK.md, phase2_hex_schmitt_180_check.json,
    ORDER_CYCLE_FIX_2026-09-04.md, G4_PHASE2_RESULTS.md, G4_PHASE2_HEX_RESULTS.md}; the certificate
    tables g4p2_tables_<id>.{json,txt,_indep.json} (14 cells) and g4p2hex_tables_<id>.{json,txt,_indep.json}
    (151 cells) with harness/g4p2hex_cells/; the control files g4p2_control_* and g4p2hex_control_*;
    harness/phase2/{G2B_RESULT.md, G2C_RESULT.md}; the run logs g4p2_run.log, phase2_run.log,
    phase2_hex_run.log, phase2_origin_check_run.log.
11. Open/wall classification and the naming staging: harness/phase2/{WALL_OPEN_PHASE2.md,
    WALL_OPEN_PHASE2.json (md5 6b257c551f6fb275dfabb03e992f57c2), wall_open_run1.log, wall_open_run2.log}
    + harness/phase2/wall_open_cells/; harness/phase2/{POOL_RANKING_2026-09-04.json,
    NICE_POINTS_2026-09-04.json}; POOL_RANKING_2026-09-04.md; NICE_POINTS_2026-09-04.md
    (harness/phase2/nice_points_cells/, 90 MB, regenerable, EXCLUDED).
12. Pre-registration and plans: ANCHORS.md (with the G2b, G2c and PERTURBATION CLASSIFICATION blocks),
    PHASE2_PLAN.md, NAMING_DECISION_BRIEF_2026-09-01.md (with its Sep-4 addenda and the executed ruling).
13. THE CATALOG v5: catalog/{catalog.json.gz, catalog.csv.gz, catalog_sightings.json.gz,
    catalog.SHA256SUMS (sha256: catalog.json.gz 6ffea7ee7a264134d7abceb6f1429901ece60408a4909e02590d3a58f21351db,
    catalog.csv.gz c1c0ae4b6eaf8583bfaa74c382dca604064a38fe83a7a305b8636e686cb28cdf,
    catalog_sightings.json.gz aab7fda4b4f8c15d2d60269ec2a3865a1dce0416a18fa37913fa8c4ca1b03c04),
    build_catalog.py, reconcile_schmitt.py, verify_counts_independent.py,
    check_satchelhedron_tetragonal_rows.py, RECONCILIATION.md, reconciliation_cubic.csv,
    reconciliation_tetragonal.csv, reconciliation_hexagonal.csv, reconciliation_summary.json,
    SATCHELHEDRON_TETRAGONAL_ROWS.md, STATUS.md, VERIFICATION_INDEX.md, and the data descriptor
    (DATA_DESCRIPTOR_v2_SCIDATA_2026-09-04.md after Tyler's rewrite)}; the raw catalog.json / catalog.csv
    are EXCLUDED (regenerable from the .gz; hashes in the SUMS file).
14. Track 4 (optional, Laves and Engel cells): track4/{TRACK4_RESULTS.md, TRACK4_CERT_LOG.md,
    g4_tables_laves17*.{json,txt}, g4_tables_engel38*.{json,txt}, independent_runs/}.
15. The paper's audit trail (text, CC-BY-4.0): paper/{TRACE.md, CLAIMS_AUDIT_2026-09-03.md,
    CLAIMS_AUDIT_V4.md, REVIEW_COLD_2026-09-03.md, REVIEW_COLD_R2_2026-09-03.md, REVIEW_COLD_R3.md};
    STATUS.md; VERIFICATION_INDEX.md; PROVENANCE.md. The manuscript PDF itself goes to arXiv, not here.
Still NOT deposited (unchanged): the Schmitt recovery tarballs (SWHIDs cited), references/ PDFs, the
compiled enumerate binary, any transcript or prompt-corpus material.

Deposit metadata v2 (suggested):
- Title: "Certified space-filling polyhedra from a gated agentic search: code, certificates, catalog,
  and per-shape data (MINT)" (the word "catalog" added).
- Version: 2 (v1 = the 2026-09-01 staged zip, never uploaded; if v1 was never published, publish v2 as
  the first version and keep this note).
- Description: the v2 block of ZENODO_DESCRIPTION.txt (house first-person disclosure; snapshot date
  2026-09-04; phase-2 and catalog numbers).
- Keywords: plesiohedron, Dirichlet stereohedron, space-filling polyhedron, Voronoi cell, space groups,
  cubic, tetragonal, trigonal, hexagonal, combinatorial type, catalog, polyform enumeration.
- Related identifiers: as v1, plus the GitHub mirror https://github.com/Tyorden/plesiohedron-census
  (is-supplemented-by; NOTE: gh repo view FAILED at 22:26 PDT 2026-09-04, repository being created by
  #166; verify before publishing), the data descriptor DOI when it exists, the arXiv ID when assigned.
- Snapshot wording: every type is "not matched against the records checked as of 2026-09-04"; the
  observed literature maximum is 38 facets; "new to science" appears nowhere.
Wall / sensitivity check: to be re-run by the main session on the assembled zip before upload (the
2026-09-01 check covered items 1-5 only). No em dash appears in this section.
