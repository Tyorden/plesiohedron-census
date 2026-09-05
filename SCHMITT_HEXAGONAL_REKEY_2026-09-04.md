# Schmitt 2016 trigonal/hexagonal tables — BLIND independent re-key (2026-09-04, agent #147)

G5 diligence duty for the hexagonal family (52 groups, IT(143)-IT(194)). This is the
second, independent transcription of Schmitt's Sec. 2.2.3 "Trigonal groups" and
2.2.4 "Hexagonal groups", done without access to the accepted digitization.

Source: `references/Schmitt_2016_dissertation.pdf`, printed pp. 82-118 = PDF pp. 87-123
(PDF page = printed + 5; verified on PDF 87, footer "82", which opens Sec. 2.2.3 with the
basis diagrams and the IT(143) header; PDF 124 opens Sec. 2.2.5 Cubic; PDF 86 is the tail
of the tetragonal IT(142) table and carries no trigonal rows).

Output: `harness/schmitt_hexagonal_rekey.json` (45 blocks, 958 rows; per row f-vector,
b-ratio, generating point, PDF and printed page, row index in block; per block the
group label(s) as printed and the header facts verbatim: normalizer + basis, "only the
normalizer for ..." remarks, reduced-domain vertices, upper bound with citation,
lower-bound remark if printed, b-ratio sweep, grid size).
Diff script: `harness/rekey_hexagonal_diff.py` (read-only on both files).

## Method

1. **Blind.** `harness/schmitt_hexagonal_tables.json`, `harness/digitize_schmitt_hexagonal.py`,
   `SCHMITT_HEXAGONAL_DIGITIZATION_2026-09-04.md` and the batch-2 results docs were not
   opened until the re-key file was complete and saved. The only prior material read was
   the tetragonal digitization doc (for table format) and the cubic/tetragonal pointers.
2. **Visual transcription.** Every PDF page 87-124 rendered at 200 dpi (`pdftoppm -r 200`)
   and read as an image, page by page; every row typed from the image into a scratch
   transcript (`scratchpad/rekey/transcript.txt`) together with the header facts. Two
   glyphs flagged during the read were re-rendered at 400 dpi and resolved (below).
3. **Self-checks (compile step, `scratchpad/rekey/compile_rekey.py`):**
   - Euler V - E + F = 2 on every row: **958/958 pass**.
   - b-ratio on Schmitt's sweep grid 1/2 + 3k/1000, 0 <= k <= 1000: **958/958 pass**
     (a strong check on 3-vs-8 and 1-vs-7 misreads in the b-ratio column, since e.g.
     838/1000 and 883/1000 are off-grid while 833/1000 is on it).
   - Row counts per block and per PDF page recorded in the JSON (`totals`).
   - Cross-check of the visual read against a fresh `pdftotext -layout` parse of PDF
     87-123: the text layer parses to exactly **958 rows** and matches the visual read
     positionally on every page, **0 discrepancies** (f-vector, b-ratio, point). This is
     a check on my own typing, not on the accepted file.
4. **Diff vs the accepted file** only after step 3 (`rekey_hexagonal_diff.py`): rows
   matched by (block, b-ratio, point) as exact Fractions; reports row counts per block,
   f-vector differences on matched keys, keys present on one side only (this catches
   b-ratio and point differences), PDF-page differences, duplicate keys within a block,
   row order, and header facts (normalizer + basis, "only for" attribution, grid size,
   upper bound).

## Totals

| item | re-key (#147) | accepted (#143) |
|---|---|---|
| printed table blocks | 45 | 45 |
| rows | **958** | **958** |
| Euler failures | 0 | (0 per their `_meta.checks`) |
| enantiomorphic pairs sharing one table | 144/145, 151/153, 152/154, 169/170, 171/172, 178/179, 180/181 | same |

Rows per block (re-key): 143:2, 144/145:9, 146:19, 147:13, 148:63, 149:5, 150:13,
151/153:29, 152/154:64, 155:89, 156:3, 157:3, 158:4, 159:9, 160:17, 161:17, 162:8,
163:22, 164:11, 165:23, 166:60, 167:84, 168:4, 169/170:16, 171/172:34, 173:8, 174:2,
175:4, 176:23, 177:5, 178/179:97, 180/181:69, 182:30, 183:3, 184:4, 185:7, 186:8,
187:3, 188:8, 189:3, 190:23, 191:3, 192:7, 193:14, 194:16. Identical to the accepted
file block for block.

Rows per PDF page (re-key): 88:11, 89:23, 90:31, 91:41, 92:18, 93:29, 94:30, 95:34,
96:49, 97:40, 98:6, 99:13, 100:26, 101:16, 102:31, 103:25, 104:34, 105:31, 106:49,
107:30, 108:20, 109:34, 110:10, 111:27, 112:12, 113:49, 114:41, 115:37, 116:32, 117:30,
118:11, 119:12, 120:13, 121:23, 122:10, 123:30 (PDF 87 carries the IT(143) header only).

## Discrepancy list (re-key vs accepted)

| # | block | PDF page | field | re-key | accepted | resolution |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | **0 discrepancies.** Row count per block: 0 diffs. f-vector on matched (b, point) keys: 0 diffs. Rows present in one file only (i.e. any b-ratio or point difference): 0. PDF page per row: 0 diffs. Duplicate keys within a block: none in either file. Row order within every block: identical. Header facts (normalizer + basis for all 45 blocks; the "only the normalizer for IT(a) but not for IT(b)" attribution for 151/153, 152/154, 178/179, 180/181; grid size 1 000 405 / 1 000 000 / 1 008 126 per block; upper bound with citation; lower-bound remarks for 152/154, 166, 178/179): 0 diffs. |

Glyph ambiguities flagged during the visual read and how they were resolved (both are
also consistent between the two files):

| block | PDF page | row | best read | alternative | resolution |
|---|---|---|---|---|---|
| 180/181 | 114 | (40,61,23) | b = 977/1000 | 971/1000 (7 vs 1) | 400-dpi crop: clearly "977"; both candidates are on the sweep grid, so the grid check does not discriminate here; the glyph does. Accepted file also has 977/1000. |
| 180/181 | 114 | (42,64,24) | b = 833/1000 | 838/1000 or 883/1000 (3 vs 8) | 400-dpi crop: clearly "833"; 838 and 883 are off the 1/2 + 3k/1000 grid, 833 is on it (k = 111). Accepted file also has 833/1000. |

Non-data observations (no correction to the tables needed):

- The accepted file's `_meta.source_pages` says "printed pp. 81-118 = PDF pages 86-123".
  Section 2.2.3 begins on printed p. 82 / PDF 87 (footer "82"); PDF 86 / printed 81 is
  the tail of the tetragonal IT(142) table. The accepted block for 143 itself correctly
  lists `pdf_pages [87, 88]`, so this is a one-off label in the metadata, not a data error.
  Suggested wording: "printed pp. 82-118 = PDF pages 87-123".
- The printed remark for the 180/181 block reads "(only the normalizer for IT(181) but
  not for IT(180))" — the reverse pattern from the other three pairs, where the first-
  listed group carries the normalizer. Both files transcribe it exactly as printed; the
  re-key JSON marks it "[sic - printed exactly so]".
- The IT(146) and IT(160)/IT(161) blocks use a grid of 1 000 000 points, the other
  2-D-reduced blocks 1 000 405, the 3-D-reduced blocks 1 008 126; the 169/170 and 171/172
  blocks also say 1 000 000. Both files agree on all of these.

## Verdict

**Accepted tables confirmed.** Two independent transcriptions (text-layer-primary with a
visual cross-read, #143; visual-primary blind re-key with a text-layer cross-check, #147)
agree on all 958 rows x (f-vector, b-ratio, 3 point coordinates, page) and on every
header fact compared. No corrections to `harness/schmitt_hexagonal_tables.json` are
proposed. The G5 independent re-key duty for the hexagonal family is discharged at the
transcription level; whatever downstream use is made of these rows (reconciliation,
anchors, "absent from Schmitt's printed TRIGONAL/HEXAGONAL survey" claims) can cite this
file as the second key.

Files:
- `paper_prep/MINT_plesiohedron/harness/schmitt_hexagonal_rekey.json` (new, the re-key)
- `paper_prep/MINT_plesiohedron/harness/rekey_hexagonal_diff.py` (new, the diff)
- `paper_prep/MINT_plesiohedron/SCHMITT_HEXAGONAL_REKEY_2026-09-04.md` (this report)
- scratch (session-local, not in the repo): rendered pages `scratchpad/rekey/p-087..124.png`,
  400-dpi crops `zoom114*.png`, `transcript.txt`, `compile_rekey.py`.

No git commits made (per spawn instructions); no edits to the accepted JSON.
