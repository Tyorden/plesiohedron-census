# PAPER_OUTLINE — "Certified space-filling polyhedra from a gated agentic search" (staged 2026-09-01)

One paper, seven shapes. Stronger than seven notes
(`NAMING_DECISION_BRIEF_2026-09-01.md` §"What publication looks like");
feeds the MATH-AI/HDSR arc. House rules bind: Tyler rewrites all prose from
memory before submission; AI-disclosure standard; snapshot language
everywhere ("not matched against the records checked as of 2026-09-01");
"observed max 38" for the facet folklore; NEVER "new to science".

Presentation split (Tyler's greenlit two-track decision):
- Presented fully, with names: **Satchelhedron** (IT 220, (16,25,11)),
  **Ordenhedron** (IT 201, (20,33,15)), and the two IT(224) cells
  (descriptive names — "the Pn-3m 11-facet cell", "the Pn-3m 7-facet cell" —
  pending Tyler's choice).
- Presented as certified-but-diligence-pending, systematically described,
  explicitly NOT named: the IT(212) (37,57,22), IT(230) (40,61,23), and
  IT(214) (30,47,19) cells (Engel/Koch ILL check outstanding —
  `publication/ILL_REQUEST_STAGED.md`).

## Section skeleton (with the banked doc that feeds each section)

1. **Introduction: the hunt and the honesty problem.** Bernhard's Josehedron
   as precedent and provocation (he explicitly invites follow-ups by "a
   creative LLM-based agent" — `PROVENANCE.md`); why "new shape" claims in
   this field are epistemically fragile (print-only catalogs, an
   unrecoverable 14 TB survey); our answer: pre-registered gates + exact
   certificates + measured diligence language.
   Feeds: `PROVENANCE.md`, `LANDSCAPE_SCOUT_FABLE5_2026-08-27.md`,
   `ANCHORS.md`.

2. **Setup: plesiohedra, Dirichlet stereohedra, and the cubic corridor.**
   Definitions; the record landscape (Engel's 38-facet cell; refereed bound
   38 <= max <= 92 open; Schmitt's 3,315 types from 351 CPU-years of exact
   grid sampling — a sampling, not an enumeration).
   Feeds: `SCHMITT_PRIMARY_READ_2026-08-28.md`,
   `LANDSCAPE_SCOUT_FABLE5_2026-08-27.md`.

3. **The gated harness.** Pre-registered gates G0–G5 written before any
   computation; frozen exact space-group data (G1) with the independent
   2016-lineage confirmation (Schmitt's own ops, zero discrepancies);
   pipeline regression on the Josehedron (G0) and classical controls (G2);
   floats propose / Fractions decide; the degenerate-flag routing.
   Feeds: `ANCHORS.md`, `HARNESS_DESIGN_FABLE5_2026-08-27.md`,
   `harness/G0_RESULT.md`, `G1_RESULT.md`, `G2_RESULT.md`,
   `SCHMITT_OPS_XCHECK_2026-08-28.md`, `MINT_TABLES_RESULT.md`.

4. **The sweep and the funnel.** All 36 cubic groups, 1,597 orbits, 102
   stored types; triage; the Schmitt collision screens (sighted-group and
   cross-group, 76 printed representative points recomputed exactly,
   two-origin setting recovery); the funnel 95 -> 11 -> 7. Side finding worth
   a box: the pipeline independently rediscovered the diamond cell (triakis
   truncated tetrahedron) and the screen correctly identified it — a free
   end-to-end validation.
   Feeds: `harness/PHASE1_RESULT.md`, `TRIAGE_RESULT.md`,
   `SCHMITT_COLLISION_RESULTS.md`, `CROSS_GROUP_RESULTS.md`,
   `SCHMITT_220_CHECK_RESULT.md`.

5. **Certificates (the unconditional part).** The V0–V3 ladder per finalist:
   exact re-derivation; tiling certificate proven twice (independent adapted
   audit); symmetry over ALL orthogonal maps (no signed-perm assumption);
   Burnside identity on polyform counts. Table of the seven with f-vectors,
   p-vectors, aut/site/geometric-stabilizer chains, |ops|, chirality.
   Feeds: `harness/G4_RESULTS.md`, per-shape `COORDS.md` + `render.png`
   (figures), `harness/g4_tables_*.json`.

6. **The four presented shapes.** One subsection each: Satchelhedron (the
   pentagon-dominant 11-hedron in the Josehedron's own group, f-vector absent
   from Schmitt's ENTIRE printed cubic survey — the strongest absence signal
   in the hunt); Ordenhedron (tiles with NO symmetry of its own — site =
   stab = aut = 1 — under a 24-op honeycomb group); the two Pn-3m cells (the
   group the survey visibly under-covers: 8 printed f-vectors vs 18 types
   found here). Exact coordinates, renders, roundness, polyform sequences
   (n <= 6) with OEIS cross-refs.
   Feeds: per-shape packages, `publication/ROUNDNESS.md`,
   `G5_DILIGENCE_2026-08-30.md` (per-shape verdict table).

7. **The three held shapes.** Same certificates, presented as
   certified-but-diligence-pending: their groups (212/214/230) are exactly
   Engel's and Koch's hand-mined ground and those catalogs are print-only;
   the ILL check is filed/pending; no names until it returns. This section
   IS the paper's thesis in action: the certificates are unconditional, the
   novelty language is scoped to what was actually checked.
   Feeds: `NAMING_DECISION_BRIEF_2026-09-01.md`,
   `publication/ILL_REQUEST_STAGED.md`, `SCHMITT_PRIMARY_READ` (Engel/Koch
   corrections), held-shape packages.

8. **Diligence and its limits (the measurement-framing section).** What was
   checked (Schmitt printed tables incl. 76-point exact recomputation +
   independent re-key of the six hosting-group tables; Bernhard's printed
   data; classical lists) and what CANNOT currently be checked by anyone
   (the ~14 TB, the print-only catalogs pre-ILL); absence-as-evidence,
   never proof; the same-f-vector-distinct-type micro-facts (>= 10 banked)
   as a caution against f-vector-level identification.
   Feeds: `G5_DILIGENCE_2026-08-30.md`, `CROSS_GROUP_RESULTS.md`,
   `SCHMITT_DATA_RECOVERY_2026-08-28.md`.

9. **Roundness.** Bernhard's own metric, control-reproduced (47.98%);
   the seven finalists' values; verdict on his record per
   `publication/ROUNDNESS.md` (snapshot wording).

10. **Methods-as-contribution + disclosure.** The gated agentic workflow
    (agents propose, gates decide, main session re-verifies, operator-error
    catches on the record); full AI-disclosure per house standard;
    reproducibility pointer to the Zenodo deposit
    (`publication/ZENODO_MANIFEST.md`).

Appendices: A. exact coordinates for all seven (from `COORDS.md`); B. the
V0–V3 ladder specification; C. polyform count tables + Burnside details;
D. the Schmitt setting-conversion (origin-choice shifts, orthohexagonal
basis) as a small independently useful note.

## Venue ladder

arXiv math.MG (needs endorsement — Tyler's existing channel) with Zenodo DOI
as the data anchor; the methods story doubles as a MATH-AI workshop
submission per the program plan. Double-anon rules do not bind here (this is
not the SVU paper), but Tyler's rewrite-before-submission rule does.

## What blocks a full draft today

1. Tyler's naming confirmation for the two IT(224) cells (descriptive vs
   personal names).
2. The ILL return for section 7's endnote (or an explicit decision to
   publish with the hold stated — the outline works either way).
3. Tyler's prose rewrite (house rule; this outline and all package text are
   staging material, not submission text).
