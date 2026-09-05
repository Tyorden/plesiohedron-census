# Schmitt 2016 trigonal + hexagonal tables — digitization (2026-09-04)

Source: `references/Schmitt_2016_dissertation.pdf`, Section 2.2.3 "Trigonal groups"
(printed pp. 81–100) and Section 2.2.4 "Hexagonal groups" (printed pp. 101–118),
PDF pages 86–123 (PDF page = printed + 5). Output:
`harness/schmitt_hexagonal_tables.json` (same schema as
`harness/schmitt_tetragonal_tables.json`: per-block entries with header facts,
page citation per block and per row). Script: `harness/digitize_schmitt_hexagonal.py`
(deterministic; re-run reproduces the file).

## Method — what this is and is not

- **Text layer primary.** `pdftotext -layout` of PDF pp. 86–123, rows parsed with the
  same regular expression as the batch-1 harvest (`(V, E, F) | b-ratio | (x, y, z)`),
  Euler V − E + F = 2 asserted on every row while writing. Block header facts
  (normalizer + basis, reduced-domain vertices, upper bound with citation, lower-bound
  remark, b-range/steps, grid size) parsed from the same text layer; the normalizer
  bases' fraction glyphs (the text layer prints 2/3 as "32" or "23", 1/2 as "12" or
  "21") are normalized as min/max of the two digits — every such fraction is in (0,1) —
  and the raw metrical-parameters sentence is kept verbatim in
  `metrical_parameters_text`.
- **Visual cross-read (this session, Fable 5.1).** Rendered pages (`pdftoppm -r 120`)
  PDF **88, 97, 105, 114, 123** were read as images and compared row by row against
  the text-layer parse: every f-vector, b-ratio and generating point on those pages
  (**153 rows**: IT 143 ×2, 144/145 ×9, 155 ×40 [p. 97 part], 166 ×26 [p. 105 part],
  167 ×5, 178/179 ×41 [p. 114 part], 193 ×14, 194 ×16) plus the block headers printed
  there (R143, R144, R146, R156, R167, R194, the 180/181 normalizer remark). Also
  read visually (headers/conventions, not rows): PDF 87 (Sec. 2.2.3 basis-change
  text), PDF 176–177 (App. B). **Result: 0 discrepancies** between the visual read
  and the text layer on those rows.
- **Not a second independent re-key.** One machine parse cross-read by one reader on
  a 16% row sample (153/958). A second independent re-key (different agent/person, no
  access to this file) remains a **G5 duty for any group hosting a finalist**, as for
  the cubic and tetragonal tables.
- Rule followed: transcribe what is printed; nothing inferred. Points are stored **as
  printed** (Schmitt's orthohexagonal basis B'', see Conventions); the conversion is a
  documented, gate-confirmed step downstream, not an edit of the digitized data.

## Coverage

| item | count |
|---|---|
| Space groups covered | IT(143)–IT(194), all 52 |
| Printed table blocks | 45 (seven enantiomorphic pairs print ONE table each: 144/145, 151/153, 152/154, 169/170, 171/172, 178/179, 180/181) |
| Rows transcribed | **958** (f-vector, b-ratio, generating point; PDF page per row) |
| Header facts per block | normalizer + basis (text-layer normalized), reduced-domain vertices, upper bound (with citation), lower-bound remark if printed, b-ratio range/steps, grid size, raw metrical-parameters sentence |
| Frequency column | **none printed in any trigonal/hexagonal table** (as in the tetragonal tables); `freq` is `null` throughout |
| Distinct printed b-ratios | 38 (3497/1000: 443 rows, 797/1000: 245, 4/5: 99, 7/2: 41, 1/2: 38, 527/1000: 21, 2: 15, 5/4: 12, then 7/8, 7/5 (4 each), 163/200, 13/5 (3), ...) |
| Max facets in the family | **34** — IT(178/179) (64, 96, 34) at b = 163/200, point (32/125, −19/125, 43/1500), PDF 114 |
| Pages | PDF 86–123; PDF 124 confirmed to start Sec. 2.2.5 Cubic (IT(195)) |

Rows per block (block: rows): 143:2, 144/145:9, 146:19, 147:13, 148:63, 149:5, 150:13,
151/153:29, 152/154:64, 155:89, 156:3, 157:3, 158:4, 159:9, 160:17, 161:17, 162:8,
163:22, 164:11, 165:23, 166:60, 167:84, 168:4, 169/170:16, 171/172:34, 173:8, 174:2,
175:4, 176:23, 177:5, 178/179:97, 180/181:69, 182:30, 183:3, 184:4, 185:7, 186:8,
187:3, 188:8, 189:3, 190:23, 191:3, 192:7, 193:14, 194:16.

Header facts worth knowing for phase-2 use:
- Grid sizes: 1 000 405 (2-D reduced domains, normalizer basis ε b3': 143, 144/145,
  156–159, 168, 173, 183–186), 1 000 000 (146, 160, 161, 169/170, 171/172), 1 008 126
  (all 3-D reduced domains). No block in this family mentions the finer
  1 000 981 800-point grid that 98/122/141/142 used (`finer_grid_mentioned` false
  throughout).
- b-ratio sweep is uniformly 1/2, ..., 7/2 in 1001 steps of 3/1000 (every block).
- Upper bounds quoted with sources: [BS01, Theorem 2.4/2.7/2.12], [BS06, Corollary
  1.6/2.8, Proposition 2.7/4.1] for trivial-stabilizer points; Theorem 1.2.6 in general
  (30 / 54 / 102 / 198 depending on the group).
- Lower-bound remarks are printed for 152/154 ([BS06, Lemma 4.2]), 166 (Dress et al.
  [DHM93], 6 facets) and 178/179 ([BS06, Example 4.4], 32 facets).

## Conventions (the part that differs from the tetragonal tables)

- **b-ratio** = ||b3'||/||b1'|| = c/a in the ITA (primed) basis — his hexagonal-section
  headers use the primed basis for this ratio ("value ||b3'||/||b1'||", PDF 88).
- **Generating points are printed in his orthohexagonal C-centred basis**
  B'' = (2b1' + b2', b2', b3') (Sec. 2.2.3 / App. B: X = X_{B''→B'} = [[2,0,0],[1,1,0],[0,0,1]],
  ops worked as (X⁻¹AX, X⁻¹a)). Conversion to the ITA hexagonal basis used by our
  frozen ops: **x' = 2x'', y' = x'' + y'', z' = z''**. Evidence: (i) his printed
  reduced-domain vertices are, under this reading, exactly the normalizer's special
  points (e.g. R143's (1/6,0,0), (1/6,1/6,0) = (1/2,0,0)_N and (2/3,1/3,0)_N in the
  P6/mmm basis he prints; R147's (1/3,0,0) = (2/3,1/3,0)' on the 3-fold axis); (ii) the
  pre-registered gate G2c (`harness/phase2/g2c_controls.py`, ANCHORS G2c hypothesis H1)
  reproduces the printed f-vector of all six required rows (IT 143, 147, 155, 166, 178,
  194 — incl. the 34-facet maximum and a special-position row) under this conversion,
  and the alternative H0 (verbatim ITA) was never needed. Origin: no trigonal/hexagonal
  group has two ITA origin choices; rhombohedral groups are on hexagonal axes (obverse,
  centering (0,0,0), (2/3,1/3,1/3), (1/3,2/3,2/3)) in both his tables and our freeze.
- **Second members of enantiomorphic pairs** (145, 153, 154, 170, 172, 179, 181): the
  printed point is for the first member; G2c found the S178 row reproduces in IT(179)
  only under z → −z (as 95/96 in batch 1). The sweep's P2 pass runs verbatim first,
  then z → −z, and records the conversion per sighting.

## Discrepancy log

| # | block | row | visual | text layer | resolution |
|---|---|---|---|---|---|
| — | — | — | — | — | **0 content discrepancies** over the 153 visually cross-read rows × (3 + 1 + 3) entries and the headers on those pages. |
| meta | 178/179, 180/181 | normalizer | "(only the normalizer for IT(178) but not for IT(179))" / "(... IT(181) but not for IT(180))" | same | wrapped remark kept verbatim in `normalizer`. |
| meta | 166, 191 | normalizer | "...; so the normalizer is identical..." | same (truncated to the header field) | prose beyond the basis kept as printed in the field. |

Observations recorded, not inferred from:
- The text layer of the normalizer bases renders fractions as adjacent digits in
  unreliable order (e.g. "32 b01" and "23 b01" both for 2/3 b1' on PDF 87–88; "12 b03"
  and "21 b03" both for 1/2 b3'); the normalization rule (min/max) was confirmed
  against the rendered pages 88, 114, 123 and is the only editing applied.
- IT(155) R32 prints 89 rows (the largest trigonal table); IT(178/179) prints 97 rows
  and hosts the family maximum (34 facets), consistent with his Sec. 2.3 remark that
  178 "seems to generate stereohedra with the third most facets after IT(214)".

## Verification results

(a) **Euler.** All 958 rows satisfy V − E + F = 2 (asserted in the script; `euler_ok`
per block).

(b) **Visual vs text layer.** 0 discrepancies on the 153-row sample (pages above).

(c) **Per-group maximum facet count vs Schmitt's own Sec. 2.3 remarks** (printed
p. 151 / PDF 156, text layer):

| group | Sec. 2.3 remark (verbatim) | table max F | check |
|---|---|---|---|
| 150 | "Matching lower bounds for Bochiş & Santos [BS06] are provided." Block header: f2 ≤ 16 [BS06, Corollary 1.6] trivial stabilizer | 16 | agrees (16 attained) |
| 152 | "We improved the lower bound of Bochiş & Santos [BS06] from 13 to 25 facets (both DV-stereohedra are generated by points with trivial stabilizer)." | 25 ((45,68,25) @ 527/1000 and (46,69,25) @ 797/1000) | agrees |
| 159 | "Matching lower bounds for Bochiş & Santos [BS06] are provided." Block header: f2 ≤ 16 [BS06, Corollary 1.6] | 16 | agrees |
| 166 | "We improved the lower bound of Dress et al. [DHM93] from 6 to 22 facets." Block header remark: [DHM93] 6 facets | 22 ((38,58,22) @ 527/1000 = the G2c S166 row) | agrees |
| 178 | "We improved the lower bound of Bochiş & Santos [BS06] from 32 to 34 facets (both DV-stereohedra are generated by points with trivial stabilizer). This group seems to generate stereohedra with the third most facets after IT(214)." Block header: [BS06, Example 4.4] 32 facets | 34 ((64,96,34) @ 163/200 = the G2c S178 row; exact chain: stabilizer 1, aut 1) | agrees |

No other trigonal/hexagonal group is commented on in Sec. 2.3.

(d) **G2c rows verbatim.** The six rows the G2c gate reproduced are present exactly
(asserted by `g2c_controls.py` against this file): IT(143) (8,12,6) @ 3497/1000
(1/6,0,0) [PDF 88]; IT(147) (10,15,7) @ 3497/1000 (33/100,−1/500,0) [PDF 89]; IT(155)
(48,73,27) @ 797/1000 (−193/750,−53/250,6/125) [PDF 97]; IT(166) (38,58,22) @ 527/1000
(−16/375,−16/125,31/500) [PDF 105]; IT(178) (64,96,34) @ 163/200
(32/125,−19/125,43/1500) [PDF 114]; IT(194) (18,30,14) @ 797/1000 (1/3,0,1/4) [PDF 123].

## Honest limits

- **Sample cross-read, single reader.** 153 of 958 rows were visually verified; the
  remaining 805 rest on the pdfTeX text layer, which showed 0 discrepancies on the
  sample here and 0 on all 1,476 tetragonal rows in the batch-1 digitization. The
  sweep's P2 pass runs every row through the exact chain, and any f-vector that
  fails to reproduce is quarantined and listed — a second, computational, check of
  every row (a transcription error would show up there as a mismatch).
- **Not transcribed:** Schmitt's per-block prose beyond the header facts.
- **Not checked here:** stabilizer triviality of the points behind the [BS06]/[BS01]
  bound remarks; type-level identity of any row (f-vector equality is not type
  equality — the collision screen is the batch-2 triage step).

## Files

- `harness/schmitt_hexagonal_tables.json` — the digitization (45 blocks, 958 rows,
  `_meta` with method/limits).
- `harness/digitize_schmitt_hexagonal.py` — the parser (re-run reproduces the file).
- Scratch (session-local, not committed): rendered page PNGs, text-layer dump.
