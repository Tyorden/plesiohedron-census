# ILL requests — STAGED, ready to send (2026-09-01)

Purpose: the two print-only prior catalogs that motivate HOLDING the three
mined-group finalists (IT 212, 214, 230) before naming them
(`NAMING_DECISION_BRIEF_2026-09-01.md`, two-track option A, greenlit by Tyler).
Schmitt 2016 confirms-and-corrects both works (he found coordinate errors in
Koch–Fischer and mistakes in Engel's Abb. 3, per
`SCHMITT_PRIMARY_READ_2026-08-28.md`), which cuts both ways: they are real
prior catalogs AND unreliable ones — hence primary reads before personal
names in their mined ground.

Exact citations (transcribed from the bibliography of the archived
`references/Schmitt_2016_dissertation.pdf`, cross-checked against
`LANDSCAPE_SCOUT_FABLE5_2026-08-27.md` for Eng81a's DOI):

1. **[Eng81a]** Peter Engel, "Über Wirkungsbereichsteilungen von kubischer
   Symmetrie," *Zeitschrift für Kristallographie* **154**, no. 3-4 (1981),
   pp. 199–215. doi:10.1524/zkri.1981.154.3-4.199 (De Gruyter/Oldenbourg;
   paywalled, print-only in practice).
2. **[Eng81b]** Peter Engel, "Über Wirkungsbereichsteilungen von kubischer
   Symmetrie. II. Die Typen von Wirkungsbereichspolyedern in den symmorphen
   kubischen Raumgruppen," *Zeitschrift für Kristallographie* **157**, no. 3-4
   (1981), pp. 259–275. doi:10.1524/zkri.1981.157.3-4.259 (title, issue and
   pages verified on Crossref 2026-09-03; a volume-level duplicate record
   gives 259-276, resolved in favour of the issue-level record). NOTE: the
   subtitle says part II covers the SYMMORPHIC cubic groups; all six groups of
   the seven finalists (201, 212, 214, 220, 224, 230) are non-symmorphic, so
   part II bears on none of them by its title, and the exposure rests on part
   I (scope unknown) and Koch. (Part II — Schmitt's per-group remarks cite it for
   most cubic groups; request it WITH part I, same journal volume year.)
3. **[Koc72]** Elke Koch, "Wirkungsbereichspolyeder und
   Wirkungsbereichsteilungen zu kubischen Gitterkomplexen mit weniger als
   drei Freiheitsgraden," PhD thesis, Universität Marburg, 1972.
   (Published digest of the same material, if the thesis loan fails:
   [Koc73] same title, *Z. Kristallographie* **138** (1973), pp. 196–215.)

## Ready-to-send request text (LA public library / university ILL form)

> Hello — I would like to request the following three items via interlibrary
> loan (scans of the cited pages are fine where lending is not possible):
>
> 1. Engel, Peter. "Über Wirkungsbereichsteilungen von kubischer Symmetrie."
>    Zeitschrift für Kristallographie 154 (1981), no. 3-4, pages 199-215.
>    DOI: 10.1524/zkri.1981.154.3-4.199.
> 2. Engel, Peter. "Über Wirkungsbereichsteilungen von kubischer Symmetrie.
>    II. Die Typen von Wirkungsbereichspolyedern in den symmorphen kubischen
>    Raumgruppen." Zeitschrift für Kristallographie 157 (1981), no. 3-4, pages
>    259-275. DOI: 10.1524/zkri.1981.157.3-4.259.
> 3. Koch, Elke. "Wirkungsbereichspolyeder und Wirkungsbereichsteilungen zu
>    kubischen Gitterkomplexen mit weniger als drei Freiheitsgraden." PhD
>    thesis (Dissertation), Universität Marburg, 1972. If the thesis cannot
>    be lent, the journal version suffices: Koch, Elke, same title,
>    Zeitschrift für Kristallographie 138 (1973), pages 196-215.
>
> I need the tables/plates listing space-filling polyhedra (Dirichlet
> domains / Wirkungsbereiche) for the cubic space groups — in particular
> anything covering groups P4_332, P4_132, I4_132, I-43d, and Ia-3d
> (international numbers 212, 213, 214, 220, 230). I am an independent
> researcher checking new computational results against these historical
> catalogs. Thank you.

## What to check when the copies arrive (the HELD-shape gate)

Per held finalist, diff its certified data against every plate/table row for
its group (and the enantiomorphic partner group for 212/213):

| held finalist | group | f-vector | p-vector | aut |
|---|---|---|---|---|
| `ceb70631e274e727` | IT(212) P4_332 (+ 213 partner) | (37,57,22) | 3^6 4^6 5^6 10^3 12^1 | 3 |
| `359beee832567a71` | IT(230) Ia-3d | (40,61,23) | 4^20 11^2 20^1 | 4 |
| `aa6b0077c3234d24` | IT(214) I4_132 | (30,47,19) | 3^4 4^5 5^6 6^2 10^2 | 2 |

The bar: f-vector first; on any f-vector hit, face-type multiset; on any
remaining ambiguity, rebuild the plate's cell from its printed generating
data through the exact pipeline and compare canonical codes (the
`schmitt_collision_check.py` pattern). Also REQUIRED while the volumes
are open (round-1 finding, 2026-09-03, harness/round1_computations/RESULTS.md):
the Satchelhedron's line 24d of IT(220) (it is a WALL type at x = 0 between two
open (22,35,15) types, i.e. exactly the kind of transition point a hand
parameter study of a one-parameter position records, and Koch's title scope
covers positions with fewer than three degrees of freedom) and the Pn-3m
11-facet cell's 2-dof position 24k of IT(224). Check rows: S (16,25,11)
3^2 4^1 5^8 aut 4; P11 (14,23,11) 3^4 4^4 6^3 aut 2.

Outcome rules (pre-registered here): a match => that shape reframes to
first-explicit-realization per the ANCHORS kill criteria and is NOT named
personally; no match => the diligence statement extends to "including
Engel 1981 I+II and Koch 1972/73 primary reads" and naming may proceed.

Status: STAGED — not sent. Sending is Tyler's action (his library accounts).
