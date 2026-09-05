# Schmitt 2016 tetragonal tables — digitization (2026-09-04)

Source: `references/Schmitt_2016_dissertation.pdf`, Section 2.2.2 "Tetragonal groups",
printed pp. 27–81 = PDF pages 32–86 (PDF page = printed + 5). Output:
`harness/schmitt_tetragonal_tables.json` (per-group entries, page citation per group
and per row). Model for the format: the accepted cubic digitization in
`harness/triage_phase1.py` (f-vectors only) and `harness/rekey_tables.json`; this
file goes further and carries b-ratio, generating point and header facts.

## Method — what this is and is not

- **Single-pass visual transcription.** Every one of the 55 PDF pages was rendered
  (`pdftoppm -r 120`) and read as an image, page by page, by Fable 5.1 in this
  session; rows and header facts were typed from the images into a scratch file
  before the text layer for those pages was consulted (the text layer of printed
  pp. 27–29 had been seen earlier in the session while locating the section; the
  remaining pages were typed blind).
- **Text-layer cross-check, two ways.** The typed transcription was then diffed
  row-for-row (f-vector, b-ratio, point, order) against (i) a fresh
  `pdftotext -layout` parse of PDF pp. 32–87 and (ii) the phase-2 sweep's harvest
  `harness/schmitt_tetragonal_rows_harvested.json` (1,476 rows).
- **Not a second independent re-key.** One reader, cross-checked against a machine
  text layer. A second independent re-key (different agent/person, no access to
  this file) remains a **G5 duty for any group hosting a finalist**, exactly as for
  the cubic tables (`rekey_tables.json` precedent).
- Rule followed: transcribe what is printed; nothing inferred. Where a header wording
  differs between groups (e.g. the "Initially we let the b-ratio vary ..." wording
  for 98/122/141/142) the JSON records the variant, not a normalized value.

## Coverage

| item | count |
|---|---|
| Space groups covered | IT(75)–IT(142), all 68 |
| Printed table blocks | 65 (three enantiomorphic pairs print ONE table each: 76/78, 91/95, 92/96) |
| Rows transcribed | **1,476** (f-vector, b-ratio, generating point; page per row) |
| Header facts per block | normalizer + basis, reduced-domain vertices, upper bound (with citation), lower-bound remark if printed, b-ratio range/steps, grid size |
| Frequency column | **none printed in any tetragonal table** (unlike the cubic Sec. 2.2.5 tables); `freq` is `null` throughout |
| Pages read | PDF 32–87 (87 confirmed to be the start of Sec. 2.2.3 Trigonal; IT(142)'s table ends on PDF 86 / printed 81) |

Rows per block (block: rows): 75:3, 76/78:12, 77:8, 79:10, 80:27, 81:16, 82:40, 83:3,
84:25, 85:13, 86:36, 87:23, 88:52, 89:5, 90:14, 91/95:84, 92/96:69, 93:32, 94:42,
97:35, 98:130, 99:2, 100:3, 101:6, 102:8, 103:4, 104:10, 105:5, 106:7, 107:8, 108:6,
109:15, 110:14, 111:8, 112:20, 113:15, 114:32, 115:8, 116:31, 117:8, 118:53, 119:22,
120:17, 121:24, 122:101, 123:2, 124:7, 125:7, 126:16, 127:3, 128:21, 129:7, 130:21,
131:11, 132:12, 133:20, 134:31, 135:16, 136:19, 137:16, 138:19, 139:14, 140:11,
141:65, 142:52.

Header facts worth knowing for phase-2 use:
- Grid sizes: 1 000 405 (2-D reduced domains, groups with normalizer basis eps b3':
  75, 77, 79, 80, 99–110), 1 000 000 (76/78), 1 008 126 (3-D reduced domains),
  2 000 376 (91/95, 92/96); 98, 122, 141, 142 add a finer grid of 1 000 981 800 points
  at selected b-ratios (98: 377/250 and 38/25; 122: 5/4; 141: 1/2; 142: 253/500).
- b-ratio sweep is uniformly 1/2, ..., 7/2 in 1001 steps of 3/1000.
- Upper bounds are quoted with their sources ([BS01]/[BS06] for trivial-stabilizer
  points, Theorem 1.2.6 in general: 38 / 70 / 134 depending on the group).

## Discrepancy log

| # | group | row | visual | text layer | resolution |
|---|---|---|---|---|---|
| — | — | — | — | — | **0 content discrepancies** over 1,476 rows × (3 + 1 + 3) entries, against both the fresh `pdftotext` parse and the phase-2 harvest. |
| meta | 142 | page list | PDF 85–86 | PDF 85–87 | my text parser attaches a block to every page up to the next header; the IT(142) table visibly ends on PDF 86. Page list in the JSON follows the visual read. Not a data discrepancy. |

Observations recorded, not inferred from:
- IT(91)/IT(95) prints the f-vector **(34,54,22) twice**, at two different points
  ((1019/1998, 25/54, 187/3996) and (133/250, 23/50, 51/500), both at b = 4/5, printed
  p. 40 / PDF 45). Both rows are in the JSON exactly as printed. Every other block has
  distinct f-vectors per row.
- The harvested file `schmitt_tetragonal_rows_harvested.json` is therefore confirmed
  complete and exact at the row level (its `source` line says "printed pp. 27-48";
  the correct span is printed pp. 27–81 — a label error in that file, not a data error).

## Verification results

(a) **Euler.** All 1,476 rows satisfy V − E + F = 2 (asserted while writing the JSON;
`euler_ok: true` per block).

(b) **Visual vs text layer.** 0 discrepancies (see log above).

(c) **Per-group maximum facet count vs Schmitt's own Sec. 2.3 remarks**
(printed p. 151 / PDF 156; quoted verbatim from the text layer):

| group | Sec. 2.3 remark (verbatim) | table max F | check |
|---|---|---|---|
| 76 | "We confirmed the findings of Koch & Fischer [KF72]. However, they made mistakes in calculating the coordinates they present in their paper. These mistakes occurred since they did not compute in exact arithmetic as we were told by Koch." Block header: "Koch & Fischer [KF72] found a stereohedron with 24 facets for this group." | **24** ((44,66,24) @ 797/1000, (20/333, 44/999, 0)) | agrees |
| 84 | "Matching lower bounds for Bochiş & Santos [BS01] are provided." Block header: f2 ≤ 15 [BS01, Theorem 2.12] for trivial stabilizer, ≤ 70 in general. | 16 ((28,42,16) @ 797/1000); a 15-facet row (25,38,15) is present | consistent: the trivial-stabilizer bound 15 is attained in the table; the 16-facet row exceeds 15, so it must come from a point with non-trivial stabilizer (its z = 0). Not verified here (no stabilizer computation was done). |
| 91 | "We improved the lower bound of Bochiş & Santos [BS06] from 17 to 26 facets (both DV-stereohedra are generated by points with trivial stabilizer)." Block header: "Lemma 4.2 in [BS06] implies that there exists a stereohedron with at least 17 facets for this group." | **26** ((48,72,26) @ 14/25, (538/999, 13/333, 71/2664)) | agrees |
| 98 | "We improved the lower bound of Bochiş & Santos [BS06] from 29 to 35 facets (both DV-stereohedra are generated by points with trivial stabilizer). This group seems to generate stereohedra with the second most facets after IT(214) = I4_132." Block header: "In [BS06, Example 4.5] a stereohedron with 29 facets was constructed for this group." | **35** ((66,99,35) @ 727/500, (62/125, 41/125, 79/1000)) | agrees |
| 141 | "Matching lower bounds for Bochiş & Santos [BS01] are provided." Block header: f2 ≤ 18 [BS01, Theorem 2.7] trivial stabilizer; "Examples of stereohedra with 18 facets are known for this group, see [BS01, Example 2.9]." | 29 ((54,81,29) @ 527/1000); 18-facet rows present ((29,45,18), (31,47,18), (32,48,18)) | consistent: 18 attained; rows above 18 necessarily sit at non-trivial-stabilizer points (all have x = 1/2 or lie on the reduced-domain boundary) — not verified here. |
| 140 | (no Sec. 2.3 remark) Block header: "Examples of stereohedra with 8 facets are known for this group, see [BS01, Example 2.5]." | 13 | 8-facet row (10,16,8) present |

No other tetragonal group is commented on in Sec. 2.3 (the remaining remarks there
concern 150–178 (trigonal/hexagonal) and the cubic groups already checked in
`triage_phase1.py`).

(d) **G2b rows verbatim.** All three rows the G2b gate reproduced
(`harness/phase2/G2B_RESULT.md` lines 35–37) are present exactly:
IT(75) (10,15,7) @ 1/2, (2825/5652, −1/5652, 0) [PDF 33 / printed 28];
IT(76) (44,66,24) @ 797/1000, (20/333, 44/999, 0) [PDF 33 / printed 28];
IT(77) (28,42,16) @ 1/2, (539/5652, −187/5652, 0) [PDF 34 / printed 29].
Also re-confirmed: the two IT(79) rows cited in STATUS (2026-09-03 later 2),
(18,28,12) @ 7/2 and (24,36,14) @ 1/2, both at (0,0,0) [PDF 34 / printed 29].

## Honest limits

- **Single reader.** Zero discrepancies between one visual pass and the text layer is
  strong evidence the text layer is clean for these pages (pdfTeX output, no scanned
  content), but it is not the same as two independent readers. G5 re-key still owed
  for finalist-hosting groups.
- **Rendering.** No page was ambiguous at 120 dpi: all minus signs, subscripts and
  fraction bars were legible; the two-line reduced-domain lists (3-D domains) were
  read as printed. No unreadable spots.
- **Not transcribed:** Schmitt's per-block prose beyond the header facts (e.g. the
  "Since the fundamental domain was reduced by the normalizer ..." sentence, identical
  across the eps-b3' groups) is summarized in `_meta`, not copied per block.
- **Not checked here:** stabilizer triviality of the points behind the 84/141 rows
  above the [BS01] bounds; type-level identity of any row (f-vector equality is not
  type equality — the phase-2 type-level diligence this file enables is still to do).
- The thesis's own printed page for each group (index pp. 181–182) agrees with the
  `printed_pages[0]` recorded here for every block.

## Files

- `harness/schmitt_tetragonal_tables.json` — the digitization (65 blocks, 1,476 rows,
  `_meta` with method/limits).
- `harness/schmitt_tetragonal_rows_harvested.json` — phase-2 text-layer harvest,
  confirmed exact (unchanged).
- Scratch (session-local, not committed): rendered page PNGs, `visual.txt` (typed
  transcription), `parse_text.py`, `diff_visual.py`.
