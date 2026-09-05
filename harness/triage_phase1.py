#!/usr/bin/env python
"""triage_phase1.py — deterministic triage of the Phase-1 unmatched types into a G4 shortlist.

Inputs : phase1_types.json (the accepted Phase-1 store, 2026-08-29)
Output : TRIAGE_RESULT.md (full ranked table of all unmatched types + TOP-10 G4 shortlist)
Gates  : ANCHORS.md G4/G5. LANGUAGE: "not matched against catalog snapshot of 2026-08-28"
         ONLY — no novelty claims. Schmitt ch.2 is a sampling survey: absence from his
         printed tables is evidence, not proof.

SCHMITT IN-TEXT TABLE DIGITIZATION (new in this step, 2026-08-30):
  The per-group f-vector lists below were transcribed from the archived primary source
  references/Schmitt_2016_dissertation.pdf, cubic section 2.2.5, printed pp. 119-150
  (PDF pages 124-155), by visual read (Fable 5, triage session 2026-08-30). f-vectors
  ONLY (his generating points / frequencies not transcribed). Checks applied:
    (a) every transcribed f-vector satisfies V - E + F = 2 (asserted below);
    (b) per-group max facet counts agree with Schmitt's own Sec. 2.3 discussion remarks
        (197: max 17 = Engel confirmed; 198: Koch 18->24; 199: Koch 20->24;
         205: 13->18; 206: 17->28; 210: 10->17; 212: 22->29; 214: (70,106,38) Engel;
         220: Koch 17->25; 227: max 16 vs Smith's unreproduced 20; 228: Koch 12->16).
  NOT yet independently double-keyed: treat PRESENT/ABSENT flags as provisional pending
  a second independent transcription (queued as a G5 duty). IT(212)=P4_332 and
  IT(213)=P4_132 are an enantiomorphic pair; the thesis prints ONE table for both
  (printed pp. 133-135) — group 213 aliases the 212 list here.

  Semantics of the flag (G5 wording):
    P (present) : the type's f-vector appears in Schmitt's printed table for that
                  sighted group => a TYPE-LEVEL check is required at G5 (his in-text
                  tables stop at f-vectors; same f-vector != same combinatorial type —
                  proven concretely by the Josehedron vs his IT(220) (12,22,12) cell,
                  see SCHMITT_220_CHECK_RESULT.md).
    A (absent)  : the f-vector does NOT appear in his printed table for that sighted
                  group => stronger candidate; still only snapshot language (his grid
                  sampling under-covers special positions — exactly where we swept).
    U (unknown) : that group's table is not digitized (should not occur: all 36 cubic
                  groups are digitized below; branch kept for honesty).

Deterministic: no timestamps in the table body, stable sort keys, byte-identical
across re-runs on the same store.
"""

import json
import math
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.join(HERE, "phase1_types.json")
OUT = os.path.join(HERE, "TRIAGE_RESULT.md")

RUN_DATE = "2026-08-30"  # fixed label, not a timestamp
CATALOG_SNAPSHOT = "2026-08-28"

CORRIDOR = {198, 199, 205, 206, 212, 213, 214, 220}  # scout's 6 + Phase-1's flagged additions 205/206
SPECIAL_GROUPS = {220, 230}  # task weighting: I-43d (Josehedron's home) and Ia-3d (its normalizer; 9 unmatched from 16 orbits)
SEEDED_GONS = {3, 4, 6}  # face sizes occurring in the seeded classics (pentagons counted unusual per task wording,
                          # although the seeded Schmitt-220 representative does carry two)
MAX_FACETS_KILL = 38  # observed literature max (Schmitt 2016, sampling; ANCHORS amendment: observed, not proven)

# ---------------------------------------------------------------------------
# Schmitt 2016 in-text f-vector tables, cubic groups (printed page in comment).
# ---------------------------------------------------------------------------
SCHMITT_FVECTORS = {
    195: [(5, 8, 5), (5, 9, 6), (8, 12, 6), (6, 11, 7), (8, 13, 7), (6, 12, 8), (8, 16, 10),
          (14, 24, 12), (16, 27, 13)],  # p. 119
    196: [(5, 8, 5), (8, 12, 6), (6, 12, 8), (8, 16, 10), (14, 24, 12)],  # p. 120
    197: [(4, 6, 4), (5, 9, 6), (8, 12, 6), (6, 12, 8), (10, 17, 9), (12, 19, 9), (8, 15, 9),
          (10, 18, 10), (11, 19, 10), (12, 20, 10), (7, 15, 10), (9, 17, 10), (13, 22, 11),
          (14, 23, 11), (10, 20, 12), (13, 23, 12), (14, 25, 13), (15, 26, 13), (17, 28, 13),
          (18, 29, 13), (20, 32, 14), (24, 36, 14), (20, 33, 15), (22, 35, 15), (26, 39, 15),
          (24, 38, 16), (24, 39, 17)],  # pp. 120-121
    198: [(8, 14, 8), (11, 21, 12), (12, 22, 12), (14, 24, 12), (19, 31, 14), (21, 35, 16),
          (22, 36, 16), (26, 40, 16), (26, 42, 18), (30, 46, 18), (32, 48, 18), (29, 47, 20),
          (30, 48, 20), (32, 50, 20), (33, 53, 22), (34, 54, 22), (36, 56, 22), (40, 62, 24)],  # pp. 121-122
    199: [(8, 12, 6), (10, 17, 9), (13, 22, 11), (13, 24, 13), (14, 25, 13), (15, 26, 13),
          (16, 27, 13), (18, 29, 13), (17, 29, 14), (19, 31, 14), (19, 32, 15), (21, 34, 15),
          (22, 35, 15), (23, 36, 15), (22, 36, 16), (23, 37, 16), (24, 38, 16), (25, 39, 16),
          (26, 40, 16), (23, 38, 17), (25, 40, 17), (26, 41, 17), (27, 42, 17), (28, 43, 17),
          (29, 44, 17), (30, 45, 17), (27, 43, 18), (28, 44, 18), (31, 47, 18), (30, 47, 19),
          (33, 50, 19), (32, 50, 20), (33, 51, 20), (34, 52, 20), (35, 53, 20), (36, 54, 20),
          (34, 53, 21), (37, 56, 21), (36, 56, 22), (37, 57, 22), (38, 58, 22), (39, 59, 22),
          (41, 62, 23), (43, 65, 24)],  # pp. 122-123
    200: [(5, 8, 5), (5, 9, 6), (6, 10, 6), (8, 12, 6), (6, 11, 7), (6, 12, 8), (8, 16, 10)],  # pp. 123-124
    201: [(6, 12, 8), (12, 19, 9), (11, 19, 10), (12, 20, 10), (7, 15, 10), (13, 22, 11),
          (14, 24, 12), (15, 26, 13), (17, 28, 13), (18, 29, 13), (17, 29, 14), (20, 32, 14),
          (24, 36, 14), (22, 35, 15), (24, 38, 16), (25, 39, 16)],  # p. 124
    202: [(4, 6, 4), (5, 8, 5), (5, 9, 6), (8, 12, 6), (6, 11, 7), (6, 12, 8), (8, 16, 10),
          (14, 24, 12)],  # p. 125
    203: [(5, 8, 5), (8, 12, 6), (10, 15, 7), (8, 13, 7), (9, 14, 7), (8, 15, 9), (10, 20, 12),
          (12, 22, 12), (14, 24, 12), (14, 25, 13), (18, 30, 14), (16, 30, 16)],  # p. 125
    204: [(4, 6, 4), (5, 8, 5), (5, 9, 6), (8, 12, 6), (10, 15, 7), (6, 11, 7), (7, 12, 7),
          (8, 13, 7), (9, 14, 7), (10, 16, 8), (6, 12, 8), (10, 18, 10), (11, 19, 10),
          (12, 20, 10), (7, 15, 10), (9, 17, 10), (13, 22, 11), (10, 20, 12), (14, 25, 13),
          (17, 28, 13), (24, 36, 14)],  # p. 126
    205: [(8, 12, 6), (6, 12, 8), (7, 13, 8), (10, 18, 10), (11, 21, 12), (12, 22, 12),
          (13, 23, 12), (14, 24, 12), (15, 25, 12), (19, 30, 13), (15, 27, 14), (16, 28, 14),
          (17, 29, 14), (18, 30, 14), (19, 31, 14), (20, 32, 14), (21, 33, 14), (20, 34, 16),
          (21, 35, 16), (22, 36, 16), (24, 38, 16), (25, 39, 16), (26, 42, 18), (28, 44, 18)],  # p. 127
    206: [(5, 8, 5), (8, 12, 6), (10, 18, 10), (9, 17, 10), (10, 19, 11), (13, 22, 11),
          (8, 17, 11), (13, 23, 12), (14, 24, 12), (15, 25, 12), (16, 26, 12), (14, 25, 13),
          (16, 27, 13), (17, 28, 13), (18, 29, 13), (17, 29, 14), (18, 30, 14), (19, 31, 14),
          (20, 32, 14), (21, 33, 14), (22, 34, 14), (17, 30, 15), (18, 31, 15), (19, 32, 15),
          (20, 33, 15), (21, 34, 15), (22, 35, 15), (19, 33, 16), (21, 35, 16), (22, 36, 16),
          (23, 37, 16), (24, 38, 16), (25, 39, 16), (26, 40, 16), (23, 38, 17), (24, 39, 17),
          (25, 40, 17), (26, 41, 17), (28, 43, 17), (30, 45, 17), (23, 39, 18), (25, 41, 18),
          (26, 42, 18), (27, 43, 18), (28, 44, 18), (29, 45, 18), (30, 46, 18), (25, 42, 19),
          (27, 44, 19), (28, 45, 19), (29, 46, 19), (30, 47, 19), (32, 49, 19), (29, 47, 20),
          (30, 48, 20), (31, 49, 20), (32, 50, 20), (34, 52, 20), (32, 51, 21), (33, 52, 21),
          (34, 53, 21), (36, 55, 21), (34, 54, 22), (36, 56, 22), (38, 58, 22), (37, 58, 23),
          (40, 61, 23), (42, 64, 24), (41, 64, 25), (44, 67, 25), (46, 70, 26), (50, 76, 28)],  # pp. 127-129
    207: [(4, 6, 4), (5, 8, 5), (5, 9, 6), (8, 12, 6), (6, 12, 8), (8, 15, 9)],  # p. 129
    208: [(5, 9, 6), (6, 11, 7), (6, 12, 8), (7, 13, 8), (11, 18, 9), (12, 19, 9), (9, 16, 9),
          (11, 19, 10), (12, 20, 10), (8, 16, 10), (9, 17, 10), (13, 22, 11), (14, 23, 11),
          (10, 20, 12), (14, 24, 12), (15, 25, 12), (16, 27, 13), (17, 28, 13), (16, 28, 14),
          (17, 29, 14), (20, 32, 14), (24, 36, 14), (17, 30, 15), (20, 33, 15), (24, 38, 16),
          (25, 39, 16), (24, 39, 17)],  # p. 130
    209: [(4, 6, 4), (5, 8, 5), (5, 9, 6), (8, 12, 6), (6, 12, 8), (8, 15, 9), (14, 24, 12)],  # p. 131
    210: [(5, 8, 5), (8, 12, 6), (10, 15, 7), (8, 13, 7), (9, 14, 7), (10, 18, 10), (8, 16, 10),
          (10, 20, 12), (12, 22, 12), (13, 23, 12), (14, 24, 12), (15, 26, 13), (16, 27, 13),
          (16, 28, 14), (19, 32, 15), (20, 33, 15), (16, 30, 16), (24, 39, 17)],  # pp. 131-132
    211: [(4, 6, 4), (5, 8, 5), (6, 9, 5), (5, 9, 6), (7, 11, 6), (8, 12, 6), (10, 15, 7),
          (8, 13, 7), (9, 14, 7), (6, 12, 8), (10, 17, 9), (8, 15, 9), (10, 18, 10),
          (11, 19, 10), (12, 20, 10), (9, 17, 10), (12, 21, 11), (13, 22, 11), (10, 20, 12),
          (15, 25, 12), (16, 26, 12), (16, 27, 13), (17, 28, 13), (19, 31, 14), (20, 32, 14),
          (24, 36, 14), (24, 38, 16)],  # pp. 132-133
    212: [(8, 14, 8), (10, 17, 9), (8, 15, 9), (10, 18, 10), (12, 20, 10), (9, 17, 10),
          (11, 20, 11), (12, 21, 11), (13, 22, 11), (14, 23, 11), (12, 22, 12), (13, 23, 12),
          (14, 24, 12), (13, 24, 13), (14, 25, 13), (15, 26, 13), (16, 27, 13), (17, 28, 13),
          (16, 28, 14), (17, 29, 14), (18, 30, 14), (19, 31, 14), (16, 29, 15), (17, 30, 15),
          (19, 32, 15), (20, 33, 15), (21, 34, 15), (22, 35, 15), (23, 36, 15), (16, 30, 16),
          (19, 33, 16), (20, 34, 16), (21, 35, 16), (22, 36, 16), (23, 37, 16), (24, 38, 16),
          (20, 35, 17), (21, 36, 17), (22, 37, 17), (23, 38, 17), (24, 39, 17), (25, 40, 17),
          (26, 41, 17), (30, 45, 17), (24, 40, 18), (25, 41, 18), (26, 42, 18), (27, 43, 18),
          (28, 44, 18), (29, 45, 18), (30, 46, 18), (32, 48, 18), (25, 42, 19), (27, 44, 19),
          (28, 45, 19), (29, 46, 19), (30, 47, 19), (31, 48, 19), (32, 49, 19), (28, 46, 20),
          (29, 47, 20), (30, 48, 20), (31, 49, 20), (32, 50, 20), (33, 51, 20), (34, 52, 20),
          (29, 48, 21), (30, 49, 21), (31, 50, 21), (32, 51, 21), (33, 52, 21), (34, 53, 21),
          (35, 54, 21), (36, 55, 21), (32, 52, 22), (33, 53, 22), (34, 54, 22), (35, 55, 22),
          (36, 56, 22), (37, 57, 22), (38, 58, 22), (35, 56, 23), (36, 57, 23), (37, 58, 23),
          (38, 59, 23), (39, 60, 23), (40, 61, 23), (39, 61, 24), (40, 62, 24), (41, 63, 24),
          (42, 64, 24), (39, 62, 25), (40, 63, 25), (41, 64, 25), (42, 65, 25), (43, 66, 25),
          (44, 67, 25), (43, 67, 26), (44, 68, 26), (45, 69, 26), (46, 70, 26), (46, 71, 27),
          (48, 73, 27), (50, 76, 28), (52, 79, 29)],  # pp. 133-135 (single table for the 212/213 pair)
    214: [(9, 16, 9), (13, 21, 10), (13, 22, 11), (14, 24, 12), (16, 26, 12), (17, 27, 12),
          (14, 25, 13), (15, 26, 13), (16, 27, 13), (17, 28, 13), (18, 29, 13), (19, 30, 13),
          (16, 28, 14), (17, 29, 14), (18, 30, 14), (19, 31, 14), (20, 32, 14), (24, 36, 14),
          (19, 32, 15), (20, 33, 15), (21, 34, 15), (22, 35, 15), (23, 36, 15), (24, 37, 15),
          (21, 35, 16), (23, 37, 16), (24, 38, 16), (25, 39, 16), (26, 40, 16), (24, 39, 17),
          (25, 40, 17), (26, 41, 17), (27, 42, 17), (28, 43, 17), (30, 45, 17), (25, 41, 18),
          (26, 42, 18), (27, 43, 18), (28, 44, 18), (29, 45, 18), (30, 46, 18), (26, 43, 19),
          (27, 44, 19), (29, 46, 19), (30, 47, 19), (31, 48, 19), (32, 49, 19), (31, 49, 20),
          (32, 50, 20), (33, 51, 20), (34, 52, 20), (30, 49, 21), (33, 52, 21), (34, 53, 21),
          (35, 54, 21), (36, 55, 21), (35, 55, 22), (36, 56, 22), (37, 57, 22), (38, 58, 22),
          (34, 55, 23), (37, 58, 23), (38, 59, 23), (39, 60, 23), (40, 61, 23), (39, 61, 24),
          (41, 63, 24), (42, 64, 24), (41, 64, 25), (43, 66, 25), (44, 67, 25), (43, 67, 26),
          (45, 69, 26), (46, 70, 26), (45, 70, 27), (47, 72, 27), (48, 73, 27), (47, 73, 28),
          (49, 75, 28), (50, 76, 28), (49, 76, 29), (51, 78, 29), (52, 79, 29), (51, 79, 30),
          (53, 81, 30), (54, 82, 30), (53, 82, 31), (55, 84, 31), (56, 85, 31), (55, 85, 32),
          (58, 88, 32), (57, 88, 33), (59, 90, 33), (60, 91, 33), (61, 93, 34), (62, 94, 34),
          (61, 94, 35), (63, 96, 35), (64, 97, 35), (66, 100, 36), (68, 103, 37),
          (70, 106, 38)],  # pp. 136-138
    215: [(4, 6, 4), (5, 8, 5), (6, 9, 5), (5, 9, 6), (8, 12, 6), (8, 13, 7), (6, 12, 8),
          (14, 24, 12)],  # p. 138
    216: [(4, 6, 4), (5, 8, 5), (8, 12, 6), (6, 12, 8), (14, 24, 12)],  # pp. 138-139
    217: [(4, 6, 4), (5, 8, 5), (6, 9, 5), (5, 9, 6), (6, 10, 6), (7, 11, 6), (8, 12, 6),
          (10, 15, 7), (6, 12, 8), (10, 17, 9), (12, 19, 9), (8, 15, 9), (11, 19, 10),
          (12, 20, 10), (9, 17, 10), (14, 23, 11), (10, 20, 12), (17, 28, 13), (24, 36, 14),
          (26, 39, 15)],  # p. 139
    218: [(5, 9, 6), (6, 10, 6), (8, 12, 6), (6, 12, 8), (7, 13, 8), (10, 17, 9), (12, 19, 9),
          (8, 15, 9), (11, 19, 10), (12, 20, 10), (8, 16, 10), (9, 17, 10), (13, 22, 11),
          (14, 23, 11), (10, 20, 12), (14, 24, 12), (15, 26, 13), (16, 27, 13), (17, 28, 13),
          (18, 29, 13), (19, 30, 13), (16, 28, 14), (20, 32, 14), (24, 36, 14), (20, 33, 15),
          (22, 35, 15), (26, 39, 15), (24, 38, 16), (24, 39, 17), (26, 41, 17)],  # p. 140
    219: [(4, 6, 4), (5, 8, 5), (5, 9, 6), (8, 12, 6), (8, 13, 7), (6, 12, 8), (8, 15, 9),
          (14, 24, 12)],  # pp. 140-141
    220: [(8, 15, 9), (12, 20, 10), (10, 19, 11), (15, 24, 11), (8, 17, 11), (9, 18, 11),
          (12, 22, 12), (13, 23, 12), (14, 24, 12), (16, 26, 12), (17, 27, 12), (14, 25, 13),
          (15, 26, 13), (16, 27, 13), (17, 28, 13), (18, 29, 13), (21, 32, 13), (16, 28, 14),
          (17, 29, 14), (18, 30, 14), (19, 31, 14), (20, 32, 14), (21, 33, 14), (22, 34, 14),
          (23, 35, 14), (24, 36, 14), (18, 31, 15), (19, 32, 15), (20, 33, 15), (21, 34, 15),
          (22, 35, 15), (24, 37, 15), (25, 38, 15), (19, 33, 16), (23, 37, 16), (24, 38, 16),
          (25, 39, 16), (26, 40, 16), (27, 41, 16), (24, 39, 17), (25, 40, 17), (26, 41, 17),
          (27, 42, 17), (28, 43, 17), (29, 44, 17), (30, 45, 17), (26, 42, 18), (27, 43, 18),
          (28, 44, 18), (29, 45, 18), (30, 46, 18), (29, 46, 19), (32, 49, 19), (32, 50, 20),
          (34, 52, 20), (33, 52, 21), (36, 55, 21), (38, 58, 22), (37, 58, 23), (40, 61, 23),
          (42, 64, 24), (44, 67, 25)],  # pp. 141-143
    221: [(4, 6, 4), (5, 8, 5), (5, 9, 6), (8, 12, 6), (6, 12, 8)],  # p. 143
    222: [(5, 8, 5), (8, 12, 6), (10, 15, 7), (8, 13, 7), (9, 14, 7), (6, 12, 8), (12, 20, 10),
          (14, 23, 11), (17, 28, 13), (18, 29, 13), (24, 36, 14)],  # pp. 143-144
    223: [(5, 8, 5), (5, 9, 6), (6, 10, 6), (8, 12, 6), (10, 15, 7), (7, 12, 7), (8, 13, 7),
          (9, 14, 7), (10, 16, 8), (6, 12, 8), (7, 13, 8), (11, 19, 10), (12, 20, 10),
          (8, 16, 10), (9, 17, 10), (13, 22, 11), (10, 20, 12), (17, 28, 13), (16, 28, 14),
          (24, 36, 14)],  # p. 144
    224: [(8, 12, 6), (6, 12, 8), (12, 19, 9), (12, 20, 10), (14, 24, 12), (17, 28, 13),
          (24, 36, 14), (25, 39, 16)],  # pp. 144-145
    225: [(4, 6, 4), (5, 8, 5), (5, 9, 6), (8, 12, 6), (6, 12, 8), (14, 24, 12)],  # p. 145
    226: [(4, 6, 4), (5, 8, 5), (5, 9, 6), (8, 12, 6), (7, 12, 7), (6, 12, 8), (8, 15, 9)],  # p. 146
    227: [(4, 6, 4), (5, 8, 5), (6, 9, 5), (8, 12, 6), (10, 15, 7), (8, 13, 7), (9, 14, 7),
          (10, 20, 12), (12, 22, 12), (14, 24, 12), (16, 30, 16)],  # pp. 146-147
    228: [(6, 11, 7), (6, 12, 8), (12, 19, 9), (12, 20, 10), (10, 20, 12), (14, 24, 12),
          (15, 25, 12), (15, 26, 13), (17, 28, 13), (18, 29, 13), (17, 29, 14), (20, 32, 14),
          (24, 36, 14), (22, 35, 15), (24, 38, 16), (25, 39, 16)],  # p. 147
    229: [(4, 6, 4), (5, 8, 5), (6, 9, 5), (5, 9, 6), (7, 11, 6), (8, 12, 6), (10, 15, 7),
          (8, 13, 7), (9, 14, 7), (6, 12, 8), (11, 19, 10), (12, 20, 10), (9, 17, 10),
          (10, 20, 12), (17, 28, 13), (24, 36, 14)],  # p. 148
    230: [(8, 13, 7), (8, 14, 8), (10, 17, 9), (12, 20, 10), (10, 19, 11), (11, 20, 11),
          (12, 21, 11), (14, 23, 11), (12, 22, 12), (13, 23, 12), (14, 24, 12), (15, 25, 12),
          (16, 26, 12), (17, 27, 12), (19, 29, 12), (15, 26, 13), (17, 28, 13), (18, 29, 13),
          (19, 30, 13), (15, 27, 14), (16, 28, 14), (17, 29, 14), (18, 30, 14), (19, 31, 14),
          (20, 32, 14), (21, 33, 14), (22, 34, 14), (23, 35, 14), (24, 36, 14), (16, 29, 15),
          (19, 32, 15), (20, 33, 15), (21, 34, 15), (22, 35, 15), (23, 36, 15), (24, 37, 15),
          (21, 35, 16), (22, 36, 16), (23, 37, 16), (24, 38, 16), (25, 39, 16), (26, 40, 16),
          (20, 35, 17), (23, 38, 17), (24, 39, 17), (25, 40, 17), (26, 41, 17), (27, 42, 17),
          (28, 43, 17), (30, 45, 17), (25, 41, 18), (26, 42, 18), (27, 43, 18), (28, 44, 18),
          (29, 45, 18), (30, 46, 18), (25, 42, 19), (27, 44, 19), (28, 45, 19), (29, 46, 19),
          (30, 47, 19), (31, 48, 19), (32, 49, 19), (29, 47, 20), (30, 48, 20), (31, 49, 20),
          (32, 50, 20), (33, 51, 20), (34, 52, 20), (36, 54, 20), (32, 51, 21), (33, 52, 21),
          (34, 53, 21), (36, 55, 21), (34, 54, 22), (35, 55, 22), (36, 56, 22), (37, 57, 22),
          (38, 58, 22), (35, 56, 23), (36, 57, 23), (38, 59, 23), (39, 60, 23), (40, 61, 23),
          (38, 60, 24), (40, 62, 24), (42, 64, 24), (42, 65, 25), (44, 67, 25), (42, 66, 26),
          (44, 68, 26), (46, 70, 26), (48, 73, 27)],  # pp. 148-150
}
SCHMITT_FVECTORS[213] = SCHMITT_FVECTORS[212]  # enantiomorphic pair, one printed table

# Cross-checks of the digitization against Schmitt's own Sec. 2.3 remarks (printed pp. 151-154).
SCHMITT_MAXF_REMARKS = {197: 17, 198: 24, 199: 24, 205: 18, 206: 28, 210: 17, 212: 29,
                        214: 38, 220: 25, 227: 16, 228: 16}

# ---------------------------------------------------------------------------
# Ranking weights (all documented; deterministic).
# ---------------------------------------------------------------------------
W_FACET = 3.0          # per facet (higher = rarer; task: >20 notable, observed literature max 38)
B_F_GT20 = 10.0        # bonus if F > 20
W_AUT = 4.0            # * log2(combinatorial aut order)   (>1 = symmetric = prettier / more checkable)
W_STAB = 2.0           # * log2(max site-stabilizer order over sightings)  (special positions weighted up)
B_CORRIDOR = 6.0       # any sighting in a corridor group
B_SPECIAL_GROUP = 4.0  # any sighting in IT(220) or IT(230)
W_PNOV = 3.0           # * (#distinct face sizes outside {3,4,6}, capped at 3)
W_SIGHT = 1.5          # * log2(1 + #sightings)  (robustness of the sighting)
W_SPECIALPOS = 1.5     # * (3 - min stratum_dim over sightings)  (fixed Wyckoff point > line > plane > general)
W_VERT = 0.1           # * vertex count (mild; task lists vertex count as a feature)
B_SCHMITT_ABSENT = 5.0 # f-vector absent from EVERY sighted group's printed table (snapshot evidence only)


def pfmt(p):
    c = Counter(p)
    return " ".join(f"{g}^{c[g]}" for g in sorted(c))


def log2(x):
    return math.log2(x) if x > 0 else 0.0


def main():
    with open(STORE) as fh:
        store = json.load(fh)
    types = store["types"]

    lines_sanity = []
    kill_hits = []
    problems = []

    # --- Sanity 0: self-check the digitized Schmitt tables -------------------
    n_rows = 0
    for g in sorted(set(SCHMITT_FVECTORS) - {213}):
        rows = SCHMITT_FVECTORS[g]
        for (V, E, F) in rows:
            n_rows += 1
            if V - E + F != 2:
                problems.append(f"SCHMITT DIGITIZATION EULER FAIL group {g}: {(V, E, F)}")
        if len(set(rows)) != len(rows):
            problems.append(f"SCHMITT DIGITIZATION DUPLICATE ROW group {g}")
        maxF = max(F for (_, _, F) in rows)
        if g in SCHMITT_MAXF_REMARKS and maxF != SCHMITT_MAXF_REMARKS[g]:
            problems.append(
                f"SCHMITT DIGITIZATION MAXF MISMATCH group {g}: table max {maxF} != Sec2.3 remark {SCHMITT_MAXF_REMARKS[g]}")
    lines_sanity.append(
        f"- Schmitt digitization self-check: {n_rows} f-vector rows over 36 cubic groups "
        f"(212/213 shared), all Euler-consistent, no in-group duplicates, per-group max facet "
        f"counts agree with Schmitt's Sec. 2.3 remarks for the 11 groups he comments on: "
        + ("PASS" if not any(p.startswith("SCHMITT") for p in problems) else "FAIL (see problems)"))

    # --- Sanity 1-3: store checks -------------------------------------------
    for tid in sorted(types):
        t = types[tid]
        V, E, F = t["f_vector"]
        if V - E + F != 2:
            problems.append(f"EULER FAIL {tid}: f=({V},{E},{F})")
        if F > MAX_FACETS_KILL:
            kill_hits.append(f"KILL CRITERION {tid}: F={F} > {MAX_FACETS_KILL}")
        if len(t["p_vector"]) != F:
            problems.append(f"P-VECTOR LENGTH FAIL {tid}: |p|={len(t['p_vector'])} != F={F}")
        if sum(t["p_vector"]) != 2 * E:
            problems.append(f"P-VECTOR EDGE SUM FAIL {tid}: sum(p)={sum(t['p_vector'])} != 2E={2 * E}")
        for s in t["sightings"]:
            if t["aut_order"] % s["stabilizer_order"] != 0:
                problems.append(
                    f"STAB|AUT FAIL {tid}: stab {s['stabilizer_order']} does not divide aut {t['aut_order']} "
                    f"(group {s['group']}, point {tuple(s['point'])})")

    unmatched = sorted(tid for tid in types if not types[tid]["seeded"])
    seeded = sorted(tid for tid in types if types[tid]["seeded"])
    lines_sanity.append(f"- Euler V-E+F=2: checked for all {len(types)} stored types: "
                        + ("ALL PASS" if not any(p.startswith('EULER') for p in problems) else "FAIL"))
    lines_sanity.append(f"- p-vector consistency (|p|=F and sum(p)=2E) for all {len(types)} types: "
                        + ("ALL PASS" if not any(p.startswith('P-VECTOR') for p in problems) else "FAIL"))
    lines_sanity.append(f"- site-stabilizer divides aut, every sighting: "
                        + ("ALL PASS" if not any(p.startswith('STAB') for p in problems) else "FAIL"))
    maxF_store = max(t["f_vector"][2] for t in types.values())
    lines_sanity.append(f"- kill criterion (>38 facets): max stored facet count = {maxF_store}: "
                        + ("NO HITS" if not kill_hits else "HITS - QUARANTINE"))
    recount_note = (f"- recount: {len(unmatched)} unmatched + {len(seeded)} seeded = {len(types)} types; "
                    f"STATUS/PHASE1_RESULT claim 95 + 7 = 102: "
                    + ("MATCH" if (len(unmatched), len(seeded)) == (95, 7) else
                       f"DISCREPANCY (found {len(unmatched)}+{len(seeded)}) - reported, not forced"))
    lines_sanity.append(recount_note)

    # --- Features + score ----------------------------------------------------
    rows = []
    for tid in unmatched:
        t = types[tid]
        V, E, F = t["f_vector"]
        aut = t["aut_order"]
        sightings = t["sightings"]
        groups = sorted({s["group"] for s in sightings})
        max_stab = max(s["stabilizer_order"] for s in sightings)
        min_dim = min(s["stratum_dim"] for s in sightings)
        n_sight = len(sightings)
        nov_gons = sorted({g for g in t["p_vector"] if g not in SEEDED_GONS})
        fw = t["first_witness"]

        flags = {}
        for g in groups:
            tbl = SCHMITT_FVECTORS.get(g)
            if tbl is None:
                flags[g] = "U"
            else:
                flags[g] = "P" if (V, E, F) in tbl else "A"
        if all(v == "A" for v in flags.values()):
            schmitt_class = "ABSENT-all"
        elif any(v == "P" for v in flags.values()):
            schmitt_class = "present"
        else:
            schmitt_class = "UNKNOWN"

        score = (W_FACET * F
                 + (B_F_GT20 if F > 20 else 0.0)
                 + W_AUT * log2(aut)
                 + W_STAB * log2(max_stab)
                 + (B_CORRIDOR if any(g in CORRIDOR for g in groups) else 0.0)
                 + (B_SPECIAL_GROUP if any(g in SPECIAL_GROUPS for g in groups) else 0.0)
                 + W_PNOV * min(3, len(nov_gons))
                 + W_SIGHT * log2(1 + n_sight)
                 + W_SPECIALPOS * (3 - min_dim)
                 + W_VERT * V
                 + (B_SCHMITT_ABSENT if schmitt_class == "ABSENT-all" else 0.0))

        rows.append({
            "id": tid, "V": V, "E": E, "F": F, "aut": aut, "p": pfmt(t["p_vector"]),
            "groups": groups, "max_stab": max_stab, "min_dim": min_dim, "n_sight": n_sight,
            "nov": nov_gons, "fw": fw, "flags": flags, "schmitt": schmitt_class,
            "score": round(score, 2),
        })

    rows.sort(key=lambda r: (-r["score"], -r["F"], -r["aut"], r["id"]))

    # --- Per-group counts ----------------------------------------------------
    by_witness = Counter(r["fw"]["group"] for r in rows)
    by_sighted = Counter(g for r in rows for g in r["groups"])
    absent_all = [r for r in rows if r["schmitt"] == "ABSENT-all"]

    sym = {}
    for t in types.values():
        for s in t["sightings"]:
            sym[s["group"]] = s["group_symbol"]

    # --- TOP-10 why lines ----------------------------------------------------
    def why(r):
        bits = []
        bits.append(f"{r['F']} facets")
        if r["aut"] > 1:
            bits.append(f"aut {r['aut']}")
        cg = [g for g in r["groups"] if g in CORRIDOR]
        if cg:
            bits.append("corridor " + "/".join(f"{g} {sym[g]}" for g in cg))
        sg = [g for g in r["groups"] if g in SPECIAL_GROUPS and g not in cg]
        if sg:
            bits.append("+".join(f"{g} {sym[g]}" for g in sg))
        if r["nov"]:
            bits.append("faces incl. " + ",".join(f"{g}-gon" for g in r["nov"]))
        if r["min_dim"] <= 1:
            bits.append(f"special-position stratum (dim {r['min_dim']}, stab {r['max_stab']})")
        bits.append(f"{r['n_sight']} sighting(s)")
        bits.append("Schmitt f-vec ABSENT in sighted group(s)" if r["schmitt"] == "ABSENT-all"
                    else "Schmitt f-vec present -> G5 type-level check")
        return "; ".join(bits)

    top10 = rows[:10]

    # --- Emit ----------------------------------------------------------------
    out = []
    out.append(f"# TRIAGE result — Phase-1 unmatched types -> G4 shortlist ({RUN_DATE})\n")
    out.append("Script: `triage_phase1.py` (deterministic; byte-identical across re-runs). "
               "Store: `phase1_types.json` (Phase-1 ACCEPTED 2026-08-29). Gates: `../ANCHORS.md` "
               "G4 (finalist certificates) and G5 (novelty diligence — NOT run here).\n")
    out.append(f"**LANGUAGE (G5): every type below is \"not matched against the catalog snapshot of "
               f"{CATALOG_SNAPSHOT}\". No novelty claim. The Schmitt column is f-vector-level evidence "
               "from his printed in-text tables (a 351-CPU-year grid SAMPLING, not an enumeration): "
               "\"A\" = absent there (stronger candidate, still only snapshot language), \"P\" = present "
               "(same f-vector does NOT mean same type — the Josehedron/Schmitt-220 pair proves this — "
               "so a G5 type-level check is required).**\n")

    out.append("## Sanity duties\n")
    out.extend(lines_sanity)
    if kill_hits:
        out.append("\n### KILL-CRITERION HITS\n")
        out.extend(f"- {k}" for k in kill_hits)
    if problems:
        out.append("\n### PROBLEMS (reported, not forced)\n")
        out.extend(f"- {p}" for p in problems)
    out.append("")

    out.append("## Schmitt in-text table digitization (new this step)\n")
    out.append("All 36 cubic per-group f-vector tables from Schmitt 2016 Sec. 2.2.5 "
               "(`references/Schmitt_2016_dissertation.pdf`, printed pp. 119-150, PDF pages 124-155) "
               f"were transcribed at f-vector level into `triage_phase1.py` ({n_rows} rows; 212/213 share "
               "one printed table for the enantiomorphic pair). Verification applied: every row passes "
               "Euler; per-group max facet counts agree with Schmitt's own Sec. 2.3 discussion for all 11 "
               "groups he comments on (197,198,199,205,206,210,212,214,220,227,228). LIMIT: single-pass "
               "visual transcription, not yet independently double-keyed — flags are provisional; an "
               "independent re-key is queued as a G5 duty. The previously banked IT(220) row "
               "f=(12,22,12) (SCHMITT_220_CHECK_RESULT.md) is contained in the digitized 220 table: "
               f"{'CONSISTENT' if (12, 22, 12) in SCHMITT_FVECTORS[220] else 'INCONSISTENT'}.\n")

    out.append("## TOP-10 G4 SHORTLIST\n")
    for i, r in enumerate(top10, 1):
        fwp = "(" + ", ".join(r["fw"]["point"]) + ")"
        out.append(f"{i}. `{r['id']}` — **{r['fw']['group']} {sym[r['fw']['group']]}** at {fwp}, "
                   f"f=({r['V']}, {r['E']}, {r['F']}), p={r['p']}, aut={r['aut']} "
                   f"[score {r['score']}]  \n   {why(r)}")
    out.append("")

    out.append("## Full ranked table (all unmatched types)\n")
    out.append("Schmitt column: per sighted group, P = f-vector in his printed table for that group, "
               "A = absent, U = table not digitized. min-dim: 0 fixed Wyckoff point / 1 line sample / "
               "2 plane sample / 3 general position (minimum over sightings).\n")
    out.append("| rank | id | f-vector | p-vector | aut | witness | stab | min-dim | sgt | sighted groups | Schmitt | score |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        flag_s = " ".join(f"{g}:{r['flags'][g]}" for g in r["groups"])
        out.append(f"| {i} | `{r['id']}` | ({r['V']}, {r['E']}, {r['F']}) | {r['p']} | {r['aut']} "
                   f"| {r['fw']['group']} {sym[r['fw']['group']]} | {r['max_stab']} | {r['min_dim']} "
                   f"| {r['n_sight']} | {flag_s} | {r['schmitt']} | {r['score']} |")
    out.append("")

    out.append("## f-vectors ABSENT from every sighted group's printed Schmitt table "
               f"({len(absent_all)} of {len(rows)})\n")
    for r in absent_all:
        out.append(f"- `{r['id']}` f=({r['V']}, {r['E']}, {r['F']}) p={r['p']} aut={r['aut']} — sighted in "
                   + ", ".join(f"{g} {sym[g]}" for g in r["groups"])
                   + " — his grid sampled these groups without printing this f-vector (evidence, not proof).")
    out.append("")

    out.append("## Per-group counts (unmatched types)\n")
    out.append("| group | symbol | corridor | first-witness here | sighted here |")
    out.append("|---|---|---|---|---|")
    for g in sorted(by_sighted):
        out.append(f"| {g} | {sym[g]} | {'Y' if g in CORRIDOR else ''} | {by_witness.get(g, 0)} | {by_sighted[g]} |")
    out.append("")

    out.append("## Ranking recipe (all weights explicit, deterministic)\n")
    out.append(f"score = {W_FACET}*F + {B_F_GT20}*[F>20] + {W_AUT}*log2(aut) + {W_STAB}*log2(max stab) "
               f"+ {B_CORRIDOR}*[corridor sighting] + {B_SPECIAL_GROUP}*[sighted in 220 or 230] "
               f"+ {W_PNOV}*min(3, #face sizes outside {{3,4,6}}) + {W_SIGHT}*log2(1+#sightings) "
               f"+ {W_SPECIALPOS}*(3 - min stratum dim) + {W_VERT}*V + {B_SCHMITT_ABSENT}*[Schmitt ABSENT-all]. "
               "Tie-break: F desc, aut desc, id asc. Weights are triage judgment, not measurements; "
               "they are stated so the ranking is reproducible and criticizable.\n")

    out.append("## Honest limits\n")
    out.append("- The Schmitt cross-check is F-VECTOR level only (his in-text tables stop there); type-level "
               "diligence (canonical-code comparison at his generating points, the schmitt_220_check.py "
               "pattern) is a G5 duty for every shortlisted type flagged P. His results storage/14TB data "
               "is not recoverable online (SCHMITT_DATA_RECOVERY_2026-08-28.md), so printed tables + our "
               "recomputation at his points is the achievable bar.")
    out.append("- The digitized tables are a single-pass visual transcription (Euler- and remark-checked, "
               "but not double-keyed). Any G5 verdict that leans on a specific P/A cell must first re-read "
               "that printed page.")
    out.append("- A type sighted only at special positions may exist in Schmitt's unprinted data even when "
               "flagged A: his table prints one representative point per f-vector and his grid was dense "
               "in general position; conversely P does not kill a candidate (different type, same f-vector).")
    out.append("- Aut orders are combinatorial map automorphism counts; geometric stabilizer certification "
               "is G4/V2, not claimed. Roundness (the beatable 47.98% benchmark) is NOT computed here — it "
               "needs exact metric cells and belongs with the G4 certificate work.")
    out.append("- Features NOT computed: roundness/isoperimetric quotient, geometric symmetry group, "
               "polyform counts (G4 Burnside), Wyckoff letter identification for witness points, "
               "Engel-1981 cross-check (Tyler-gated, priority recalibrated down), Bernhard Fig. 12 "
               "type-level diff (G5 (d)).")
    out.append("- The ranking weights are stated judgment calls; re-ranking under different weights is "
               "one `triage_phase1.py` edit away and does not touch the store.")
    out.append("")

    with open(OUT, "w") as fh:
        fh.write("\n".join(out))

    print(f"wrote {OUT}")
    print(f"unmatched={len(unmatched)} seeded={len(seeded)} problems={len(problems)} kill_hits={len(kill_hits)}")
    print(f"schmitt ABSENT-all: {len(absent_all)}")
    for i, r in enumerate(top10, 1):
        print(f"  top{i:2d} {r['id']} grp {r['fw']['group']} f=({r['V']},{r['E']},{r['F']}) aut {r['aut']} "
              f"schmitt {r['schmitt']} score {r['score']}")
    if problems or kill_hits:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
