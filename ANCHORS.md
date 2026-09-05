# MINT_plesiohedron — pre-registered gates (written BEFORE any computation, 2026-08-28)
House rule: anchors first; a gate FAILING quarantines everything downstream of it.

G0 REGRESSION (the pipeline must re-derive the known): the new harness, run on the
   josehedron generating orbit, must reproduce T=12, 12 facets per cell with
   p-vector 4 triangles + 8 quadrilaterals, |ops|=24 (12 proper), and tables
   semantically equal to paper_prep/SCI_OEIS_josehedron/data/josehedron_tables.json
   (same nbr multiset per type up to relabeling; enumerator on both gives identical
   fixed/free n<=6). FAIL => nothing else runs.
G1 SPACE-GROUP OPS EXACT: frozen spacegroups.json passes, for every group: identity
   present; exact closure under composition mod 1 (Fractions); inverses present;
   op count matches ITA order for the listed setting. Verified by an independent
   checker sharing no code with the generator. FAIL => freeze regenerated.
G2 CUBIC CONTROLS: sweep pipeline on Pm-3m general position must yield the cube
   Voronoi cell (P1-like orbit degenerations excluded); on the FCC/BCC lattice-only
   orbits it must yield rhombic dodecahedron / truncated octahedron by canonical
   code matching seeded catalog entries computed from published vertex data.
G3 EXACT-CONFIRMATION INVARIANT: no type enters the dedupe store as new without the
   exact-Fraction re-derivation agreeing with the float sighting (facet count,
   p-vector, canonical code). Degenerate flags route out per the design doc.
G4 FINALIST CERTIFICATE: any shape advanced toward naming/publication passes the
   paper-I-standard ladder (V0-V3 in HARNESS_DESIGN): exact re-derivation, tiling
   certificate verified by an independent adapted audit, symmetry certification
   (stabilizer over ALL orthogonal maps; Bravais point group of the actual lattice,
   NOT signed-perms), Burnside identity on its polyform counts.
G5 NOVELTY DILIGENCE (blocking for any public claim): checked against (a) seeded
   catalog incl. 5 parallelohedra + classical plesiohedra + josehedron, (b) Schmitt
   2016 ch.2 tables [TYLER GATE CLOSED 2026-08-28: PDF archived + primary read in
   SCHMITT_PRIMARY_READ_2026-08-28.md; diligence = f-vector diff vs his group table
   AND type-level diff vs his GitHub data (clone pending Tyler ok); note his ch.2 is
   sampling, not enumeration - absence there is evidence, not proof of novelty],
   (c) Engel 1981 tables [TYLER GATE: ILL - priority RECALIBRATED DOWN 2026-08-28,
   Schmitt confirms+corrects Engel's I4_132 results; ILL now optional, Tyler's
   call], (d) Bernhard Table 1 + Fig 12. Claim wording is measurement-framed:
   "not matched against catalog snapshot of <date>"; never "new to science".
   AMENDMENT 2026-08-28 (post-Schmitt-read): the "38 facets max" folklore is
   OBSERVED (351-CPU-year exact sampling), not proven - refereed record stays
   38<=max<=92 open. All our wording uses "observed max 38".
KILL CRITERIA (from LANDSCAPE_SCOUT): >38-face finding = assume bug until proven
otherwise; Schmitt-complete-and-contains-candidate => reframe to first-realization;
no public naming/announcement before G5; wall + disclosure rules apply throughout.

G2b - METRIC CONTROLS (pre-registered 2026-09-03, appended BEFORE any phase-2
   computation; existing text above untouched). Scope: the Gram-metric path
   (phase2/metric.py, phase2/sweep_voronoi_gram.py, phase2/exact_cell_gram.py -
   siblings, accepted modules unmodified). Design decision recorded up front:
   trigonal/hexagonal groups run in the ITA HEXAGONAL basis of the frozen ops
   (Gram [[1,-1/2,0],[-1/2,1,0],[0,0,(c/a)^2]], cleared to integers), NOT
   Schmitt's orthohexagonal C-centered basis - the Gram form makes his basis
   change unnecessary and keeps R integer; b-ratio = c/a = ||b3'||/||b1'|| as
   printed on his p.27. Assertions (exact arithmetic decides; float proposes):
   (a) HEXAGONAL PRISM: P6/mmm #191 origin orbit (Wyckoff 1a = hexagonal
       lattice), c/a in {1/2, 1, 2}: every case must give canon code ==
       seed_catalog.json hexagonal_prism, aut 24, f=(12,18,8), 0 non-simple
       vertices.
   (b) ELONGATED DODECAHEDRON: body-centered tetragonal lattice = origin orbit
       (2a) of I4/mmm #139 and of I4 #79 (Schmitt 2016 printed p.29 = PDF p.34,
       IT(79) rows: (18,28,12) at b-ratio 7/2 point (0,0,0); (24,36,14) at 1/2
       point (0,0,0)). Gram diag(1,1,(c/a)^2). c/a in {7/2, 2, 3/2} must give
       the seed elongated_dodecahedron code, aut 16, exactly 2 non-simple
       (4-valent apex) vertices; c/a in {1/2, 1, 7/5} must give the seed
       truncated_octahedron code, aut 48. Pre-derived threshold: the (0,0,+-c)
       facet of the BCT cell exists iff c/a < sqrt2 (c/a = sqrt2 is FCC), so
       7/5 and 3/2 bracket it; sqrt2 itself is irrational and not tested.
   (c) CUBIC SANITY: #221/#225/#229 origin orbits through the Gram path with
       G = I must give vertex sets, neighbor sets, p-vectors and canon codes
       IDENTICAL to exact_cell.clip_cell (non-Gram path) and matching the
       catalog (cube / rhombic dodecahedron / truncated octahedron).
   (d) SCHMITT TETRAGONAL ROWS (phase-2 analogue of schmitt_220_check; points
       in the space-group coordinate system, as his cubic points were): the
       exact cell at each printed (group, b-ratio, point) must have the printed
       f-vector. Rows: IT(75) P4 (10,15,7) b=1/2 x=(2825/5652,-1/5652,0)
       [PRIMARY]; IT(76) P4_1 (44,66,24) b=797/1000 x=(20/333,44/999,0);
       IT(77) P4_2 (28,42,16) b=1/2 x=(539/5652,-187/5652,0). All three
       required (printed p.28-29 = PDF p.33-34, visual read + text layer agree).
   (e) METRIC INVARIANTS on every cell above: R^T G R = G exactly for every op
       of the group used; float/exact agreement (facet count, p-vector,
       neighbor site sets) unless the float cell is degeneracy-flagged (then
       exact supersedes, recorded); the cutoff certificate 4*rho^2 <= D^2 held
       in the G-norm with the candidate block proven complete by the exact
       coordinate bound |x_i| <= D*sqrt((G^-1)_ii).
   FAIL on any required assertion quarantines phase 2 (no hunt sweep). No hunt
   sweep runs in this step regardless. Main session re-runs
   phase2/g2b_controls.py (exit 0 required) before acceptance.

G2c - HEXAGONAL-FAMILY CONTROLS (pre-registered 2026-09-04, appended BEFORE any
   batch-2 computation; existing text above untouched). Scope: phase 2 batch 2 =
   the trigonal + hexagonal groups (IT 143-194, 52 groups) through the SAME
   accepted Gram modules as batch 1 (phase2/metric.py, sweep_voronoi_gram.py,
   exact_cell_gram.py, unmodified) in the ITA HEXAGONAL basis of the frozen G1
   ops (rhombohedral groups on hexagonal axes, obverse setting, centering
   (0,0,0),(2/3,1/3,1/3),(1/3,2/3,2/3)); Gram = metric.gram_hexagonal(c/a) =
   [[2q^2,-q^2,0],[-q^2,2q^2,0],[0,0,2p^2]] for c/a = p/q; b-ratio = c/a
   = ||b3'||/||b1'|| as printed (Schmitt's hexagonal-section headers use the
   primed = ITA basis for this ratio). No trigonal/hexagonal group has two ITA
   origin choices (no origin-shift ambiguity in this family; the freeze's
   setting is the only one). Exact arithmetic decides; float proposes.
   POINT-CONVENTION HYPOTHESES (declared before the run; the gate records which
   one the exact chain confirms, and requires ONE convention for all rows):
     H1 (primary): Schmitt's printed generating points and reduced-domain
        vertices for IT 143-194 are coordinates in his orthohexagonal basis
        B'' = (2b1'+b2', b2', b3') (his App. B / Sec. 2.2.3: X = XB''->B' =
        [[2,0,0],[1,1,0],[0,0,1]], ops worked as (X^-1 A X, X^-1 a)); the
        conversion to the ITA basis is p' = X p'', i.e. x' = 2x'', y' = x''+y'',
        z' = z''. Reason recorded up front: his printed R143 vertices (1/6,0,0),
        (1/6,1/6,0) are, under H1, exactly the normalizer P6/mmm special points
        (1/2,0,0)_N and (2/3,1/3,0)_N in the basis he prints for it; under H0
        they are not special points of anything.
     H0 (alternative): printed points verbatim in the ITA basis (as his
        tetragonal points were, G2b(d)).
     b-ratio alternative (only if H1/H0 both fail at c/a = b): b =
        ||b3''||/||b1''|| = c/(sqrt3 a), i.e. (c/a)^2 = 3 b^2 (rational Gram
        [[1,-1/2,0],[-1/2,1,0],[0,0,3b^2]]).
     Second members of enantiomorphic pairs sharing one printed table
     (144/145, 151/153, 152/154, 169/170, 171/172, 178/179, 180/181): the
     printed point is run verbatim first; if the f-vector fails, z -> -z (the
     conversion that reproduced all rows of 95/96 in batch 1) is tried; the
     conversion used is recorded per row. FVEC-MISMATCH after both =
     quarantine, never patched.
   Assertions:
   (a) HEXAGONAL PRISM (re-run of G2b(a)): P6/mmm #191 origin orbit, c/a in
       {1/2, 1, 2} -> seed hexagonal_prism code, aut 24, f=(12,18,8), 0
       non-simple vertices. Must still pass.
   (b) RHOMBOHEDRAL LATTICE: R-3m #166 origin orbit on hexagonal axes (3 points
       per conventional cell, is_lattice must be True). Rhombohedral angle
       alpha vs c/a derived here: cos alpha = (c^2/9 - a^2/6)/(c^2/9 + a^2/3),
       so FCC (alpha 60 deg) at c/a = sqrt6 ~ 2.4495, simple cubic (90 deg) at
       c/a = sqrt6/2 ~ 1.2247, BCC (109.47 deg) at c/a = sqrt6/4 ~ 0.6124. All
       three are irrational, so each is BRACKETED by rationals and the
       parallelohedron code on each side is recorded (required: a seed-catalog
       parallelohedron on every side, identical on both sides of a bracket
       unless recorded otherwise):
         FCC bracket {12/5, 5/2}; SC bracket {6/5, 5/4}; BCC bracket {3/5, 5/8}.
       Prediction recorded (not required): truncated octahedron on both sides
       of the SC and BCC brackets; the FCC bracket may show rhombic
       dodecahedron for c/a > sqrt6 (12 relevant vectors: 6 in-plane + 3 + 3).
       GENERIC c/a in {1, 2, 3}: the code must be one of the seed-catalog
       parallelohedra {hexagonal_prism, elongated_dodecahedron,
       rhombic_dodecahedron, truncated_octahedron} (cube excluded: alpha = 90
       is irrational in c/a), identified by name in the result, with aut equal
       to the seed's, and STABLE: c/a +- 1/24 gives the same code. The
       elongated dodecahedron is predicted impossible here (its combinatorial
       aut 16 has no element of order 3, the site symmetry -3m has); if it
       appears the gate FAILS by the stab | aut rule.
   (c) SCHMITT TRIGONAL/HEXAGONAL PRINTED ROWS (points converted per the
       hypothesis that the gate confirms, one convention for all): the exact
       cell at (group, b, point) must have the printed f-vector. Required rows
       (text layer of references/Schmitt_2016_dissertation.pdf, Sec. 2.2.3-2.2.4,
       printed pp. 82-118 = PDF 87-123; visual cross-read in the digitization
       note):
         S143 IT(143) P3       (8,12,6)   b=3497/1000 (1/6, 0, 0)               PDF 88
         S147 IT(147) P-3      (10,15,7)  b=3497/1000 (33/100, -1/500, 0)       PDF 89
         S155 IT(155) R32      (48,73,27) b=797/1000  (-193/750, -53/250, 6/125) PDF 97
         S166 IT(166) R-3m     (38,58,22) b=527/1000  (-16/375, -16/125, 31/500) PDF 105
         S178 IT(178) P6_122   (64,96,34) b=163/200   (32/125, -19/125, 43/1500) PDF 114
              [his hexagonal-family maximum, 34 facets; also run in IT(179)
              with the enantiomorph rule above, conversion recorded]
         S194 IT(194) P6_3/mmc (18,30,14) b=797/1000  (1/3, 0, 1/4)             PDF 123
              [a special position under H1: (2/3,1/3,1/4)' on the 3-fold axis]
       All six required; the same convention must reproduce all six.
   (d) METRIC INVARIANTS on every cell above: R^T G R = G exactly for every op
       of the group used; the cutoff certificate 4*rho^2 <= D^2 in the G-norm
       with the candidate block complete by the exact coordinate bound; float/
       exact agreement (facet count, p-vector, neighbor site sets) unless the
       float cell is degeneracy-flagged (exact supersedes, recorded); Euler;
       one canonical code across the orbit cells clipped; site-stabilizer
       order divides the combinatorial aut order.
   FAIL on any required assertion quarantines batch 2 (no hexagonal sweep).
   Main session re-runs phase2/g2c_controls.py (exit 0 required) before
   acceptance. Kill criteria of the G2/G2b blocks apply verbatim (>38 facets
   = assume bug; "observed max 38", never proven; snapshot language only).

PERTURBATION CLASSIFICATION, PHASE 2 — pre-registered 2026-09-04 (appended BEFORE
   any run of harness/phase2/wall_open_phase2.py; existing text above untouched).
   PURPOSE: replace the heuristic open/wall LABELS carried on the 165 G4-certified
   phase-2 cells (TRIAGE_PHASE2_RESULT.md / TRIAGE_PHASE2_HEX_RESULT.md: open-likely /
   indeterminate / wall-suspect, derived from counts of stored b-ratios; and the
   three computed top-3 verdicts of COLLISION_PHASE2_RESULTS.md) by COMPUTED verdicts.
   SCOPE: the 14 tetragonal cells in the verdict-table order of
   harness/G4_PHASE2_RESULTS.md and the 151 hexagonal-family cells in the summary-
   table order of harness/G4_PHASE2_HEX_RESULTS.md, each at its stored FIRST WITNESS
   (group, point, b = c/a) in phase2_types.json (sha256 71685b9b...) and
   phase2_hexagonal_types.json (sha256 7494c7b2...), both READ-ONLY (sha256 asserted
   before and after). Pre-run facts from the stores: stratum dims tetragonal
   {1: 5, 2: 1, 3: 8}, hexagonal {0: 1, 1: 22, 2: 9, 3: 119}; c/a in [1/2, 11/4];
   81 of 165 witness cells carry nonsimple_vertices > 0.
   CHAIN (accepted, imported unchanged): sweep_phase2_tetragonal.evaluate for the
   tetragonal family, sweep_phase2_hexagonal.evaluate for the hexagonal family —
   orbit (frozen G1 ops) -> metric.gram_tetragonal / gram_hexagonal (R^T G R = G
   asserted) -> sweep_gram float PROPOSAL (W = 2, 3, 4 on the window guard) ->
   exact_cell_gram clip on the orbit representative (warm start; 4 rho^2 <= D^2
   certificate asserted; Euler asserted) -> canonical code; orbit-congruence check;
   G3 invariant: float/exact agreement (facet count, p-vector, neighbour set) or the
   float cell's degeneracy flag, in which case EXACT SUPERSEDES and float_superseded
   is recorded per perturbed cell. Kill criteria live (> 38 facets, float or exact).
   A ChainError (any reason) is a QUARANTINE row: recorded with its reason, never
   counted as SAME and never as DIFFERENT.
   DIRECTIONS (exact rationals throughout):
   (i) POINT, within the witness stratum: tangent basis = primitive integer basis of
       the nullspace of {R - I : (R, t) in the site stabilizer} by the row reduction
       of c1_wall_open.nullspace_basis (deterministic order; asserted to have the
       stored stratum_dim vectors). Fixed Wyckoff point (dim 0): point direction NOT
       APPLICABLE, recorded as such. Line (dim 1): the one free direction; plane
       (dim 2): two independent directions; general (dim 3): three. Steps delta in
       {-1/48, -1/96, +1/96, +1/48} in fractional coordinates of the ITA conventional
       cell (the hexagonal basis of the frozen ops for IT 143-194) along each basis
       vector — the cubic round's steps verbatim. REFINEMENT (c1 verbatim): on any
       side whose smallest step is not SAME the step is halved repeatedly down to
       1/1536; the verdict on that side uses the smallest step tested.
   (ii) METRIC: c/a -> c/a * (1 + eps), eps in {-1/96, -1/192, +1/192, +1/96} at the
       witness point (relative steps, so the Gram matrix stays a rational function of
       the witness b); refinement halving to eps = 1/3072. The verdict step 1/192
       relative is <= 1/96 absolute for every cell with c/a <= 2 (163 of 165); for the
       two cells with c/a > 2 (11/4 and 65/32) it is 11/768 and 65/6144 — stated, not
       hidden. (The top-3 tetragonal round used ABSOLUTE b-steps 1/96, 1/48; the two
       schemes coincide at c/a = 1.)
   VERDICTS. Side status at the finest step tested: SAME (canonical code == the
   store's) / DIFFERENT / QUARANTINE. A direction is WALL when both of its sides are
   DIFFERENT. POINT verdict over the point directions and METRIC verdict over the
   metric direction, each by c1_wall_open.py lines 103-109: OPEN = every side SAME;
   WALL = some direction WALL; ONE-SIDED = otherwise (some side DIFFERENT, no
   direction on both sides); point verdict "n/a" at dim 0. COMBINED verdict (the
   classification that replaces the label) over ALL applicable directions together
   (point basis + metric): OPEN = the canonical type is unchanged under every
   perturbation of the scheme; WALL = the type changes on both sides in some
   direction (the witness sits on a transition); ONE-SIDED = some side changes but no
   direction on both sides; INDETERMINATE = any side ends in QUARANTINE. OPEN means
   "holds on the tested neighbourhood", never an interval proof.
   FLAGS (recorded, never verdict inputs): LINE-ISOLATED — c1 names only OPEN / WALL
   / ONE-SIDED (no such term exists in the folder, grep 2026-09-04), so it is defined
   here before the run: stratum dim 1 AND the single point direction is WALL, i.e.
   the type occurs at an isolated point of its Wyckoff line at the witness metric
   (the Satchelhedron pattern of c1, verdict WALL on the 24d line). NON-SIMPLE-VERTEX
   — nonsimple_vertices > 0 in the exact witness cell (a vertex with > 3 incident
   facets is a degenerate Voronoi vertex that a generic perturbation resolves);
   recorded at the witness and for every perturbed cell. STAB-CHANGE — a perturbed
   point whose site-stabilizer order differs from the witness's (the step landed on
   a special point of the stratum); recorded.
   NEIGHBOUR BOOKKEEPING (the naming-relevant fact): every DIFFERENT perturbed cell
   is named by (f-vector, p-vector, aut, non-simple count) and its stored id = the
   canonical code looked up in the union of the two phase-2 stores (the hexagonal
   store contains every tetragonal-store type including the 102 cubic seeds —
   checked), else "not stored"; type-level Schmitt status = the stored type has a
   pass-P2 sighting (kind schmitt_printed: Schmitt's printed representative cell
   reproduced by the chain at his printed (group, b, point)), reported with the
   group(s); f-vector-level status = f printed in the witness group's table of the
   accepted digitizations (schmitt_tetragonal_tables.json / schmitt_hexagonal_
   tables.json; enantiomorphic pairs share one table). Snapshot wording only ("not
   matched against the records checked as of 2026-09-04"); no naming; no store write.
   AGREEMENT RULE (heuristic label class vs COMBINED verdict): agree iff
   (open-likely, OPEN) or (wall-suspect, WALL) or (carried OPEN, OPEN) or (carried
   WALL/THIN BAND, WALL); indeterminate labels are "n/a"; every other combination is
   a disagreement and is listed cell by cell.
   REGRESSION (asserted): the POINT verdicts of the three top-3 tetragonal cells
   must equal COLLISION_PHASE2_RESULTS.md (4e9c9b076cfec323 OPEN; 49cedbdd58376fac
   WALL with wall direction (1, 1, 0); f654982d74d740f6 OPEN) — same steps, same
   chain. Their METRIC verdicts are compared and reported, not asserted (relative vs
   absolute steps).
   DETERMINISM: per-cell results are pure functions of (stored witness, scheme);
   WALL_OPEN_PHASE2.json is written with sorted keys and NO timings; a second full
   run must reproduce it byte for byte (md5 stated in the results doc). Execution:
   <= 8 forked workers, foreground batches (rule 29), per-cell record files
   harness/phase2/wall_open_cells/<id>.json for resume at a clean boundary; timings
   go to the .md only.
   CORRECTION 2026-09-04 (post-run, factual pre-run count only; the scheme above is
   unchanged and was run as written): FIVE certified cells have c/a > 2, not two —
   30f2a1e483babf55 (11/4), d176b8d859dd651a (5/2), d1f1121757598de0 (9/4),
   4b6055c7aa3d341b (17/8), 11a9fe078850b5cd (65/32); for them the relative verdict
   step 1/192 is 11/768, 5/384, 3/256, 17/1536, 65/6144 absolute (between 1/70 and
   1/95). 160 of 165 cells have c/a <= 2. Recorded in WALL_OPEN_PHASE2.md.
