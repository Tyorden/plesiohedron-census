# PUBLICATION_STATUS — the seven finalists (packaged 2026-09-01)

Built by `publication/build_packages.py` (exit 0, deterministic; every derived
number re-asserted against `harness/phase1_types.json`, the banked
`g4_tables_*.json`, and the accepted n<=4 counts of `harness/G4_RESULTS.md` at
build time). Names per Tyler's greenlit two-track decision
(`NAMING_DECISION_BRIEF_2026-09-01.md`, option A with personal names).
Language rule, stated once for this whole tree: every shape is "not matched
against the records checked as of 2026-09-01"; survival of every printed
representative is evidence, never proof; "new to science" appears nowhere.
**Main session re-verifies before anything here is called ready.**

## Per-shape status

| package | id | IT / f-vector | status | roundness | counts | OEIS drafts |
|---|---|---|---|---|---|---|
| `8cf50403_Satchelhedron` | `8cf50403cf88c455` | 220, (16,25,11) | **PUBLISHABLE-NOW, named (Satchelhedron)** | 37.7554% | n<=6, Burnside-verified n<=6 | 3 (fixed/one-sided/free) |
| `2de0a211_Ordenhedron` | `2de0a21129cabe90` | 201, (20,33,15) | **PUBLISHABLE-NOW, named (Ordenhedron)** | 9.8394% | n<=6 (Burnside n<=4; see counts.md) | 3 |
| `c4ea3f32_Pn3m_11facet` | `c4ea3f32fdd6dc51` | 224, (14,23,11) | **PUBLISHABLE-NOW, name pending Tyler** | 10.7278% | n<=6, Burnside-verified n<=6 | 3 |
| `f98a3ee5_Pn3m_7facet` | `f98a3ee5675fc121` | 224, (10,15,7) | **PUBLISHABLE-NOW, name pending Tyler** | 4.9197% | n<=6, Burnside-verified n<=6 | 3 |
| `ceb70631_IT212_37-57-22_HELD` | `ceb70631e274e727` | 212, (37,57,22) | **HELD — Engel/Koch ILL** (do NOT name) | 28.9090% | n<=6 (free = one-sided: chiral honeycomb) | none by design |
| `359beee8_IT230_40-61-23_HELD` | `359beee832567a71` | 230, (40,61,23) | **HELD — Engel/Koch ILL** (do NOT name) | 23.5573% | n<=6 | none by design |
| `aa6b0077_IT214_30-47-19_HELD` | `aa6b0077c3234d24` | 214, (30,47,19) | **HELD — Engel/Koch ILL** (do NOT name) | 11.1503% | n<=6 (free = one-sided: chiral honeycomb) | none by design |

Roundness control: the Josehedron through the same exact pipeline gives
47.9833% vs Bernhard's printed ~47.98% — metric convention confirmed
(`ROUNDNESS.md`). No finalist beats his record; it stands on the snapshot
record.

## What exists per package

`COORDS.md` (generating group/point, site data, scaled orbit, exact Fraction
vertex coordinates + facet cycles + neighbor sites, f/p/aut/site/geometric
stabilizer, chirality status, certificate + diligence statements) ·
`render.png` (p-vector asserted before rendering) · banked
`g4_tables_<id>.json` + `.txt` (byte-copied) + `_proper.txt` export ·
`counts.md` (fixed/free/one-sided n<=6 via the banked A398957 enumerator;
n<=4 prefixes asserted == accepted G4; internal identities checked; Burnside
n<=6 where the growth enumerator fit the cap — Satchelhedron and both Pn-3m
cells). Publishable-four packages additionally: `oeis_draft_{fixed,onesided,
free}.txt` + `oeis_afile.txt` (12 drafts total — DRAFTS ONLY, Tyler sequences
slots per `OEIS_DRAFTS_NOTE.md`).

Top level: `ROUNDNESS.md` · `ILL_REQUEST_STAGED.md` (ready-to-send text,
exact Engel 1981 I+II and Koch 1972/73 citations from the archived Schmitt
bibliography) · `ZENODO_MANIFEST.md` (deposit packing list; SWHIDs referenced
not re-deposited; wall check performed — no sensitive content) ·
`PAPER_OUTLINE.md` (the one seven-shape paper, section-by-section source map)
· `build_summary.json` (machine-readable counts + roundness).

## What remains (all operator / Tyler)

1. **Send the ILL requests** (`ILL_REQUEST_STAGED.md`) — unblocks the three
   held shapes' naming decision on return.
2. **Choose names (or keep descriptive) for the two IT(224) cells**; update
   the OEIS NAME lines + package titles if personal names are chosen.
3. **Sequence OEIS submissions** (5-slot limit; wave-gamma already staged) —
   per shape: fixed first (hosts the program), then one-sided, then free;
   run the existence search per draft first.
4. **Optional before OEIS submission:** an independent second-implementation
   verification of the n = 5..6 terms for the shapes where the Python growth
   check exceeded the cap (Ordenhedron and the three held shapes) — the
   Josehedron bar was two independent implementations at every published
   term.
5. **Zenodo deposit** per `ZENODO_MANIFEST.md` (Tyler pushes; license lines
   confirmed at deposit time), then the paper per `PAPER_OUTLINE.md` with
   Tyler's prose rewrite (house rule).
6. **Main-session re-verification** of this build: re-run
   `publication/build_packages.py` (exit 0 required; deterministic except
   wall-clock notes) before any of it is called ready.
