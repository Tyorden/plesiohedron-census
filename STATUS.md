# MINT_plesiohedron STATUS
2026-08-28: gates pre-registered (ANCHORS.md) before any computation. Build step 1
(space-group freeze + exact closure, targeting G1) launched as a background agent.
TYLER GATES OPEN: Schmitt 2016 PDF (browser download) · Engel 1981 (ILL). Nothing
in G5 can close without them; G0-G3 computation may proceed.

2026-08-28 (later): G1 CLOSED - ALL PASS. spacegroups.json frozen (230 groups, 4,425
ops, translations exact n/12 rationals, spglib 2.7.0); independent no-shared-code
audit verifies identity/closure/inverses/orders for all 230; RE-RUN BY THE MAIN
SESSION (exit 0) before acceptance. Caveats banked: origin-choice-1 freeze for the
24 two-origin groups; centered groups carry conventional-cell coset lists. Next:
G0 josehedron regression through the new pipeline (needs sweep_voronoi + exact_cell
+ canon_code build), then G2 cubic controls.

2026-08-28 (later 2): G0 CLOSED - ALL IN-SCOPE ASSERTIONS PASS, re-run by the main
session (exit 0) before acceptance. The new pipeline (orbit -> float sweep -> exact
clip -> canonical code) re-derives the Josehedron from its generating orbit: 12
points/conventional cell (PERIOD 24), detL=256 giving T_primitive=6 == banked tables,
12 facets 4tri+8quad float AND exact with identical neighbor site sets, one canonical
code across all 12 cells (163 bytes, aut order 4 == site symmetry). Unit tests ALL
PASS (relabeling/mirror/distinctness; aut orders 48/48/48/24). Honest deferrals
recorded in G0_RESULT.md: ops/nbr-table/enumerator clauses belong to the mint_tables
step (not claimed). Design amendment accepted: non-simple vertices FLAGGED not fatal
(the Josehedron itself is non-simple - the design's exclude rule would reject the
regression target; ANCHORS G3's degeneracy routing reads accordingly). NEXT: G2 cubic
controls (seeded catalog: 5 parallelohedra by canonical code), then mint_tables step,
then the cubic sweep.

2026-08-28 (later 3): *** SCHMITT TYLER-GATE CLOSED *** Tyler downloaded the PDF
(browser beat the anti-bot wall); archived at references/Schmitt_2016_dissertation.pdf;
primary-source read banked in SCHMITT_PRIMARY_READ_2026-08-28.md. VERDICTS: (1) ch. 2
is a 351-CPU-year exact-arithmetic GRID SAMPLING of 145 groups (tetragonal/trigonal/
hexagonal/cubic; monoclinic+orthorhombic omitted citing Santos-series <38), finding
3,315 combinatorial types / 238 f-vectors, max 38 facets (Engel's I4_132 cell, his 4
types confirmed, no 5th) - NOT a complete enumeration, so KILL CRITERION 1 DOES NOT
TRIGGER in the strong form; a covered-group candidate stays possible but MUST be
diffed against his tables (f-vector) + GitHub data (type). (2) The folklore "38 max
proven" OVERSTATES the thesis - no grid-fineness bound is proven; refereed record
stays 38<=max<=92 open; our wording = "observed max 38" (measurement framing).
(3) Engel-1981 ILL priority DOWN (Schmitt confirms+corrects Engel/Koch-Fischer; ILL
now optional, Tyler's call). (4) Our harness = his pipeline + canonical codes;
Lemma B.2 (Koch slab bound) citable for sweep neighbor-completeness. PENDING TYLER:
ok to clone github.com/moritzschmitt/plesiohedron (code+data) for type-level
diligence?

2026-08-28 (later 4): *** JOSEHEDRON GROUP SETTLED + SCHMITT TYPE-CHECK RUN ***
(1) spglib on the generating orbit: IT(220) = I-43d, Wyckoff 12a, site symmetry -4
(order 4 == G0 aut order, independent cross-check). Bernhard never stated the group;
new recorded fact; 220 is in the scout's 8-group chiral corridor. (2) Schmitt's
IT(220) table (printed p.141) CONTAINS f=(12,22,12): point (143/1746, 289/3492,
295/3492), frequency 46/1.0e9. (3) EXACT TYPE COMPARISON (schmitt_220_check.py,
result banked): his cell = 6tri+4quad+2pent, aut 1; Josehedron = 4tri+8quad, aut 4.
NO MATCH - same f-vector, DIFFERENT combinatorial type. So IT(220) realizes
f=(12,22,12) by >=2 distinct types (new small fact), the Josehedron's type is NOT
in Schmitt's in-text representative table, and its special-position (12a) home is
exactly the corridor grid sampling under-covers - Bernhard's novelty claim
SURVIVES this diligence layer and our special-position sweep rationale is
STRENGTHENED. Limit honestly held: table lists one representative point per
f-vector; type-level closure needs Schmitt's published data (GitHub, pending ok).

2026-08-28 (later 5): G2 CLOSED - ALL IN-SCOPE ASSERTIONS PASS (provisional until
the main session re-runs g2_controls.py, exit 0 required). Built: (1)
harness/g2_seed_catalog.py - independent seeded catalog of the 5 parallelohedra
from published exact integer vertex data (Coxeter cube/rhombic dodeca/trunc octa;
rational affine image of the regular hexagonal prism; Fedorov elongated dodeca),
faces via exact all-integer hull-free enumeration (no scipy, no
sweep_voronoi/exact_cell import - independence ast-audited in B1c; only shared
module is canon_code, the identity function itself); writes seed_catalog.json
(f-vectors (8,12,6)/(12,18,8)/(14,24,12)/(18,28,12)/(24,36,14), auts
48/24/48/16/48, 5 codes pairwise distinct). (2) harness/g2_controls.py - gate:
control point sets DERIVED from frozen spacegroups.json (origin orbits of
Pm-3m#221/Fm-3m#225/Im-3m#229 = SC/FCC/BCC lattices, asserted), each through the
full chain (sweep W=2 float -> exact clip with provable 4*rho2<=D^2 cutoff ->
canon), float/exact agreement incl. neighbor site sets, ONE code per orbit,
MATCH REQUIRED vs catalog: cube / rhombic dodecahedron / truncated octahedron all
MATCH; 3 pipeline codes pairwise distinct; auts 48/48/48 == catalog. Honest
reading recorded in G2_RESULT.md: general-position Pm-3m (48 pts/cell) is the
P1-like degeneration ANCHORS excludes - the control is the lattice (Wyckoff
1a/4a/2a) Voronoi cell. Deferrals: hex prism + elongated dodeca are catalog-only
(await Phase-2 metric sweeps); Gram-metric path untested (still
NotImplementedError); aut orders are combinatorial (geometric C6 = G4/V2).
Deterministic: catalog sha + gate output byte-identical across re-runs. NEXT:
mint_tables step, then the cubic phase-1 sweep.

2026-08-28 (later 6): G2 ACCEPTED - main-session re-run of g2_controls.py: exit 0,
all 18 assertions PASS (byte-identical verdict to the builder's run). Aut orders
sanity-checked against literature (48/48/48 pipeline; catalog hex prism 24 = D6h,
elongated dodeca 16 = D4h). Gate G2 is CLOSED. Remaining before the cubic phase-1
sweep: the mint_tables step (closes G0's honest deferrals: |ops|=24 (12 proper),
nbr-table semantic equality to josehedron_tables.json, enumerator fixed/free n<=6).

2026-08-28 (later 7): MINT_TABLES STEP DONE - G0's three DEFERRED clauses CLOSED,
all 8 assertions PASS (provisional until the main session re-runs
harness/mint_tables.py, exit 0 required; run is deterministic - RESULT md and
derived JSON byte-identical across re-runs). Built harness/mint_tables.py:
independent all-Fraction derivation (BASE mod 8 -> G0 pipeline exact cells ->
exact primitive lattice detL=256 (= BCC <8e1,8e2,(4,4,4)>, verified both ways) ->
T=6 types -> nbr table -> signed-perm op search with completeness argument
Aut(BCC)=O_h) writing mint_josehedron_tables.json in the banked schema;
josehedron_tables.json loaded ONLY as comparison target (ast-audited, M0).
CLAUSE A: the "24" = honeycomb point ops MOD LATTICE (= point group of IT(220)
I-43d, -43m, 12 proper; the enumerator's ops object), NOT the -4 site symmetry
(order 4, verified via orbit.site_stabilizer on the frozen IT(220) entry;
24 = 6 types x 4). Derived ops: 24 (12 proper), closed, rotation parts == the 24
distinct IT(220) rotation parts; op-by-op equal to banked ops (24/24, proper
12/12, translation-normalized). CLAUSE B: explicit bijection verified exact on
all 6 nbr rows (witness = identity: independent tie-breaks landed on the banked
labels/basis; search was general, 720 perms + unimodular M from the bases).
CLAUSE C: banked workflow verbatim (banked export_tables.py + banked compiled
enumerate binary): derived vs banked tables IDENTICAL fixed/free n<=6 AND == the
banked verified record (free 1,2,15,131,1360,15133; fixed 6,36,308,3030,32262,
362010; one-sided supplement via proper_ops also identical, 1,4,30,261,2717,
30265). TASKING DISCREPANCY RECORDED (not papered over): the step instruction's
"published free n<=6 = 1,4,16,116,903,8551 (A397708/9)" matches nothing in the
tree; A397708/9 are the SPHENOID sequences, Josehedron = A398957/8 - gate
anchored to ANCHORS G0 wording + banked verified results instead. G0 is now
FULLY closed. NEXT: the cubic phase-1 sweep.

2026-08-28 (later 8): MINT_TABLES ACCEPTED - main-session re-run: exit 0, all 8
assertions PASS. G0's three deferred clauses (ops/nbr-table/enumerator) are now
CLOSED - G0 is fully closed, no deferrals outstanding. Interpretive finding banked:
ANCHORS G0's "24" = the honeycomb point group modulo lattice (=-43m point group of
IT(220), 12 proper), NOT the cell site symmetry (-4, order 4); 24 = T(6) x site(4).
OPERATOR-ERROR CATCH (ledger-grade): the spawn prompt (#88) wrongly cited
A397708/A397709 + the SPHENOID free counts (1,4,16,116,903,8551) as the Josehedron
anchors; the builder detected the mismatch (grep came up empty), refused the wrong
anchor, gated on ANCHORS' actual wording, and reported the discrepancy instead of
forcing agreement. Correct Josehedron record: free 1,2,15,131,1360,15133; fixed
6,36,308,3030,32262,362010; one-sided 1,4,30,261,2717,30265 (A398957 family).
PIPELINE NOW FULLY VALIDATED END-TO-END (orbit -> cells -> tables -> enumerator).
NEXT: cubic phase-1 sweep (the actual hunt).

2026-08-28 (later 9): SCHMITT REPO RECOVERED - via Software Heritage (11 full
crawls 2016-2019; Wayback was network-unreachable, and turned out redundant: repo
frozen after 2016-06-21, all crawls bit-identical). Recovered into
references/schmitt_repo_recovery/: full 3-commit git history + code
(plesiohedron.cpp/h, spacegrp.cpp, Makefile, 1-line README) + data/2d + data/3d
(generated C++ isometry representations, wallpaper groups 2-17 and space groups
2-230; 495 files 22MB). Durable copies = the two SWH tarballs (tracked); citable
SWHIDs in SCHMITT_DATA_RECOVERY_2026-08-28.md. DECISIVE NEGATIVE: the repo is
software+inputs ONLY - no results storage, no type-classification code; the
3,315-type tables and ~14TB output were NEVER on GitHub, Refubium bitstreams hold
only the PDF (OAI-PMH bypassed the bot wall), DataCite/Zenodo/figshare/forks all
empty. Type-level survey data is NOT recoverable online; options = printed
tables, recomputation with the recovered suite, or author contact (committer
identity preserved in the report; outreach = Tyler's call, not performed).
G5(b) diligence standard accordingly: thesis in-text tables + our own exact
recomputation at his printed representative points (the schmitt_220_check.py
pattern) = the achievable bar. NEW CHECK QUEUED: diff his 2016 data/3d isometry
representations (groups 2-230) against our frozen G1 spacegroups.json - a fully
independent historical cross-check of the G1 freeze.

2026-08-28 (later 10): SCHMITT OPS CROSS-CHECK COMPLETE - the queued diff of
his 2016 data/3d isometry representations (N=2..230) against the frozen G1
spacegroups.json ran clean. New: harness/xcheck_schmitt_ops.py (exact
Fractions arithmetic throughout, deterministic, exit 0) +
SCHMITT_OPS_XCHECK_2026-08-28.md. Format reverse-engineered first: 4x4
rational affine matrices (column convention, coset reps mod the full lattice)
+ splitters_ = centering vectors in spacegrp.cpp (cases 16..230 only; N<16
centering absent from recovered code). Result: 148 EXACT, 81
CONJUGATE-VERIFIED, 0 FINGERPRINT-ONLY, 0 MISMATCH, 0 PARSE-FAIL. The 81
decompose exactly into: 24 = the IT two-origin groups (he used origin choice
2; recovered shifts are the tabulated 1/4- and 1/8-shifts), 52 = trigonal/
hexagonal 143-194 in an orthohexagonal C-centered basis (single lattice map
M=[[1/2,0,0],[1/2,-1,0],[0,0,+-1]]), 5 = C-monoclinics 5/8/9/12/15 with
borrowed (assumed) centering. Enantiomorph guard PASS (all 22 chiral-pair
groups matched with proper M - no mirror-type identification). Negative
controls confirm the comparator detects translation corruption, wrong screw,
wrong centering, enantiomorph swap, wrong point group. VERDICT: a fully
independent 2016-era derivation agrees operation-by-operation with the G1
freeze on all 229 comparable groups; zero discrepancies. Main session re-run
required before acceptance.

2026-08-28 (later 10): SCHMITT-OPS CROSS-CHECK ACCEPTED - main-session re-run of
xcheck_schmitt_ops.py: exit 0, EXCEPTIONS none. All 229 comparable groups (2-230)
agree with the frozen G1 spacegroups.json in exact rational arithmetic: 148 EXACT,
81 CONJUGATE-VERIFIED decomposing exactly into 3 documented setting differences
(24 origin-choice-2 groups w/ recovered canonical shifts; 52 trigonal/hexagonal in
his orthohexagonal C-centered basis, one lattice map resolves all w/ enantiomorph
guard PASS; 5 groups w/ centering vectors absent from his code, flagged as capped).
0 MISMATCH / 0 PARSE-FAIL / negative controls prove non-vacuity. The G1 freeze now
carries an INDEPENDENT-LINEAGE HISTORICAL CONFIRMATION: Schmitt's 2016 pre-LLM
derivation (polymake-era C++, used in a 351-CPU-year published survey) vs our 2026
spglib freeze - zero discrepancies in either direction. This is the epistemic-
independence anchor class: different decade, different toolchain, different author.

2026-08-29: *** PHASE-1 CUBIC SWEEP ACCEPTED *** Main-session re-run (exit 0,
215s): all substantive output IDENTICAL to the builder's run (phase1_types.json
byte-identical, 1.4MB; PHASE1_RESULT.md diff = wall-clock decimals only).
THE HAUL: 1,597 orbits across all 36 cubic groups, every orbit through the full
G3 chain (float -> exact -> canon), 0 quarantines, 0 float/exact disagreements.
Store: 102 types = 7 seeded + 95 NOT MATCHED against the catalog snapshot of
2026-08-28 (G5 wording; NO novelty claims - diligence never run on these). Max
stored facets 23 (in Ia-3d #230, which alone carries 9 unmatched types from just
16 orbits). Corridor groups swept completely. NEXT: triage the 95 (facet
outliers, aut-rich ones, corridor natives) -> G4 finalist certificates for
shortlist -> G5 diligence (Schmitt per-group tables at f-vector level + Bernhard
Table 1/Fig 12 + classical lists) -> only then any naming talk. Also queued:
trigonal/hexagonal phase 2.

2026-08-29 (correction, append-only): the "later 8" entry's shorthand "the
SPHENOID free counts (1,4,16,116,903,8551)" is wrong about the values: those
are A385028's counts (bisymmetric hendecahedron, track_b/JIS cell, n=1..6).
The A-numbers in the wrong anchor were the sphenoid's; the values were
A385028's. Caught by the MATH-AI claims audit 2026-08-29. Also: Bernhard's
arXiv PDF (2604.07160, 17pp) is now archived at
references/Bernhard_2026_josehedron_arxiv2604.07160.pdf after a page-by-page
read confirmed the paper nowhere states a space group / IT number / Wyckoff
position (the draft's claim is TRUE at primary-source level).

2026-08-30: TRIAGE OF THE 95 DONE (provisional until the main session re-runs
harness/triage_phase1.py, exit 0; run is deterministic - TRIAGE_RESULT.md
byte-identical across re-runs). Built harness/triage_phase1.py +
harness/TRIAGE_RESULT.md: all 95 unmatched types ranked by explicit weighted
features (facets, aut, corridor/220/230 sightings, site-stabilizer, stratum dim,
sightings, face sizes outside {3,4,6}, Schmitt flag). SANITY ALL PASS: Euler
V-E+F=2 for all 102 stored types; p-vector |p|=F and sum(p)=2E; stab|aut per
sighting; recount 95+7=102 == STATUS; max facets 23, NO kill-criterion hits.
NEW DILIGENCE ASSET: all 36 cubic per-group f-vector tables of Schmitt 2016
Sec. 2.2.5 digitized at f-vector level into triage_phase1.py (881 rows, printed
pp. 119-150 of the archived PDF; 212/213 share one printed table; every row
Euler-checked; per-group max facets agree with his Sec. 2.3 remarks for all 11
groups he comments on; consistent with the banked IT(220) (12,22,12) row).
LIMIT: single-pass transcription, independent re-key queued as a G5 duty.
CROSS-CHECK RESULT: 88/95 types have their f-vector IN his printed table for at
least one sighted group (=> G5 type-level check needed there - f-vector match is
not type match, per the Josehedron/Schmitt-220 precedent); 7/95 are ABSENT from
every sighted group's printed table (stronger candidates, snapshot language
only): 8cf50403cf88c455 (16,25,11) 5^8-faced in 220 I-43d only;
f3d0f39a0b9676b9 (10,17,9) in 214 only; 2de0a21129cabe90 (20,33,15) in 201; and
four 224 Pn-3m types (c4ea3f32fdd6dc51, 9b69eefb8bd8437c, d2d935e5499e6e11,
f98a3ee5675fc121 - his printed 224 table has only 8 f-vectors; our special-
position sweep found 18 types there). TOP-10 G4 SHORTLIST (see TRIAGE_RESULT.md
for why-lines): 1 ceb70631e274e727 212 (37,57,22) aut3; 2 359beee832567a71 230
(40,61,23) aut4 (p-vector 4^20 11^2 20^1 - two 11-gons + a 20-gon); 3
fd96e7fc36481986 199 (36,54,20) aut12; 4 998994bcf8df722b 206 (30,45,17) aut12;
5 8c69db9e84095469 199 (30,45,17) aut12; 6 2001fe7ea92fd0ad 212 (16,30,16)
aut24; 7 afeb1ae44c1a3443 198 (32,48,18) aut6; 8 c314dedd38208a2e 212
(30,46,18) aut2 (7- and 9-gons); 9 aa6b0077c3234d24 214 (30,47,19) aut2; 10
ea1baec328356a32 201 (25,39,16) aut6. All ten have their f-vector in Schmitt's
printed table for a sighted group, so each needs the type-level check (his
representative point through our exact pipeline) before any G4 certificate is
worth cutting. G4 SHOULD CERTIFY FIRST: run schmitt_220_check-style exact type
comparisons at his printed representative points for the top-10 f-vector/group
pairs (cheap, decisive either way), then V0-V3 certificates for the survivors,
starting with #1/#2 (facet-count leaders) and #6 (aut 24, most symmetric).
NO renders, NO novelty language - all wording remains "not matched against
catalog snapshot of 2026-08-28".

2026-08-30 (later): *** PRE-G4 SCHMITT COLLISION SCREEN COMPLETE — 6 OF THE
TOP-10 ARE SCHMITT'S PRINTED CELLS; 4 SURVIVE *** Built
harness/schmitt_collision_check.py (generalizes the schmitt_220_check.py
pattern; results in harness/SCHMITT_COLLISION_RESULTS.md). For all 21
(group, f-vector) pairs where a TOP-10 type is sighted AND Schmitt's printed
per-group table contains its f-vector, his generating grid point was
transcribed from VISUAL reads of the archived PDF (printed pp. 122-150 = PDF
pages 127-155, page cites per row in the results doc; text layer cross-check
agrees verbatim on all 21; NO discrepancies vs the triage digitization),
orbited under the frozen G1 ops, and pushed through float-sweep(W=2) ->
exact-clip (4*rho^2<=D^2 asserted) -> canonical-code, then compared to the
stored type's code. SETTING FIX APPLIED (documented, machine-derived): the 5
pairs in two-origin groups (201/203/224/227/228) convert his origin-choice-2
point to our origin-choice-1 setting via the xcheck-recovered shifts
(x_ours = x_his - v; v: 3/4^3 for 201/224, 7/8^3 for 203/227, (1/8,1/8,5/8)
for 228) — without the shift IT(203) reproduced a wrong f-vector, with it all
five match his printed rows. VERDICTS (exit 0, no timeouts, runtimes 0.1-60s):
COLLISIONS (SAME TYPE — the candidate IS Schmitt's printed cell; reframe per
kill criteria): rank 3 fd96e7fc36481986 (199), rank 4 998994bcf8df722b
(206+220+230), rank 5 8c69db9e84095469 (199+212+214), rank 6 2001fe7ea92fd0ad
(203+210+212+227), rank 7 afeb1ae44c1a3443 (198+212), rank 10
ea1baec328356a32 (201+208+224+228) — 17/21 pairs SAME; for 9 of them his
printed point IS literally one of our stored sighting points (collision
foregone; deterministic recomputation recorded). SURVIVORS (DIFFERENT TYPE at
his printed point, and not equal to ANY of our 102 stored types): rank 1
ceb70631e274e727 212 (37,57,22); rank 2 359beee832567a71 230 (40,61,23);
rank 8 c314dedd38208a2e 212 (30,46,18); rank 9 aa6b0077c3234d24 214
(30,47,19). Each survivor pair is a new micro-fact of the Josehedron/
Schmitt-220 class: that group realizes the shared f-vector by >=2 distinct
combinatorial types (e.g. Schmitt's 212-(37,57,22) cell is 3^9 4^4 6^2 7^2
8^4 13^1 aut 1 vs ours 3^6 4^6 5^6 10^3 12^1 aut 3). STATED ONCE: DIFFERENT
does NOT establish novelty — his table prints one representative point per
f-vector from a grid sampling; survivors remain "not matched against the
catalog snapshot of 2026-08-28". G4 SHOULD NOW CERTIFY ONLY ranks 1, 2, 8, 9
(plus the 7 ABSENT-all types from triage, unaffected by this screen).
Main-session re-run of schmitt_collision_check.py (exit 0) required before
acceptance.

2026-08-30 (later): COLLISION SCREEN ACCEPTED - main-session re-run of
schmitt_collision_check.py: exit 0, all 21 verdicts identical to the agent's
two runs. FINAL: 17 SAME (6 candidate types killed - they ARE Schmitt's
printed cells; 9 foregone since his printed point is a stored sighting) /
4 DIFFERENT survivors to G4: (37,57,22) aut 3 in IT(212), (40,61,23) aut 4 in
IT(230), (30,46,18) aut 2 in IT(212), (30,47,19) aut 2 in IT(214) - both facet
leaders live. Each survivor = a same-f-vector-two-types micro-fact; none of
Schmitt's 4 printed cells at those f-vectors matches any of our 102 stored
types. G4 QUEUE = 4 survivors + the 7 ABSENT-all types (11 candidates).
Setting catch banked: two-origin-group points require origin-choice-2 shifts
(from the accepted ops cross-check) - IT(203) provably wrong without them.

2026-08-30 (later): *** G4 CERTIFICATES CUT FOR 3 PRIORITY CANDIDATES — ALL
V0-V3 PASS *** (provisional until the main session re-runs
harness/g4_certify.py, exit 0 required; run is deterministic — G4_RESULTS.md
identical across re-runs except timing decimals, derived g4_tables_*.json
byte-identical). Built harness/g4_certify.py (parameterized by stored type id;
default = the 3 priority candidates) + harness/G4_RESULTS.md. Ladder per
ANCHORS G4 / HARNESS_DESIGN V0-V3: V0 exact re-derivation from the stored
witness (orbit -> float sweep -> exact clip with 4*rho^2<=D^2 asserted ->
canonical code; code/f/p/aut + all witness metadata match the store); V1
tiling certificate (exact primitive lattice, all T rep cells clipped exactly
w/ identical canon code, volume identity T*vol==detL from geometry, all T*F
facet slots full-facet paired 1:1 reciprocally, translate-completeness +
interior disjointness via exhaustive 2*rho-ball bisector check => tiling by
the measure argument) VERIFIED TWICE — generator + an independent adapted
audit sharing no geometry code with exact_cell/mint_tables (fresh
supporting-plane facet scan, own volumes, pairing claims re-proven); V2
symmetry certification (cell stabilizer over ALL orthogonal maps by
Gram-triple matching, NO signed-perm assumption; Bravais point group of the
ACTUAL lattice via GL3(Z) Gram preservation with a proven coefficient bound —
order 48, embedding = signed perms CHECKED not assumed, for all three); V3
Burnside (tables derived generalizing mint_tables, ops complete over the
Bravais embedding, identity+closure exact, banked export_tables + compiled
enumerate n<=4, banked POLYFORMS_II burnside_generic: |ops|*free(n)==sum
Fix_m(n) ALL PASS n<=4 w/ independent fixed recount). VERDICTS:
(a) ceb70631e274e727 IT(212) f=(37,57,22): site=stab_geo=aut=3, |ops|=24 ALL
PROPER (chiral honeycomb), free n<=4 = 1,5,59,1065, fixed 8,88,1384,25064;
(b) 359beee832567a71 IT(230) f=(40,61,23): site=stab_geo=2 < aut=4
(combinatorial-vs-geometric symmetry GAP, design fingerprint item 4),
|ops|=48 (24 proper), free 1,7,112,2349, fixed 24,276,5096,111732;
(c) 8cf50403cf88c455 IT(220) f=(16,25,11) 5^8-pentagon cell: site=stab_geo=2
< aut=4 (same gap class), |ops|=24 (12 proper), free 1,4,25,209, fixed
12,66,524,4866. All three: free(1)=1 = ops transitive on the T types (the
plesiohedrality quotient check). Kill criteria live, none hit (max F=23).
ONE FIX BANKED: burnside_generic.py requires ops[0]=identity (its Fix_m[0]
cross-check); g4_certify orders ops identity-first (enumerate.cpp itself is
order-indifferent — mint_tables' sorted ops matched banked results).
SNAPSHOT LANGUAGE ONLY: G4 passing does NOT establish novelty — all three
remain "not matched against the catalog snapshot of 2026-08-28"; G5
(novelty diligence) is next and has not run. Remaining G4 queue: 8 of 11
(survivors c314dedd38208a2e 212, aa6b0077c3234d24 214 + the other 6
ABSENT-all triage types), certifiable with the same parameterized script.

2026-08-30 (later): G4 ACCEPTED for the 3 priority candidates - main-session
re-run exit 0, all stages identical. All three pass V0-V3 in exact arithmetic
(~70s total): tiling proven (full-facet 1:1 pairings + T*vol=detL + provable
disjointness balls), symmetry certified over ALL orthogonal maps, Burnside
identity on freshly derived tables n<=4 with the banked enumerator. NOTABLE
STRUCTURE: (37,57,22)/IT212 is a CHIRAL honeycomb (all 24 ops proper);
(40,61,23)/IT230 and (16,25,11)/IT220 are amphichiral-as-maps but only order-2
geometrically (combinatorial-vs-geometric symmetry gap - the design's
"interesting" fingerprint case); all three have free(1)=1 (ops transitive on
types = plesiohedral quotient). G4 pass != novelty. NEXT: G5 duties (re-key of
the 881-row digitization; Bernhard Table1/Fig12 + classical diff; type-closure
question) + the remaining 8-candidate G4 batch via the same script.

2026-08-30 (later): *** G4 BATCH 2 — CERTIFICATES CUT FOR THE REMAINING 8
QUEUE MEMBERS, ALL V0-V3 PASS (11/11 queue now certified, provisional until
the main session re-runs harness/g4_certify.py, exit 0 required) ***
Same ladder, same script, same gates as batch 1. CODE CHANGE (minimal, noted):
g4_certify.py DEFAULT_IDS extended to the full 11-candidate queue as
BATCH1_IDS + BATCH2_IDS, and write_results inserts a "BATCH 2" marker before
the first batch-2 candidate; the results doc is regenerated whole each run
(batch-1 sections unchanged except timing decimals; batch-1 g4_tables_*.json/
.txt byte-identical to the accepted ones), so the acceptance criterion stays a
plain no-args re-run. NO new code paths were needed — all 8 ran through the
unmodified ladder (incl. the first aut=1, site=1, dim-2/3-stratum, and T=48
candidates). Determinism checked here by two full agent runs: exit 0 both, all
11 g4_tables_*.json byte-identical, G4_RESULTS.md identical modulo timings.
BATCH 2 = the 2 collision-screen survivors + the 6 remaining ABSENT-all triage
types. VERDICTS (per-candidate wall 1.4-9.5s, total run 115s):
(1) c314dedd38208a2e IT(212) (30,46,18) aut=2: |ops|=24 ALL PROPER (chiral),
free n<=4 = 1,6,69,1081; (2) aa6b0077c3234d24 IT(214) (30,47,19) aut=2:
|ops|=24 ALL PROPER (chiral), free 1,8,72,1118; (3) f3d0f39a0b9676b9 IT(214)
(10,17,9) aut=2: |ops|=24 ALL PROPER (chiral), free 1,4,16,99;
(4) 2de0a21129cabe90 IT(201) (20,33,15) aut=1 — a fully asymmetric cell
(site=stab_geo=aut=1) whose honeycomb still carries |ops|=24 (12 proper),
free 1,9,85,1099; (5) c4ea3f32fdd6dc51 IT(224) (14,23,11) aut=2: |ops|=48
(24 proper), free 1,6,25,225; (6) 9b69eefb8bd8437c IT(224) (11,18,9) aut=2:
|ops|=48 (24 proper), free 1,5,16,111; (7) d2d935e5499e6e11 IT(224) (6,11,7)
site=stab_geo=2 < aut=4 (combinatorial-vs-geometric GAP class), |ops|=48
(24 proper), free 1,4,10,53; (8) f98a3ee5675fc121 IT(224) (10,15,7)
site=stab_geo=1 < aut=4 (GAP class), T=48, |ops|=48 (24 proper), free
1,7,19,135. All eight: V1 tiling proven twice (generator + independent
adapted audit: full-facet 1:1 pairings, T*vol=detL, disjointness balls),
V2 over ALL orthogonal maps (Bravais group order 48 = signed perms, checked
not assumed, for all), V3 Burnside |ops|*free(n)==sum Fix_m(n) ALL PASS n<=4;
free(1)=1 everywhere (ops transitive on types = plesiohedral quotient). Kill
criteria live, none hit (batch-2 max F=19); no TIMEOUT-DEFERRED stages.
STATED ONCE: G4 pass != novelty — all 11 remain "not matched against the
catalog snapshot of 2026-08-28"; G5 novelty diligence has not run. SCOREBOARD:
11/11 G4-queue candidates certified (3 accepted batch 1 + 8 provisional batch
2). NEXT: main-session re-run for batch-2 acceptance, then G5 duties.

2026-08-30 (later): *** G4 COMPLETE - 11/11 CERTIFIED *** Main-session re-run
of the full queue: exit 0, all stages pass (113s). Batch 2 adds 8: two more
CHIRAL honeycombs (IT212 (30,46,18), IT214 (30,47,19)) + a small chiral
(10,17,9) in IT214; a fully asymmetric cell (site=stab=aut=1) in IT201 tiling
under |ops|=24; four IT(224) types incl. two more symmetry-gap cases
(stab_geo < aut). free(1)=1 across all 11. Every candidate: tiling proven
twice, symmetry over all orthogonal maps, Burnside exact. G4 != novelty; G5
NEXT: (1) independent re-key of the 881-row digitization, (2) Bernhard Table
1 / Fig 12 diff vs the 11, (3) classical-lists diff, (4) type-closure
decision (recompute w/ recovered suite vs author contact - Tyler gate).

2026-08-30 (later): *** G5 DILIGENCE RUN ON THE 11 - REPORT BANKED ***
(G5_DILIGENCE_2026-08-30.md; provisional until the main session re-runs
harness/g5_rekey_check.py, exit 0 required; run is deterministic).
(1) RE-KEY CLEAN: the six hosting-group tables (201, 212/213, 214, 220, 224,
230 = 386 of the 881 rows) independently re-transcribed from VISUAL PDF page
reads into harness/rekey_tables.json WITHOUT consulting triage_phase1.py,
then three-way diffed (visual re-key vs pdftotext text layer vs triage
digitization): 0 discrepancies, all rows f-vector AND frequency identical,
all 11 candidate P/A flags re-verified. Single-pass caveat CLOSED for these
six groups (30 non-hosting tables remain single-pass). (2) BERNHARD DIFF:
all printed cell data extracted (Table 1 + Fig 6 + Fig 12/Sec 7.3); his face
counts {5,8,12,14,17,20} vs candidate facet counts {7,9,11,15,18,19,22,23} -
EMPTY intersection: ALL 11 NO-MATCH; only KP-both and Lidinoid-both print no
counts (UNDECIDABLE-FROM-PAPER, no candidate near them). (3) CLASSICAL DIFF:
no f-vector collision with any classical cell (web-verified: triakis trunc
tetra is (16,30,16) 3^12 6^4 - the tasking's "(16,28,14)?" was wrong; it
equals killed type 2001fe7ea92fd0ad = the diamond cell, consistency bonus;
sphenoid + bisymmetric hendecahedra both (11,20,11) 3^4 4^7 vs our F=11
candidates (16,25,11) 5^8 and (14,23,11) 6^3 - different f AND p).
(4) NEW CROSS-GROUP SCAN: only 8cf50403cf88c455 (16,25,11) is absent from
the ENTIRE printed cubic survey; the other 10 candidate f-vectors appear in
OTHER (non-sighted) groups' tables => ~60 cross-group (group,f-vector)
representative points queued for schmitt_collision_check-style type checks
(cheap, unblocked) before any public wording. Flag outside the 11:
stored non-candidate type ea22673a3a17c26a (8,14,8) 3^4 4^4 matches the
gyrobifastigium at f+p level (type check mandatory if ever advanced).
REMAINING BEFORE PUBLIC WORDING: cross-group queue + type-closure past
printed representatives (recovered-suite recompute vs author contact -
TYLER GATE) + operator decisions (Engel/ILL waiver, naming, deposit
sequencing). NO public claims made; all wording "not matched against the
catalog snapshot of 2026-08-30".

2026-08-30 (later): G5 ROUND 1 ACCEPTED - main-session re-run of
g5_rekey_check.py exit 0. Re-key CLEAN (386 rows, three-way agreement);
Bernhard diff: all 11 NO-MATCH (his printed face counts {5,8,12,14,17,20}
disjoint from candidates); classical diff: all 11 NO-MATCH. TWO SIDE FINDINGS:
(1) killed type 2001fe7ea92fd0ad IS the triakis truncated tetrahedron
(f=(16,30,16) 3^12 6^4, web-verified - the tasking's guessed f-vector was
wrong and the agent verified instead of trusting): the sweep REDISCOVERED the
diamond cell and the collision screen correctly identified it - a free
rediscovery validation of the whole chain; (2) stored non-candidate
ea22673a3a17c26a matches gyrobifastigium at f+p level. NEW WORK QUEUED: the
ABSENT-all flag was sighted-group-scoped; 10 of 11 candidate f-vectors appear
for OTHER groups in the survey (~60 cross-group representative points) ->
cross-group collision batch next. Still before ANY public wording: that batch,
type-closure past printed reps (Tyler gate on author contact), operator
decisions. Snapshot language: 2026-08-30.

2026-09-01: *** CROSS-GROUP BATCH ACCEPTED - G5 COMPUTATIONAL WORK COMPLETE ***
(The #113 agent was killed by a usage limit AFTER its run completed; results
were on disk; main-session re-run: exit 0, byte-identical.) 55/55 cross-group
printed-representative pairs checked (transcriptions verified 4 ways; IT(222)
origin shift newly machine-recovered; per-pair certificates asserted).
VERDICTS: 4 candidates COLLIDED (their types ARE Schmitt printed cells in
other groups: c314dedd@198, f3d0f39a@212, 9b69eefb@208, d2d935e5@204/208/228)
- reframed out per kill criteria. SEVEN FINALISTS survive every printed
representative in the entire cubic survey: #1 (37,57,22) IT212 CHIRAL, #2
(40,61,23) IT230, #3 (16,25,11) IT220 pentagon cell (f-vector absent from the
whole printed survey - vacuous survivor, strongest), #5 (30,47,19) IT214
CHIRAL, #7 (20,33,15) IT201 asymmetric, #8 (14,23,11) IT224, #11 (10,15,7)
IT224. Standing caveat: printed tables are one representative per (group,f)
from a sampling; survival != novelty; snapshot 2026-09-01. THE FUNNEL:
1,597 orbits -> 95 unmatched -> 11 G4-certified -> 7 through all printed-rep
screening. REMAINING BEFORE ANY PUBLIC WORDING (all non-computational /
operator): type-closure decision (recovered-suite recompute vs author
contact), Engel ILL (optional), naming, deposit sequencing.

2026-09-01 (later): *** PUBLICATION PACKAGES BUILT FOR ALL SEVEN FINALISTS ***
(publication/ tree; builder publication/build_packages.py ran exit 0; every
derived number asserted at build time against phase1_types.json, the banked
g4_tables_*.json, and the accepted G4 n<=4 counts; provisional until the main
session re-runs build_packages.py, exit 0 — deterministic except wall-clock
notes). NAMES EXECUTED per Tyler's greenlit two-track decision: IT(220)
(16,25,11) pentagon flagship = SATCHELHEDRON; IT(201) (20,33,15) fully
asymmetric cell = ORDENHEDRON (for Tyler Satchel Orden, Bernhard personal-name
precedent); the two IT(224) cells stay descriptive pending Tyler; the three
mined-group cells (212/214/230) are HELD for the Engel/Koch ILL check —
packaged, marked, NOT named, no OEIS drafts. PER SHAPE: COORDS.md (exact
Fraction vertices + facet cycles + neighbor sites + generating data),
render.png (p-vector asserted pre-render), banked tables byte-copied +
proper_ops export, counts.md with fixed/free/one-sided EXTENDED TO n<=6 for
ALL SEVEN (banked A398957 enumerator; n<=4 prefixes == accepted G4; fixed
columns identical across full/proper runs; fixed>=one-sided>=free and
one-sided<=2*free everywhere; free==one-sided for the two chiral honeycombs
as required). Burnside |G|*free(n)==sum Fix n<=6 EXTENDED and ALL PASS for
Satchelhedron + both 224 cells (banked burnside_generic); Ordenhedron + held
three remain Burnside-verified at n<=4 (growth check exceeded the cap —
recorded in each counts.md). ROUNDNESS (Bernhard's metric, V(cell)/V(outer
circumsphere)): Josehedron CONTROL through our exact pipeline = 47.9833% vs
his printed ~47.98% — MATCH, convention confirmed; finalists: Satchelhedron
37.7554%, ceb70631/212 28.9090%, 359beee8/230 23.5573%, aa6b0077/214
11.1503%, 224-11facet 10.7278%, Ordenhedron 9.8394%, 224-7facet 4.9197% —
NO finalist beats 47.98%; his record stands on the snapshot record. OEIS: 12
drafts staged (4 shapes x fixed/one-sided/free) in house format with snapshot
+ AI-disclosure sentences and a-files; DRAFTS ONLY — slots are 5-concurrent,
wave-gamma staged, TYLER SEQUENCES (publication/OEIS_DRAFTS_NOTE.md). Top
level: PUBLICATION_STATUS.md, ILL_REQUEST_STAGED.md (exact Eng81a/Eng81b/
Koc72(+Koc73 fallback) citations transcribed from the archived Schmitt
bibliography; ready-to-send), ZENODO_MANIFEST.md (SWHIDs referenced not
re-deposited; wall check: no sensitive content), PAPER_OUTLINE.md ("Certified
space-filling polyhedra from a gated agentic search", 10 sections + section->
banked-doc source map), ROUNDNESS.md, build_summary.json. REMAINING (operator):
send ILL; name-or-keep the 224 pair; sequence OEIS; optional independent
n=5..6 verification for the shapes past the Burnside cap before submitting;
Zenodo deposit; Tyler's prose rewrite; main-session re-run for acceptance.

2026-09-01 (later): PUBLICATION KIT ACCEPTED - main-session re-run of
publication/build_packages.py exit 0 (deterministic, all build-time
assertions against banked data passed). Satchelhedron + Ordenhedron named and
fully packaged; 224 pair packaged awaiting names; mined-three packaged HELD;
12 OEIS drafts; ILL staged; Zenodo manifest; paper outline. Roundness control
MATCHED Bernhard (47.9833% vs printed 47.98%); no finalist beats his record
(best: Satchelhedron 37.76%). Honest gaps per-shape in counts.md (Ordenhedron
Burnside n<=4 cap; dual-implementation bar open for n=5..6 on some shapes).

2026-09-03: DUAL-IMPLEMENTATION BAR MET for the four publishable-now cells
(independent-verifier task). New publication/verify_counts_independent.py
(pure-stdlib Python, fresh code: translation-canonical FIXED growth, then
orbit-representative quotient by ops / proper_ops for free / one-sided, with
the Burnside identity asserted at every n for both groups; shares no code
with the banked export_tables.py + enumerate binary, harness/mint_tables.py,
or the Josehedron reference_enum.py). CONTROL: Josehedron banked record
reproduced EXACTLY (18/18 cells, n<=6, 6.8 s) before any new shape was run.
RESULT: Satchelhedron, Ordenhedron, Pn-3m 11-facet, Pn-3m 7-facet ALL MATCH
the banked counts.md values at every n<=6 (72/72 cells fixed/one-sided/free;
Burnside ok; all table sanity checks incl. op-automorphism ok). Wall: 9.3 s /
85.5 s / 31.3 s / 10.6 s. Ordenhedron's open n=5..6 Burnside gap is closed by
this run. Report: publication/INDEPENDENT_COUNTS_2026-09-03.md (per-shape
banked-vs-independent tables, hashes, exact re-run commands); raw logs+JSON in
publication/independent_runs/. counts.md files NOT edited (their honest-gap
sentences now superseded by the report; update them at acceptance). HELD
cells not run (out of scope). Awaiting main-session re-run for acceptance.

2026-09-03: *** SHAPES PAPER DRAFTED - paper/draft.tex (13 pp, tectonic, compiles
clean) *** "Seven certified space-filling polyhedra in the cubic space groups,
including the Satchelhedron and the Ordenhedron" (arXiv-style, math.MG primary /
math.CO secondary, author Tyler Satchel Orden, ORCID on the title page). Sections:
intro (Josehedron precedent + the catalog problem) · setting/notation · the
pipeline in one page (G1 freeze + 229/229 Schmitt-ops confirmation, exact
confirmation, G0/G2, cites the MATH-AI methods paper as "in submission") · sweep
and funnel (1,597 -> 102 -> 95 -> 11 -> 7; 76 printed points; diamond-cell
rediscovery box) · the seven cells (master table, V0-V3 ladder, certificate-data
table, one subsection per cell incl. the three HELD cells unnamed; two figures
from publication/*/render.png) · polyform counts n<=6 with Burnside status stated
per cell (n<=6 for Satchelhedron + both 224 cells; n<=4 for Ordenhedron + held
three; dual-implementation bar unmet at n=5,6) · diligence and limits (classical,
Bernhard, Schmitt 881-row digitization + 386-row re-key + 76 exact recomputations
with the origin-2 shifts; print-only Engel/Koch unchecked -> hold) · five same-f-
vector-distinct-type micro-facts · roundness (control 47.9833%; no finalist beats
47.98%) · data availability ([ZENODO-DOI], [A-NUMBERS] placeholders, SWHIDs) ·
AI-disclosure paragraph (house standard; operator-error catch sentence) ·
Appendix A exact coordinates for all seven. NUMBER DISCIPLINE: master table,
counts table and the coordinate appendix are GENERATED by paper/make_tables.py
from publication/*/COORDS.md, build_summary.json and paper/wyckoff_check.txt
(new: paper/wyckoff_check.py ran spglib 2.7.0 on the seven orbits - group
numbers agree with every package; Wyckoff letters 220:24d(2..), 201:24h(1),
224:24k(..m), 224:48l(1), 212:8c(.3.), 230:48g(..2), 214:24f(2..)); every
hand-typed number is mapped to its source file in paper/TRACE.md. Snapshot
wording throughout ("not matched against the records checked as of
2026-09-01"); "new to science" appears nowhere; no em-dashes. NOT DONE / TYLER:
this is staging text - the house rule (Tyler rewrites all prose from memory
before submission) is written into the draft as a bracketed disclosure sentence
that must be made true; the two 224 cells still carry descriptive names; the
ILL return decides the held three; DOI/A-numbers to be substituted; Bernhard's
ref 12 gives Engel II as pp. 259-276 vs the ILL doc's 259-275 (draft follows
the ILL doc; resolve on the physical copy).

2026-09-03 (later): INDEPENDENT COUNTS ACCEPTED into the record. The 2026-09-03
dual-implementation result (verify_counts_independent.py, 72/72 + 18/18 control)
is folded into publication/build_summary.json by the new deterministic
publication/apply_independent_counts.py (asserts every term of the four
publishable cells against independent_runs/*.json before rewriting the status
string; exit 0). The earlier "dual-implementation bar unmet at n=5,6" wording
for Satchelhedron / Ordenhedron / both Pn-3m cells is superseded; held cells
unchanged (Burnside n<=4, single enumerator at n=5,6).

2026-09-03 (later): *** ROUND 1 ON THE SHAPES PAPER: COMPUTATIONS + draft_v2 ***
Inputs: paper/REVIEW_COLD_2026-09-03.md, paper/CLAIMS_AUDIT_2026-09-03.md.
COMPUTATIONS banked in harness/round1_computations/ (run_all.sh -> RESULTS.md;
c1-c5 scripts, exact, deterministic; awaiting main-session re-run):
 C1 open/wall in the Wyckoff stratum (+-1/96, +-1/48 along every tangent
    direction, refined to 1/1536 where needed): S = WALL on the 24d line
    (x,0,1/4) at x=0, neighbours (22,35,15) 3^4 5^10 8^1 (x<0; stored
    0ee26ed4, sighted at x=1/3) and (22,35,15) 3^6 4^1 6^8 (0<x<1/12; not
    stored, no grid point of ours in that interval either); (22,35,15) IS
    printed in Schmitt's IT(220) table. O, P11, P7, H212, H230 OPEN. H214 OPEN
    but on a short interval (survives +-1/192, fails +1/96). Reviewer's
    numbers reproduced exactly.
 C2 full isometry group of each solid, centre-free (distance-preserving map
    automorphisms): Isom = site for all seven (2,1,2,1,3,2,2), every isometry
    fixes the site => G is the full symmetry group of every honeycomb (closes
    reviewer Q6). P11 achiral solid (site mirror); the other six chiral
    solids; hands from the g4 tables: S 6+6, O 12+12, P7 24+24, H230 12+12;
    H212/H214 all one hand.
 C3 IT(214) 8a (1/8,1/8,1/8): f=(30,45,17), p=4^6 5^6 6^2 8^3, aut 12, site
    6, T=4, simple; canonical code == stored 8c69db9e84095469 (triage rank 5,
    killed by the collision screen as Schmitt's printed 199/212/214 cell):
    the sweep REDISCOVERED the Laves-graph plesiohedron; it has six pentagons.
    The v1 pentagon sentence was false and is gone.
 C4 roundness both conventions (exact smallest enclosing sphere): coincide
    for Josehedron (by -4 symmetry; the control cannot discriminate) and
    Satchelhedron; differ for the other six (MES ratio larger: O 13.80, P11
    13.96, P7 6.90, H212 29.17, H230 27.50, H214 13.99 %); none reaches 47.98
    under either.
 C5 Bernhard's 12 points: spglib IT(220) 12a (-4..); frozen orbit of
    (0,1/4,3/8) equals his point set and reproduces the seed code.
PAPER: paper/draft_v2.tex (v1 untouched; 16 pp, tectonic, 1 negligible
0.96pt overfull in the appendix). P1 open/wall column in Table 1 +
Satchelhedron reframed as the transition cell (absence = one point of a line);
P2 catalog exposure per cell (new Table 4): Engel II = symmorphic groups only
(Crossref title) => covers none of the six groups; Koch = <3 dof => covers the
five special-position cells, S most exposed (wall of a line); ILL pending
because print-only/paywalled; P3 Laves paragraph in Sec 4 + Sec 5.2; P4 Sec 2
Prop (T*site=|ops|, proof) + Lemma (hands, proof) + V2 rewritten from C2, P4_132
/ self-enantiomorphic I4_132 reasoning; P5 Lemma (cutoff) with proof in Sec 3,
V1 as a real sketch (disjointness ball + volume => tiling); P6 counts table v2
(two enumerators n<=6 for the four; daggers on held n=5,6); P7 roundness
section rewritten, both-convention table; P8 bracketed note removed,
placeholders kept; P9 "pending the author's choice" removed, warm Bernhard
sentence in the acknowledgements, names not in the abstract's first sentence
(title unchanged; bracketed NOTE TO OPERATOR as a LaTeX comment only); P10
semicolons 3/170 sentences, "exact" 1, 0 em-dashes, The-openers 19%, epigrams
gone; P11 DOIs added, Engel II subtitle + 259-275, ROUNDNESS.md p.8 -> p.6 and
convention-inference corrected (build_packages.py text too), ILL doc updated,
COORDS.md update lines for all seven (C1/C2 facts; 359beee8 reversing count
per audit 4c), G5 doc pentagon correction. Also fixed: "four groups" -> five,
full weight list, integer-or-half-integer, dangling "whose", "Both are
Schmitt's cells", 76 entries / 39 for the finalists, 78 unpursued, 16^3,
control triples, 18 f-vectors vs 8 rows, kill-criterion explanation, spglib
circularity note, "orbit doubles" rephrased, held-cell OEIS reason.
NOT DONE (deliberate): figures (reviewer W10) untouched; no renaming; Tyler's
prose rewrite still required; Zenodo/OEIS placeholders remain.

2026-09-03 (Fable 5.1 subagent): *** TRACK-4 QUICK WINS RUN - LAVES-17 + ENGEL-38
POLYFORM SEQUENCES STAGED (track4/) *** Both are KNOWN cells (no novelty claimed
anywhere; only the sequences are new). (A) LAVES GRAPH PLESIOHEDRON: literature
web-verified (Wikipedia Laves graph: symmetry I4_132, Voronoi cells 17-faced per
Schoen 2008; Coxeter 1955 CJM 7:18-23); spglib 2.7.0 on the frozen-IT(214) orbit
of (1/8,1/8,1/8) = Wyckoff 8a, site .32; Wikipedia's integer vertex set is the
MIRROR of our 8a orbit (exact set check; canon_code is mirror-invariant). Chain:
17 facets, f=(30,45,17), p=4^6 5^6 6^2 8^3, aut 12, T=4 - canonical code ==
Phase-1 store type 8c69db9e84095469 (the type the collision screen killed as
Schmitt's printed cell: it IS the Laves cell). G4 ladder V0-V3 ALL PASS (chiral
honeycomb, |ops|=24 all proper). Counts n<=6: fixed 4,34,416,6000,94740,1582610;
free = one-sided 1,4,22,278,4005,66346; DUAL-IMPLEMENTATION BAR MET n<=6
(verify_counts_independent.py 18/18 MATCH, Burnside every n, 48 s). (B) ENGEL'S
38-FACET STEREOHEDRON: Schmitt's printed IT(214) representative for (70,106,38),
(427/6984, 761/6984, 1421/6984) freq 153, printed p.138 = PDF p.143, VISUAL READ
+ text layer agree; IT(214) single-origin. Chain: 38 facets, f=(70,106,38),
p=3^12 4^11 5^6 6^5 8 16 20 28, aut 1, T=24 (= Engel's 24 aspects), spglib
general position 48i; 2 non-simple vertices (float degenerate-flagged, exact
decides). G4 ladder ALL PASS (V1 audit 521 s). Counts n<=6 (each run ~170 s,
under the 20-min cap): fixed 24,456,13384,477102,18876408,796541508; free =
one-sided 1,25,559,20051,786517,33195798; independent verifier MATCH n<=5
(15/15, 366 s); n=6 INFEASIBLE for the Python verifier (8e8 forms) -> that term
rests on the banked enumerator alone (flagged in the draft; Tyler decides n<=5
vs n<=6). Which of Engel's four 38-facet types this is: NOT identified (Engel
1981 not in hand). HARNESS FINDING: mint_tables.derive_lattice scans
range(-P,P+1)^3 - infeasible at PERIOD 6984 (two runs killed in that loop);
track4_certify.py substitutes a coset-complete derive_lattice_cosets (self-checked
== grid version on Laves P=24 and Josehedron P=8); harness g4_certify.py itself
untouched. STAGED: track4/laves17_LavesGraphPlesiohedron/ and
track4/engel38_EngelStereohedron/ (COORDS.md, counts.md, render.png, tables,
oeis_afile.txt, oeis_draft_{fixed,onesided,free}.txt in house format with
literature names + citations + attribution sentence + disclosure + ~~~~; since
one-sided == free for both chiral honeycombs the NOTE recommends ONE entry per
cell for that pair -> 2 distinct sequences per cell). TRACK4_RESULTS.md has the
full record + exact re-run commands. DRAFTS ONLY - Tyler sequences submissions.
AWAITING main-session re-run (track4_certify.py, ~20 min; build_track4_packages.py;
the two verify_counts_independent.py commands) before acceptance.

2026-09-03 (later): TRACK 4 ACCEPTED - main-session battery: track4_certify.py
ALL LADDERS PASS (911 s), build_track4_packages.py exit 0, independent counts
Laves n<=6 18/18 and Engel n<=5 15/15 all MATCH with Burnside at every n.
Laves-graph plesiohedron (IT214 8a, f=(30,45,17), 4^6 5^6 6^2 8^3, aut 12;
== phase-1 type 8c69db9e) and Engel's 38-facet stereohedron (Schmitt's printed
IT214 point, f=(70,106,38), T=24) certified; 4 distinct authored OEIS drafts
staged in track4/ (one-sided = free for both chiral honeycombs). Harness
finding banked: derive_lattice grid scan infeasible at large P; coset-complete
version used in track4_certify (reasoning accepted; two controls).

2026-09-03 (later): *** ROUND 2 ON THE SHAPES PAPER: COMPUTATIONS + draft_v3 ***
Input: paper/REVIEW_COLD_R2_2026-09-03.md (major revision: W1 naming rule,
W2 false roundness sentence, W3 open/wall definition). COMPUTATIONS banked in
harness/round2_computations/ (run_all.sh -> RESULTS.md, exit 0; r1-r8 exact,
deterministic; awaiting main-session re-run):
 R1 roundness of classical cells, both conventions (coincide for all): cube
    36.7553, rhombic dodecahedron 47.7465, TRUNCATED OCTAHEDRON 68.3292
    (= 24/(5 sqrt5 pi)), elongated dodecahedron 28.2942 (family max at e=0),
    maximal hexagonal prism 47.7465 (Bernhard's), equilateral prism 44.3811,
    Josehedron 47.9833, Laves cell 29.1675. Bernhard's p. 6 sentence quoted
    verbatim; his cube/RD/prism figures reproduced => his convention fixed =>
    his "roundest SFPH known to date" fails under its own definition.
 R2 Schmitt's grid reconstructed from printed data: barycentric grid of
    denominator D over a triangulation of the reduced domain, boundary incl.;
    count identity solved exactly for R220 (D=873, (9,24,25,9)), R201
    (D=1816, one tetrahedron, C(1819,3)), R212 (D=1062, (7,16,15,5)). All 62
    printed IT(220) points in R220 with denominators | 8D. (0,0,1/4) = centre
    of the top face, weight 1/2 on the diagonal, D odd => NOT a grid point;
    the 24d line's only normalizer image in R220 is that face's y=0 segment,
    every point of which has weight 1/2 => NO point of the 24d line is in his
    IT(220) grid.
 R3 Schmitt's printed IT(220) (22,35,15) rep (-1/8,55/2328,437/3492): p =
    3^4 4^6 6^2 7^2 8^1, aut 1, general position: NEITHER wall neighbour (a
    third (22,35,15) type in IT(220); sixth same-f-vector item).
 R4 Ordenhedron non-simple vertices: site symmetries 3, 23, -3, -3, 3; free
    action => 6, 12, 6, 6, 6 equidistant sites, so >4 cells meeting there is
    forced by the group; facets at v (4,5,4,4,4) read from the cell (degree in
    the Delaunay polytope; not forced by H).
 R5 Ordenhedron region box scan: 389/729 points of the side-1/12 cube are the
    type; first axial change at 1/24 both ways on all axes.
 R6 Laves sightings: 199 8a, 212 8c (1/8,3/8,5/8), 213 8c (1/8,1/8,1/8), 214
    8a + 8b; all eight-point orbits; spglib gives I4_132 for every point set.
 R7 Schmitt's printed frequencies vs printed grid counts: exact in 8 of 35
    cubic tables; short in 27 (1 point .. 61.4% for IT(230)); hosts 201 1.92%,
    212 0, 214 0.07%, 220 0.14%, 224 0, 230 61.4%. Rows == 881 digitization.
 R8 *** IT(201)/IT(224): Schmitt's printed reduced domain (the Im-3m standard
    asymmetric unit) is NOT a fundamental domain of the normalizer in his
    origin-choice-2 coordinates (normalizer origin is the 23 point (1/4)^3,
    verified by conjugation on the frozen tables); its normalizer images
    cover ~24% of the parameter space (4-fold there); the generating points of
    O, P7, P11 have NO image in the domain => his IT(201)/IT(224) grids could
    not produce cells congruent to any of the three. IT(220)/Ia-3d control
    passes. Stated in the paper as a fact about the printed domain and
    coordinates, with the caveat that the computation's actual domain cannot
    be read from the dissertation. ***
PAPER: paper/draft_v3.tex (v2 untouched; 18 pp, tectonic, 0 warnings, 0 ??).
F1 one criterion: "f-vector absent from Schmitt's printed table for the cell's
own group" (verified: separates {S,O,P11,P7} from {H212,H230,H214}); stated
in Sec 1 with the sentence that it is about Schmitt's tables only, that each
named cell's absence has a mechanical explanation (R2/R8), and that it is
independent of Koch/Engel exposure; Sec 5.5 and Sec 7 reworded to be naming-
neutral; operator comment removed. F2 Sec 9 rewritten as a measurement-framed
correction with the verbatim quote + Table 5 v3 (classical + Laves +
Josehedron above the rule). F3 open/wall defined locally as a property of
(type, point); axial-probe test stated with its limits; dim-0 n/a; "this is
the explanation" -> "consistent with"; H214 interval bounds [1/64, 5/192] in
text and Table 4; R2/R3 folded into Sec 5.2. F4 Lemma 1 clauses added
(G+C = same-hand cells; site ops are isometries of C); chirality defined
relative to the full symmetry group (= G by Sec 5.1); isom = site flagged as
a result. F5 Koch's unit = lattice complex; Engel I/II scope from Schmitt's
Sec 2.1/2.3 (Eng81b cited only for symmorphic groups; Eng81a = IT(214) record
+ slice diagram); Koch's per-group facet counts (212: 22, 220: 17, 224: 16,
230: 23; note H212 = 22, H230 = 23 facets); Engel 1986 and Sabariego-Santos
III added with Crossref/arXiv-verified data; Laves orbit letters per group.
F6 tells cut (It never triggered / They are this paper / not a proof of
anything / anecdote / acknowledgement closer); 15 semicolons in prose, 0 em-
dashes, The-openers 21%. Also: W7 rediscovery paragraph headed; W8(a) weight
explanation (absent types ranked 26-88); W8(b) IT(224) 18-vs-8 pursued (all
10 absent f-vectors at special positions; 2 finalists, 2 = his cells
elsewhere, 6 unpursued); W9 Ordenhedron region estimated; W11 Koch DOI,
Sec 8 item 4 duplicate cut, Sec 8 item 6 added. NOT DONE (deliberate): no
renaming (title unchanged); Zenodo/OEIS placeholders; Tyler's prose rewrite;
the other two-origin groups (203, 222, 227, 228) not checked for the R8
domain issue. TRACE.md v3 block appended.

2026-09-03 (later 2): PHASE-2 GROUNDWORK + GATE G2b BUILT AND PASSED 21/21
(provisional until the main session re-runs harness/phase2/g2b_controls.py,
exit 0 required; wall 1.5 s). Pre-registered FIRST as an appended ANCHORS.md
block "G2b - METRIC CONTROLS" (existing text untouched). New sibling modules in
harness/phase2/ (accepted modules unmodified): metric.py (integer Gram
matrices from rational c/a per crystal family; exact bisectors/G-norm; exact
coordinate bound |x_i| <= D*sqrt((G^-1)_ii) for candidate completeness;
R^T G R = G compatibility check), sweep_voronoi_gram.py (exact PD +
compatibility validation, well-conditioned proposal embedding, delegates to
the accepted sweep() Gram hook), exact_cell_gram.py (exact clipper with the
metric-correct 4*rho^2 <= D^2 certificate in the G-norm; identity metric ==
exact_cell.clip_cell byte-for-byte on SC/FCC/BCC). BASIS DECISION: hexagonal
family in the ITA hexagonal basis with rational Gram (Schmitt's orthohexagonal
C-centered basis is unnecessary under the Gram form and would need
half-integer R). G2b results: (a) hexagonal prism from P6/mmm 1a at c/a
1/2,1,2 - code match, aut 24; (b) elongated dodecahedron from the BCT lattice
(I4/mmm 2a AND I4 2a) at c/a 7/2, 2, 3/2 - code match, aut 16, 2 non-simple
apex vertices; truncated octahedron at 1/2, 1, 7/5 (sqrt2 threshold
bracketed; SOURCE: Schmitt 2016 printed p.29 = PDF p.34 IT(79) rows
(18,28,12)@7/2 and (24,36,14)@1/2 at (0,0,0), visual + text layer agree;
Wikipedia "Elongated dodecahedron" BCT c/a > sqrt2; analytic derivation of
the threshold); (c) cubic Gram path with G=I identical to the non-Gram path
on #221/#225/#229 and catalog-matching; (d) THREE Schmitt tetragonal rows
reproduce his printed f-vectors exactly: IT(75) (10,15,7)@1/2 [pentagonal
prism, aut 20], IT(76) (44,66,24)@797/1000 [aut 1, PERIOD 3996], IT(77)
(28,42,16)@1/2 [aut 2] - his tetragonal point/b-ratio conventions confirmed
(points in space-group coordinates, b-ratio = c/a). G2 DEFERRALS CLOSED: hex
prism and elongated dodecahedron are now pipeline-produced, not catalog-only.
PHASE2_PLAN.md written: tetragonal first, 5,825 metric-independent orbits over
68 groups (5,689 special on the {1,2,3,4,6,8,12} grid + 136 general controls,
exact count 57.6 s) x 13 coarse b-ratios (1/2..7/2 step 1/4) = 75,725
candidates (~104,850 with Schmitt's printed b-ratios); measured 0.08-0.9 s per
cell => ~32-45 min on 12 workers, <= 1.5 h with bisection. Kill criteria
carried over. NO HUNT SWEEP RUN. Files: harness/phase2/{metric.py,
sweep_voronoi_gram.py, exact_cell_gram.py, g2b_controls.py, plan_counts.py,
G2B_RESULT.md}, PHASE2_PLAN.md, ANCHORS.md (appended block).

2026-09-04 (early): PHASE 2 BATCH 1 — TETRAGONAL HUNT SWEEP RUN (first
non-cubic hunt; IT 75-142, 68 groups). harness/sweep_phase2_tetragonal.py
built on the accepted Gram modules (phase2/metric.py, sweep_voronoi_gram.py,
exact_cell_gram.py; G2b 21/21, main-session accepted) with sweep_phase1.py as
the structural model (its helpers imported, not re-typed). Chain per
(group, orbit, b-ratio): exact orbit -> Gram diag(q^2,q^2,p^2) with R^T G R = G
asserted -> float proposal (W=2..4) -> exact clip of TWO orbit cells (pts[0]
and pts[n//2]) with the G-norm certificate, cutoff warm-started from a
float-neighbor pre-clip (certificate decides; cost per exact cell 0.01-0.02 s)
-> canonical code; orbit-congruence check (F, p-vector, code equal across the
two exact cells; float (F,p) uniform over all cells) with (group, b) quarantine
+ purge on violation; G3 invariant enforced; kill criteria live (>38 = never a
type). Store seeded with all 102 phase-1 cubic types (first_sighting_system
"cubic (phase 1 store)"). Passes: P1 5,825 orbits (5,689 special on the
{1,2,3,4,6,8,12} grid + 136 general; count matches PHASE2_PLAN exactly) x 13
coarse b-ratios = 75,725; P2 Schmitt's 1,476 printed tetragonal rows harvested
at run time from the pdftotext layer (PDF pp. 32-86; G2b rows asserted
present) = 1,641 evaluations (pairs run in both groups); P3 the 5 most
frequent printed non-grid b-ratios (3497/1000, 4/5, 797/1000, 38/25, 7/5) x
5,825 = 29,125; P4 1,014 new line/fixed orbits of the 1/24 grid x 13 = 13,182
(4,992 plane orbits at 1/24 skipped by design); P5 1-D transition bisection
(depth <= 4, cap 26/orbit; 22 cap hits) on 4,086 orbits. RESULT: 148,816
candidates, 294,772 exact cells, wall 965 s on 12 workers (nice 10; FQ1 solver
untouched), budget NOT hit, nothing cut. Store 891 types = 102 cubic + 789
tetragonal ("not matched against catalog snapshot of 2026-09-03"; NO novelty
claim): 404 sighted by OUR menu (F 6..26; the 26-facet cell is IT(98) I4_122
line orbit (1/12,1/4,1/8) at b=5/4, aut 2, 102 sightings), 385 seen ONLY at
Schmitt's printed points (his cells reproduced; max F 35 = his IT(98) runner-
up). 19 cubic-store types re-sighted in tetragonal groups (the 5 parallelohedra
+ 14 others). b-ratio dependence (menu-sighted types): 60 of 404 seen at
exactly one b value; 85 seen only at bisection midpoints; 1 only at a Schmitt
b-ratio. Groups by tetragonal-menu type count: 98 (60), 141 (59), 122 (57),
92 (43), 96 (38), 91 (34), 88 (33), 118 (32), 94 (31), 80 (30); 24 groups
(mostly the 4mm / 4/mmm families with plane strata, plus second
enantiomorphs) minted no new type from the menu; only 99 and 123 sighted no
tetragonal type at all.
QUARANTINES 426, all in P2, all classified post-run
(harness/phase2_schmitt_origin_check.py, PHASE2_SCHMITT_ORIGIN_CHECK.md):
424 f-vector mismatches = coordinate conventions, 0 residual — 348 rows in the
13 ITA two-origin groups (frozen setting = origin choice 1, Schmitt = choice 2;
one origin shift per group reproduces ALL its rows, e.g. P4/n (1/4,3/4,0),
I4_1/a (0,1/4,1/8)) and 107 rows in 95/96 (second enantiomorph; z -> -z
reproduces all rows); 2 crashes = exact_cell.order_cycle's float-proposed
cycle order failing its exact convexity check on two b=3497/1000 rows with
PERIOD 5652 (IT(80), IT(110)) — open item (exact fallback ordering), those two
printed rows are not reproduced. Schmitt screen: 1,474 of 1,476 printed rows
reproduce at f-vector level. LIMITS: the 348 shifted re-runs were not added to
the store (check script is read-only), so "Schmitt-only" 385 under-counts his
types; type-level diligence vs his tetragonal data NOT done (digitization is
cubic-only); plane strata only at the coarse grid; 51 of 56 printed b-ratios
not swept; irrational transitions bracketed only; phase2_types.json is 86 MB.
Files: harness/{sweep_phase2_tetragonal.py, phase2_types.json,
PHASE2_RESULT.md (+ addendum), schmitt_tetragonal_rows_harvested.json,
phase2_run.log, phase2_schmitt_origin_check.py, PHASE2_SCHMITT_ORIGIN_CHECK.md,
phase2_schmitt_origin_check.json, phase2_origin_check_run.log}.

2026-09-04 (later): ORDER_CYCLE FIX — the two PHASE-2 crash quarantines
resolved (provisional until the main session re-runs the battery).
harness/ORDER_CYCLE_FIX_2026-09-04.md. CAUSE: exact_cell.order_cycle's float
atan2 proposal uses the in-plane frame (u, w = n x u); on the two b=3497/1000
PERIOD-5652 rows the Gram bisector normals have entries ~4e6 vs ~3.5e10, so
|w|/|u| ~ 1e10, the projected y's reach 1e12-1e14 against x ~ 1, every float
angle collapses to +-pi/2 and the exact verifier (correctly) refused the
order. The facets themselves are fine convex polygons (exact order passes,
zero collinear triples). FIX (exact_cell.py only, +50/-5 lines; the Gram
sibling imports order_cycle and inherits it): sibling helper
order_cycle_exact = rational 2-D projections (x, y) = ((p-c).u, (p-c).w)
around the exact centroid, comparator half-plane then sign of the 2-D cross
product, no floats; engaged ONLY when the float order fails the unchanged
strict convexity check, and its result must pass the SAME assertion. Float
order that passes is returned unchanged => byte-identical outputs on every
previously accepted input. NON-REGRESSION: g0_regression, g2_controls,
mint_tables, g4_certify (all 11), schmitt_220_check, schmitt_collision_check
(21 pairs), phase2/g2b_controls all exit 0; G0/G2/MINT_TABLES/SCHMITT_220
results and all g4_tables_*.txt + mint_tables_*.txt byte-identical to HEAD;
G4_RESULTS.md, SCHMITT_COLLISION_RESULTS.md, G2B_RESULT.md identical after
masking timing tokens (restored to HEAD afterwards). Both selftests PASS;
order_cycle_exact == float order up to rotation on all 78 selftest facets.
THE TWO ROWS (harness/repro_crash.py, exit 0; crashed before): IT(80) I4_1
(353/1413, 235/942, 0) -> exact f=(32,48,18) = printed, p 3^4 4^6 5^2 6^1
8^2 9^2 10^1, aut 1; IT(110) I4_1cd (1/4, 1411/5652, 0) -> exact
f=(24,36,14) = printed, p 4^4 5^4 6^6, aut 4; certificate 4rho^2 <= D^2 and
orbit congruence held on both; fallback fired on 2 facets per row. Schmitt
f-vector screen now 1,476/1,476 printed tetragonal rows (1,215 + 348 + 107
+ 2). NOT DONE: phase2_types.json / PHASE2_RESULT.md not rewritten (record
stands; the two rows stay listed as crash quarantines there, resolved by the
note); the two cells not added to the store; main-session battery re-run.

2026-09-04 (later): SCHMITT TETRAGONAL TABLES DIGITIZED (type-level diligence on
the phase-2 tetragonal cells is now possible). Sec. 2.2.2 (printed pp. 27-81 =
PDF 32-86), IT(75)-IT(142): every printed per-group table transcribed by a
SINGLE-PASS VISUAL read of the rendered pages (Fable 5.1), typed before the text
layer was consulted, then diffed row-for-row against a fresh pdftotext parse AND
harness/schmitt_tetragonal_rows_harvested.json. RESULT: 65 printed blocks (68
groups; 76/78, 91/95, 92/96 share one table each), 1,476 rows (f-vector,
b-ratio, generating point; NO frequency column is printed in any tetragonal
table), header facts per block (normalizer+basis, reduced-domain vertices,
upper bound with citation, lower-bound remark if printed, b-range/steps, grid
size), PDF+printed page per block and per row. CHECKS: Euler V-E+F=2 all 1,476
rows; 0 content discrepancies visual vs text layer (one page-list artifact for
142 only); G2b rows IT(75)(10,15,7)@1/2, IT(76)(44,66,24)@797/1000,
IT(77)(28,42,16)@1/2 present verbatim; max facets vs Sec. 2.3 remarks agree:
76 -> 24 (KF72 confirmed), 91 -> 26 (17->26), 98 -> 35 (29->35), 84 and 141
"matching lower bounds" (15 and 18 attained; their higher rows 16 and 29 must sit
at non-trivial-stabilizer points, not verified here). Observed: IT(91/95) prints
(34,54,22) twice at two points (both kept). The harvest file's "printed pp.
27-48" source label is wrong (span is 27-81); its rows are exact. LIMITS: one
reader cross-checked against a machine text layer, NOT a second independent
re-key -> G5 duty still owed for any finalist-hosting group; no page was
unreadable at 120 dpi. Files: harness/schmitt_tetragonal_tables.json,
SCHMITT_TETRAGONAL_DIGITIZATION_2026-09-04.md.

2026-09-04 (later 2): TRIAGE PHASE 2 (tetragonal) — G4 shortlist from the 404
MENU-sighted types. harness/triage_phase2.py (deterministic, byte-identical on
re-run; model triage_phase1.py + b-ratio features) -> harness/
TRIAGE_PHASE2_RESULT.md. INTEGRITY: phase2_types.json sha256 71685b9a...69f7a3
MATCHES phase2_types.SHA256SUMS; recount 102 cubic + 789 tetragonal = 891, split
404 menu / 385 Schmitt-printed-only = store fields = PHASE2_RESULT claim; Euler
+ p-vector (|p|=F, sum p = 2E) on all 891; stabilizer | aut on all 148,390
stored sightings; max F stored 35 (menu 26), NO >38 hit; menu/S-only flags
consistent with stored pass labels. SCHMITT SOURCE: the visual digitization
harness/schmitt_tetragonal_tables.json used as primary (1,476 rows, Euler
PASS); cross-checked in-script against the text-layer harvest row-for-row on
(groups, f, b, point mod 1): IDENTICAL, and the flag-relevant projection
(group, f, b) has 0 symmetric-difference entries => P/A flags identical under
either source. Flags labelled "visual single-pass + text-layer cross-checked,
NOT re-keyed" = provisional (G5 re-key duty still owed). FEATURES: F (20+
bonus), aut, witness stratum (min dim over menu sightings), #b (distinct
b-ratios, menu passes P1/P3/P4/P5 only), per-orbit b-count, #groups,
p-novelty (odd>=5 or >=7-gons), Schmitt flag per sighted group (P / Pb = at a
b we also hit / A), plus two cheap type-level facts from the stored P2 pass:
S-CELL = the type reproduces one of his printed cells at his generating point
(176 of 404 are S-cell -> type-level match, excluded from the shortlist per
the kill criterion "Schmitt-contains-candidate => first-realization"; 228
menu-only), and P-RESOLUTION = how his printed row with the same (group, f)
reproduced: 'other' (a different stored type; id given) or 'unres' (row not
stored: origin-choice-2 groups / 95-96 / the two order_cycle rows). COUNTS:
ABSENT-all only 4 of 404 (all small, F 8-12, single-b, wall-suspect; ranks
302-368) — the 400 others share an f-vector with a printed row in >= 1
sighted group. Open/wall LABEL ONLY (no perturbation runs): open-likely 292
(same orbit at >= 3 b), indeterminate 52, wall-suspect 60 (single b).
Metric-thin 126 (1b 60, P5-only 85, P3-only 1 — matches PHASE2_RESULT).
F>=20: 61; aut>1: 173; dim-0 witness 7, line 56, plane 81, general-only 260.
TOP-15 (non-S-cell; all flagged P -> G5 type-level check required, none A):
#1 4e9c9b076cfec323 IT(92) P4_12_12 (5/24,5/24,0) f=(40,60,22) aut 2, 5 b
(77/64..83/64) open-likely, 11-gons; #2 49cedbdd58376fac IT(92) same orbit
f=(44,66,24) aut 2 at b=19/16 ONLY (wall-suspect, P5-only; 12-gons); #3
f654982d74d740f6 IT(141) I4_1/amd (0,1/12,1/12) f=(38,57,21) aut 2, 3 b, 14-
gon, printed row unres (origin shift); #4 4f6d3e68cbd9e729 IT(98) I4_122
general (1/12,3/8,1/6) f=(42,63,23) aut 1, 5 b incl. 797/1000 and 4/5;
#5 1497877268495988 IT(91)/95 line (0,1/12,0) f=(32,48,18) aut 2, 20 b, 363
sightings; #6 e0d18e5ea938d649 IT(122) I-42d (1/24,1/4,1/8) f=(36,54,20)
aut 2, p 3^4 4^8 8^8; #7 6797ab70c6015039 IT(76)/78/92/96 f=(32,48,18) 26 b;
#8 cd4fb52572edcb73 IT(86)/93/118/134 f=(30,45,17) 29 b; #9-#15: IT(76)
(36,54,20) and (40,60,22); IT(98) general orbit (1/12,3/8,1/6) at (42,63,23)
x3 / (40,60,22) / (32,48,18) line orbit; IT(95) (40,60,22). Group weight of
the shortlist: IT(98) x5, IT(76/78) x3, IT(92/96) x2, 91/95, 141, 122, 86,
95. COLLISION SCREEN worklist emitted for all 15 (printed b, point, PDF page,
P2 outcome). LIMITS: flags f-vector-level and provisional; 'other' says only
that HIS PRINTED representative is a different type (his 14 TB may still hold
ours); 'unres' rows need the shifted-origin re-run before any verdict; O/W is
a label from stored sightings; #b bounded by the menu (51/56 printed b never
swept); no roundness / geometric symmetry / Burnside / Engel / Bernhard.
Snapshot language only ("not matched against catalog snapshot of
2026-09-03"). Files: harness/triage_phase2.py, harness/TRIAGE_PHASE2_RESULT.md.

2026-09-04 (later 3): PHASE-2 (tetragonal) COLLISION SCREEN + FIRST PERTURBATION
CERTIFICATES on the TOP-15 shortlist. harness/collision_phase2_check.py
(pattern schmitt_collision_check.py + round1_computations/c1_wall_open.py;
accepted Gram modules via sweep_phase2_tetragonal.evaluate; certificate
4*rho^2 <= D^2 asserted on cell 0 AND a second orbit cell, Euler, orbit
congruence; exact arithmetic decides; 600 s per-pair cap, no hit; 12 s wall;
deterministic, md5-identical on re-run after masking timings) ->
harness/COLLISION_PHASE2_RESULTS.md + collision_phase2_results.json. INPUTS:
phase2_types.json sha256 71685b9a...69f7a3 verified before AND after (store
untouched, read-only); schmitt_tetragonal_tables.json rows (each worklist row
asserted present with its PDF page); conversions = PHASE2_SCHMITT_ORIGIN_CHECK
(origin-2 shift +s for 86/134/141, z->-z for 95/96, none for the IT(80)
order_cycle row), every alternative documented conversion re-run -> same code
in all 5 applicable pairs. RESULTS (27 pairs): 7 UNRES: all 7 reproduce the
printed f-vector after conversion (0 FVEC-MISMATCH); 6 DIFFERENT, 1 SAME —
Q17 IT(134) P4_2/nnm printed (219/500,-31/500,47/250) b=797/1000 + shift
(1/4,3/4,1/4) IS shortlist #8 cd4fb52572edcb73 (30,45,17) => #8 REFRAMES
(first-realization, kill criterion). Schmitt's cells for Q05 IT(141) (38,57,21)
and Q14 IT(86) (30,45,17) are NOT in the store (menu never sampled them; not
added); Q24 IT(80) crash row's cell = stored 19c7c8de77b6ce20; Q02/Q04 IT(96)
= the same stored types as their IT(92) twins (cf92c5d0 / ab93cbeb); Q27
IT(95) = stored f6abc569d035765a. 20 OTHER: all 20 confirmed DIFFERENT from
the store (stated P2 sighting present on the stated id, f-vector = printed,
canon_code != target). POST-SCREEN: 14 of 15 survive (all but #8), snapshot
language only ("not matched against catalog snapshot of 2026-09-03";
DIFFERENT != novelty, stated once). PERTURBATION (top-3, +-1/96, +-1/48 along
stratum tangents AND in b, refined to 1/1536 where a step flips; point and
metric classified separately): #1 4e9c9b07 IT(92) (5/24,5/24,0) b=5/4: point
OPEN / b OPEN (short +x side: +1/768 SAME, +1/384..+1/192 = #2 49cedbdd,
+1/96.. = 60c6a7023f6e4280). #2 49cedbdd same point b=19/16: point WALL at
every step to 1/1536 (-x: #1; +x: 60c6a702) / b OPEN on [455/384, 115/96]
=> a THIN BAND in (x,b) (width < 1/768 in x at 19/16; seen at b=5/4 in #1's
scan) — the triage 'wall-suspect / metric-thin (1 b)' label was b-based and
is refuted in b, survives as 'thin in x'; whether #2 is a G4 finalist of its
own or the transition type between #1 and 60c6a702 is a main-session call.
#3 f654982d IT(141) (0,1/12,1/12) b=1/2: point OPEN (both plane directions;
-y side short: -1/384 SAME, -1/192 = a NOT-STORED (31,48,19) cell with 3
non-simple vertices) / b OPEN on [23/48, 49/96]; +1/48 in b and +1/96 in z
give 9ff7306e4a6cbf44 (34,51,19). LIMITS: type-level only at the 27 printed
representatives (all other Schmitt flags stay f-vector-level; digitization
single-pass, not re-keyed; 51 of 56 printed b-ratios never swept); OPEN =
holds on the tested neighbourhood, not an interval proof; no G4 (roundness,
geometric symmetry, Burnside, Engel, Bernhard) run for any survivor. NOT DONE:
PROGRAM_LEDGER entry (main session), G4 certificates for the 14 survivors.

2026-09-04 (later 4): *** G4 CERTIFICATES, PHASE 2 (TETRAGONAL, GRAM METRIC) — 14/14
SURVIVORS PASS V0-V3 *** (harness/g4_certify_gram.py, sibling of the accepted cubic
g4_certify.py [unmodified; its metric-independent pieces imported: exact vector bits,
crystal-basis fan volume, the independent affine audit v1_audit/_a_*, banked V3 tool
paths]; Gram chain = accepted phase2/metric.py + sweep_voronoi_gram.py +
exact_cell_gram.py). SANITY GATE (runs first, both PASS): (1) truncated octahedron —
I4/mmm #139 origin orbit at c/a=1 (G=I, same integer sites as Im-3m #229) through the
Gram ladder == the cubic ladder on Im-3m #229 origin, 14 numbers identical (code, f,
p, aut 48, T=1, detL=864, vol, slots 14, geometric stabilizer 48, Bravais 48, |ops|
48, 24 proper, fixed [1,7,67,734] / free [1,2,6,35]); the one legitimate difference is
the SITE symmetry (16 vs 48) and the new |H/L| vs T*|site| check correctly reports
I4/mmm's honeycomb as having the LARGER full group Im-3m; (2) banked cubic G4 row
ceb70631e274e727 IT(212) through the Gram ladder with G=I reproduces G4_RESULTS.md
exactly (T=8, detL=1728, vol 216, site 3, stab 3, aut 3, Bravais 48, |ops| 24, fixed
[8,88,1384,25064], free [1,5,59,1065]). CONVENTIONS: sites/vertices in the crystal
basis x PERIOD, G=diag(q^2,q^2,p^2) for c/a=p/q; all volumes crystal-basis measures
(Euclidean = same factor sqrt(det G)/q^3 for cell, covolume, torus), so T*vol =
detL = covol(L) is exact-rational; facets/pairings are affine, the metric enters via
the Voronoi bisector claims (G-norm, generator V1d + the audit's fresh Gram layer:
shared-vertex G-equidistance, vertex-side, facet normal || G(r-c)); V3 tables are
metric-independent adjacency data (stated once). LADDER per cell: V0 exact
re-derivation at the witness (group, point, b) with every store field asserted; V1
tiling certificate in the G-norm (all T reps exact, identical code; T*vol=detL;
T*F slots paired 1:1; translate-completeness over the certified G-ball 4rho^2 with
every in-ball G-bisector weakly satisfied, no unlisted 2-face contact) + independent
audit; V2 site stabilizer (frozen ops) / combinatorial aut / SOLID isometry group =
map automorphisms preserving the G-form pairwise, each solved as an affine map with
A^T G A = G asserted, re-derived by a G-Gram-triple scan (equal), chirality, hands,
Bravais group of L in G, honeycomb point group |H/L|; V3 banked enumerate n<=4 +
burnside_generic + INDEPENDENT publication/verify_counts_independent.py to n=5
(15-min cap; fixed/free identical to banked for n<=4, its own Burnside all+proper ok
at every n). RESULT: all 14 PASS every rung, no deferrals, independent enumerator
reached n=5 for every cell (1-6 s each), total wall 215 s (re-run 220 s, doc
identical with timings masked). Symmetry: Isom_fix_site == Isom(solid) == site
symmetry for every cell; solids chiral except #3 f654982d (I4_1/amd, one mirror);
#7 6797ab70 and #9 086ac96f have aut 2 but Isom 1 (combinatorial-only symmetry);
|H/L| = T*|site| for all 14 => the full symmetry group of every honeycomb is
exactly its generating group. Note: #6 e0d18e5e witnessed at c/a=1 has a
metrically-cubic BCT lattice (Bravais 48) but |H/L|=8=T*|site| (site set decides).
#2 49cedbdd certified with the WALL/THIN-BAND label (finalist status = main-session
call); #8 excluded (reframed). Artifacts: harness/G4_PHASE2_RESULTS.md,
g4p2_tables_<id>.json/.txt/_indep.json x14, g4p2_control_* (gate), g4p2_run.log.
phase2_types.json read-only (sha 71685b9a... unchanged). LANGUAGE: G4 != novelty;
all 14 stay "not matched against the catalog snapshot of 2026-09-03"; G5 not run.
MAIN SESSION RE-RUN BEFORE ACCEPTANCE (exit 0 required, ~4 min):
cd <repo>/harness && python3 g4_certify_gram.py

## 2026-09-04 (later 5) — THE CATALOG built (#141, main-session verified) + wording correction
- catalog/: 891 exact-confirmed types (102 cubic-first, 789 tetragonal-first; 175 distinct f-vectors; max 35 facets, kill bar 38 never crossed), catalog.json/csv + sightings sidecar, f-vector reconciliation vs Schmitt cubic (986 printed pairs: 292 matched, 33 of ours absent, 694 unreached by our menu) and tetragonal (1,639 pairs: 700 matched, 67 absent, 939 unreached, 669 of those stored via P2 at his own point). Independent recount: 0 failures, exit 0 (main session re-ran). Data-descriptor draft + venue scout (Zenodo first; Sci Data vs Acta A; two venue pages bot-walled, unverified).
- CORRECTION to the 2026-09-01 entry's shorthand "whole printed survey": (16,25,11) is printed in tetragonal IT(134) and IT(141). Both rows computed exactly under every documented origin shift (catalog/check_satchelhedron_tetragonal_rows.py, main-session re-run): DIFFERENT types from the Satchelhedron and from every stored type. The claim is "absent from the printed CUBIC survey" — the paper already says so; registry + dashboard corrected; the old entry stands as written (append-only).
- Definitional note: "groups by tetragonal-menu type count" can be counted type-globally (98: 60, 141: 59, 122: 57 ...) or sighting-locally (98: 48, 122: 39, 92: 33 ...); both are correct, wording must say which.

2026-09-04 (later 6): *** PHASE 2 BATCH 2 — HEXAGONAL FAMILY (IT 143-194, 52 groups)
SWEPT, TRIAGED, COLLISION-SCREENED *** (subagent #143; provisional until the main
session re-runs phase2/g2c_controls.py and the recount). Rule 29 honoured: every
computation ran in foreground calls; the sweep is a resumable driver (per-invocation
budget + append-only resume log) and completed in 2 invocations (420 s + 394 s).
GATE G2c (ANCHORS block appended BEFORE any batch-2 computation; phase2/g2c_controls.py
-> G2C_RESULT.md, exit 0, 5.6 s): ALL REQUIRED ASSERTIONS PASS. (a) hexagonal prism
P6/mmm origin at c/a 1/2, 1, 2 (re-run of G2b(a)); (b) R-3m #166 origin orbit IS the
rhombohedral lattice (3 pts/cell): FCC bracket {12/5, 5/2} -> rhombic dodecahedron on
BOTH sides; SC bracket {6/5, 5/4} -> truncated octahedron / rhombic dodecahedron
(DIFFERENT sides: the cube transition at c/a = sqrt6/2 separates the two regimes);
BCC bracket {3/5, 5/8} -> truncated octahedron both sides; generic c/a = 1 ->
truncated octahedron, c/a = 2 and 3 -> rhombic dodecahedron, all stable at +-1/24;
the pre-recorded prediction ("truncated octahedron both sides of the SC bracket") was
WRONG and is recorded as such — exact arithmetic decided; (c) SCHMITT POINT
CONVENTION: his trigonal/hexagonal generating points are printed in his
orthohexagonal basis B'' = (2b1'+b2', b2', b3') (App. B); conversion x' = 2x'',
y' = x''+y'', z' = z'' (hypothesis H1) reproduces the printed f-vector of all six
pre-registered rows — IT(143) (8,12,6), IT(147) (10,15,7), IT(155) (48,73,27),
IT(166) (38,58,22), IT(178) (64,96,34) = his hexagonal-family MAXIMUM (34 facets,
exact: stab 1, aut 1, p 3^10 4^7 5^8 6^4 7^2 12 18 26), IT(194) (18,30,14) at a
special position — the verbatim alternative H0 was never needed; the IT(178) row
reproduces in IT(179) only under z -> -z (recorded); b-ratio = c/a; (d) R^T G R = G,
certificate, float/exact agreement, Euler, one code per orbit, stab | aut on every cell.
DIGITIZATION (harness/schmitt_hexagonal_tables.json, digitize_schmitt_hexagonal.py,
SCHMITT_HEXAGONAL_DIGITIZATION_2026-09-04.md): Sec. 2.2.3-2.2.4, printed pp. 82-118 =
PDF 87-123; 45 blocks (7 enantiomorphic pairs share one table), 958 rows, 38 distinct
printed b-ratios, family max 34 facets; text layer primary + visual cross-read of every
row on PDF 88, 97, 105, 114, 123 (153 rows, 0 discrepancies); Euler all 958; Sec. 2.3
remarks (150, 152, 159, 166, 178) agree with the table maxima; NOT an independent
re-key (G5 duty owed). No frequency column printed.
PLAN COUNTS (phase2/plan_counts.py hexagonal; family argument added, default output
unchanged; PHASE2_PLAN.md Appendix 2): 4,547 special-position orbits (dim0 120, dim1
1,525, dim2 2,902) + 104 general = 4,651 orbits; 42 s.
SWEEP (harness/sweep_phase2_hexagonal.py -> phase2_hexagonal_types.json 65 MB [raw +
resume log gitignored; .gz + SHA256SUMS committed], PHASE2_HEX_RESULT.md): store seeded
with all 891 batch-1 types (sha 71685b9a... verified); menus 4,651 coarse + 676 1/24-line
orbits (2,740 plane samples skipped by design); passes P1 60,463 / P2 1,276 / P3 23,255
(b in {3497/1000, 797/1000, 4/5, 527/1000, 7/8}) / P4 8,788 / P5 1,951 orbits =
108,580 candidates, 212,912 exact cells, 0 skipped; STORE 1,583 = 891 prior + **692
hexagonal-first** (288 menu-sighted + 404 Schmitt-printed-only); 43 prior types
re-sighted (17 cubic-first, 26 tetragonal-first); MAX FACETS stored 34 (his IT(178)
row), from OUR MENU 24; NO >38 sighting (kill criteria never fired); 0 congruence
purges; 42 bisection cap hits; QUARANTINES 46, all schmitt_fvec_mismatch in IT(180)
P6_222 — explained by Schmitt's own remark on the 180/181 table ("only the normalizer
for IT(181) but not for IT(180)": the printed points are IT(181)'s; the pre-registered
z->-z rule was applied to the second-LISTED member only), read-only re-run
(phase2_hex_schmitt_180_check.py -> PHASE2_HEX_SCHMITT_180_CHECK.md): 46/46 reproduce
under z -> -z, all 46 cells already in the store, store unchanged. Schmitt screen:
1,230/1,276 (row x group) evaluations reproduce verbatim (H1 1,085; H1+zflip 145 on
153/154/179) + 46 under the read-only re-run = 1,276/1,276.
TRIAGE (harness/triage_phase2_hexagonal.py -> TRIAGE_PHASE2_HEX_RESULT.md +
triage_phase2_hex_shortlist.json; deterministic, byte-identical on re-run): sanity all
PASS (sha match, Euler, p-vector, stab | aut on every sighting, recount 891/692/288/404 =
store fields); 288 menu-sighted: S-cell 124, ABSENT-all 5, open-likely 214 /
indeterminate 24 / wall-suspect 50 (labels), metric-thin 91, F >= 20: 41, aut > 1: 135,
max menu F 24; printed b swept 9 of 38.
COLLISION SCREEN (store-side + recomputation, collision_phase2_hex_check.py ->
COLLISION_PHASE2_HEX_RESULTS.md, exit 0, store sha unchanged): SURVIVORS 151 of 288
(f-vector absent from every sighted group's table, or DIFFERENT from the cell at every
printed row of that (group, f)); COLLISION 124 (all S-cell: his printed cells
reproduced by our menu -> first-realization framing); UNRESOLVED 13 (their only
unresolved pairs are the 46 IT(180) rows; the read-only re-run finds all 13 DIFFERENT
at every printed 180 row — recorded, store verdict stands). Top-10 survivors
re-confirmed by recomputation at his printed points: 26 pairs, all DIFFERENT TYPE, all
consistent with the stored P2 cells. TOP-10 (id, group, c/a, f, aut, O/W label): #1
c49077384aaebeb0 IT(178) P6_122 b=5/4 (44,66,24) aut 2, 12 b, open-likely, 14-gons;
#2 59585d778cb3a7a4 IT(178) b=3/4 (40,60,22) aut 2, 22 b; #3 095ce61d28388c98 IT(178)
b=1 (40,60,22) aut 2, 24 b; #4 9be0f2271a14b6a9 IT(178) b=1 (36,54,20) aut 4, 20 b;
#5 2d654c836f3731c6 IT(178) b=1 (36,54,20) aut 2, 30 b (also 169/170); #6
b0f80776885f3ae1 IT(178) b=1/2 (36,54,20) aut 2, 17 b; #7 a348875c3f707895 IT(178)
b=1/2 (36,54,20) aut 2, 21 b; #8 dcc38ea9177089b9 IT(178) b=1/2 (36,54,20) aut 2, 3 b;
#9 5b86a254c715306c IT(169) P6_1 b=797/1000 (40,60,22) aut 1, 6 b; #10
f05f0b009e0929f6 IT(169) b=3/4 (32,48,18) aut 2, 39 b — all open-likely (label only,
no perturbation runs). Group weight: IT(178) x8, IT(169) x2 (Schmitt's own "third most
facets" group). LANGUAGE: all 151 survivors are "not matched against the records
checked as of 2026-09-04"; no naming; "observed max 38". NOT DONE: G4 for any
survivor; perturbation certificates; second independent re-key; PROGRAM_LEDGER main-
session acceptance; git commit (main session). MAIN-SESSION RE-RUN (exit 0 required):
cd <repo>/harness/phase2 && python3 g2c_controls.py
cd <repo>/harness && python3 triage_phase2_hexagonal.py   # deterministic recount, exit 0; TRIAGE_PHASE2_HEX_RESULT.md byte-identical
cd <repo>/harness && python3 collision_phase2_hex_check.py   # exit 0; deterministic except timing columns
Files: ANCHORS.md (G2c block appended), phase2/{g2c_controls.py, G2C_RESULT.md,
plan_counts.py}, harness/{digitize_schmitt_hexagonal.py, schmitt_hexagonal_tables.json,
sweep_phase2_hexagonal.py, phase2_hexagonal_types.json(.gz, .SHA256SUMS),
phase2_hexagonal_records.jsonl (ignored), phase2_hex_run.log, PHASE2_HEX_RESULT.md,
triage_phase2_hexagonal.py, TRIAGE_PHASE2_HEX_RESULT.md, triage_phase2_hex_shortlist.json,
collision_phase2_hex_check.py, COLLISION_PHASE2_HEX_RESULTS.md,
collision_phase2_hex_results.json, phase2_hex_schmitt_180_check.py,
PHASE2_HEX_SCHMITT_180_CHECK.md, phase2_hex_schmitt_180_check.json},
SCHMITT_HEXAGONAL_DIGITIZATION_2026-09-04.md, PHASE2_PLAN.md (Appendix 2 appended),
.gitignore (raw store + resume log lines appended, never sorted).

2026-09-04 (later 7): *** G4 CERTIFICATES, PHASE 2 BATCH 2 (HEXAGONAL FAMILY, GRAM
METRIC IN THE ITA HEXAGONAL BASIS) — 151/151 COLLISION-SCREEN SURVIVORS PASS V0-V3 ***
(subagent #145; provisional until the main session re-runs harness/g4_certify_hex.py,
exit 0 required). Rule 29 honoured: every computation ran in foreground calls; the
driver is a resumable process pool (per-invocation budget, per-cell records in
harness/g4p2hex_cells/, doc written atomically) and completed in ONE invocation.
CODE: harness/g4_certify_gram.py (the ACCEPTED tetragonal Gram-aware ladder) received
exactly two behaviour-preserving edits — a family switch in gram_of (crystal_family
'hexagonal' -> metric.gram_hexagonal(c/a)) and an optional INDEP_WORKERS hook
(default None = previous subprocess args). Its tetragonal `--gate-only` re-run after
the edit: exit 0, stdout identical to the pre-edit baseline with timings masked, the
six non-timing g4p2_control_* artifacts byte-identical (md5), the two *_indep.json
differ only in wall_s/t_* fields. harness/g4_certify_hex.py (new) imports the ladder
functions unchanged (v0_rederive, v1_generate, v1_audit_gram, v2_symmetry,
v3_tables_burnside, run_ladder) and adds the gates, the pool driver, the results doc,
a fresh hexagonal-prism polyform enumerator and a fresh generating-group check.
SANITY GATES (all PASS, 10 s): (i) hexagonal prism = P6/mmm #191 origin at c/a=1:
code == seed, f=(12,18,8), aut 24, site 24, Isom_fix_site 24, Isom(solid) 24,
Bravais 24, T=1, |H/L|=24=T*|site|; Burnside counts n<=4 from the ladder (banked
enumerate + independent enumerator, reached n=5) fixed [1,4,24,168] / free
[1,2,5,20] / one-sided [1,2,5,23] EQUAL to the fresh independent hexagonal-prism
enumeration (8 neighbours = the 8 integer vectors of minimal G-norm; point group = the
24 integer matrices preserving G brute-forced in [-2,2]^9, 12 proper). (ii) rhombic
dodecahedron = R-3m #166 origin at c/a=3 vs the ACCEPTED cubic ladder (g4_certify.py
functions, unmodified) on Fm-3m #225 origin: code (== seed), f=(14,24,12), p=4^12,
aut 48, T=1, slots 12, 6 non-simple vertices, FIXED counts [1,6,50,475] identical;
the metric-dependent numbers differ as predicted before the run and are explained:
site/Isom_fix/Isom/Bravais/|H/L| = 12 (-3m) vs 48 (m-3m) because c/a=3 is not
metrically cubic (FCC is at the irrational sqrt6), so the FREE counts (orbits under
the honeycomb's OWN group, 12 vs 48 ops) are [1,2,8,54] vs [1,1,4,20] (prediction
free_hex(2)=2 vs 1 confirmed); detL/vol are crystal-basis measures in different bases.
VERIFIED by fresh code: the unimodular M=((-1,1,0),(1,0,0),(1,-1,1)) carries the 12
hexagonal-basis neighbour vectors onto the 12 cubic-basis ones and conjugates the 12
hexagonal honeycomb ops into a subgroup of the 48 cubic ones. (iii) banked tetragonal
row 1497877268495988 (IT 91, #5) through the extended code: tables JSON byte-identical
to the banked g4p2_tables_1497877268495988.json (10,780 bytes), banked + independent
counts identical to the banked _indep.json rows, V2 numbers (2,2,2,2,0,2,16,8)
identical to G4_PHASE2_RESULTS.md.
RESULT (harness/G4_PHASE2_HEX_RESULTS.md, 2,651 lines): all 151 survivors PASS every
rung (V0 151, V1 gen 151, V1 audit 151, V2 151, V3 151); no deferral; the independent
enumerator reached n=5 for every cell; max facets among the survivors 24 (kill bar 38
never approached); store sha 7494c7b2... verified before the run and unchanged after.
Symmetry: 140 chiral solids / 11 achiral; 121 chiral honeycombs with all translation
classes of one hand; 19 chiral solids occur in BOTH hands inside one honeycomb — all in
R-3 (9), R-3c (7), R3c (3), whose inversion / c-glide maps a cell to its mirror image
(the honeycomb is achiral, the solid chiral; consistent, not a contradiction);
combinatorial-only symmetry (aut > Isom) in 15 cells; Bravais orders 24 (hexagonal P)
x105 and 12 (rhombohedral R) x46. FIRST IN THIS PROGRAM, double-checked: 3 cells have
Isom(solid) > site AND |H/L| = 12 > T*|site| = 6 — #29 f0b07b168368759b (first witness
R-3 #148 at (0,1/2,0), c/a=3/4, f=(14,24,12)), #53 4db369a636f4396b (P3_112 #151 at
(0,1/2,0), c/a=3/2, f=(18,30,14)), #113 105e41c2798e6180 (R-3 #148 at (0,0,5/24),
c/a=2, f=(16,27,13)). Double-check 1 (in-worker, fresh): every listed isometry
re-verified G-orthogonal and vertex-permuting; the extra ones fix the site and map the
site set to itself but their linear parts are not in the first-witness site group.
Double-check 2 (parent, fresh, run on ALL 151 cells): the orbit of the witness point
under every hexagonal-family group of the frozen ops (directly, then with an origin
shift in (Z/P)^3) — the largest point-op count reproducing the site set never exceeds
the ladder's |H/L| (asserted for every cell) and equals it for all 151: #29 and #113
are R-3m #166 honeycombs (site symmetry 4 and 6 there = |H/L|/T = Isom_fix_site),
#53 is a P6_422 #181 honeycomb after the origin shift (0,0,1/3) (site symmetry 4 =
222). The store already carries sightings of these types in the full groups (136, 3,
2), so the collision screen covered the supergroup's Schmitt tables; the summary
table's IT column is the FIRST-WITNESS group and the doc says so. Nothing contradicts
the accepted modules or the triage labels (labels carried verbatim from
TRIAGE_PHASE2_HEX_RESULT.md, not re-derived). Runtime: 446 s wall for the complete
run (5 cells in parallel, independent enumerator --workers 2; sum of per-cell walls
2,008 s; load peaked ~12.8 on 16 cores with the three protected PIDs untouched).
DETERMINISM: two fresh runs and two resumed rebuilds agree byte for byte with timings
masked, md5 9a84d24be576713a002d4f0387839760 (= `md5 -q` of the file written by
`--resume --mask-timings`). LANGUAGE: G4 != novelty; all 151 stay "not matched against
the records checked as of 2026-09-04"; no naming; "observed max 38". NOT DONE: G5;
perturbation certificates; second independent re-key; git commit (main session).
MAIN-SESSION RE-RUN BEFORE ACCEPTANCE (exit 0 required; ~8 min; exit 3 = resume):
PY=python3; cd <repo>/harness; $PY g4_certify_hex.py --fresh --budget-s 420; rc=$?; while [ $rc -eq 3 ]; do $PY g4_certify_hex.py --resume --budget-s 420; rc=$?; done; echo exit $rc
$PY g4_certify_hex.py --resume --mask-timings && md5 -q G4_PHASE2_HEX_RESULTS.md   # must print 9a84d24be576713a002d4f0387839760
$PY g4_certify_hex.py --resume                                                     # restores the timed doc
$PY g4_certify_gram.py --gate-only                                                 # tetragonal default unchanged, exit 0
Files: harness/{g4_certify_gram.py (2 hunks), g4_certify_hex.py, G4_PHASE2_HEX_RESULTS.md,
g4p2hex_tables_<id>.json/.txt/_indep.json x151, g4p2hex_cells/<id>.json x151 + _gates.json,
g4p2hex_control_* (12 files: prism, cubic-path rhombic dodecahedron, R-3m rhombic
dodecahedron, tetragonal control)}; phase2_hexagonal_types.json read-only.

2026-09-04 (later 8): *** COMPUTED OPEN/WALL CLASSIFICATION OF ALL 165 G4-CERTIFIED
PHASE-2 CELLS (14 tetragonal + 151 hexagonal-family) — replaces the heuristic triage
labels *** (subagent #148, Claude Fable 5.1; PROVISIONAL until the main session re-runs
harness/phase2/wall_open_phase2.py --fresh and reproduces the JSON md5). PRE-REGISTERED
FIRST: ANCHORS.md block "PERTURBATION CLASSIFICATION, PHASE 2 — pre-registered
2026-09-04" appended before any run (point steps +-1/48, +-1/96 along the c1
nullspace_basis tangent directions of the witness stratum, refined to 1/1536; metric
c/a*(1+eps), eps +-1/96, +-1/192 relative, refined to 1/3072; verdicts by c1 lines
103-109 per direction class and COMBINED over all directions; INDETERMINATE on a
quarantined side; flags LINE-ISOLATED / NON-SIMPLE-VERTEX / STAB-CHANGE defined
there — c1 has no LINE-ISOLATED term, so it is defined in the block). One post-run
CORRECTION appended to ANCHORS (a pre-run count: five cells, not two, have c/a > 2;
scheme unchanged). CHAIN: the accepted sweep_phase2_tetragonal.evaluate /
sweep_phase2_hexagonal.evaluate imported unchanged (G3 invariant, cutoff certificate,
orbit congruence, kill criteria live); stores read-only, sha256 asserted before and
after. RESULTS (COMBINED verdict): tetragonal 13 OPEN + 1 WALL (49cedbdd58376fac,
the known thin-band cell: line-isolated on the (x,x,0) line, metric OPEN); hexagonal
102 OPEN + 40 WALL + 9 ONE-SIDED; no INDETERMINATE, no quarantine, no crash, no
float-superseded row, no stabilizer change; 3,879 chain evaluations; neighbours
never exceeded 26 facets. Point/metric separately (hexagonal): POINT 101 OPEN / 40
WALL / 9 ONE-SIDED / 1 n/a (the one fixed-point witness f0b07b168368759b, OPEN in
c/a); METRIC 130 OPEN / 20 WALL / 1 ONE-SIDED. HEURISTIC vs COMPUTED: 114 agree, 35
disagree (all hexagonal: 17 open-likely -> WALL, 7 open-likely -> ONE-SIDED, 9
wall-suspect -> OPEN, 2 wall-suspect -> ONE-SIDED), 16 indeterminate labels resolved
(11 OPEN, 5 WALL); the b-count heuristic was wrong in both directions. REGRESSION
PASS (asserted): the three top-3 tetragonal POINT verdicts equal
COLLISION_PHASE2_RESULTS.md (OPEN / WALL (1,1,0) / OPEN). READING: 40 of the 41 wall
cells carry non-simple vertices at the witness (the general-position witnesses sit on
the sweep's rational grid points where Voronoi vertices coincide), the 41st is the
simple thin-band cell; but 36 OPEN cells also have ns > 0 (symmetry-forced
coincidences), so ns > 0 alone is not a wall criterion. NAMING-RELEVANT FACT (per
wall cell, in WALL_OPEN_PHASE2.md "Wall cells"): every wall-side neighbour is named
by f, p, aut, stored id, Schmitt-printed-TYPE status (pass-P2 sighting, groups) and
f-printed status; 24 wall cells have every wall-side neighbour stored, 25 have at
least one wall-side neighbour that is a Schmitt-printed TYPE, 16 have a neighbour
that is itself a certified cell, 17 have a wall-side neighbour in no store (31 such
cells, recorded read-only, never added). DETERMINISM: two fresh runs byte-identical,
WALL_OPEN_PHASE2.json md5 6b257c551f6fb275dfabb03e992f57c2 (sorted keys, no
timings); runtime 83 s and 82 s wall (8 forked workers, foreground, load peaked
~12.6 on 16 cores, protected PIDs untouched). LANGUAGE: OPEN = holds on the tested
neighbourhood, never an interval proof; no naming; every type stays "not matched
against the records checked as of 2026-09-04". NOT DONE: perturbation at the other
sightings of each type; G5; git commit (main session; add
harness/phase2/{wall_open_phase2.py, WALL_OPEN_PHASE2.json, WALL_OPEN_PHASE2.md,
wall_open_run1.log, wall_open_run2.log} and harness/phase2/wall_open_cells/ by name;
verify with git ls-files per own-goal 45). Docs that still carry the heuristic labels
(TRIAGE_PHASE2*_RESULT.md, G4_PHASE2*_RESULTS.md, the catalog) are NOT edited here;
they should cite WALL_OPEN_PHASE2.md as the label authority.
MAIN-SESSION RE-RUN BEFORE ACCEPTANCE (exit 0 required; ~90 s):
cd <repo>/harness/phase2 && nice -n 10 python3 wall_open_phase2.py --fresh --jobs 8 --budget-s 540; echo exit $?; md5 -q WALL_OPEN_PHASE2.json   # must print 6b257c551f6fb275dfabb03e992f57c2 (exit 3 = budget stop: re-run the same command without --fresh to resume)

2026-09-04 (later 9): *** POOL RANKING STAGED FOR FLAGSHIP CHOICE (#149, PROVISIONAL
until the main-session re-run) ***. Staging only — no names produced; naming is Tyler's.
POOL: the 115 cells with COMBINED verdict OPEN in harness/phase2/WALL_OPEN_PHASE2.json
(md5 6b257c551f6fb275dfabb03e992f57c2): 13 tetragonal (IT 75-142), 51 trigonal (IT
143-167), 51 hexagonal (IT 168-194). SCORING PRE-REGISTERED at 13:41 PDT, before any
feature was computed, in paper_prep/MINT_plesiohedron/POOL_RANKING_2026-09-04.md
(PREREG-BEGIN..END; the script reads the block back and never regenerates it): score =
F (f2/4) + P (polygon kinds + pentagons/2 capped 4 + odd >= 7-gons capped 4) + A (1.5
log2 aut + 1 if Isom = aut) + C (1.5 chiral + 0.5 enantiomorphic group) + R (10 x
roundness / 47.9833 Josehedron control) + I (integer-presentation scale <= 24: 2, <= 96:
1) + D (3 - stratum dim) + E (-2 if Engel/Koch KNOWN-mined, 0 if UNKNOWN) + S (story
flags: +2 family facet record, +2 aut = 1, +1 f-vector unprinted in own group, +1 site =
Isom = aut); ties roundness, f2, id. CHAIN: g4_certify_gram.v0_rederive (accepted,
unmodified; asserts canonical code / f / p / aut against the frozen stores) -> exact
cell; Isom(solid) re-derived by cell_stabilizer_gram and EQUAL to
G4_PHASE2_RESULTS.md / G4_PHASE2_HEX_RESULTS.md for all 115; f, p, aut, c/a, stratum,
witness cross-checked against WALL_OPEN_PHASE2.json (all agree); roundness =
site-centred outer circumsphere (radius^2 = rho^2 of the certificate, the ROUNDNESS.md
definition; Euclidean volume = crystal-basis volume x sqrt(det G)); minimal enclosing
sphere exact (Welzl in the G inner product, verified; equals the c4 brute force on all
45 cells with <= 30 vertices), reported not scored. OUTPUT: harness/phase2/
POOL_RANKING_2026-09-04.json (115 rows, every feature, sorted keys, no timings) md5
75cacf7e762bda859234d2843888cb94; the MD carries the pre-registration, top-5 per
system with one-line hooks and "what a name would attach to" paragraphs, pool
records, score-blind notes, the full 115-row table. TOP-5 PER SYSTEM (id, group, c/a,
f, aut/Isom, chiral, roundness site): tetragonal 4e9c9b076cfec323 IT92 P4_12_12 5/4
(40,60,22) 2/2 chiral 35.78% · 164d4bd63d82d0c3 IT76 P4_1 5/4 (40,60,22) 1/1 30.22% ·
6797ab70c6015039 IT76 P4_1 3/2 (32,48,18) 2/1 31.54% · 213c7a114d5a97a8 IT98 I4_122
11/16 (42,63,23) 1/1 15.44% · 4f6d3e68cbd9e729 IT98 I4_122 3/4 (42,63,23) 1/1 16.20%;
trigonal a93f8fe7ecdc5851 IT144 P3_1 9/8 (32,48,18) 1/1 42.99% · e598ffd8a1cac138
IT144 P3_1 29/32 (32,48,18) 1/1 37.30% · c0071756347c5a8a IT144 P3_1 1 (28,42,16) 1/1
43.46% · 466b12546dd936c3 IT161 R3c 527/1000 (26,40,16) 1/1 41.00% · c82ebc15c49c1413
IT154 P3_221 527/1000 (38,57,21) 1/1 17.65%; hexagonal c49077384aaebeb0 IT178 P6_122
5/4 (44,66,24) 2/2 chiral 24.45% (top overall) · 8d90c524c89922d9 IT169 P6_1 11/8
(36,54,20) 1/1 32.76% · 9c0b7e0c29dfebb2 IT169 P6_1 3/4 (36,54,20) 1/1 39.39% ·
3ddc41389e6d484f IT171 P6_2 1 (32,48,18) 1/1 26.45% · 30f2a1e483babf55 IT178 P6_122
11/4 (29,44,17) 1/1 26.82%. All chiral, all in enantiomorphic groups except 466b1254
(R3c) and the two IT98 cells. RECORDS: roundest site-centred c0071756347c5a8a 43.46%
(nothing reaches the Josehedron's 47.98%); roundest MES cff2d5fb5e0d4149 IT171 P6_2
(23,35,14) 46.73%; most facets 24 (c49077384aaebeb0; tetragonal max 23, trigonal 21);
most pentagons 8 (16025e0680843c36 IT169, 4a560e459032166a IT154); largest face
16-gon (4 cells); highest aut 4 (3 cells); 81/115 fully asymmetric; 109/115 chiral,
6 achiral (the R-3 fixed-point cell, the I4_1/amd cell, four R-3m cells); stratum
dims 0/1/2/3 = 1/16/5/93. SCORE-BLIND NOTE: the one fixed-point cell
f0b07b168368759b (IT148 R-3, c/a 3/4, (14,24,12), 3^4 4^4 5^4, aut 4 fully realized,
achiral, m = 108, the smallest and best-presented cell in the pool) ranks 77 because
the weights favour facet-heavy cells; if a small pinned symmetric cell is wanted it is
the one to look at. PRESENTATION: no pool cell has a small-denominator presentation at
its witness (I = 0 for all 115; best Cartesian scale 5280, best lattice-basis scale
108) — the Josehedron integer-coordinate hook is absent here; a nicer point on the
same open stratum or a nicer c/a inside the tested band c/a(1 +- 1/96) was not
searched. EXPOSURE: Engel 1981 / Koch 1972 exposure UNKNOWN for every tetragonal,
trigonal and hexagonal group (print-only, unread; ILL pending) — E = 0 throughout and
the term does not move the ranking today. Schmitt printed-f: every pool f-vector is
printed in its own group's table (0 absent), none exceeds its group's printed maximum.
LANGUAGE: no names; "not matched against the records checked as of 2026-09-04"
everywhere; OPEN = holds on the tested neighbourhood. Wall scan of every output:
clean. DETERMINISM: two fresh runs byte-identical (JSON md5 above, MD identical), 67 s
wall each, 6 forked workers, foreground, load peaked ~11 on 16 cores, protected PIDs
8014/7417/13578 untouched. NOT DONE: git commit (main session: add harness/phase2/
{pool_ranking_2026-09-04.py, POOL_RANKING_2026-09-04.json, pool_ranking_run1.log,
pool_ranking_run2.log} and paper_prep/MINT_plesiohedron/POOL_RANKING_2026-09-04.md by
name; verify with git ls-files per own-goal 45); no outreach; no re-weighting; no
renders.
MAIN-SESSION RE-RUN BEFORE ACCEPTANCE (exit 0 required; ~70 s):
cd <repo>/harness/phase2 && POOL_JOBS=6 nice -n 10 python3 pool_ranking_2026-09-04.py; echo exit $?; md5 -q POOL_RANKING_2026-09-04.json   # must print 75cacf7e762bda859234d2843888cb94

2026-09-04 (later 10): *** NICE-POINT SEARCH FOR THE TOP-3 POOL CELLS PER SYSTEM (#153,
Claude Fable 5.1; PROVISIONAL until the main session re-runs the verify command below) ***
Staging for naming; no names produced. QUESTION: inside the neighbourhood WALL_OPEN_PHASE2
certified for each of the 9 cells (rank 1-3 per system in POOL_RANKING_2026-09-04.json md5
75cacf7e...), is there a generating point / c/a with smaller exact vertex denominators that
keeps the SAME canonical type? PRE-REGISTERED 15:10 PDT before any chain evaluation
(paper_prep/MINT_plesiohedron/NICE_POINTS_2026-09-04.md, PREREG-BEGIN..END; the search set
was enumerated by `nice_points_2026-09-04.py --plan` and quoted verbatim): per direction
the extent = largest tested |eps| with every smaller tested step SAME (refinement rows
included); points with every coordinate of denominator <= 48 inside the product of extents;
c/a of denominator <= 16 inside the metric band (+ the witness c/a); niceness = m_lattice
(site-centred conventional-basis vertex denominator), then m_cartesian (tetragonal) /
m_eisenstein (hexagonal family, in-plane), then c/a simplicity, then point denominators;
kill = any type change is discarded and COUNTED. CHAIN: sweep_phase2_tetragonal.evaluate /
sweep_phase2_hexagonal.evaluate (the WALL_OPEN functions, unmodified) on all 43,217
candidates; every SAME candidate re-derived by g4_certify_gram.v0_rederive as a synthetic
witness (code/f/p/aut asserted against the frozen stores; stores sha256 unchanged); witness
m values reproduce the pool JSON (asserted). RESULTS (best presentation per cell; m_lattice /
second scale): tetragonal 4e9c9b076cfec323 IT92 P4_12_12 point (3/16, 3/16, 0) c/a 5/4 ->
748000 / Cartesian 149600 (witness 38041920 / 7608384); 164d4bd63d82d0c3 IT76 P4_1 witness
(1/8, 1/6, 5/12) c/a 5/4 stays best -> 7257600 / 1451520; 6797ab70c6015039 IT76 P4_1 point
(1/8, 3/16, 7/16) c/a 3/2 -> 56160 / 37440 (witness 466560 / 155520); trigonal a93f8fe7ecdc5851
IT144 P3_1 witness (1/12, 3/8, 1/6) c/a 9/8 stays best -> 174960 / Eisenstein 6480;
e598ffd8a1cac138 IT144 P3_1 same point (1/8, 1/6, 5/12) at c/a 9/10 -> 151632000 / 4212000
(witness at 29/32: 3400600320 / 4043520); c0071756347c5a8a IT144 P3_1 point (1/11, 4/11, 2/11)
c/a 1 -> 11297286 / 513513 (witness 6073608960 / 1518402240); hexagonal c49077384aaebeb0 IT178
P6_122 witness (1/12, 1/6, 1/4) c/a 5/4 stays best -> 415800 / 16632; 8d90c524c89922d9 IT169
P6_1 point (2/27, 10/27, 4/27) c/a 11/8 -> 2.8e16 / 2.4e14 (witness 1.4e21 / 1.1e19);
9c0b7e0c29dfebb2 IT169 P6_1 point (1/11, 4/11, 2/11) c/a 3/4 -> 988416 / 988416 (witness
804980880 / 268326960). 6 of 9 improved; NONE approaches the Josehedron control (same
functions: IT220 12a (3/8, 0, 1/4), vertex denominator 24 in the conventional cubic cell) —
the integer-coordinate hook is absent for all nine at this resolution (statement about the
denominator-48/16 grid inside the tested extents, not an impossibility proof). c/a lever:
only e598ffd8 admits a second denominator-<= 16 value (9/10) inside its band. FACT OF RECORD:
IT 76 / 144 / 169 are polar (every op fixes c), so a z-shift of the generating point
translates the orbit: z is a free coordinate, the z-ties in the tables are congruences, and
the effective search there is over (x, y, c/a); no (x, y, c/a) class was both SAME and
DIFFERENT (0 mixed, as congruence requires). FINDING ABOUT WALL_OPEN_PHASE2 (pre-registered
expectation was 0): 3,558 of 43,217 candidates changed type (0 quarantined), per cell 0 / 464 /
29 / 132 / 29 / 957 / 0 / 759 / 1188; EVERY one moved in two or more tested directions at once
(0 axis-parallel, also 0 with exactly one of (x, y, c/a) moved in the polar cells) — the
on-axis SAME extents held everywhere, so the OPEN verdicts stand as stated, but the PRODUCT
of per-axis intervals is not a type-constant box (walls are not axis-aligned). Consequence:
a chosen presentation is certified at its OWN (point, c/a) — done here for every SAME
candidate — never inherited from the witness verdict. OUTPUTS: harness/phase2/
NICE_POINTS_2026-09-04.json (sorted keys, no timings; per cell witness / best / top-3 with
exact site-centred vertices, scale histogram, changed-candidate list with the other type's
id, per-type counts) md5 cf6645fcbb96a530cbb71a2d20bb325a; the MD with pre-registration,
per-cell tables, tellable-coordinates paragraphs, type-changed section, Josehedron
comparison; per-cell full-row caches (vertices for all 39,659 SAME rows) in
harness/phase2/nice_points_cells/ (90 MB, regenerable; RECOMMEND not committing them —
main-session decision, no .gitignore edit made). DETERMINISM: three cells deleted from the
cache and recomputed -> cache files, JSON and MD byte-identical. RUNTIME: 1,046 s of chain
compute over 9 foreground batches (3 / 3 / 77 / 42 / 34 / 136 / 275 / 160 / 316 s), 8 forked
workers, load peaked ~14 on 16 cores, protected PIDs 8014 / 7417 / 13578 untouched; assembly 4
s. Wall sweep of all outputs: 0 hits. NOT DONE: git commit (main session; add by name:
harness/phase2/{nice_points_2026-09-04.py, NICE_POINTS_2026-09-04.json} and
paper_prep/MINT_plesiohedron/NICE_POINTS_2026-09-04.md; verify with git ls-files); no
outreach; no names; no renders.
MAIN-SESSION RE-RUN BEFORE ACCEPTANCE (exit 0 required; ~18 min fresh, 8 workers):
cd <repo>/harness/phase2 && rm -rf nice_points_cells && NICE_JOBS=8 nice -n 10 python3 nice_points_2026-09-04.py; echo exit $?; md5 -q NICE_POINTS_2026-09-04.json   # must print cf6645fcbb96a530cbb71a2d20bb325a

2026-09-04 (later 11; pointer entry appended 17:50 PDT by work-log agent #156, append-only; H4
STATUS-append duty): five accepted phase-2 results of this day have their full entries in sibling
files rather than here — (1) THE CATALOG v2 (#146, 1,583 types / 177 certified; catalog/STATUS.md
line 110; ledger 2026-09-04 14:35 est.), (2) BLIND RE-KEY of Schmitt's trigonal/hexagonal tables
(#147, 958 rows, 0 discrepancies, G5 re-key duty CLOSED for the hexagonal family;
SCHMITT_HEXAGONAL_REKEY_2026-09-04.md; ledger 13:55 est.), (3) CATALOG v3 (#150, open/wall
verdicts + Schmitt type status; pool 13 tetragonal + 102 hexagonal-family; catalog/STATUS.md line
227; ledger 15:40 est.), (4) TETRAGONAL STORE-SIDE S-CELL RULE + CATALOG v4 (#152, 177 COLLISION /
121 SURVIVOR / 106 UNRESOLVED over the 404 menu-sighted types; 14 certified survivors unchanged;
harness/COLLISION_PHASE2_RESULTS.md addendum; catalog/STATUS.md line 335; ledger 14:16 PDT),
(5) THE 62 UNSTORED TETRAGONAL PRINTED ROWS RECOMPUTED + CATALOG v5 (#154, 62/62 reproduce; 106
UNRESOLVED -> 24 COLLISION / 82 SURVIVOR / 0; tetragonal 201 / 203 / 0; pool unchanged; facts:
Schmitt's IT(95) (30,45,17) row at b=797/1000 IS the Laves-cell type 8c69db9e, his IT(137) (18,28,12)
row is the elongated-dodecahedron type; first report REJECTED for run-dependent md5s, corrected
(rule 30), accepted; COLLISION_PHASE2_RESULTS.md addendum + CORRECTION; catalog/STATUS.md lines
424/522; ledger 15:23-15:31 PDT). Tetragonal digitization remains single-keyed + text-layer
cross-checked (re-key duty owed); hexagonal digitization doubly keyed. Regime record:
control/FABLE51_WORK_LOG_2026-09-03_to_04.md.

2026-09-04 22:48 PDT (later 12; subagent #165, Claude Fable 5.1; PROVISIONAL until the main session
reviews the diff and re-compiles): *** SEVEN-SHAPE PAPER draft_v4 + CLAIMS AUDIT V4 + COLD REVIEW R3
+ SCI DATA DESCRIPTOR v2 + ZENODO MANIFEST/DESCRIPTION v2 *** on the main-session naming ruling
(Tyler delegated 22:19 PDT). draft_v4.tex written from draft_v3.tex by a replacement script with
one-match assertions (scratchpad make_v4.py, 36 edits; make_v4_r3.py, 3; W12 wording, 4); v3
untouched. CHANGES v3 -> v4: (1) abstract rewritten: two named cells, the Satchelhedron wall/parity
story with the cubic scope noun (grid reconstruction hedged as "the barycentric scheme that
reproduces his printed point counts exactly for three groups"; "at the grid size he used, nor at
any grid size with an odd denominator", NOT "at any budget"), the Ordenhedron open type, five
systematic labels, seven same-f instances, the census sentence; (2) intro: the two-track paragraph
replaced by the naming-rule paragraph (author's choice, stated as non-evidential; Koch exposure on
the same footing for named and labelled cells; ILL pending); the wall sentence reframed;
(3) "held" wording removed everywhere (headings, captions, Sec 5.5, 6, 7, 8, 10); H212/H230/H214
kept as letters ("labels only"); (4) Sec 5: type-identifier sentence (sha1[:16]); Sec 5.2:
tetragonal 134/141 (16,25,11) rows cited, closing paragraph reframed to the story, pentagon count
corrected (3 of 6, was "four of the five": CLAIMS F2); Sec 5.3: open-type certificate sentence;
Sec 5.4: "nine special + one general" (was "all at special positions": CLAIMS F1, P7 is 48l);
(5) Sec 8: seventh instance, (16,25,11) across systems (catalog/SATCHELHEDRON_TETRAGONAL_ROWS.md);
(6) NEW Sec 10 "A census beyond the cubic system" + Table 6 (numbers from catalog/STATUS.md v5,
catalog.json summary, PHASE2_RESULT/PHASE2_HEX_RESULT, G4_PHASE2*, COLLISION_PHASE2*, G2B/G2C,
WALL_OPEN_PHASE2.md aggregate): 68 + 52 groups; 148,816 / 294,772 and 108,580 / 212,912; 1,583 =
102 + 789 + 692 (404/385, 288/404); 1,476 + 958 rows; 203/201/0 and 151/124/13; 14 + 151 = 165
certified; 115/41/9; 35 heuristic disagreements; 40-of-41 / 36 non-simple facts; (20,36,18) wall
cell; 177 / 196 / 35 vs 38; 3,315 rows; (7) Data availability: [ZENODO-DOI] -> "DOI is minted at
deposit" + GitHub mirror URL; [A-NUMBERS] -> "A-numbers are assigned on approval (drafts staged)";
phase-2 and catalog files listed; (8) Disclosure -> house first-person form with the drafting
clause and "I take full responsibility" (REWRITE CONDITION comment kept); (9) bibliography:
orden2026methods "in preparation for submission" (no "mathai submitted" ledger line as of 22:20
PDT); zenodo entry without placeholder; new catalog + descriptor entries; (10) \texorpdfstring on
two headings (hyperref warnings gone); snapshot macro -> 2026-09-04; date -> Draft v4 of 2026-09-04.
TABLES: cd paper && python3 make_tables.py && python3 make_roundness_v3.py (exit 0, 0; git shows
no diff: byte-identical). COMPILE (scratch dir with ../publication symlinked): tectonic
--keep-logs draft_v4.tex -> 0 errors, 20 pages, 0 undefined, 0 overfull/underfull, 0 hyperref
token warnings; pdf md5 7de1578353176a602cd8d6b848c0e32d; 0 em dashes; tells 23 prose semicolons
/ 221 sentences, 24% The-openers. CLAIMS_AUDIT_V4.md: 101 claims, 99 PASS from v3, 2 FAIL (F1
Sec 5.4 special positions; F2 pentagon count), both FIXED in v4 -> 101/101; table identities
asserted by script (Euler, sum p = 2E, T*site = ops, isom = site, 4rho2 <= Dc^2, T*vol = detL,
D^2 >= 4rho2, slots = T*F, fixed(1) = T, fixed(2) = T*F/2, fixed >= one-sided >= free <= 2free);
FLAGGED: GitHub URL did not resolve (gh repo view, 22:26 PDT; #166 creating). REVIEW_COLD_R3.md:
verdict minor revision; APPLIED W1-W7 (any-budget overreach, abstract hedge, tetragonal
survivors 14-of-15 not 203, evaluation unit, type-id pointer, census table, IT(180) clause);
TYLER W8-W13 (names in the title; process sentences in Sec 10; prose density; Ordenhedron region
estimate; item 7 placement; Koch remark read; H-letter labels). DESCRIPTOR:
catalog/DATA_DESCRIPTOR_v2_SCIDATA_2026-09-04.md, title "Exact generating points and combinatorial
types of 1,583 plesiohedra from three crystal families" (96 chars, no colon/parenthesis), abstract
169 words (limit 170; counted by script), Sci Data headings, numbers from catalog v5, house
disclosure, Appendix A Acta Cryst A framing, Appendix B Zenodo-first recommendation kept.
ZENODO: publication/ZENODO_MANIFEST.md v2 section (items 6-15: what the refreshed zip must
contain; zip NOT built; #166 owns the public repo); ZENODO_DESCRIPTION.txt v2 block.
NAMING_DECISION_BRIEF: ruling-as-executed appended. NOT DONE (by rule): git commit (main session,
add by name: paper/{draft_v4.tex, CLAIMS_AUDIT_V4.md, REVIEW_COLD_R3.md},
catalog/DATA_DESCRIPTOR_v2_SCIDATA_2026-09-04.md, publication/{ZENODO_MANIFEST.md,
ZENODO_DESCRIPTION.txt}, NAMING_DECISION_BRIEF_2026-09-01.md, STATUS.md, PROVENANCE.md,
VERIFICATION_INDEX.md); no outreach; Tyler's rewrite precedes any submission. UNTESTED AGAINST:
Bernhard/Schmitt PDFs not re-opened (record-level items); no phase-2 computation re-run here;
arXiv TeX Live compile; the GitHub URL; a crystallographer's read of the Koch remark.
MAIN-SESSION CHECK: cd <repo>/paper && tectonic --keep-logs draft_v4.tex && grep -c "^!" draft_v4.log && pdfinfo draft_v4.pdf | grep Pages   # expect 0 and 20 (paper/ compiles in place because ../publication/ is present)
