# catalog/ STATUS (MINT Track 3 - THE CATALOG)

2026-09-04 (subagent #141, Claude Fable 5.1): TRACK 3 BUILT - first machine-readable
census of the program's exact-confirmed plesiohedron combinatorial types, reconciled
against Schmitt 2016 at f-vector level; provisional until the main session re-runs
`verify_counts_independent.py` (exit 0 required) and, for the follow-up type check,
`check_satchelhedron_tetragonal_rows.py`.

FILES (all under paper_prep/MINT_plesiohedron/catalog/):
- build_catalog.py -> catalog.json (3.8 MB; summary + 891 records + field_sources),
  catalog.csv (891 rows; canon_code and sightings omitted), catalog_sightings.json.gz
  (sidecar, {type_id: [sighting]}); deterministic (byte-identical across re-runs).
  Inputs read-only: harness/phase1_types.json, harness/phase2_types.json.gz
  (decompressed bytes hashed against phase2_types.SHA256SUMS =
  71685b9a...69f7a3 before use), spacegroups.json, triage_phase1.py SCHMITT_FVECTORS
  (ast-parsed, never imported), rekey_tables.json, schmitt_tetragonal_tables.json,
  the three collision-result files, g4_tables_*/g4p2_tables_* pointers,
  round1_computations/c1_wall_open.json, paper/wyckoff_check.txt, publication/ names.
- reconcile_schmitt.py -> RECONCILIATION.md, reconciliation_cubic.csv,
  reconciliation_tetragonal.csv, reconciliation_summary.json; deterministic.
- verify_counts_independent.py (no shared code with the builder): recounts from the
  stores and asserts equality with catalog.json; exit 0, 0 failures.
- check_satchelhedron_tetragonal_rows.py -> SATCHELHEDRON_TETRAGONAL_ROWS.md
  (imports the accepted harness/sweep_phase2_tetragonal.evaluate read-only; needs
  paper_prep_venv python).
- DATA_DESCRIPTOR_DRAFT.md, VENUE_SCOUT.md, this STATUS.md; run logs
  build_catalog_run.log, reconcile_run.log, check_run.log.

COUNTS (catalog.json summary; independently recounted): 891 types = 102 cubic-first
+ 789 tetragonal-first; 7 seeded (1 never sighted by any sweep: Schmitt's IT(220)
general (12,22,12) representative); tetragonal-first 404 menu-sighted / 385
Schmitt-printed-only; 19 cubic-first types re-sighted in tetragonal groups (18 by
the menu); types with >= 1 cubic sighting 99, with >= 1 tetragonal sighting 808;
175 distinct f-vectors (65 cubic-first, 153 tetragonal-first); max F 35 (menu 26,
cubic 23); G4 accepted 12 (11 cubic + Laves), provisional g4p2 tables on disk 14
(agent #140 running; the number moves); names 2 program / 2 descriptive / 3 HELD;
Schmitt type-level SAME 589 / DIFFERENT 282 / unchecked 20; f-vector flag over
sighted groups P 880 / A 10 / n/a 1. Per-group table in build_catalog_run.log and
catalog.json["summary"]["per_group"] (top first-here: IT98 137, IT122 91, IT91 70,
IT92 70, IT141 37, IT80 30; cubic IT230 9, IT204 8, IT214 8).

RECONCILIATION HEADLINE (f-vector level; match != identity; absence = evidence;
his survey = sampling): CUBIC 986 printed (group,f) pairs from 881 rows: (a) 292
matched by our menu (309 type-sightings), (b) 33 of ours absent from his table for
that group (34 type-sightings), (c) 694 of his unreached by our menu; whole-system
distinct f: his 194 / ours 63 / shared 62; only (16,25,11) of ours is in no cubic
table. TETRAGONAL 1,639 printed (group,f) pairs from 1,476 rows (1,641 with shared
tables): (a) 700 matched (355 at a c/a we also sampled; 988 type-sightings), (b) 67
absent (68), (c) 939 unreached by our menu = 941 rows, of which 669 stored via P2
at his own point and 270 with no stored type; whole-system his 163 / ours 80 /
shared 80; his f-vectors unreached anywhere by our menu 83 (4 even counting P2).

FINDINGS vs STATUS.md / named-shape claims:
1. NO count in STATUS.md is contradicted: 102/789/404/385, 19 re-sighted, max 23/26/35,
   0 phase-1 quarantines, 11 + Laves G4, all reproduce. One definitional note: the
   STATUS 2026-09-04 line "Groups by tetragonal-menu type count: 98 (60), 141 (59),
   122 (57) ..." uses the store's type-GLOBAL flag (a type counts for group g if it
   is menu-sighted anywhere and sighted in g by any pass); the sighting-local count
   (types whose sighting IN g came from the menu) is 98: 48, 141: 59, 122: 39, 92:
   33, 96: 32, 91: 23, 88: 33, 118: 15, 94: 17, 80: 21. Both are correct under their
   definition; the wording should say which.
2. SATCHELHEDRON: the banked "(16,25,11) absent from the ENTIRE printed cubic survey"
   holds, but the STATUS 2026-09-01 shorthand "whole printed survey" does not: the
   f-vector IS printed in two TETRAGONAL tables, IT(134) P4_2/nnm at c/a = 4/5, point
   (43/125,-1/10,11/50) (PDF p. 78) and IT(141) I4_1/amd at c/a = 797/1000, point
   (62/125,62/125,0) (PDF p. 84). Both rows were never stored (two-origin groups).
   Follow-up run today: both cells, under every documented origin shift, are
   DIFFERENT types from the Satchelhedron (IT134 cell 3^2 4^6 5^1 7^1 8^1 aut 1;
   IT141 cell 3^3 4^4 6^3 7^1 aut 1; neither is any stored type), so (16,25,11) is
   realised by at least 3 distinct types across his survey plus ours. The paper's
   own-group criterion is unaffected; the "whole printed survey" shorthand should
   read "cubic survey". Provisional until the main session re-runs the check.
3. ORDENHEDRON: (20,33,15) absent from the IT(201) table (as banked); printed in 9
   other cubic groups (all 9 representatives DIFFERENT, accepted cross-group screen)
   and in 5 tetragonal tables (91/95 at 14/25, 98 at 2, 122 at 2, 142 at 2); three
   of those rows were stored via P2 under other ids (21e0b5a7ebe148d6,
   802c7ba284e53e8d, 3282abd05218d9c6 = DIFFERENT by the dedupe), IT(95) and IT(142)
   rows not stored (unchecked). No contradiction.
4. The two IT(224) cells and the three HELD cells: no contradiction; their f-vectors
   appear in many tetragonal tables, mostly stored via P2 under other ids (DIFFERENT
   by dedupe); the unstored rows are listed per type in catalog.json.
5. The phase-2 store carries ONLY tetragonal sightings for cubic-first types
   (phase1_sightings is a count); any consumer of phase2_types.json alone would see
   the Satchelhedron with zero sightings. The catalog merges both stores.
6. One cubic-first type (2001fe7ea92fd0ad, triakis truncated tetrahedron) carries
   schmitt_printed_only=True in the phase-2 store (386 True flags vs the 385 headline);
   already noted by triage_phase2; recorded in field_sources.

RE-RUN COMMANDS (main session, absolute paths):
  python3 <repo>/catalog/verify_counts_independent.py
  python3 <repo>/catalog/build_catalog.py
  python3 <repo>/catalog/reconcile_schmitt.py
  python3 <repo>/catalog/check_satchelhedron_tetragonal_rows.py

UNTESTED AGAINST: a second independent re-key of the tetragonal digitization; the
14 provisional g4p2 certificates (agent #140, not accepted); Engel 1981 (print-only);
any venue page for Scientific Data or Acta Cryst A (fetch blocked); trigonal /
hexagonal / lower-symmetry groups (not swept). Wording: snapshot language only
("not matched against the records checked as of 2026-09-04"); "observed max 38".
No harness file modified; no commit; no outreach. FQ1 8014 and PIDs 7417/13578/9155
untouched; all runs under nice 10, seconds each.

2026-09-04 01:55 (append-only; recorded by doc-gap audit #144 from the ledger): ACCEPTED by the
main session - verify_counts_independent.py re-run exit 0 (0 failures) and
check_satchelhedron_tetragonal_rows.py re-run (both tetragonal (16,25,11) rows DIFFERENT
types). The "provisional" wording above is historical. Own-goal 46 (scope noun) and 47
(mid-run commit of this folder) booked in the own-goal ledger. Ledger 2026-09-04 01:55;
corpus #141 OUTCOME; registry A25/A26.

2026-09-04 (later; subagent #146, Claude Fable 5.1): *** THE CATALOG v2 - HEXAGONAL
FAMILY FOLDED IN + BOTH PHASE-2 G4 BATCHES *** provisional until the main session re-runs
`verify_counts_independent.py` (exit 0 required). v1 (891 types) stays reproducible from
git: `git show 06e5d30:paper_prep/MINT_plesiohedron/catalog/{build_catalog,reconcile_schmitt,verify_counts_independent}.py`
(no flag; the three scripts were rewritten in place as v2). Rule 29 honoured: every run
was a foreground call (seconds each, nice 10). No harness file modified; no commit; no
outreach; FQ1 8014 and PIDs 7417/13578 untouched.

FILES (all under paper_prep/MINT_plesiohedron/catalog/):
- build_catalog.py v2 -> catalog.json (9.2 MB), catalog.csv (4.4 MB), catalog_sightings.json.gz
  (258,521 sightings = 1,597 cubic + 148,390 tetragonal + 108,534 hexagonal), NEW committed
  forms catalog.json.gz (0.77 MB) / catalog.csv.gz (0.51 MB) with catalog.SHA256SUMS
  (gzip mtime 0; two consecutive runs byte-identical on all five files). Inputs read-only;
  the hexagonal store phase2_hexagonal_types.json.gz was verified before use: gz sha256
  2974c26b... and decompressed sha256 7494c7b26114a68f1177158eb311a05546ba0b15cd5b1a27569c633858983a55
  == both lines of phase2_hexagonal_types.SHA256SUMS; phase-2 store 71685b9a... as in v1.
  v1 schema kept (every v1 column name and every v1 catalog_id); NEW columns:
  first_sighting_family, first_sighting_crystal_system, crystal_families_sighted,
  crystal_systems_sighted (trigonal/hexagonal split), n/groups/c_over_a *_hexagonal(_menu),
  sighted_by_kinds_hexagonal, schmitt_printed_only_hexagonal, g4_status {accepted-cubic,
  certified-tetragonal, certified-hexagonal, none}, g4_certificate_file, g4_results_doc,
  g4_acceptance, g4_chiral_solid (+ _source), g4_chiral_honeycomb (n_improper == 0 in the
  tables file), schmitt_fvector_printed_anywhere_hexagonal, schmitt_match_hexagonal.
  field_sources names the source of every new column. Sightings sidecar rows carry
  crystal_system and, for hexagonal P2 rows, printed_point_Bpp / conversion /
  schmitt_primary_group / pdf_page. catalog_id MINT-H001..H692 for hexagonal-first types.
- reconcile_schmitt.py v2 -> reconciliation_hexagonal.csv (new), reconciliation_cubic/
  tetragonal.csv (unchanged numbers), reconciliation_summary.json (v2), RECONCILIATION.md
  APPEND-ONLY: the v1 text is preserved byte for byte (asserted) and the cubic/tetragonal
  headline numbers recomputed from the v2 catalog are asserted equal to it; dated section
  "## v2 (2026-09-04): hexagonal family (IT 143-194)" appended.
- verify_counts_independent.py v2 (no shared code): recounts from the three raw stores,
  the certificate files on disk and the two phase-2 G4 docs; 0 failures, exit 0.
- DATA_DESCRIPTOR_DRAFT.md: dated v2 section appended. This STATUS.md; run logs
  build_catalog_run.log, reconcile_run.log, verify_run.log.

COUNTS (catalog.json v2 summary; independently recounted): 1,583 types = 102 cubic-first
+ 789 tetragonal-first + 692 hexagonal-first (288 menu-sighted / 404 Schmitt-printed-only;
first-witness crystal system trigonal 398 / hexagonal 294); 7 seeded (1 never sighted);
43 prior types re-sighted in the hexagonal family (17 cubic-first, 26 tetragonal-first;
34 by our menu, 9 only at his printed points); types with >= 1 sighting: cubic 99,
tetragonal 808, hexagonal family 735 (trigonal groups 450, hexagonal groups 353); all 52
groups IT 143-194 have sightings; 196 distinct f-vectors (65 / 153 / 167 by first family);
max F 35 overall (tetragonal, unchanged), hexagonal-first 34 (his IT(178) row), hexagonal
menu 24; kill bar 38 never crossed. G4: 177 certified = accepted-cubic 12 (11 + Laves)
+ certified-tetragonal 14 (accepted 2026-09-04 01:35) + certified-hexagonal 151 (accepted
2026-09-04 13:25); none 1,406; provisional 0. CHIRAL SOLIDS where the certificate records
it: 153 chiral / 12 achiral (tetragonal 13/1, hexagonal 140/11); the 12 cubic
certificates record no solid-chirality rung (null, said so in field_sources). CHIRAL
HONEYCOMBS (all point ops proper, from the tables files): 138 of 177 (cubic 5, tetragonal
12, hexagonal 121 = the G4_PHASE2_HEX_RESULTS "121 chiral honeycombs" figure). Schmitt
type-level SAME 1,125 / DIFFERENT 449 / unchecked 9; f-vector flag P 1,568 / A 14 / n/a 1
(the 5 hexagonal-first A's = the triage's "ABSENT-all 5"). schmitt_match_hexagonal:
SURVIVOR 151 / COLLISION 124 / UNRESOLVED 13 (re-derived here from the store + tables with
the documented rule and asserted == TRIAGE_PHASE2_HEX_RESULT.md for all 288; survivors ==
the 151 certificates), printed-only S-cell 404, prior re-sighted 43, n/a 848. Hexagonal
groups by types first witnessed there (first/sighted/menu-sighted): 178: 109/138/45,
155: 71/110/33, 152: 65/86/28, 167: 64/103/27, 148: 52/79/25, 181: 49/102/44,
166: 47/79/57, 180: 46/63/49 (full table in build_catalog_run.log).

RECONCILIATION HEADLINE, HEXAGONAL FAMILY (f-vector level; match != identity; absence =
evidence; his survey = sampling): 958 printed rows in 45 blocks -> 1,276 printed (group,f)
pairs (7 enantiomorphic pairs share a table); (a) 510 matched by our menu (278 at a c/a we
also sampled; 728 type-sightings), (b) 40 of ours absent from his table for that group
(42 type-sightings), (c) 766 of his unreached by our menu = 766 rows, of which 733 stored
via P2 at his own point, 33 = IT(180) rows reproduced only by the read-only z->-z re-run
(cells already stored; the printed points are IT(181)'s per his normalizer remark), 0 with
no stored type; whole-family distinct f: his 177 / our menu 95 / shared 94; his f-vectors
unreached anywhere by our menu 83 (0 even counting P2 + the read-only rows); ours in no
trigonal/hexagonal table: 1, (20,36,18). Cross-family: 137 of his 177 also printed in a
cubic table, 152 in a tetragonal table, 3 in this family only. Cubic/tetragonal numbers
unchanged from v1 (986/292/33/694; 1,639/700/67/939).

FINDINGS vs STATUS.md / the G4 docs:
1. NO count in STATUS.md (later 5/6/7) or in G4_PHASE2_RESULTS.md / G4_PHASE2_HEX_RESULTS.md
   is contradicted: 1,583 = 891 + 692 (288 + 404), 43 re-sighted (17 + 26), max 34 / menu
   24, 1,230 + 46 = 1,276 P2 reproductions, 151/124/13, 14/14 and 151/151 certified,
   140/11 chiral, 121 chiral honeycombs all reproduce from the stores and files.
2. Definitional note (not a contradiction): STATUS (later 6) and the G4 hex doc number
   survivors by SURVIVOR rank (1-151, = survivors_ranked); the triage FULL-table rank runs
   over all 288 (e.g. survivor #9 5b86a254c715306c is full-table rank 10, #10
   f05f0b009e0929f6 is rank 11). The catalog column states both.
3. NEW arithmetic facts (from the stores, not interpreted): the three digitizations total
   881 + 1,476 + 958 = 3,315 rows and their distinct f-vectors union to 238 with printed
   max 38 - equal to the "3315 combinatorial types / 238 f-vectors / max 38" Schmitt's own
   text states for his survey (SCHMITT_PRIMARY_READ line 36). His "145 space groups"
   versus our 36 + 68 + 52 = 156 digitized groups is left to the main session to read
   against the primary text. Consequence, scope noun included: of our 196 f-vectors, exactly
   ONE, (20,36,18), is printed in none of his tables in any of the three digitized families
   (MINT-H152 f07d69523ef41b37, IT(178) P6_122 at c/a = 3/2, aut 2, survivor rank 63,
   certified-hexagonal, unchecked at type level because no printed representative exists);
   the Satchelhedron's (16,25,11) is absent from the cubic tables only (printed in 2
   tetragonal and 6 trigonal/hexagonal rows, all 6 stored via P2 under other ids =
   DIFFERENT types by the dedupe).
4. catalog.json (9.2 MB) now exceeds the repo's "> 5 MB stay out" whitelist policy (v1 was
   3.8 MB and is tracked); catalog.csv is 4.4 MB. The .gz forms + catalog.SHA256SUMS are
   written as the committed forms (store convention). .gitignore was NOT edited (own-goal
   44/45 rules); the main session decides whether to append ignore lines for the raw
   catalog.json (and .csv) before `git add`.
5. The hexagonal store's prior_first_witness equals the phase-2 first_witness or, where
   that is null (81 cubic-first types), phase-2's phase1_first_witness (asserted); the
   catalog witness columns follow v1 (phase-1 witness for cubic-first types).

RE-RUN COMMANDS (main session, absolute paths, in this order):
  python3 <repo>/catalog/build_catalog.py
  python3 <repo>/catalog/reconcile_schmitt.py
  python3 <repo>/catalog/verify_counts_independent.py
  (exit 0 each; catalog.SHA256SUMS and RECONCILIATION.md must be unchanged by the re-run)

UNTESTED AGAINST: the independent re-key of the trigonal/hexagonal digitization (agent
#147, in progress; G5 duty); computed open/wall for the 165 phase-2 certified cells
(agent #148; the catalog's open_wall column is still v1's 10 types); Engel 1981 / Koch
print-only records (cubic exposure applies to the hexagonal groups too); the 43 prior
types' hexagonal status is f-vector level only (not collision-screened in this family).
Wording: snapshot language only ("not matched against the records checked as of
2026-09-04"); "observed max 38"; G4 != novelty; no hexagonal-family type is named.

2026-09-04 (later; subagent #150, Claude Fable 5.1): *** THE CATALOG v3 - COMPUTED OPEN/WALL
VERDICTS + TYPE-LEVEL SCHMITT STATUS FOLDED IN *** provisional until the main session re-runs the
three scripts below (exit 0 each; catalog.SHA256SUMS, RECONCILIATION.md and
reconciliation_summary.json unchanged by the re-run). v2 (1,583 types, 177 certified) stays
reproducible from git:
`git show 169ccb4:paper_prep/MINT_plesiohedron/catalog/{build_catalog,reconcile_schmitt,verify_counts_independent}.py`
(no flag; the three scripts were rewritten in place as v3). Rule 29 honoured: every run was a
foreground call (seconds each, nice 10). No harness file modified; no commit; no outreach; FQ1 8014
and PIDs 7417/13578 untouched.

FILES (all under paper_prep/MINT_plesiohedron/catalog/):
- build_catalog.py v3 -> catalog.json (10.7 MB, ignored), catalog.csv (5.5 MB, ignored), the committed
  forms catalog.json.gz (0.84 MB) / catalog.csv.gz (0.56 MB) and catalog.SHA256SUMS (gzip mtime 0; two
  consecutive runs byte-identical on all five files). catalog_sightings.json.gz UNCHANGED (sha256
  aab7fda4... as in v2; only the build label in its SHA256SUMS line changed). Every v1/v2 column keeps
  its name, position and value (0 diffs over 1,583 rows x 78 columns against the v2 file); the v1 AND
  v2 summary numbers are asserted unchanged. NEW columns (10, appended after the v2 columns):
  open_wall_verdict (OPEN / WALL / ONE-SIDED / not-computed), open_wall_verdict_source (c1 cubic /
  phase2 #148 / none - named so because the v2 column open_wall_source already exists and is kept
  verbatim), open_wall_point_verdict, open_wall_metric_verdict, open_wall_flags,
  open_wall_verdict_pointer (file + record + doc rank + previous heuristic label + acceptance record),
  open_wall_scheme, open_wall_scheme_date (2026-09-04 pre-registered / 2026-09-03 c1),
  schmitt_type_status (SURVIVOR / COLLISION / UNRESOLVED / printed-only / not-screened),
  schmitt_type_status_source (doc pointer, rank, pair counts). Sources verified before use:
  harness/phase2/WALL_OPEN_PHASE2.json (md5 6b257c551f6fb275dfabb03e992f57c2 asserted == the value
  WALL_OPEN_PHASE2.md states; 165 cells, 0 crashes; store hashes == the two verified stores, unchanged
  after the run; ids == the 165 certificate files; per-family verdict counts == the file's aggregate
  block; witness point / c/a / group / f / aut / stratum dim == the stores; top-3 tetragonal POINT
  verdicts == collision_phase2_results.json 'perturbation'), harness/round1_computations/
  c1_wall_open.json (7 cubic finalists; .verdict == the v1/v2 open_wall head token),
  harness/collision_phase2_results.json (27 pairs -> 15 targets; per-target status == the 'Summary per
  shortlist type' lines of COLLISION_PHASE2_RESULTS.md), collision_phase2_hex_results.json +
  TRIAGE_PHASE2_HEX_RESULT.md (counts == the section-1 line of COLLISION_PHASE2_HEX_RESULTS.md; top-10
  post block == the doc). NEW summary blocks: open_wall_verdict_counts, open_wall_verdict_source_counts,
  schmitt_type_status_counts, open_wall_x_schmitt_type_status, naming_pool (+ note); field_sources
  entries added for every new column (the v2 'open_wall' entry gained a bracketed v3 note, its v2 text
  intact); top-level v2_reproducibility line; inputs block records the wall/open file md5 + sha256.
- reconcile_schmitt.py v3 -> RECONCILIATION.md APPEND-ONLY one level further: the v1 + v2 text is
  preserved byte for byte (asserted: the v1 and v2 sections regenerated from the v3 catalog equal the
  preserved text; verified as an exact prefix against the v2 file), dated section "## v3 (2026-09-04):
  computed open/wall verdicts x type-level Schmitt status" appended (cross-tab per family, naming pool
  with ids, the 50 certified phase-2 cells outside the pool with POINT/METRIC/flags, limits);
  reconciliation_cubic/tetragonal/hexagonal.csv unchanged; reconciliation_summary.json gained v3_*
  blocks (copied from the catalog summary).
- verify_counts_independent.py v3 (no shared code): recounts the new columns from the raw verdict /
  screen / certificate files with its own loaders and asserts every per-row value and every v3 summary
  block, the cross-tab and the pool; 0 failures, exit 0.
- DATA_DESCRIPTOR_DRAFT.md: dated v3 section appended (data-records additions, technical validation
  items 8-11 with the pre-registered scheme, limitations). This STATUS.md; run logs regenerated.

COUNTS (catalog.json v3 summary; independently recounted): open_wall_verdict per first-sighting
family - cubic OPEN 6 / WALL 1 / ONE-SIDED 0 / not-computed 95 (c1 finalists); tetragonal OPEN 13 /
WALL 1 / ONE-SIDED 0 / not-computed 775; hexagonal OPEN 102 / WALL 40 / ONE-SIDED 9 / not-computed
541 (= PROGRAM_LEDGER 2026-09-04 14:10). schmitt_type_status - cubic not-screened 102; tetragonal
SURVIVOR 14 / COLLISION 1 / UNRESOLVED 0 / printed-only 385 / not-screened 389; hexagonal SURVIVOR
151 / COLLISION 124 / UNRESOLVED 13 / printed-only 404 / not-screened 0. CROSS-TAB (verdict x
status): tetragonal OPEN x SURVIVOR 13, WALL x SURVIVOR 1, not-computed x {COLLISION 1, printed-only
385, not-screened 389}; hexagonal OPEN x SURVIVOR 102, WALL x SURVIVOR 40, ONE-SIDED x SURVIVOR 9,
not-computed x {COLLISION 124, UNRESOLVED 13, printed-only 404}; cubic OPEN x not-screened 6, WALL x
not-screened 1, not-computed x not-screened 95 (every certified phase-2 cell is a SURVIVOR by
construction: the certificate sets equal the screens' survivor sets). NAMING POOL = certified AND OPEN
AND unnamed: tetragonal 13 (MINT-T004 / T005 / T076 / T137 / T151 / T152 / T264 / T716 / T721 / T722 /
T758 / T766 / T767), hexagonal 102, cubic 0 (the 6 OPEN accepted-cubic cells all carry a program
name, a descriptive package name or a HELD marker; 5 accepted-cubic types have no perturbation run
on record) - asserted == 13 + 102 in the builder and recounted by the verifier; full id lists in
catalog.json summary.naming_pool and RECONCILIATION.md v3.

FINDINGS / DEFINITIONAL NOTES:
1. NO count in STATUS.md, WALL_OPEN_PHASE2.md, COLLISION_PHASE2_RESULTS.md,
   COLLISION_PHASE2_HEX_RESULTS.md or the ledger is contradicted: 115 / 41 / 9, 13 / 1, 102 / 40 / 9,
   151 / 124 / 13, 14 + 1, 13 + 102 all reproduce from the files.
2. The three v2 open_wall strings for the tetragonal top-3 ("point OPEN / c-over-a OPEN" twice,
   "point WALL / c-over-a OPEN") agree with the #148 verdicts (POINT asserted equal; METRIC OPEN on all
   three under the relative scheme).
3. schmitt_type_status for tetragonal-first types: only the 15 shortlist types were ever
   collision-screened; 176 of the 389 not-screened menu-sighted types are S-cells (type-level SAME by
   pass P2, already in schmitt_type_level_status) and would be COLLISION under the hexagonal screen's
   store-side rule, which was never run on the tetragonal family. The column says not-screened and
   the source column states the S-cell fact; extending the rule is a main-session decision, not made
   here.
4. Cubic-first types are not-screened by the two phase-2 screens by construction (their cubic-round
   pair verdicts stay in schmitt_type_level_*); the 12 accepted-cubic types therefore show
   not-screened in the cross-tab - a scope fact, not a gap in the cubic record.
5. catalog.csv (raw) is now 5.5 MB (> 5 MB) as well as catalog.json (10.7 MB); both are already
   ignored since v2; the .gz forms + catalog.SHA256SUMS remain the committed forms. No .gitignore edit.
6. Untracked files from another agent seen in the tree (POOL_RANKING_2026-09-04.* under
   paper_prep/MINT_plesiohedron/ and harness/phase2/) were not read, used or touched.

RE-RUN COMMANDS (main session, absolute paths, in this order):
  python3 <repo>/catalog/build_catalog.py
  python3 <repo>/catalog/reconcile_schmitt.py
  python3 <repo>/catalog/verify_counts_independent.py
  (exit 0 each; catalog.SHA256SUMS, RECONCILIATION.md and reconciliation_summary.json must be unchanged)
  catalog.SHA256SUMS (v3): catalog.json 2c83bc205288ede8690274475ad16364ab9407171fda070eaf88341f8f07b772
  (10,703,643 bytes); catalog.json.gz a304d84393742131bd1428acbe8b6090b2961485ba3b9476c756853ed21e079a
  (837,986); catalog.csv a795ddd6d0e2813706c6a018a6addd9b4cffbef98ad9af273b56d504803a8c28 (5,466,784);
  catalog.csv.gz b56fc8d10d773b4e8b61c9012c2eb0ecfae574f416ba3067fadabb9975531174 (561,564);
  catalog_sightings.json.gz aab7fda4b4f8c15d2d60269ec2a3865a1dce0416a18fa37913fa8c4ca1b03c04 (1,217,329;
  unchanged from v2).

UNTESTED AGAINST: the blind re-key of the trigonal/hexagonal digitization (agent #147; a changed row
could move a hexagonal type between SURVIVOR / COLLISION / UNRESOLVED); a second independent
implementation of the perturbation chain (the verdicts are #148's, re-run once by the main session);
sightings other than the first witness (verdicts are per first witness only); step sizes below
1/1536 (point) and 1/3072 relative (metric); Engel 1981 / Koch print-only records (G5 for every pool
member); the tetragonal store-side collision rule (not run). Wording: snapshot language only; OPEN =
holds on the tested neighbourhood; SURVIVOR != novelty; no type is named here.

2026-09-04 (later; subagent #152, Claude Fable 5.1): *** THE CATALOG v4 - TETRAGONAL STORE-SIDE SCHMITT
STATUS FOLDED IN (both phase-2 families under one rule) *** provisional until the main session re-runs the
four commands below (exit 0 each; the harness script must print md5 64cc7bb82e85164914d7ec441cfc1304 and
"addendum appended: False"; catalog.SHA256SUMS, RECONCILIATION.md and reconciliation_summary.json unchanged
by the re-run). v3 stays reproducible from git:
`git show e01618b:paper_prep/MINT_plesiohedron/catalog/{build_catalog,reconcile_schmitt,verify_counts_independent}.py`
(no flag; the three scripts were rewritten in place as v4). Rule 29 honoured: every run was a foreground
call (seconds each, nice 10). Harness: ONE new file pair (collision_phase2_tetragonal_storeside.py / .json)
plus a dated append-only addendum to COLLISION_PHASE2_RESULTS.md; no other harness file modified; both
stores read-only (sha256 verified before and after). No commit; no outreach; FQ1 8014 and PIDs 7417/13578
untouched. Untracked files of agent #151 (paper_prep/S2_polyhex_symmetry/data/live_2026-09-04/) not touched.

WHAT CHANGED (the consistency step queued in the ledger 2026-09-04 15:40; no new mathematics, no cell
computed). v3 finding 3 said 176 of the 389 not-screened tetragonal menu-sighted types are S-cells and would
be COLLISION under the hexagonal screen's store-side rule, never run on the tetragonal family:
- harness/collision_phase2_tetragonal_storeside.py re-implements the rule of collision_phase2_hex_check.py
  lines 115-139 as a pure function (the hexagonal script imports the sweep modules and needs the venv's
  numpy; this one runs on plain python3) and ASSERTS its equivalence on the hexagonal family FIRST:
  SURVIVOR 151 / COLLISION 124 / UNRESOLVED 13 of 288, per-type verdict == TRIAGE_PHASE2_HEX_RESULT.md
  full table for all 288, survivor ranking identical: PASS. Rule text stated once in the addendum.
  Row <-> stored P2 cell keying: hexagonal (group, printed_point_Bpp, b) exact as the hexagonal script;
  tetragonal (group, point mod 1, b) as triage_phase2.py frac_key (exact keying gives the same 404
  verdicts; recorded in the JSON). 1215 stored tetragonal P2 cells keyed (= TRIAGE_PHASE2_RESULT.md).
- Tetragonal, all 404 menu-sighted types: PURE rule COLLISION 176 (= the 176 S-cells) / SURVIVOR 116 /
  UNRESOLVED 112. OVERLAY of COLLISION_PHASE2_RESULTS.md's 27 recomputed shortlist pairs (SAME -> COLLISION;
  DIFFERENT on an unstored row -> that row resolved): COLLISION 177 / SURVIVOR 121 / UNRESOLVED 106.
  Without the overlay 5 of the 14 certified survivors (shortlist ranks 1, 2, 3, 13, 15, whose worklists
  had unstored second-enantiomorph / two-origin / IT(80) rows) and cd4fb52572edcb73 read UNRESOLVED; the
  recomputation resolved exactly those rows. Both verdicts are stored per type.
- Shortlist consistency: 0 disagreements with the 15 'Summary per shortlist type' lines; the 14 certified
  survivors stay SURVIVOR; cd4fb52572edcb73 stays COLLISION. Transitions v3 -> v4 over the 404:
  not-screened -> COLLISION 176 / SURVIVOR 107 / UNRESOLVED 106; SURVIVOR 14 and COLLISION 1 unchanged.
  Of the 107 new SURVIVORs, 4 have an f-vector printed in no sighted group's table and 103 have every
  printed row at their (group, f) reproduced as a different stored type. The 106 UNRESOLVED hang on 62
  distinct unstored printed rows (rows quarantined in the sweep: two-origin groups 86, 88, 126, 130, 133,
  134, 137, 138, 141, 142; second enantiomorphs 95, 96; IT(80) order_cycle rows) - 99 types on a single
  row, 6 on two, 1 on three; none has been recomputed, so UNRESOLVED is neither survivor nor collision.

CATALOG v4 (build_catalog.py / reconcile_schmitt.py / verify_counts_independent.py rewritten in place):
- Columns: none added or renamed (89, identical to v3). Diff v3 (git e01618b catalog.json.gz) vs v4:
  exactly 404 rows differ, all tetragonal-first menu-sighted, in schmitt_type_status (389 rows) and
  schmitt_type_status_source (404 rows; the 15 shortlist rows only gain a v4 clause) - nothing else.
  Summary: the two counting blocks (schmitt_type_status_counts, open_wall_x_schmitt_type_status) follow;
  NEW block schmitt_type_status_tetragonal_storeside (pure / overlaid / v3 counts, transitions, JSON md5);
  NEW inputs entry collision_screen_tetragonal_storeside_v4 (md5 + sha256); top-level v3_reproducibility
  line; field_sources schmitt_type_status gained a [v4] clause. Every v1 / v2 / v3 summary number outside
  those blocks asserted unchanged; catalog_sightings.json.gz byte-identical (aab7fda4...). Two consecutive
  builds byte-identical on all five files.
- schmitt_type_status counts v4: cubic not-screened 102 (scope fact); tetragonal SURVIVOR 121 / COLLISION
  177 / UNRESOLVED 106 / printed-only 385 / not-screened 0; hexagonal 151 / 124 / 13 / 404 / 0 (unchanged).
  Cross-tab tetragonal: OPEN x SURVIVOR 13, WALL x SURVIVOR 1, not-computed x {SURVIVOR 107, COLLISION 177,
  UNRESOLVED 106, printed-only 385}.
- NAMING POOL unchanged: 13 tetragonal + 102 hexagonal-family + 0 cubic (asserted in the builder and the
  reconciler; recounted by the verifier); every pool member SURVIVOR.
- reconcile_schmitt.py v4: RECONCILIATION.md APPEND-ONLY one level further (checked: the v3 file is an exact
  prefix of the v4 file; v1 + v2 regenerated from the v4 catalog and asserted equal; the v3 section kept
  verbatim as the pre-rule record); dated v4 section with the cross-tab, the v3 -> v4 tetragonal status
  table, the pool and the v4 limits. reconciliation_summary.json: v3_* blocks renamed v4_* plus
  v4_schmitt_type_status_tetragonal_storeside. Deterministic (two runs byte-identical).
- verify_counts_independent.py v4 (no shared code): its OWN implementation of the rule reproduces the
  hexagonal screen 151/124/13 per type, re-derives all 404 tetragonal verdicts (pure and overlaid) and
  asserts them == the JSON, == every catalog row, and the JSON md5 == the addendum's and the catalog's
  stated value; 0 failures, exit 0.
- catalog.SHA256SUMS (v4): catalog.json a022869a9a46b2ba8a3a5a22fc39e71f6aa13f99b6747a750514c2b9d47e4af3
  (10,827,542 bytes); catalog.json.gz 0419aad920fdaff02a3a89ce22d464f56c76ea61e7ebec09a8de59d3806ce50e
  (847,322); catalog.csv 26671a3fb5186c0db5b25fdba1d2f42aa749c3087b7e7136655d2ae350310102 (5,587,941);
  catalog.csv.gz 8ab558fd068f99680a0f7e55a84b8a5c40717303c4a090eed0d6879ae28b0554 (572,505);
  catalog_sightings.json.gz aab7fda4b4f8c15d2d60269ec2a3865a1dce0416a18fa37913fa8c4ca1b03c04 (1,217,329;
  unchanged since v2). Raw catalog.json / .csv stay ignored; no .gitignore edit.
- Wall sweep: 0 hits in all 15 created / edited files (script, JSON, addendum, the three scripts,
  RECONCILIATION.md, reconciliation_summary.json, catalog.json / .csv, the three run logs, this file,
  DATA_DESCRIPTOR_DRAFT.md). DATA_DESCRIPTOR_DRAFT.md: dated v4 section appended.

RE-RUN COMMANDS (main session, absolute paths, in this order):
  python3 <repo>/harness/collision_phase2_tetragonal_storeside.py
  python3 <repo>/catalog/build_catalog.py
  python3 <repo>/catalog/reconcile_schmitt.py
  python3 <repo>/catalog/verify_counts_independent.py
  (exit 0 each; the harness script prints md5 64cc7bb82e85164914d7ec441cfc1304 and "addendum appended: False";
  catalog.SHA256SUMS, RECONCILIATION.md and reconciliation_summary.json must be unchanged)

UNTESTED AGAINST: everything the v3 entry lists (blind re-key #147; a second perturbation implementation;
Engel / Koch print-only records) plus: the 62 unstored rows behind the 106 UNRESOLVED tetragonal types have
never been recomputed at the printed point with the documented conversions (PHASE2_SCHMITT_ORIGIN_CHECK.md) -
a recomputation pass like the shortlist's would move each of them to SURVIVOR or COLLISION; the tetragonal
digitization is a single visual pass, text-layer cross-checked, not re-keyed. Wording: snapshot language only
("not matched against the records checked as of 2026-09-04"); SURVIVOR != novelty; UNRESOLVED != survivor;
COLLISION = first-realization reframe; no type is named here.

2026-09-04 15:19 PDT (subagent #154, Claude Fable 5.1): *** THE CATALOG v5 - THE 62 UNSTORED TETRAGONAL PRINTED ROWS
RECOMPUTED; THE 106 UNRESOLVED SETTLED (no tetragonal UNRESOLVED left) *** provisional until the main session
re-runs the four commands below (exit 0 each; the harness script must print rows JSON md5
90b8b94b7585e95afa5025f54bd4b941, overlay JSON md5 6d0ee2362e93ea9f8e154f610fd4f289 and "addendum appended:
False"; catalog.SHA256SUMS, RECONCILIATION.md and reconciliation_summary.json unchanged by the re-run). v4 stays
reproducible from git: `git show 27e0083:paper_prep/MINT_plesiohedron/catalog/{build_catalog,reconcile_schmitt,verify_counts_independent}.py`
(no flag; the three scripts were rewritten in place as v5). Rule 29 honoured: every run was a foreground call
(recomputation 43 s single process under nice 10; build/reconcile/verify seconds each). Harness: ONE new script +
TWO new JSONs (collision_phase2_tetragonal_rows_recompute.py, collision_phase2_tetragonal_rows_recomputed.json,
collision_phase2_tetragonal_unresolved_overlay.json) plus a dated append-only addendum to COLLISION_PHASE2_RESULTS.md
(196 lines added, 0 removed; git diff checked); the accepted modules phase2/{metric,sweep_voronoi_gram,exact_cell_gram}.py
and sweep_phase2_tetragonal.py were imported, never modified; phase2_types.json / .gz READ-ONLY (sha256 71685b9a...
verified before and after; nothing minted). No commit; no outreach; FQ1 8014 and PIDs 7417/13578 untouched.
Untracked files of other agents (#153) not touched.

WHAT CHANGED (the pass the v4 UNTESTED-AGAINST line asked for). v4 left 106 menu-sighted tetragonal-first types
UNRESOLVED because 62 printed rows at their (group, f) were never stored by pass P2 (two-origin groups 86, 88, 126,
130, 133, 134, 137, 138, 141, 142 and the second enantiomorphs 95, 96: Schmitt's coordinates in another setting,
quarantined as schmitt_fvec_mismatch; IT(80): the order_cycle crash row).
- harness/collision_phase2_tetragonal_rows_recompute.py recomputes every one of the 62 rows at the printed point
  through the accepted exact chain (sweep_phase2_tetragonal.evaluate; certificate asserted per cell) under EVERY
  documented convention of its group (PHASE2_SCHMITT_ORIGIN_CHECK.md via collision_phase2_check.conversions_for
  verbatim: all origin shifts that reproduced every row, primary = best_shift; 95/96: z -> -z primary + the other
  signed-axis transforms; IT(80): verbatim) AND the other origin / enantiomorph reading (printed point verbatim = what
  P2 ran), recorded but never counted. 306 cells computed. RESULT: 62/62 rows REPRODUCED (printed f-vector back under
  every documented convention, one canonical code per row across the 4 conventions in every two-origin / 95 / 96 row);
  the other reading reproduced the printed f in 0/62 (as expected: those are the P2 quarantines); 0 QUARANTINE, 0
  AMBIGUOUS, 0 timeouts; the two rows already recomputed for the shortlist (Q14 IT(86), Q24 IT(80)) give the same
  codes. 17 row cells are stored under no id (types our menu never sampled; read-only, not added); 26 row cells are one
  of their hanging types (-> the 24 collisions; two types are SAME at two rows each); 17 are stored types outside the
  106 (15 already COLLISION / printed-only S-cells, expected; 2 cubic-first store types, see FACTS).
- Verdicts (rule stated once): per UNRESOLVED type, any hung-on row SAME -> COLLISION; all rows REPRODUCED and
  DIFFERENT -> SURVIVOR; any row not reproduced -> UNRESOLVED. The 106 -> COLLISION 24 / SURVIVOR 82 / UNRESOLVED 0.
  Tetragonal menu-sighted totals (404): v4 COLLISION 177 / SURVIVOR 121 / UNRESOLVED 106 -> v5 COLLISION 201 /
  SURVIVOR 203 / UNRESOLVED 0. Transitions: COLLISION->COLLISION 177, SURVIVOR->SURVIVOR 121, UNRESOLVED->COLLISION 24,
  UNRESOLVED->SURVIVOR 82. The 14 certified survivors were never UNRESOLVED and are untouched (asserted in the harness
  script, the builder and the verifier); cd4fb52572edcb73 stays COLLISION; the 15 shortlist statuses unchanged.
- FACTS recorded, no status effect: (1) Schmitt's printed IT(95) P4_322 (30,45,17) row at b = 797/1000,
  point (309/500, 59/500, 1/8), IS the accepted-cubic Laves-cell type 8c69db9e84095469 (4^6 5^6 6^2 8^3, aut 12) -
  a cross-system sighting of a literature-named cell at his printed tetragonal representative (cubic-first types are
  not-screened by the phase-2 screens by construction). (2) His IT(137) P4_2/nmc (18,28,12) row at b = 3497/1000,
  point (1/4, -1/4, 1/4), is the cubic-store type c1824c64dfbb3615 (4^8 6^4, aut 16: the elongated-dodecahedron
  f-vector and p-vector). (3) Type 5c6382a9ef3bc209 (COLLISION at its hung-on IT(133) row) also equals the recomputed
  IT(142) (58/125, 58/125, 29/250) b = 3497/1000 cell, a group where our menu never sighted it (secondary hit; no
  status effect). No row reproduced under no convention; no SURVIVOR type's code appeared at any recomputed row.

CATALOG v5 (build_catalog.py / reconcile_schmitt.py / verify_counts_independent.py rewritten in place):
- Columns: none added or renamed (89, identical to v4). Diff v4 (git 27e0083 catalog.json.gz) vs v5: exactly 106
  rows differ, all tetragonal-first menu-sighted, in schmitt_type_status and schmitt_type_status_source only (the
  source text gains a [v5] clause naming each recomputed row with its PDF page, verdict and row-cell id). Summary:
  schmitt_type_status_counts and open_wall_x_schmitt_type_status follow; NEW block
  schmitt_type_status_tetragonal_unresolved_recomputed (md5s, row status counts, cells computed, hits classified,
  counts_106, counts before/after, transitions, still_unresolved [], secondary hits, recorded facts); NEW inputs
  entry collision_screen_tetragonal_rows_recomputed_v5 (both files, md5 + sha256); top-level v4_reproducibility line;
  field_sources schmitt_type_status gained a [v5] clause. Every v1 / v2 / v3 / v4 summary number outside those blocks
  asserted unchanged; catalog_sightings.json.gz byte-identical (aab7fda4...). Two consecutive builds byte-identical on
  all five files; reconcile and verify byte-identical on re-run.
- Cross-tab tetragonal (v5): OPEN x SURVIVOR 13, WALL x SURVIVOR 1, not-computed x {SURVIVOR 189, COLLISION 201,
  printed-only 385}; hexagonal and cubic unchanged.
- NAMING POOL unchanged: 13 tetragonal + 102 hexagonal-family + 0 cubic (asserted in the builder and the reconciler;
  recounted by the verifier); every pool member SURVIVOR.
- reconcile_schmitt.py v5: RECONCILIATION.md APPEND-ONLY one level further (checked: the committed v4 file is an exact
  prefix of the v5 file; v1 + v2 regenerated from the v5 catalog and asserted equal; v3 and v4 sections kept verbatim);
  dated v5 section with the cross-tab, the v4 -> v5 tetragonal status table (incl. the 106 row), the pool and the v5
  limits. reconciliation_summary.json: v4_* blocks renamed v5_* plus v5_schmitt_type_status_tetragonal_unresolved_recomputed.
- verify_counts_independent.py v5 (no shared code): own keying of the 62 recomputed rows to each type's own
  unstored-row list, own comparison of the recorded canonical code with the store's, own check that every recorded
  cell's code id is the sha1 of its code and that its f-vector equals the digitized printed row's; asserts == the
  overlay JSON per type, == every catalog row, md5s == the addendum's and the catalog's; tetragonal 201/203/0; the 15
  shortlist statuses and the 13 + 102 pool unchanged; 0 failures, exit 0.
- catalog.SHA256SUMS (v5): catalog.json 011fc534bd3880e1ed816e7f8e537df9b4eb4cd8a014cdc9d44e869bbabd9513
  (10,891,630 bytes); catalog.json.gz 7c4a3d80921fe685c5df7924c42333d302fbcb81a1e6e66d4d6a685d39ae648f (858,899);
  catalog.csv 7122a8d3d901ae3dac3290ff07273570907a103c13159a55ad903080f976ea35 (5,645,919); catalog.csv.gz
  ca2114b4cf54c96a65309c53e17b639b11e5217c913edf8dcfd3fdf1a13c3918 (577,616); catalog_sightings.json.gz
  aab7fda4b4f8c15d2d60269ec2a3865a1dce0416a18fa37913fa8c4ca1b03c04 (1,217,329; unchanged since v2). Raw
  catalog.json / .csv stay ignored; no .gitignore edit.
- Wall sweep: new-vocabulary check (alphabetic tokens in every created / edited file not already present in the
  committed tree) reviewed: 0 employer / client terms. DATA_DESCRIPTOR_DRAFT.md: dated v5 section appended.

RE-RUN COMMANDS (main session, absolute paths, in this order):
  cd <repo>/harness && nice -n 10 python3 <repo>/harness/collision_phase2_tetragonal_rows_recompute.py
  python3 <repo>/catalog/build_catalog.py
  python3 <repo>/catalog/reconcile_schmitt.py
  python3 <repo>/catalog/verify_counts_independent.py
  (exit 0 each; the harness script prints "rows JSON md5 90b8b94b7585e95afa5025f54bd4b941; overlay JSON md5
  6d0ee2362e93ea9f8e154f610fd4f289; addendum appended: False; store sha unchanged: True"; catalog.SHA256SUMS,
  RECONCILIATION.md and reconciliation_summary.json must be unchanged; verify prints "0 failures")

UNTESTED AGAINST: the blind re-key of the tetragonal digitization (still a single visual pass, text-layer
cross-checked; a changed row moves a type between statuses); a second independent implementation of the exact chain
(the 306 cells are one chain's output, re-run once by the main session); Schmitt's unprinted data (his tables print
ONE point per (group, f) from a grid sampling, so SURVIVOR is type-level at every printed representative of the
type's (group, f) pairs and nothing more); Engel 1981 / Koch print-only records (G5 for every pool member); the
cubic-first types' status in the tetragonal tables (two of the 62 recomputed rows ARE cubic-store types - recorded,
not folded into schmitt_type_status, which stays not-screened for cubic-first types by construction). Wording:
snapshot language only ("not matched against the records checked as of 2026-09-04"); SURVIVOR != novelty;
COLLISION = first-realization reframe; no type is named here.

2026-09-04 15:29 PDT (subagent #154, Claude Fable 5.1) CORRECTION to the v5 entry above (append-only; the old text stands as
written): the md5s it states (rows 90b8b94b..., overlay 6d0ee236...) and its catalog.SHA256SUMS were RUN-DEPENDENT. The
main-session re-run produced rows b0549f9c... / overlay 0db5a709... with identical verdict content, so build_catalog.py's
md5-in-addendum assertion failed (exit 1) and the verifier reported 108 failures. Cause: the rows JSON carried a
top-level wall_seconds and a per-cell secs, and the overlay referenced the rows file by that changing md5. Fix: all
timings moved to the run log (no timing field in either JSON; asserted by the builder and the verifier); the two files
are byte-identical across runs. STABLE md5s: collision_phase2_tetragonal_rows_recomputed.json
4d27ce41466509feab6a180249330af7; collision_phase2_tetragonal_unresolved_overlay.json a3716a2330c6dbe9c93414dfe8e832ee.
A dated CORRECTION paragraph with the stable md5s was appended to the #154 addendum in COLLISION_PHASE2_RESULTS.md (old
text untouched; the script appends it once, only when the addendum heading exists without the current md5s). The builder
and the verifier now ALSO assert content equality with the addendum's tables (62 row lines: status + code id; 106 type
lines: verdict) rather than relying on the md5 alone. Verdict content unchanged: 62 REPRODUCED; the 106 -> 24 COLLISION /
82 SURVIVOR / 0 UNRESOLVED; tetragonal 201 / 203 / 0; pool 13 + 102. Re-run: build -> reconcile -> verify exit 0, 0
failures; SHA256SUMS identical across two builds; RECONCILIATION.md still append-only (committed v4 file an exact
prefix). catalog.SHA256SUMS (v5, corrected): catalog.json 4768f18b22f786bfa999962739a0895c6cdb876119c3735b74c376738c7cc2b8
(10,891,630 bytes); catalog.json.gz 6ffea7ee7a264134d7abceb6f1429901ece60408a4909e02590d3a58f21351db (858,911);
catalog.csv a83a205ed72388b7a922d30af91bded9e452b9026e6f19ea2de564f03a0483b0 (5,645,919); catalog.csv.gz
c1c0ae4b6eaf8583bfaa74c382dca604064a38fe83a7a305b8636e686cb28cdf (577,635); catalog_sightings.json.gz aab7fda4... unchanged.
RE-RUN (same four commands as the v5 entry, same order); expected harness line: "rows JSON md5
4d27ce41466509feab6a180249330af7; overlay JSON md5 a3716a2330c6dbe9c93414dfe8e832ee; addendum appended: False;
correction appended: False; store sha unchanged: True"; then build / reconcile / verify exit 0, "0 failures",
catalog.SHA256SUMS + RECONCILIATION.md + reconciliation_summary.json unchanged.
