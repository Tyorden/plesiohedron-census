# MINT program plan — shapes, papers, catalog, naming (Fable 5, 2026-08-27)
Synthesis of LANDSCAPE_SCOUT + HARNESS_DESIGN (both in this folder). Status: planning;
build gated on Tyler's two diligence steps (Schmitt PDF download; Engel 1981 ILL) + go.

## The open space (from the scouts, one line each)
- No machine-readable catalog of plesiohedron combinatorial types exists ANYWHERE.
- Engel 1981: print-only, symmorphic cubic groups only; "172 types" is secondhand.
- Schmitt 2016 dissertation: closest modern catalog (tet/trig/hex/cubic); unread by us.
- Refereed max-facet bound: 92; realized: 38; consensus (unrefereed) says 38 is max.
- Bernhard processed ~14 of ~45 named TPMS; explicitly invites follow-ups, incl. by AI agent.
- OEIS: Kagey-Dobbelaere polyform series active; Laves-graph-17 and Engel-38 polyforms UNCLAIMED.

## Track 1 — the mint (headline)
Voronoi plesiohedron from the FISCHER-KOCH Y extremal points (fallback: C(Y), Neovius-complement).
Bernhard's exact route + the diligence he skipped (space group identified, Schmitt/Engel checked).
Paper: short note, Zenodo DOI + arXiv (math.MG/cs.CG). NAMING IS TYLER'S — precedent explicitly
celebrates it (Josehedron = his daughter Josefine; "looking at you, gyrobifastigium").
Worst case after diligence: type exists unnamed in a catalog table -> reframe as first
geometric realization + naming; still publishable, still named by Tyler.

## Track 2 — combinatorics of the mint (the differentiator)
Day-one polyform sequences (fixed/one-sided/free) for the new shape via the existing
pipeline -> 3 authored OEIS entries citing OUR shape paper. Bernhard's paper has no
combinatorics; ours ships with its own. Either §2 of the mint note or a companion.

## Track 3 — THE CATALOG (biggest claim in the space)
The sweep harness's dedupe store IS a catalog: first machine-readable census of
plesiohedron combinatorial types (per type: canonical code, F/V/E, p-vector, exemplar
coordinates, space group(s), certificates). Reconcile against Schmitt ch.2 + Engel tables.
Publications: data paper (Zenodo dataset + descriptor; venues to scout: Acta Cryst A?,
Discrete Analysis data?, JOSS for the harness software). Measurement framing per house
rules: "types found by sweep X against catalog snapshot Y" - never "all types".
This also feeds HDSR (the verification-ladder story at catalog scale).

## Track 4 — quick OEIS wins with existing pipeline (no mint needed)
Polyforms of: (a) the 17-face Laves-graph plesiohedron (P4132-family, TPMS-native),
(b) Engel's 38-face cell (vertex data reconstructible from Pegg's Wolfram notebook).
Each = 2-3 authored sequences, Kagey-Dobbelaere-adjacent, citable in Tracks 1/3.

## Track 5 — extremal records (opportunistic)
Roundness: Josehedron holds 47.98% (beatable benchmark; compute for every swept type).
Max faces: any >38 realization would contradict the Schmitt consensus - treat as a
CHECK on our sweep (finding one means a bug until proven otherwise), not a goal.

## Naming inventory (Tyler's)
The minted shape(s); the catalog itself; any new-record holder. House rule: name after
verification passes, never before.

## Order of operations
1. [TYLER] Schmitt PDF (browser, free) -> I read ch.2 tables. 2. [TYLER] Engel 1981 ILL.
3. [go] Build harness (josehedron regression first). 4. Cubic sweep -> candidates.
5. FKY targeted run. 6. Diligence -> mint note -> Tyler names -> Zenodo/arXiv.
7. Polyform runs -> OEIS. 8. Catalog reconciliation -> data paper. Track 4 anytime.
