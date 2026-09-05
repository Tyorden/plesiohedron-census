# MINT_plesiohedron — provenance (2026-08-28)
IDEA ORIGIN: Tyler Orden, 2026-08-27, verbatim: "he invented a new shape, why cant
we?" — immediately after his LinkedIn comment to Mathias Bernhard announcing the
A398957-9 josehedron polyform sequences.
INPUTS: LANDSCAPE_SCOUT_FABLE5_2026-08-27.md (agent #72 in the prompt corpus;
GO-WITH-HOOK: Fischer-Koch Y; corrections appended on intake) ·
HARNESS_DESIGN_FABLE5_2026-08-27.md (agent #73; function-level reuse map) ·
PROGRAM_PLAN_2026-08-27.md (5 tracks, written by the main session).
ANCESTOR CODE (verified, in production use): build_josehedron.py, g1_verify.py,
enumerate.cpp (publicly deposited as A398957 a-file), audit_t1_independent.py,
burnside_generic.py (ALL PASS n<=7 on both existing honeycombs, 2026-08-27).
METHOD PRECEDENT: Bernhard arXiv:2604.07160 (explicitly invites follow-ups incl.
"the help of a creative LLM-based agent" — citable).
MODEL: Fable 5 (claude-fable-5) main session + subagents per prompt corpus #72-77.

2026-09-04 (append-only, doc-gap audit #144): MODEL from 2026-09-03 = Fable 5.1
(claude-fable-5-1) main session + subagents #118-#119, #121-#122, #126, #129-#132,
#134-#137, #139-#141, #143 (all Fable 5.1); every computation re-run by the main session
before acceptance (ledger 2026-09-03/04 "verify-before-accept" lines). Model per block:
control/MODEL_ATTRIBUTION.md regime-5 rows; prompt/outcome per agent:
AuditArchive/prompt_corpus/SUBAGENT_SPAWN_PROMPTS.md.

2026-09-04 17:50 PDT (append-only, work-log agent #156): MODEL for the phase-2 continuation
= Fable 5.1 (claude-fable-5-1) main session + subagents #145 (hexagonal G4), #146 (catalog
v2), #147 (blind re-key), #148 (open/wall), #149 (pool ranking), #150 (catalog v3), #152
(store-side rule / catalog v4), #153 (nice points), #154 (62 rows / catalog v5; first report
rejected on a determinism defect, corrected, accepted) — all Fable 5.1, no overrides; every
computation re-run by the main session before acceptance (ledger 2026-09-04 12:40-15:54 PDT).
Consolidated record: control/FABLE51_WORK_LOG_2026-09-03_to_04.md.

2026-09-04 22:48 PDT (append-only, subagent #165): MODEL for the v4 paper round = Fable 5.1
(claude-fable-5-1) main session + subagent #165 (draft_v4.tex from draft_v3.tex by scripted
replacement; CLAIMS_AUDIT_V4.md; REVIEW_COLD_R3.md; catalog/DATA_DESCRIPTOR_v2_SCIDATA_2026-09-04.md;
ZENODO_MANIFEST/DESCRIPTION v2 sections; naming ruling executed). No computation was run beyond
table regeneration (make_tables.py, make_roundness_v3.py: byte-identical) and identity checks on
the generated tables; every number traces to the documents named in CLAIMS_AUDIT_V4.md. Provisional
until the main session reviews the diff and re-compiles.
