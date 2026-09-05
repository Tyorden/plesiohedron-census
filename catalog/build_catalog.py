#!/usr/bin/env python3
"""
MINT Track 3 - THE CATALOG. build_catalog.py  (v5, 2026-09-04)

Builds catalog.json + catalog.csv: one row per exact-confirmed combinatorial
type in the program's dedupe stores (phase-1 cubic sweep, phase-2 tetragonal
sweep, phase-2 batch-2 hexagonal-family sweep). Read-only on every input. Exact
arithmetic (fractions.Fraction) wherever a number is derived; all coordinates
are kept as the exact rational strings the stores carry.

VERSION NOTE. v1 (2026-09-04, subagent #141, accepted by the main session the
same day) read the cubic + tetragonal stores only (891 types). v2 adds the
hexagonal-family store (1,583 types), the two accepted phase-2 G4 batches
(14 tetragonal + 151 hexagonal certificates) and the hexagonal Schmitt
digitization. v1 behaviour is NOT kept behind a flag: it is reproducible from
the previous git version of this file,
    git show 06e5d30:paper_prep/MINT_plesiohedron/catalog/build_catalog.py
(commit 06e5d30 "THE CATALOG (MINT Track 3) final state, verified"). Every v1
column keeps its name and its catalog_id; for the 891 v1 types a v1 value
changes ONLY where hexagonal-family evidence or the accepted tetragonal G4
batch was added (systems_sighted, gate_G3 sighting counts,
schmitt_fvector_present/absent_in_sighted_groups and the flag,
schmitt_type_level_status/detail, gate_G4_certified for the 14 tetragonal
certificates); the v1 summary numbers are asserted unchanged below.

v3 (2026-09-04, subagent #150, Claude Fable 5.1) adds the COMPUTED open/wall
verdicts of the 165 G4-certified phase-2 cells (harness/phase2/
WALL_OPEN_PHASE2.json, agent #148 under the scheme pre-registered in ANCHORS.md
2026-09-04, accepted by the main session 2026-09-04 14:10) next to the 7 cubic
c1 verdicts, and a type-level Schmitt status read from the two phase-2
collision screens. v2 behaviour is NOT kept behind a flag: it is reproducible
from the previous git version of this file,
    git show 169ccb4:paper_prep/MINT_plesiohedron/catalog/build_catalog.py
(commit 169ccb4 "THE CATALOG v2 ... verified"). Every v1 and v2 column keeps
its name, its position and its value (the v2 open_wall / open_wall_source pair
included, verbatim); v3 only APPENDS columns (open_wall_verdict,
open_wall_verdict_source, open_wall_point_verdict, open_wall_metric_verdict,
open_wall_flags, open_wall_verdict_pointer, open_wall_scheme,
open_wall_scheme_date, schmitt_type_status, schmitt_type_status_source),
summary blocks (open_wall_verdict_counts, open_wall_verdict_source_counts,
schmitt_type_status_counts, open_wall_x_schmitt_type_status, naming_pool) and
field_sources entries; the v1 AND v2 summary numbers are asserted unchanged
below. NOTE on names: the task's "open_wall_source (c1 cubic / phase2 #148 /
none)" would collide with the v2 column of that name, so the short source
token lives in open_wall_verdict_source and the v2 column is untouched.

v4 (2026-09-04, subagent #152, Claude Fable 5.1) folds in the STORE-SIDE
collision-screen status of ALL 404 menu-sighted tetragonal-first types
(harness/collision_phase2_tetragonal_storeside.json: the hexagonal screen's
store-side rule applied to the tetragonal family, its hexagonal equivalence
asserted 151/124/13 first; dated addendum in COLLISION_PHASE2_RESULTS.md), so
schmitt_type_status carries the same semantics in both phase-2 families: the
389 tetragonal 'not-screened' values of v3 become SURVIVOR / COLLISION /
UNRESOLVED; the 15 shortlist statuses are asserted unchanged (14 SURVIVOR = the
14 certificates, 1 COLLISION). v3 behaviour is NOT kept behind a flag: it is
reproducible from the previous git version of this file,
    git show e01618b:paper_prep/MINT_plesiohedron/catalog/build_catalog.py
(commit e01618b "Pool ranking ... + catalog v3 (open/wall + type status) - both
verified"). No column is added or renamed; only the values of
schmitt_type_status / schmitt_type_status_source change, for those 389
tetragonal rows (the 15 shortlist rows gain a v4 clause in the source text);
the schmitt_type_status_counts and open_wall_x_schmitt_type_status summary
blocks follow; one summary block and one inputs entry are added; every other
v1 / v2 / v3 summary number is asserted unchanged and the naming pool is
asserted still 13 tetragonal + 102 hexagonal-family.

v5 (2026-09-04, subagent #154, Claude Fable 5.1) settles the 106 tetragonal
UNRESOLVED statuses of v4: the 62 unstored printed rows they hung on were
recomputed at the printed points with the documented setting conversions
(harness/collision_phase2_tetragonal_rows_recompute.py -> collision_phase2_
tetragonal_rows_recomputed.json, every computed cell; collision_phase2_
tetragonal_unresolved_overlay.json, the 106 verdicts; dated addendum in
COLLISION_PHASE2_RESULTS.md). Per type: any hung-on row SAME -> COLLISION;
all rows reproduced and DIFFERENT -> SURVIVOR; any row quarantined -> stays
UNRESOLVED. v4 behaviour is NOT kept behind a flag: it is reproducible from
    git show 27e0083:paper_prep/MINT_plesiohedron/catalog/build_catalog.py
(commit 27e0083 "Tetragonal store-side S-cell rule + catalog v4 (#152
verified)"). No column is added or renamed; only the schmitt_type_status /
schmitt_type_status_source values of the 106 v4-UNRESOLVED tetragonal-first
rows change (their source text gains a [v5] clause); the two summary blocks
that count them follow; one summary block and one inputs entry are added;
every other v1 / v2 / v3 / v4 summary number is asserted unchanged, the 15
shortlist statuses (14 SURVIVOR = the 14 certificates, 1 COLLISION) are
asserted untouched (none of them was UNRESOLVED) and the naming pool is
asserted still 13 tetragonal + 102 hexagonal-family.

INPUTS (read-only; absolute paths resolved from this file's location):
  harness/phase1_types.json            cubic store (102 types, 1,597 orbits)
  harness/phase2_types.json.gz         tetragonal store (891 types; sha256 verified
                                       against harness/phase2_types.SHA256SUMS
                                       before use; the raw .json is used only if
                                       present AND its sha256 matches)
  harness/phase2_hexagonal_types.json.gz  hexagonal-family store (1,583 types =
                                       891 prior + 692 hexagonal-first; the .gz is
                                       the committed form; decompressed bytes hashed
                                       against phase2_hexagonal_types.SHA256SUMS
                                       (raw line) and the .gz against its own line)
  harness/spacegroups.json             frozen G1 space-group table (symbols, systems)
  harness/triage_phase1.py             SCHMITT_FVECTORS (cubic digitization of
                                       Schmitt 2016 Sec. 2.2.5, 881 rows) - read by
                                       ast literal parsing, never imported
  harness/rekey_tables.json            G5 independent re-key of six cubic tables
  harness/schmitt_tetragonal_tables.json  tetragonal digitization (1,476 rows)
  harness/schmitt_hexagonal_tables.json   trigonal + hexagonal digitization (958 rows,
                                       45 blocks; 7 enantiomorphic pairs share a table;
                                       points printed in Schmitt's B'' basis)
  harness/SCHMITT_COLLISION_RESULTS.md, harness/CROSS_GROUP_RESULTS.md,
  harness/collision_phase2_results.json,
  harness/collision_phase2_hex_results.json  type-level verdicts at printed points
  harness/collision_phase2_tetragonal_storeside.json  v4: store-side status of all
                                       404 menu-sighted tetragonal types (md5
                                       asserted == the addendum's stated value)
  harness/phase2_hex_schmitt_180_check.json  read-only re-run of the 46 IT(180)
                                       rows (z -> -z then H1; cells already stored)
  harness/TRIAGE_PHASE2_HEX_RESULT.md, harness/triage_phase2_hex_shortlist.json
                                       store-side collision-screen verdicts for the
                                       288 menu-sighted hexagonal-first types
  harness/g4_tables_<id>.json, track4/g4_tables_laves17.json,
  harness/g4p2_tables_<id>.json, harness/g4p2hex_tables_<id>.json
                                       G4 certificate tables (existence + n_improper)
  harness/G4_PHASE2_RESULTS.md, harness/G4_PHASE2_HEX_RESULTS.md,
  harness/g4p2hex_cells/<id>.json      solid chirality from the V2 rung
  harness/round1_computations/c1_wall_open.json  open/wall for the 7 cubic finalists
  harness/phase2/WALL_OPEN_PHASE2.json (+ .md)  v3: computed open/wall verdicts of the
                                       165 G4-certified phase-2 cells (agent #148;
                                       file md5 asserted == the value the .md states)
  harness/COLLISION_PHASE2_RESULTS.md, harness/COLLISION_PHASE2_HEX_RESULTS.md
                                       v3: per-type summary lines asserted == the
                                       JSON-derived schmitt_type_status
  publication/PUBLICATION_STATUS.md (names, by folder convention)
  paper/wyckoff_check.txt              spglib Wyckoff letters for the 7 finalists

FIELD PROVENANCE is written into catalog.json under "field_sources" so that
every column names the store field it came from; a column whose source is
absent from the stores is null and says so in "field_sources".

LANGUAGE: every non-seeded type is "not matched against the records checked as
of 2026-09-04"; f-vector agreement is NOT type identity; Schmitt's survey is a
sampling, not an enumeration (ANCHORS.md G5 amendment); G4 is not novelty.
"""

import ast
import csv
import gzip
import hashlib
import json
import os
import re
import sys
from collections import Counter, OrderedDict, defaultdict
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # paper_prep/MINT_plesiohedron
HARNESS = os.path.join(ROOT, "harness")
TRACK4 = os.path.join(ROOT, "track4")
PUBLICATION = os.path.join(ROOT, "publication")
PAPER = os.path.join(ROOT, "paper")

SNAPSHOT = "2026-09-04"
BUILD_LABEL = "MINT Track 3 catalog build v5 (2026-09-04): cubic + tetragonal + hexagonal family + computed open/wall + type-level Schmitt status (both phase-2 families store-side; the 62 unstored tetragonal rows recomputed, no UNRESOLVED left)"
CATALOG_VERSION = 5

P1_PATH = os.path.join(HARNESS, "phase1_types.json")
P2_RAW = os.path.join(HARNESS, "phase2_types.json")
P2_GZ = os.path.join(HARNESS, "phase2_types.json.gz")
P2_SUMS = os.path.join(HARNESS, "phase2_types.SHA256SUMS")
HX_RAW = os.path.join(HARNESS, "phase2_hexagonal_types.json")
HX_GZ = os.path.join(HARNESS, "phase2_hexagonal_types.json.gz")
HX_SUMS = os.path.join(HARNESS, "phase2_hexagonal_types.SHA256SUMS")
SG_PATH = os.path.join(HARNESS, "spacegroups.json")
TRIAGE1 = os.path.join(HARNESS, "triage_phase1.py")
REKEY = os.path.join(HARNESS, "rekey_tables.json")
TET_TABLES = os.path.join(HARNESS, "schmitt_tetragonal_tables.json")
HEX_TABLES = os.path.join(HARNESS, "schmitt_hexagonal_tables.json")
COLL_CUBIC = os.path.join(HARNESS, "SCHMITT_COLLISION_RESULTS.md")
XGROUP = os.path.join(HARNESS, "CROSS_GROUP_RESULTS.md")
COLL_TET = os.path.join(HARNESS, "collision_phase2_results.json")
COLL_HEX = os.path.join(HARNESS, "collision_phase2_hex_results.json")
COLL_TET_SS = os.path.join(HARNESS, "collision_phase2_tetragonal_storeside.json")   # v4
COLL_TET_OV = os.path.join(HARNESS, "collision_phase2_tetragonal_unresolved_overlay.json")   # v5: the 106 verdicts
COLL_TET_ROWS = os.path.join(HARNESS, "collision_phase2_tetragonal_rows_recomputed.json")    # v5: the 62 rows, every cell
HEX180 = os.path.join(HARNESS, "phase2_hex_schmitt_180_check.json")
TRIAGE_HEX_MD = os.path.join(HARNESS, "TRIAGE_PHASE2_HEX_RESULT.md")
TRIAGE_HEX_JSON = os.path.join(HARNESS, "triage_phase2_hex_shortlist.json")
G4P2_MD = os.path.join(HARNESS, "G4_PHASE2_RESULTS.md")
G4HEX_MD = os.path.join(HARNESS, "G4_PHASE2_HEX_RESULTS.md")
G4HEX_CELLS = os.path.join(HARNESS, "g4p2hex_cells")
C1_WALL = os.path.join(HARNESS, "round1_computations", "c1_wall_open.json")
WALL_OPEN_JSON = os.path.join(HARNESS, "phase2", "WALL_OPEN_PHASE2.json")
WALL_OPEN_MD = os.path.join(HARNESS, "phase2", "WALL_OPEN_PHASE2.md")
COLL_TET_MD = os.path.join(HARNESS, "COLLISION_PHASE2_RESULTS.md")
COLL_HEX_MD = os.path.join(HARNESS, "COLLISION_PHASE2_HEX_RESULTS.md")
WYCKOFF = os.path.join(PAPER, "wyckoff_check.txt")

OUT_JSON = os.path.join(HERE, "catalog.json")
OUT_CSV = os.path.join(HERE, "catalog.csv")
OUT_SIGHTINGS = os.path.join(HERE, "catalog_sightings.json.gz")

CUBIC_FIRST = "cubic (phase 1 store)"
TET_FIRST = "tetragonal (phase 2)"
HEX_FIRST = "hexagonal (phase 2 batch 2)"
HEX_GROUPS = list(range(143, 195))

# v1 summary numbers (catalog.json v1, accepted 2026-09-04): asserted unchanged in v2
V1_SUMMARY = dict(n_types_cubic_first=102, n_types_tetragonal_first=789, n_seeded=7,
                  n_seeded_never_sighted=1, n_tetragonal_first_menu_sighted=404,
                  n_tetragonal_first_schmitt_printed_only=385, n_cubic_first_resighted_tetragonal=19,
                  n_cubic_first_resighted_tetragonal_menu=18, max_F_cubic_first=23,
                  max_F_tetragonal_menu=26, max_F_tetragonal_first=35,
                  n_distinct_fvectors_cubic_first=65, n_distinct_fvectors_tetragonal_first=153)
# v2 summary numbers (catalog.json v2, accepted 2026-09-04 14:35): asserted unchanged in v3
V2_SUMMARY = dict(n_types_total=1583, n_types_hexagonal_first=692, n_hexagonal_first_menu_sighted=288,
                  n_hexagonal_first_schmitt_printed_only=404, n_prior_resighted_hexagonal=43,
                  n_prior_resighted_hexagonal_menu=34, n_cubic_first_resighted_hexagonal=17,
                  n_tetragonal_first_resighted_hexagonal=26, n_G4_certified_accepted=177,
                  n_G4_provisional_tables_present=0, max_F_all=35, max_F_hexagonal_menu=24,
                  max_F_hexagonal_first=34, n_distinct_fvectors=196, n_distinct_fvectors_hexagonal_first=167,
                  n_named_program=2, n_held=3, n_descriptive_pending=2,
                  per_system_types_sighted={"cubic": 99, "tetragonal": 808, "hexagonal": 735})
V2_CHIRAL = dict(solid_chiral=153, solid_achiral=12, honeycomb_chiral=138, honeycomb_achiral=39)
V2_HEXMATCH = dict(hexagonal_first_SURVIVOR=151, hexagonal_first_COLLISION=124, hexagonal_first_UNRESOLVED=13,
                   hexagonal_first_S_cell_printed_only=404, prior_resighted_in_family=43, no_hexagonal_sighting=848)

# v3 value sets
OW_VERDICTS = ("OPEN", "WALL", "ONE-SIDED", "not-computed")
OW_SOURCES = ("c1 cubic", "phase2 #148", "none")
TS_VALUES = ("SURVIVOR", "COLLISION", "UNRESOLVED", "printed-only", "not-screened")
FAMILIES = ("cubic", "tetragonal", "hexagonal")
PHASE2_SCHEME = ("pre-registered 2026-09-04 (ANCHORS.md block 'PERTURBATION CLASSIFICATION, PHASE 2', appended BEFORE the run): "
                 "POINT along the witness stratum's tangent basis (primitive integer nullspace basis of the site stabilizer, c1 nullspace_basis verbatim), "
                 "steps +-1/48, +-1/96 in fractional coordinates of the ITA conventional cell (hexagonal basis for IT 143-194), halving to 1/1536 on any side whose smallest step is not SAME; "
                 "METRIC c/a -> c/a(1 + eps), eps +-1/96, +-1/192 (relative), halving to 1/3072; side status at the finest step tested (SAME / DIFFERENT / QUARANTINE); "
                 "OPEN = every side SAME; WALL = both sides DIFFERENT in some direction; ONE-SIDED = some side DIFFERENT but no direction on both sides; INDETERMINATE = a QUARANTINE side (none occurred); "
                 "chain = the accepted sweep_phase2_tetragonal.evaluate / sweep_phase2_hexagonal.evaluate unchanged; first witness only; OPEN means 'holds on the tested neighbourhood', never an interval proof")
C1_SCHEME = ("c1 round-1 scheme (harness/round1_computations/c1_wall_open.md / c1_wall_open.py, run 2026-09-03, banked PROGRAM_LEDGER 2026-09-03 'shapes paper round 1 accepted'; not pre-registered): "
             "POINT along the Wyckoff-stratum tangent basis, steps +-1/96, +-1/48 (fractional, conventional cell), halving to 1/1536 on a changing side; no metric direction (cubic); "
             "OPEN = every side SAME; WALL = both sides changed in some direction; ONE-SIDED otherwise; first witness only; finite steps")


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_phase2():
    """Load the tetragonal store with the SHA256 discipline from the task."""
    # SHA256SUMS holds ONE line: "phase2_types.json  sha256 <hex>  (raw ...)" = the
    # sha256 of the RAW (decompressed) store. The .gz is verified by decompressing it
    # and hashing the bytes; the raw file, if present, must hash to the same value.
    text = open(P2_SUMS).read()
    m = re.search(r"phase2_types\.json\s+sha256\s+([0-9a-f]{64})", text)
    if not m:
        sys.exit("FATAL: cannot parse phase2_types.SHA256SUMS")
    expected = m.group(1)
    gz_sha = sha256_file(P2_GZ)
    raw_bytes = gzip.open(P2_GZ, "rb").read()
    dec_sha = hashlib.sha256(raw_bytes).hexdigest()
    if dec_sha != expected:
        sys.exit(f"FATAL: decompressed phase2_types.json.gz sha256 {dec_sha} != SHA256SUMS {expected}")
    if os.path.exists(P2_RAW):
        raw_sha = sha256_file(P2_RAW)
        if raw_sha != expected:
            sys.exit(f"FATAL: raw phase2_types.json sha256 {raw_sha} != SHA256SUMS {expected}")
    data = json.loads(raw_bytes.decode("utf-8"))
    return data, {"used": "phase2_types.json.gz (decompressed in memory; sha256 of the decompressed bytes verified against phase2_types.SHA256SUMS)",
                  "gz_file_sha256": gz_sha, "raw_sha256": dec_sha, "sha256sums_expected": expected}


def load_hexagonal():
    """Load the hexagonal-family store. SHA256SUMS holds TWO lines: the raw store's
    sha256 and the .gz file's sha256. Both are verified; the raw file, if present,
    must hash to the raw line."""
    text = open(HX_SUMS).read()
    m_raw = re.search(r"phase2_hexagonal_types\.json\s+sha256\s+([0-9a-f]{64})", text)
    m_gz = re.search(r"phase2_hexagonal_types\.json\.gz\s+sha256\s+([0-9a-f]{64})", text)
    if not (m_raw and m_gz):
        sys.exit("FATAL: cannot parse phase2_hexagonal_types.SHA256SUMS")
    exp_raw, exp_gz = m_raw.group(1), m_gz.group(1)
    gz_sha = sha256_file(HX_GZ)
    if gz_sha != exp_gz:
        sys.exit(f"FATAL: phase2_hexagonal_types.json.gz sha256 {gz_sha} != SHA256SUMS {exp_gz}")
    raw_bytes = gzip.open(HX_GZ, "rb").read()
    dec_sha = hashlib.sha256(raw_bytes).hexdigest()
    if dec_sha != exp_raw:
        sys.exit(f"FATAL: decompressed phase2_hexagonal_types.json.gz sha256 {dec_sha} != SHA256SUMS {exp_raw}")
    if os.path.exists(HX_RAW):
        raw_sha = sha256_file(HX_RAW)
        if raw_sha != exp_raw:
            sys.exit(f"FATAL: raw phase2_hexagonal_types.json sha256 {raw_sha} != SHA256SUMS {exp_raw}")
    data = json.loads(raw_bytes.decode("utf-8"))
    return data, {"used": "phase2_hexagonal_types.json.gz (the committed form; decompressed in memory; sha256 of the decompressed bytes verified against the raw line of phase2_hexagonal_types.SHA256SUMS and the .gz file against its own line)",
                  "gz_file_sha256": gz_sha, "raw_sha256": dec_sha, "sha256sums_expected_raw": exp_raw, "sha256sums_expected_gz": exp_gz}


def frac(s):
    return Fraction(s)


def pvec_str(p):
    c = Counter(p)
    return " ".join(f"{k}^{c[k]}" for k in sorted(c))


def euler_ok(f):
    v, e, F = f
    return v - e + F == 2


def load_schmitt_cubic():
    """SCHMITT_FVECTORS from triage_phase1.py via ast (no import, no execution)."""
    src = open(TRIAGE1).read()
    tree = ast.parse(src)
    fv = None
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == "SCHMITT_FVECTORS" for t in node.targets):
            fv = ast.literal_eval(node.value)
            break
    if fv is None:
        sys.exit("FATAL: SCHMITT_FVECTORS not found in triage_phase1.py")
    # the alias line: SCHMITT_FVECTORS[213] = SCHMITT_FVECTORS[212]
    if "SCHMITT_FVECTORS[213] = SCHMITT_FVECTORS[212]" not in src:
        sys.exit("FATAL: expected 213->212 alias line missing in triage_phase1.py")
    fv[213] = fv[212]
    return {g: [tuple(r) for r in rows] for g, rows in fv.items()}


def load_schmitt_blocks(path):
    """Tetragonal and hexagonal digitizations share one schema: {block: {groups, rows}}."""
    d = json.load(open(path))
    by_group = {}      # group -> list of rows (f, b, pt, pdf_page, block)
    block_of = {}
    for key, blk in d.items():
        if key == "_meta":
            continue
        for g in blk["groups"]:
            block_of[g] = key
            by_group[g] = [dict(f=tuple(r["f"]), b=r["b"], pt=tuple(r["pt"]),
                                pdf_page=r.get("pdf_page"), block=key) for r in blk["rows"]]
    return by_group, block_of, d["_meta"]


def parse_md_verdicts(path, pair_prefix):
    """Parse the verdict tables of SCHMITT_COLLISION_RESULTS.md / CROSS_GROUP_RESULTS.md.
    Returns list of dicts: pair, target, group, fvec, verdict ('SAME'/'DIFFERENT'),
    other_stored (id if the printed cell equals a different stored type)."""
    out = []
    for line in open(path):
        if not line.startswith(f"| {pair_prefix}"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        # verdict tables have a backticked target id in column 2 or 3
        ids = re.findall(r"`([0-9a-f]{16})`", line)
        if not ids or "TYPE" not in line:
            continue
        target = ids[0]
        m_group = re.search(r"\|\s*(\d{3})\s*\|", line)
        group = int(m_group.group(1)) if m_group else None
        m_f = re.search(r"\((\d+),\s*(\d+),\s*(\d+)\)", line)
        fvec = tuple(int(x) for x in m_f.groups()) if m_f else None
        verdict = "SAME" if "SAME TYPE" in line else ("DIFFERENT" if "DIFFERENT TYPE" in line else None)
        other = None
        m_o = re.search(r"= stored type `([0-9a-f]{16})`", line)
        if m_o:
            other = m_o.group(1)
        out.append(dict(pair=cells[0], target=target, group=group, fvec=fvec,
                        verdict=verdict, other_stored=other, source=os.path.basename(path)))
    return out


def parse_triage_hex_verdicts():
    """Full ranked table of TRIAGE_PHASE2_HEX_RESULT.md: rank, id, ..., verdict (col 17)."""
    out = OrderedDict()
    in_table = False
    for line in open(TRIAGE_HEX_MD):
        if line.startswith("## Full ranked table"):
            in_table = True
            continue
        if in_table and line.startswith("## "):
            break
        m = re.match(r"^\| (\d+) \| `([0-9a-f]{16})` \|", line)
        if in_table and m:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            assert len(cells) == 18, (len(cells), line[:80])
            out[m.group(2)] = dict(rank=int(m.group(1)), ow_label=cells[14], schmitt_flag=cells[15], verdict=cells[16])
    return out


def parse_g4p2_chirality():
    """'Isometry vs site vs aut summary' table of G4_PHASE2_RESULTS.md -> {id: 'chiral'/'achiral'}."""
    out = {}
    in_table = False
    for line in open(G4P2_MD):
        if line.startswith("## Isometry vs site vs aut summary"):
            in_table = True
            continue
        if in_table and line.startswith("## "):
            break
        m = re.match(r"^\| (\d+) \| `([0-9a-f]{16})` \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (chiral|achiral) \|", line)
        if in_table and m:
            out[m.group(2)] = m.group(8)
    return out


def parse_g4hex_chirality():
    """Summary table of G4_PHASE2_HEX_RESULTS.md -> {id: 'chiral'/'achiral'} (column 'chiral?')."""
    out = {}
    in_table = False
    for line in open(G4HEX_MD):
        if line.startswith("## Summary table"):
            in_table = True
            continue
        if in_table and line.startswith("## "):
            break
        m = re.match(r"^\| (\d+) \| `([0-9a-f]{16})` \|", line)
        if in_table and m:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            assert cells[6:11] == ["PASS"] * 5, line[:120]
            assert cells[11] in ("chiral", "achiral"), line[:120]
            out[m.group(2)] = cells[11]
    return out


def load_wyckoff():
    """paper/wyckoff_check.txt -> {(group, point_tuple): (letter, site_sym)}"""
    res = {}
    if not os.path.exists(WYCKOFF):
        return res
    for line in open(WYCKOFF):
        m = re.search(r"package IT\((\d+)\) \S+ gen \(([^)]*)\).*wyckoff \['(\w)'\]; site sym \['([^']*)'\]", line)
        if m:
            g = int(m.group(1))
            pt = tuple(x.strip() for x in m.group(2).split(","))
            res[(g, pt)] = (m.group(3), m.group(4))
    return res


# ---------------------------------------------------------------------------
# main build
# ---------------------------------------------------------------------------
def main():
    p1 = json.load(open(P1_PATH))
    p1_sha = sha256_file(P1_PATH)
    p2, p2_prov = load_phase2()
    hx, hx_prov = load_hexagonal()
    sg = {g["number"]: g for g in json.load(open(SG_PATH))["groups"]}
    schmitt_cubic = load_schmitt_cubic()
    schmitt_tet, tet_block_of, tet_meta = load_schmitt_blocks(TET_TABLES)
    schmitt_hex, hex_block_of, hex_meta = load_schmitt_blocks(HEX_TABLES)
    rekey = json.load(open(REKEY))
    wyck = load_wyckoff()

    # --- store integrity -------------------------------------------------
    assert set(p1["types"]) == set(p1["type_order"]), "phase1 type_order != types"
    assert set(p2["types"]) == set(p2["type_order"]), "phase2 type_order != types"
    assert set(hx["types"]) == set(hx["type_order"]), "hexagonal type_order != types"
    assert hx["complete"] is True and hx["seed_store"]["sha256"] == p2_prov["raw_sha256"], "hexagonal store was not seeded from the verified phase-2 store"
    assert hx["type_order"][:len(p2["type_order"])] == p2["type_order"], "hexagonal type_order does not start with the phase-2 order"
    cubic_ids = [t for t in hx["type_order"] if hx["types"][t]["first_sighting_system"] == CUBIC_FIRST]
    tet_ids = [t for t in hx["type_order"] if hx["types"][t]["first_sighting_system"] == TET_FIRST]
    hex_ids = [t for t in hx["type_order"] if hx["types"][t]["first_sighting_system"] == HEX_FIRST]
    assert len(cubic_ids) + len(tet_ids) + len(hex_ids) == len(hx["types"]), "unknown first_sighting_system in the hexagonal store"
    assert set(cubic_ids) == set(p1["types"]), "hexagonal store's cubic-first ids != phase1 ids"
    assert set(cubic_ids) | set(tet_ids) == set(p2["types"]), "hexagonal store's prior ids != phase2 ids"
    for t in cubic_ids:
        a, b = p1["types"][t], p2["types"][t]
        assert a["canon_code"] == b["canon_code"] and a["f_vector"] == b["f_vector"] \
            and a["p_vector"] == b["p_vector"] and a["aut_order"] == b["aut_order"], t
    for t in p2["types"]:
        a, b = p2["types"][t], hx["types"][t]
        assert a["canon_code"] == b["canon_code"] and a["f_vector"] == b["f_vector"] \
            and a["p_vector"] == b["p_vector"] and a["aut_order"] == b["aut_order"], t
        assert b["prior_sightings"] == len(a["sightings"]) + (a.get("phase1_sightings") or 0), t
        # the hexagonal store's prior_first_witness is phase2 first_witness, or phase1's when phase2's is null
        assert b["prior_first_witness"] == (a["first_witness"] if a["first_witness"] is not None else a.get("phase1_first_witness")), t
    for t, ent in hx["types"].items():
        assert hashlib.sha1(ent["canon_code"].encode("ascii")).hexdigest()[:16] == t, t
    # canonical codes pairwise distinct
    assert len({ent["canon_code"] for ent in hx["types"].values()}) == len(hx["types"])
    assert hx["n_types_prior_store"] == len(p2["types"]) and hx["n_types_hexagonal_new"] == len(hex_ids)

    # --- type-level Schmitt verdicts from the banked screens ---------------
    cubic_verdicts = parse_md_verdicts(COLL_CUBIC, "P") + parse_md_verdicts(XGROUP, "X")
    assert len([v for v in cubic_verdicts if v["source"].startswith("SCHMITT_COLLISION")]) == 21
    assert len([v for v in cubic_verdicts if v["source"].startswith("CROSS_GROUP")]) == 55
    coll_tet = json.load(open(COLL_TET))
    assert coll_tet["store_sha256"] == p2_prov["raw_sha256"]
    tet_verdicts = []
    for pr in coll_tet["pairs"]:
        v = pr["verdict"]
        verdict = "SAME" if v.startswith("SAME") else ("DIFFERENT" if v.startswith("DIFFERENT") else v)
        tet_verdicts.append(dict(pair=pr["pair"], target=pr["target"], group=pr["group"],
                                 fvec=tuple(pr["fvec"]), verdict=verdict,
                                 other_stored=pr.get("store_hit") if pr.get("store_hit") != pr["target"] else None,
                                 source="collision_phase2_results.json"))
    assert len(tet_verdicts) == 27
    # hexagonal recomputation pairs (top-10 survivors, 26 pairs; accepted 2026-09-04 12:40)
    coll_hex = json.load(open(COLL_HEX))
    assert coll_hex["store_sha256_before"] == coll_hex["store_sha256_after"] == hx_prov["raw_sha256"]
    assert coll_hex["counts_match_triage"] and coll_hex["ranking_match_triage"]
    hex_verdicts = []
    for pr in coll_hex["results"]:
        v = pr["verdict"]
        verdict = "SAME" if v.startswith("SAME") else ("DIFFERENT" if v.startswith("DIFFERENT") else v)
        assert pr["store_consistent"] is True, pr
        hex_verdicts.append(dict(pair=f'rank{pr["rank"]}', target=pr["target"], group=pr["group"],
                                 fvec=tuple(pr["fvec"]), verdict=verdict,
                                 other_stored=pr.get("store_hit") if pr.get("store_hit") != pr["target"] else None,
                                 source="collision_phase2_hex_results.json"))
    assert len(hex_verdicts) == 26
    # per type: SAME pairs, DIFFERENT pairs, and "his printed cell == this stored type" hits
    same_pairs = defaultdict(list)
    diff_pairs = defaultdict(list)
    for v in cubic_verdicts + tet_verdicts + hex_verdicts:
        key = f'{v["source"]}:{v["pair"]}:IT{v["group"]}'
        if v["verdict"] == "SAME":
            same_pairs[v["target"]].append(key)
        elif v["verdict"] == "DIFFERENT":
            diff_pairs[v["target"]].append(key)
            if v["other_stored"]:
                same_pairs[v["other_stored"]].append(key + ":printed-cell-equals-this-type")

    # --- P2 reproductions: his printed tetragonal row (g, c/a, point) -> stored type id
    # A P2 sighting is stored on the type whose exact cell at his printed point has his
    # printed f-vector; the store dedupes by canonical code, so if that id differs from
    # a type T with the same f-vector, his printed cell at that row is a DIFFERENT type
    # from T. (Rows never stored - two-origin groups, 95/96, the two order_cycle rows -
    # give no information here.)
    p2_row_to_id = {}
    for tid, ent in p2["types"].items():
        for s in ent["sightings"]:
            if s["kind"] == "schmitt_printed":
                key = (s["group"], s.get("b"), tuple(s["point"]))
                assert key not in p2_row_to_id or p2_row_to_id[key] == tid, key
                p2_row_to_id[key] = tid
    inferred_diff = defaultdict(list)   # tid -> ["IT(g) c/a=b point=pt -> stored as <id>"]
    for tid, ent in p2["types"].items():
        f = tuple(ent["f_vector"])
        for g, rows_ in schmitt_tet.items():
            for r in rows_:
                if r["f"] != f:
                    continue
                other = p2_row_to_id.get((g, r["b"], r["pt"]))
                if other is not None and other != tid:
                    inferred_diff[tid].append(f"IT{g} c/a={r['b']} pt=({','.join(r['pt'])}) -> stored as {other}")
    # the same for the hexagonal family: his printed row is keyed by (group, b, point AS
    # PRINTED in his B'' basis) = the store's printed_point_Bpp
    hx_row_to_id = {}
    for tid, ent in hx["types"].items():
        for s in ent["sightings"]:
            if s["kind"] == "schmitt_printed":
                key = (s["group"], s["b"], tuple(s["printed_point_Bpp"]))
                assert key not in hx_row_to_id or hx_row_to_id[key] == tid, key
                hx_row_to_id[key] = tid
    assert len(hx_row_to_id) == hx["schmitt_screen"]["reproduced"] == 1230
    inferred_diff_hex = defaultdict(list)
    for tid, ent in hx["types"].items():
        f = tuple(ent["f_vector"])
        for g, rows_ in schmitt_hex.items():
            for r in rows_:
                if r["f"] != f:
                    continue
                other = hx_row_to_id.get((g, r["b"], r["pt"]))
                if other is not None and other != tid:
                    inferred_diff_hex[tid].append(f"IT{g} c/a={r['b']} ptB''=({','.join(r['pt'])}) -> stored as {other}")
    # the 46 IT(180) rows: read-only re-run (z -> -z then H1), every cell already stored
    h180 = json.load(open(HEX180))
    assert h180["store_sha256"] == hx_prov["raw_sha256"] and h180["unchanged"] is True
    assert len(h180["rows"]) == 46 and all(r["reproduced"] and r["store_hit"] for r in h180["rows"])
    rows180_of = defaultdict(list)      # stored id -> printed 180 rows it reproduces (read-only)
    row180_to_id = {}
    for r in h180["rows"]:
        key = (180, r["b"], tuple(r["pt_Bpp"]))
        assert key not in hx_row_to_id, key   # these rows have no stored IT(180) P2 sighting
        row180_to_id[key] = r["store_hit"]
        rows180_of[r["store_hit"]].append(f"IT180 c/a={r['b']} ptB''=({','.join(r['pt_Bpp'])}) PDF p.{r['pdf']}")
    resolved180 = {r["id"]: r["verdict"] for r in h180["resolved"]}

    # --- hexagonal collision-screen verdicts (288 menu-sighted hexagonal-first types)
    triage_hex = parse_triage_hex_verdicts()
    shortlist = json.load(open(TRIAGE_HEX_JSON))
    assert shortlist["store_sha256"] == hx_prov["raw_sha256"]
    survivors = list(shortlist["survivors_ranked"])
    assert len(survivors) == 151 and len(set(survivors)) == 151
    assert len(triage_hex) == 288 == hx["n_types_hexagonal_menu_sighted"]
    assert Counter(v["verdict"] for v in triage_hex.values()) == Counter(coll_hex["screen_counts"]) == Counter({"SURVIVOR": 151, "COLLISION": 124, "UNRESOLVED": 13})
    assert {t for t, v in triage_hex.items() if v["verdict"] == "SURVIVOR"} == set(survivors)
    # re-derive the store-side rule here and assert it reproduces the banked verdicts
    for tid, v in triage_hex.items():
        ent = hx["types"][tid]
        assert ent["first_sighting_system"] == HEX_FIRST and not ent["schmitt_printed_only"], tid
        f = tuple(ent["f_vector"])
        my_p2 = {(s["group"], s["b"], tuple(s["printed_point_Bpp"])) for s in ent["sightings"] if s["kind"] == "schmitt_printed"}
        any_same = any_unres = False
        for g in {s["group"] for s in ent["sightings"]}:
            for r in schmitt_hex.get(g, []):
                if r["f"] != f:
                    continue
                key = (g, r["b"], r["pt"])
                if key in my_p2:
                    any_same = True
                elif key not in hx_row_to_id:
                    any_unres = True
        mine = "COLLISION" if any_same else ("UNRESOLVED" if any_unres else "SURVIVOR")
        assert mine == v["verdict"], (tid, mine, v["verdict"])

    # --- G4 pointers --------------------------------------------------------
    def tables_on_disk(prefix, folder):
        found = {}
        for fn in os.listdir(folder):
            m = re.fullmatch(prefix + r"([0-9a-f]{16})\.json", fn)
            if m:
                found[m.group(1)] = os.path.join(os.path.basename(folder), fn)
        return found
    g4_cubic = tables_on_disk("g4_tables_", HARNESS)
    g4p2 = tables_on_disk("g4p2_tables_", HARNESS)
    g4p2hex = tables_on_disk("g4p2hex_tables_", HARNESS)
    g4_track4 = {}
    t4 = json.load(open(os.path.join(TRACK4, "track4_results.json")))
    for key, ent in t4.items():
        m = re.search(r"store type ([0-9a-f]{16})", ent["stages"][0]["detail"])
        if m and all(s["verdict"] == "PASS" for s in ent["stages"]):
            g4_track4[m.group(1)] = f"track4/g4_tables_{key}17.json" if key == "laves" else f"track4/g4_tables_{key}38.json"
    for tid, rel in g4_track4.items():
        assert os.path.exists(os.path.join(ROOT, rel)), rel
    ACCEPTED_G4_CUBIC = {  # main-session accepted 2026-08-30 (STATUS.md "G4 COMPLETE - 11/11 CERTIFIED")
        "ceb70631e274e727", "359beee832567a71", "8cf50403cf88c455", "c314dedd38208a2e",
        "aa6b0077c3234d24", "f3d0f39a0b9676b9", "2de0a21129cabe90", "c4ea3f32fdd6dc51",
        "9b69eefb8bd8437c", "d2d935e5499e6e11", "f98a3ee5675fc121"}
    assert set(g4_cubic) == ACCEPTED_G4_CUBIC, (set(g4_cubic) ^ ACCEPTED_G4_CUBIC)
    assert set(g4_track4) == {"8c69db9e84095469"}, g4_track4
    # tetragonal batch: 14 certificates, main-session accepted 2026-09-04 01:35 (PROGRAM_LEDGER)
    g4p2_chiral = parse_g4p2_chirality()
    assert set(g4p2) == set(g4p2_chiral) and len(g4p2) == 14, (len(g4p2), set(g4p2) ^ set(g4p2_chiral))
    assert all(hx["types"][t]["first_sighting_system"] == TET_FIRST for t in g4p2)
    # hexagonal batch: 151 certificates, main-session accepted 2026-09-04 13:25 (PROGRAM_LEDGER)
    g4hex_chiral_md = parse_g4hex_chirality()
    assert set(g4p2hex) == set(g4hex_chiral_md) == set(survivors) and len(g4p2hex) == 151
    g4hex_chiral = {}
    for tid in g4p2hex:
        cell = json.load(open(os.path.join(G4HEX_CELLS, tid + ".json")))
        assert cell["cid"] == tid and all(s["verdict"] == "PASS" for s in cell["stages"]), tid
        assert cell["witness"] == hx["types"][tid]["first_witness"], tid
        assert cell["f_vector"] == hx["types"][tid]["f_vector"] and cell["aut_order"] == hx["types"][tid]["aut_order"], tid
        g4hex_chiral[tid] = bool(cell["sym"]["chiral"])
        assert g4hex_chiral[tid] == (g4hex_chiral_md[tid] == "chiral"), tid
    assert Counter(g4hex_chiral.values()) == Counter({True: 140, False: 11})
    assert Counter(g4p2_chiral.values()) == Counter({"chiral": 13, "achiral": 1})
    # honeycomb chirality from the certificate tables themselves (all point ops proper)
    def honeycomb_chiral(rel):
        d = json.load(open(os.path.join(ROOT, rel)))
        assert d["n_proper"] + d["n_improper"] == len(d["ops"]) and len(d["proper_ops"]) == d["n_proper"], rel
        return d["n_improper"] == 0

    g4_info = {}   # tid -> (status, pointer, doc, acceptance, chiral_solid, chiral_solid_source)
    for tid, rel in g4_cubic.items():
        g4_info[tid] = ("accepted-cubic", rel, "harness/G4_RESULTS.md", "main-session re-run 2026-08-30", None,
                        "not recorded: G4_RESULTS.md (cubic ladder) reports no solid-chirality rung")
    for tid, rel in g4_track4.items():
        g4_info[tid] = ("accepted-cubic", rel, "track4/TRACK4_RESULTS.md", "main-session battery 2026-09-03", None,
                        "not recorded: TRACK4_RESULTS.md reports honeycomb chirality only (all 24 point ops proper)")
    for tid, rel in g4p2.items():
        g4_info[tid] = ("certified-tetragonal", rel, "harness/G4_PHASE2_RESULTS.md", "main-session re-run 2026-09-04 01:35 (PROGRAM_LEDGER)",
                        g4p2_chiral[tid] == "chiral", "G4_PHASE2_RESULTS.md 'Isometry vs site vs aut summary' column 'solid' (V2 rung)")
    for tid, rel in g4p2hex.items():
        g4_info[tid] = ("certified-hexagonal", rel, "harness/G4_PHASE2_HEX_RESULTS.md", "main-session re-run 2026-09-04 13:25 (PROGRAM_LEDGER)",
                        g4hex_chiral[tid], "harness/g4p2hex_cells/<id>.json sym.chiral (V2 rung), asserted == G4_PHASE2_HEX_RESULTS.md summary column 'chiral?'")
    assert len(g4_info) == 11 + 1 + 14 + 151

    # --- names (publication tree convention: <id8>_<Name>) -----------------
    names = {}
    for fn in os.listdir(PUBLICATION):
        m = re.fullmatch(r"([0-9a-f]{8})_(.+)", fn)
        if m and os.path.isdir(os.path.join(PUBLICATION, fn)):
            names[m.group(1)] = m.group(2)
    literature_names = {  # seeded types: seed_name from the store; plus two rediscoveries
        "8c69db9e84095469": ("Laves graph plesiohedron (17 facets; Schoen 2008 / Coxeter 1955)", "literature name (rediscovered; track4)"),
        "2001fe7ea92fd0ad": ("triakis truncated tetrahedron (diamond Voronoi cell)", "literature name (rediscovered; G5 duty 3)"),
        "ea22673a3a17c26a": ("matches gyrobifastigium at f+p level ONLY; type-level check never run", "f+p match only (G5 flag)"),
    }

    # --- open/wall from documented perturbation runs -----------------------
    open_wall = {}
    c1 = json.load(open(C1_WALL))
    assert isinstance(c1, list) and len(c1) == 7
    # verdict per the c1 definition: OPEN = unchanged in every on-stratum step;
    # WALL = changes on both sides along some tangent direction.
    c1_md = {}
    for line in open(os.path.join(HARNESS, "round1_computations", "c1_wall_open.md")):
        m = re.match(r"\| (\w+) \| (\d{3}) \| \([^)]*\) \| \d \| \[.*?\] \| \*\*(OPEN|WALL)\*\*", line)
        if m:
            c1_md[m.group(1)] = m.group(3)
    for r in c1:
        on = [x for x in r["rows"] if not x["off_stratum"]]
        # per direction and side, the row at the SMALLEST tested |eps| decides that side
        smallest = {}
        for x in on:
            key = (tuple(x["direction"]), Fraction(x["eps"]) > 0)
            if key not in smallest or abs(Fraction(x["eps"])) < abs(Fraction(smallest[key]["eps"])):
                smallest[key] = x
        wall_dirs = [d for d in {k[0] for k in smallest}
                     if (d, True) in smallest and (d, False) in smallest
                     and not smallest[(d, True)]["same"] and not smallest[(d, False)]["same"]]
        any_change = any(not x["same"] for x in on)
        if wall_dirs:
            verdict = "WALL"
        elif not any_change:
            verdict = "OPEN"
        else:
            verdict = "OPEN (short interval: a larger step on one side changes the type; see source)"
        assert c1_md[r["label"]] == verdict.split()[0], (r["label"], verdict, c1_md.get(r["label"]))
        open_wall[r["id"]] = (verdict, "harness/round1_computations/c1_wall_open.json (point perturbation in the Wyckoff stratum, +-1/96, +-1/48, refined to 1/1536; verdict re-derived here and asserted == c1_wall_open.md)")
    for pt in coll_tet.get("perturbation", []):
        open_wall[pt["id"]] = (f'point {pt["point_verdict"]} / c-over-a {pt["b_verdict"]}',
                               "harness/collision_phase2_results.json 'perturbation' (point and c/a perturbed separately, +-1/96, +-1/48, refined to 1/1536)")

    # --- v3: computed open/wall verdicts (7 cubic c1 cells + 165 G4-certified phase-2 cells)
    wo_bytes = open(WALL_OPEN_JSON, "rb").read()
    wo = json.loads(wo_bytes.decode("utf-8"))
    wo_md5 = hashlib.md5(wo_bytes).hexdigest()
    wo_sha = hashlib.sha256(wo_bytes).hexdigest()
    m_md5 = re.search(r"md5 = `([0-9a-f]{32})`", open(WALL_OPEN_MD).read())
    assert m_md5 and m_md5.group(1) == wo_md5, ("WALL_OPEN_PHASE2.json md5 != the value stated in WALL_OPEN_PHASE2.md", wo_md5)
    assert wo["n_cells"] == 165 == len(wo["cells"]) and wo["n_crash"] == 0 and wo["regression_ok"] is True
    assert wo["stores"]["phase2_types.json_sha256"] == p2_prov["raw_sha256"]
    assert wo["stores"]["phase2_hexagonal_types.json_sha256"] == hx_prov["raw_sha256"] and wo["stores"]["sha256_unchanged_after_run"] is True
    assert wo["scheme"]["pre_registration"].startswith("ANCHORS.md: PERTURBATION CLASSIFICATION, PHASE 2") and wo["snapshot"] == SNAPSHOT
    assert wo["scheme"]["point_refine_to"] == "1/1536" and wo["scheme"]["metric_refine_to"] == "1/3072"
    wo_cells = OrderedDict((c["id"], c) for c in wo["cells"])
    assert len(wo_cells) == 165
    assert {t for t, c in wo_cells.items() if c["family"] == "tetragonal"} == set(g4p2)
    assert {t for t, c in wo_cells.items() if c["family"] == "hexagonal"} == set(g4p2hex)
    for fam in ("tetragonal", "hexagonal"):
        agg = wo["aggregate"][fam]
        cells_f = [c for c in wo_cells.values() if c["family"] == fam]
        assert agg["n"] == len(cells_f), fam
        assert Counter(c["combined_verdict"] for c in cells_f) == Counter(agg["combined"]), fam
        assert Counter(c["point_verdict"] for c in cells_f) == Counter(agg["point"]), fam
        assert Counter(c["metric_verdict"] for c in cells_f) == Counter(agg["metric"]), fam
        assert agg["quarantine_any"] == 0 and not any(c["flags"]["quarantine_any"] for c in cells_f), fam
    for tid, c in wo_cells.items():
        assert c["combined_verdict"] in ("OPEN", "WALL", "ONE-SIDED"), tid
        wit = p2["types"][tid]["first_witness"] if c["family"] == "tetragonal" else hx["types"][tid]["first_witness"]
        assert c["witness_point"] == "(" + ", ".join(wit["point"]) + ")" and c["c_over_a"] == wit["b"] and c["IT"] == wit["group"], tid
        assert c["base_f"] == hx["types"][tid]["f_vector"] and c["base_aut"] == hx["types"][tid]["aut_order"], tid
        assert c["stratum_dim"] == wit["stratum_dim"] and c["base_nonsimple"] == wit["nonsimple_vertices"], tid
    for pt in coll_tet["perturbation"]:   # regression: the top-3 tetragonal POINT verdicts (same steps, same chain)
        assert wo_cells[pt["id"]]["point_verdict"] == pt["point_verdict"], pt["id"]
    ow3 = OrderedDict()
    for r in c1:
        assert r["verdict"] in ("OPEN", "WALL", "ONE-SIDED") and r["verdict"] == open_wall[r["id"]][0].split()[0], r["label"]
        ow3[r["id"]] = OrderedDict([
            ("verdict", r["verdict"]), ("source", "c1 cubic"),
            ("point_verdict", r["verdict"]), ("metric_verdict", "n/a (cubic: no free metric parameter)"), ("flags", None),
            ("pointer", f"harness/round1_computations/c1_wall_open.json [label {r['label']}].verdict (wall directions {r['wall_dirs']}); c1_wall_open.md verdict table; run 2026-09-03; banked PROGRAM_LEDGER 2026-09-03 (shapes paper round 1 accepted: C1 facts)"),
            ("scheme", C1_SCHEME), ("scheme_date", "2026-09-03 (c1 run; not pre-registered)")])
    for tid, c in wo_cells.items():
        ow3[tid] = OrderedDict([
            ("verdict", c["combined_verdict"]), ("source", "phase2 #148"),
            ("point_verdict", c["point_verdict"]), ("metric_verdict", c["metric_verdict"]),
            ("flags", sorted(k for k, v in c["flags"].items() if v)),
            ("pointer", f"harness/phase2/WALL_OPEN_PHASE2.json cells[id={tid}].combined_verdict ({c['family']} doc rank {c['rank']}; POINT {c['point_verdict']} / METRIC {c['metric_verdict']}; combined walls {c['combined_walls']}; previous heuristic label '{c['previous_label']}', agreement {c['agree']}); WALL_OPEN_PHASE2.md summary table; agent #148; accepted by main-session fresh re-run 2026-09-04 14:10 (PROGRAM_LEDGER; JSON md5 {wo_md5})"),
            ("scheme", PHASE2_SCHEME), ("scheme_date", "2026-09-04 (pre-registered in ANCHORS.md before the run)")])
    assert len(ow3) == 7 + 165

    # --- v3: type-level Schmitt status from the two phase-2 collision screens
    tet_screen = OrderedDict()
    for pr in coll_tet["pairs"]:
        assert pr["verdict"] in ("SAME TYPE", "DIFFERENT TYPE"), pr
        e = tet_screen.setdefault(pr["target"], dict(rank=pr["rank"], pairs=[], n_same=0, n_diff=0))
        assert e["rank"] == pr["rank"]
        e["pairs"].append(pr["pair"])
        e["n_same" if pr["verdict"] == "SAME TYPE" else "n_diff"] += 1
    assert len(tet_screen) == 15 and sorted(e["rank"] for e in tet_screen.values()) == list(range(1, 16))
    for t in tet_screen:
        assert hx["types"][t]["first_sighting_system"] == TET_FIRST and not p2["types"][t]["schmitt_printed_only"], t
    tet_survivors = {t for t, e in tet_screen.items() if e["n_same"] == 0}
    assert tet_survivors == set(g4p2) and len(tet_screen) - len(tet_survivors) == 1
    md_tet = {}
    for line in open(COLL_TET_MD):
        m = re.match(r"^- rank (\d+) `([0-9a-f]{16})`: (survives this screen|COLLISION)", line)
        if m:
            md_tet[m.group(2)] = "SURVIVOR" if m.group(3).startswith("survives") else "COLLISION"
    assert md_tet == {t: ("SURVIVOR" if t in tet_survivors else "COLLISION") for t in tet_screen}, "COLLISION_PHASE2_RESULTS.md summary lines != JSON-derived status"
    # --- v4: store-side status of ALL 404 menu-sighted tetragonal-first types (subagent #152, 2026-09-04)
    ss_raw = open(COLL_TET_SS, "rb").read()
    ss_md5 = hashlib.md5(ss_raw).hexdigest()
    ss = json.loads(ss_raw)
    assert ss["store_tetragonal_sha256"] == p2_prov["raw_sha256"] and ss["store_hexagonal_sha256"] == hx_prov["raw_sha256"], "storeside JSON ran on other stores"
    he = ss["hexagonal_equivalence"]
    assert he["counts_match_expected"] and he["per_type_match_triage_table"] and he["survivors_ranked_match"] \
        and he["counts_here"] == {"SURVIVOR": 151, "COLLISION": 124, "UNRESOLVED": 13}, "hexagonal equivalence of the store-side rule not asserted"
    tet_ss = ss["verdicts"]
    assert len(tet_ss) == ss["n_tetragonal_menu_sighted"] == 404
    assert set(tet_ss) == {t for t in tet_ids if not p2["types"][t]["schmitt_printed_only"]}
    assert ss["shortlist_disagreements"] == [] and ss["survivors_certified_14_all_SURVIVOR"] and ss["known_collision_stays"]
    for t, e in tet_screen.items():
        assert tet_ss[t]["status"] == ("SURVIVOR" if e["n_same"] == 0 else "COLLISION") == tet_ss[t]["shortlist_doc_status"], t
    assert sum(1 for v in tet_ss.values() if v["s_cell"]) == ss["n_tetragonal_s_cells"] == 176
    assert all(v["status"] == "COLLISION" for v in tet_ss.values() if v["s_cell"])
    assert Counter(v["status"] for v in tet_ss.values()) == Counter(ss["counts_combined"]) == Counter({"COLLISION": 177, "SURVIVOR": 121, "UNRESOLVED": 106}), ss["counts_combined"]
    coll_tet_md_text = open(COLL_TET_MD).read()
    assert ("md5 %s" % ss_md5) in coll_tet_md_text, "collision_phase2_tetragonal_storeside.json md5 != the value stated in the COLLISION_PHASE2_RESULTS.md addendum"
    # --- v5: the 62 unstored rows recomputed; the 106 v4-UNRESOLVED statuses settled (subagent #154, 2026-09-04)
    ov_raw = open(COLL_TET_OV, "rb").read()
    ov_md5 = hashlib.md5(ov_raw).hexdigest()
    ov = json.loads(ov_raw)
    rows_raw = open(COLL_TET_ROWS, "rb").read()
    rows_md5 = hashlib.md5(rows_raw).hexdigest()
    rows_j = json.loads(rows_raw)
    assert ov["rows_file"] == os.path.basename(COLL_TET_ROWS) and ov["rows_file_md5"] == rows_md5, "overlay JSON does not point at the rows JSON on disk"
    assert ov["storeside_json_md5"] == ss_md5 == rows_j["storeside_json_md5"], "v5 files ran on another storeside JSON"
    assert ov["store_sha256"] == rows_j["store_sha256_before"] == rows_j["store_sha256_after"] == p2_prov["raw_sha256"], "v5 files ran on another store / store changed"
    assert ("md5 %s" % ov_md5) in coll_tet_md_text and ("md5 %s" % rows_md5) in coll_tet_md_text, "v5 JSON md5s != the values stated in the COLLISION_PHASE2_RESULTS.md #154 addendum"
    assert rows_j["n_rows"] == 62 == len(rows_j["rows"]) and dict(rows_j["row_status_counts"]) == {"REPRODUCED": 62}, rows_j["row_status_counts"]
    assert all(r["status"] == "REPRODUCED" and r["documented_conventions_agree"] and not r["other_reading_reproduces_printed_f"] for r in rows_j["rows"].values())
    assert all(rg["equal"] for rg in rows_j["regression_vs_collision_phase2_check"]) and len(rows_j["regression_vs_collision_phase2_check"]) == 2
    tet_ov = ov["verdicts"]
    v4_unres = {t for t, v in tet_ss.items() if v["status"] == "UNRESOLVED"}
    assert set(tet_ov) == v4_unres and len(tet_ov) == ov["n_types"] == 106, "overlay types != the v4 UNRESOLVED set"
    assert not (set(tet_ov) & set(tet_screen)), "a shortlist type is in the v5 overlay"
    assert set(ov["certified_14_untouched"]) == set(g4p2) and not (set(g4p2) & set(tet_ov)), "certified survivors touched by v5"
    rows_by_key = {(r["group"], r["b"], tuple(r["pt_printed"])): r for r in rows_j["rows"].values()}
    for t, v in tet_ov.items():
        assert v["status_v4"] == "UNRESOLVED" and v["f_vector"] == p2["types"][t]["f_vector"], t
        hung = {(r["group"], r["b"], tuple(r["pt"])) for r in tet_ss[t]["unstored_rows"]}
        assert {(x["group"], x["b"], tuple(x["pt"])) for x in v["rows"]} == hung, t
        verd = []
        for x in v["rows"]:
            row = rows_by_key[(x["group"], x["b"], tuple(x["pt"]))]
            assert row["status"] == "REPRODUCED" and x["row_status"] == "REPRODUCED" and row["code_id"] == x["row_cell_code_id"], t
            assert tuple(row["f"]) == tuple(row["f_printed"]) == tuple(v["f_vector"]), t
            verd.append("SAME TYPE" if row["code"] == p2["types"][t]["canon_code"] else "DIFFERENT TYPE")
        assert verd == [x["verdict"] for x in v["rows"]], t
        assert v["status"] == ("COLLISION" if "SAME TYPE" in verd else "SURVIVOR"), t
    ov_counts = Counter(v["status"] for v in tet_ov.values())
    assert ov_counts == Counter(ov["counts_106"]) == Counter({"COLLISION": 24, "SURVIVOR": 82}), ov_counts
    # content equality with the #154 addendum's two tables (the content of record; the md5 check above is secondary
    # since a file can only be hashed after it is written): 62 row lines and 106 type lines must match the JSONs
    sec154 = coll_tet_md_text.split("## Addendum 2026-09-04 (subagent #154")[1].split("\n### CORRECTION")[0]
    md_rows = {}
    for line in sec154.split("### Row-level results")[1].split("### Type-level verdicts")[0].splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 18 and cells[0].isdigit():
            m_code = re.search(r"`([0-9a-f]{16})`", cells[13])
            md_rows[(int(cells[1].split()[0]), cells[2], tuple(x.strip() for x in cells[3].strip("()").split(",")))] = (cells[6].strip("*"), m_code.group(1) if m_code else None)
    assert len(md_rows) == 62 and set(md_rows) == set(rows_by_key), "addendum row table != rows JSON (keys)"
    assert all(md_rows[k] == ("REPRODUCED", rows_by_key[k]["code_id"]) for k in rows_by_key), "addendum row table != rows JSON (status / code id)"
    md_types = {m.group(1): m.group(2) for m in re.finditer(r"^\| `([0-9a-f]{16})` \| .* \| \*\*(\w+)\*\* \|$", sec154.split("### Type-level verdicts")[1], re.M)}
    assert len(md_types) == 106 and md_types == {t: v["status"] for t, v in tet_ov.items()}, "addendum type table != overlay JSON"
    assert "wall_seconds" not in rows_j and not any("secs" in c for r in rows_j["rows"].values() for c in r["cells"]), "timing field inside the hashed rows JSON (run-dependent md5)"
    assert ov["still_unresolved"] == [] and ov["counts_404_before_v4"] == ss["counts_combined"]
    assert dict(ov["counts_404_after_v5"]) == {"COLLISION": 177 + 24, "SURVIVOR": 121 + 82, "UNRESOLVED": 0}
    hex_md_text = open(COLL_HEX_MD).read()
    m_cnt = re.search(r"Verdicts: SURVIVOR (\d+), COLLISION (\d+), UNRESOLVED (\d+) of (\d+) menu-sighted types", hex_md_text)
    assert m_cnt and [int(x) for x in m_cnt.groups()] == [151, 124, 13, 288]
    assert Counter(coll_hex["screen_counts"]) == Counter({"SURVIVOR": 151, "COLLISION": 124, "UNRESOLVED": 13})
    md_hex_post = {m.group(1): m.group(2) for m in re.finditer(r"^- #\d+ `([0-9a-f]{16})`[^\n]*: (SURVIVES[^\n]*)$", hex_md_text, re.M)}
    assert md_hex_post == coll_hex["post"] and set(md_hex_post) == set(survivors[:10]), "COLLISION_PHASE2_HEX_RESULTS.md post-screen lines != JSON post block"

    # --- assemble rows -------------------------------------------------------
    def sighting_row(s, family):
        return OrderedDict([
            ("system", family),
            ("crystal_system", sg[s["group"]]["crystal_system"]),
            ("group", s["group"]), ("group_symbol", s["group_symbol"]),
            ("point", list(s["point"])), ("kind", s["kind"]),
            ("c_over_a", s.get("b")), ("pass", s.get("pass")),
            ("stratum_dim", s["stratum_dim"]), ("site_stabilizer_order", s["stabilizer_order"]),
            ("orbit_conventional", s["orbit_conventional"]), ("orbit_primitive", s["orbit_primitive"]),
            ("lattice_degenerate", s["lattice_degenerate"]), ("degenerate_flag", s["degenerate_flag"]),
            ("float_superseded", s["float_superseded"]), ("nonsimple_vertices", s["nonsimple_vertices"]),
            ("W", s["W"]), ("congruence_checked", s.get("congruence_checked")),
            # hexagonal-family P2 sightings only (his point as printed in the B'' basis and the conversion used)
            ("printed_point_Bpp", list(s["printed_point_Bpp"]) if s.get("printed_point_Bpp") else None),
            ("conversion", s.get("conversion")),
            ("schmitt_primary_group", s.get("schmitt_primary_group")),
            ("pdf_page", s.get("pdf_page")),
        ])

    FAMILY_OF = {CUBIC_FIRST: "cubic", TET_FIRST: "tetragonal", HEX_FIRST: "hexagonal"}
    rows = []
    n_cub = n_tet = n_hex = 0
    for tid in hx["type_order"]:
        eh = hx["types"][tid]
        family = FAMILY_OF[eh["first_sighting_system"]]
        is_cubic_first = family == "cubic"
        e1 = p1["types"].get(tid)
        e2 = p2["types"].get(tid)
        f = tuple(eh["f_vector"]); p = list(eh["p_vector"])
        assert euler_ok(f) and len(p) == f[2] and sum(p) == 2 * f[1], tid
        cub_s = [sighting_row(s, "cubic") for s in (e1["sightings"] if e1 else [])]
        tet_s = [sighting_row(s, "tetragonal") for s in (e2["sightings"] if e2 else [])]
        hex_s = [sighting_row(s, "hexagonal") for s in eh["sightings"]]
        if family == "cubic":
            n_cub += 1
            catalog_id = f"MINT-C{n_cub:03d}"
        elif family == "tetragonal":
            n_tet += 1
            catalog_id = f"MINT-T{n_tet:03d}"
        else:
            n_hex += 1
            catalog_id = f"MINT-H{n_hex:03d}"
        # witness
        if family == "cubic":
            w = e1["first_witness"]
            w_src = "phase1_types.json types[id].first_witness"
            if w is None:  # seeded types carry no first_witness; use first stored sighting
                w = e1["sightings"][0] if e1["sightings"] else None
                w_src = "phase1_types.json types[id].sightings[0] (seeded type: first_witness is null in the store)"
        elif family == "tetragonal":
            w = e2["first_witness"]; w_src = "phase2_types.json types[id].first_witness"
        else:
            w = eh["first_witness"]; w_src = "phase2_hexagonal_types.json types[id].first_witness"
            assert w is not None and not eh.get("seeded"), tid
        wpt = tuple(w["point"]) if w else None
        if w:
            for x in w["point"]:
                Fraction(x)  # exact rational check
        wy = wyck.get((w["group"], wpt)) if w else None
        if wy is None and tid == "8c69db9e84095469":
            wy = ("a", ".32")  # spglib on the frozen IT(214) orbit of (1/8,1/8,1/8): STATUS 2026-09-03 track 4 (only for the 8a witness)
            wy_src = "STATUS.md 2026-09-03 (Track 4: spglib 2.7.0, IT(214) 8a, site .32) - applies to the (1/8,1/8,1/8) orbit, not necessarily to the stored first witness"
        elif wy is not None:
            wy_src = "paper/wyckoff_check.txt (spglib 2.7.0 on the package orbit)"
        else:
            wy_src = None
        # Schmitt f-vector status per sighted group (menu sightings only for the tetragonal side)
        groups_cubic = sorted({s["group"] for s in cub_s})
        groups_tet_all = sorted({s["group"] for s in tet_s})
        groups_tet_menu = sorted({s["group"] for s in tet_s if s["kind"] != "schmitt_printed"})
        groups_hex_all = sorted({s["group"] for s in hex_s})
        groups_hex_menu = sorted({s["group"] for s in hex_s if s["kind"] != "schmitt_printed"})
        f_present, f_absent = [], []
        for g in groups_cubic:
            (f_present if f in set(schmitt_cubic.get(g, [])) else f_absent).append(g)
        for g in groups_tet_all:
            (f_present if f in {r["f"] for r in schmitt_tet.get(g, [])} else f_absent).append(g)
        for g in groups_hex_all:
            (f_present if f in {r["f"] for r in schmitt_hex.get(g, [])} else f_absent).append(g)
        f_any_cubic = sorted(g for g, rows_ in schmitt_cubic.items() if f in set(rows_) and g != 213)
        f_any_tet = sorted(g for g, rows_ in schmitt_tet.items() if f in {r["f"] for r in rows_})
        f_any_hex = sorted(g for g, rows_ in schmitt_hex.items() if f in {r["f"] for r in rows_})
        if groups_cubic or groups_tet_all or groups_hex_all:
            fflag = "P" if f_present else "A"
        else:
            fflag = "n/a (seeded type never sighted by a sweep)"
        # type-level
        s_cell_sightings = [s for s in tet_s if s["kind"] == "schmitt_printed"]
        h_cell_sightings = [s for s in hex_s if s["kind"] == "schmitt_printed"]
        type_level = []
        if s_cell_sightings:
            type_level.append(f"SAME: reproduces {len(s_cell_sightings)} printed tetragonal cell(s) at his generating point (phase-2 pass P2 sighting)")
        if h_cell_sightings:
            type_level.append(f"SAME: reproduces {len(h_cell_sightings)} printed trigonal/hexagonal cell(s) at his generating point (phase-2 batch-2 pass P2 sighting; conversion H1 or H1+zflip per sighting)")
        if rows180_of.get(tid):
            type_level.append(f"SAME: reproduces {len(rows180_of[tid])} printed IT(180/181)-table row(s) in the IT(180) setting under z -> -z then H1 (read-only re-run PHASE2_HEX_SCHMITT_180_CHECK; the printed points belong to IT(181) per Schmitt's normalizer remark; cell already stored): " + "; ".join(rows180_of[tid]))
        if same_pairs.get(tid):
            type_level.append("SAME at printed representative(s): " + "; ".join(same_pairs[tid]))
        if diff_pairs.get(tid):
            type_level.append(f"DIFFERENT from his printed representative in {len(diff_pairs[tid])} (group,f) pair(s): " + "; ".join(diff_pairs[tid]))
        if inferred_diff.get(tid):
            type_level.append(f"DIFFERENT (inferred from the dedupe store: his printed tetragonal row with this f-vector was reproduced by pass P2 and stored under another id) at {len(inferred_diff[tid])} row(s): " + "; ".join(inferred_diff[tid]))
        if inferred_diff_hex.get(tid):
            type_level.append(f"DIFFERENT (inferred from the dedupe store: his printed trigonal/hexagonal row with this f-vector was reproduced by batch-2 pass P2 and stored under another id) at {len(inferred_diff_hex[tid])} row(s): " + "; ".join(inferred_diff_hex[tid]))
        if tid in resolved180:
            type_level.append(f"READ-ONLY remark on the IT(180) rows (PHASE2_HEX_SCHMITT_180_CHECK; store verdict stands): {resolved180[tid]}")
        if not type_level:
            type_level_status = "unchecked at type level"
        elif any(x.startswith("SAME") for x in type_level):
            type_level_status = "SAME as a Schmitt printed cell (type-level; first-realization reframe per kill criterion)"
        else:
            type_level_status = "DIFFERENT from every checked printed representative (not identity evidence; sampling caveat)"
        # G4
        g4 = None; g4_status = "no"; g4_status_v2 = "none"; g4_doc = None; g4_acc = None; g4_chiral = None; g4_chiral_src = "no certificate"; g4_hc = None
        if tid in g4_info:
            g4_status_v2, g4, g4_doc, g4_acc, g4_chiral, g4_chiral_src = g4_info[tid]
            g4_hc = honeycomb_chiral(g4)
            # v1 strings kept verbatim for the cubic ladder and track4 (doc/date order differs between them in v1)
            g4_status = (f"yes (accepted; {g4_doc}, {g4_acc})" if g4_doc.startswith("track4") else f"yes (accepted; {g4_acc}, {g4_doc})")
        # name
        name = None; name_status = "none"
        if eh.get("seeded"):
            name = eh.get("seed_name"); name_status = "seeded classical (G2 seed catalog)"
        elif tid[:8] in names:
            nm = names[tid[:8]]
            if nm in ("Satchelhedron", "Ordenhedron"):
                name, name_status = nm, "named (program; Tyler's 2026-09-01 decision)"
            elif nm.endswith("_HELD"):
                name, name_status = nm, "HELD (Engel/Koch ILL pending; do NOT name)"
            else:
                name, name_status = nm, "descriptive package name (naming pending Tyler)"
        elif tid in literature_names:
            name, name_status = literature_names[tid]
        # gate G3
        n_s = len(cub_s) + len(tet_s) + len(hex_s)
        if eh.get("seeded") and n_s == 0:
            g3 = "seeded from published vertex data (G2 seed catalog); NEVER sighted by a sweep - not exact-confirmed by the pipeline"
        elif eh.get("seeded"):
            g3 = f"seeded (G2 seed catalog) AND sighted by the sweep {n_s} time(s) through the full G3 chain"
        else:
            g3 = f"G3 exact-confirmed (float -> exact clip -> canonical code) at {n_s} stored sighting(s)"
        # b-ratios (tetragonal columns unchanged from v1; hexagonal separately)
        b_menu = sorted({Fraction(s["c_over_a"]) for s in tet_s if s["kind"] != "schmitt_printed" and s["c_over_a"]})
        b_all = sorted({Fraction(s["c_over_a"]) for s in tet_s if s["c_over_a"]})
        hb_menu = sorted({Fraction(s["c_over_a"]) for s in hex_s if s["kind"] != "schmitt_printed" and s["c_over_a"]})
        hb_all = sorted({Fraction(s["c_over_a"]) for s in hex_s if s["c_over_a"]})
        # hexagonal Schmitt match status
        if not hex_s:
            hmatch = "n/a (no hexagonal-family sighting)"
        elif family == "hexagonal" and eh["schmitt_printed_only"]:
            hmatch = f"S-cell, printed-only: reproduces {len(h_cell_sightings)} printed trigonal/hexagonal row(s) at his printed point (pass P2); never reached by our menu; not collision-screened (screen covered menu-sighted types)"
        elif family == "hexagonal":
            v = triage_hex[tid]
            if v["verdict"] == "COLLISION":
                hmatch = f"COLLISION (S-cell): reproduces {len(h_cell_sightings)} printed row(s) AND menu-sighted; first-realization reframe (store-side screen, TRIAGE_PHASE2_HEX_RESULT.md full-table rank {v['rank']} of 288)"
            elif v["verdict"] == "UNRESOLVED":
                hmatch = f"UNRESOLVED (store-side screen, triage full-table rank {v['rank']} of 288): the only unresolved pairs are IT(180) rows; read-only re-run says: {resolved180.get(tid, 'not listed')}"
            else:
                hmatch = f"SURVIVOR (store-side screen; survivor rank {survivors.index(tid) + 1} of 151 = G4_PHASE2_HEX_RESULTS.md #; triage full-table rank {v['rank']} of 288): f-vector absent from every sighted group's table, or DIFFERENT from the stored cell at every printed row of that (group, f)" + \
                         (f"; recomputation at his printed points (collision_phase2_hex_results.json post): {coll_hex['post'][tid]}" if tid in coll_hex["post"] else "")
        else:
            hmatch = (f"prior ({family}-first) type re-sighted in the hexagonal family; " +
                      (f"S-cell: reproduces {len(h_cell_sightings)} printed row(s) at his point (pass P2)" if h_cell_sightings else "no P2 sighting") +
                      f"; f-vector flag over sighted hexagonal groups {'P' if any(g in f_present for g in groups_hex_all) else 'A'}; not collision-screened in this family (screen covered hexagonal-FIRST menu-sighted types)")
        ow = open_wall.get(tid)
        o3 = ow3.get(tid)
        # v3 type-level Schmitt status (phase-2 collision screens only)
        if family == "cubic":
            sts = "not-screened"
            sts_src = ("cubic-first type: the two phase-2 collision screens cover phase-2-first types only (COLLISION_PHASE2_RESULTS.md = tetragonal top-15 shortlist; "
                       "COLLISION_PHASE2_HEX_RESULTS.md = the 288 menu-sighted hexagonal-first types); the cubic-round pair verdicts (SCHMITT_COLLISION_RESULTS.md 21 pairs, CROSS_GROUP_RESULTS.md 55 pairs) stay in schmitt_type_level_status / schmitt_type_level_detail")
        elif family == "tetragonal":
            if e2["schmitt_printed_only"]:
                sts = "printed-only"
                sts_src = (f"phase2_types.json schmitt_printed_only=True: S-cell reproducing {len(s_cell_sightings)} printed tetragonal row(s) at his printed point by pass P2, never reached by our menu; "
                           "outside every collision screen (TRIAGE_PHASE2_RESULT.md S-cell rule; COLLISION_PHASE2_RESULTS.md covered the top-15 shortlist only)")
            elif tid in tet_screen:
                e = tet_screen[tid]
                sts = "SURVIVOR" if e["n_same"] == 0 else "COLLISION"
                v4 = tet_ss[tid]
                sts_src = (f"harness/COLLISION_PHASE2_RESULTS.md 'Summary per shortlist type' rank {e['rank']} of 15 ({len(e['pairs'])} printed pair(s): {e['n_diff']} DIFFERENT / {e['n_same']} SAME; "
                           f"collision_phase2_results.json pairs {', '.join(e['pairs'])}); worklist = TRIAGE_PHASE2_RESULT.md top-15 shortlist; asserted == the doc's summary line"
                           f"; v4 store-side rule (COLLISION_PHASE2_RESULTS.md addendum 2026-09-04, collision_phase2_tetragonal_storeside.json): pure rule {v4['status_pure_store_side_rule']}, with this type's recomputed pairs overlaid {v4['status']} (asserted == this status)")
            else:
                v4 = tet_ss[tid]
                sts = v4["status"]
                assert v4["status_catalog_v3"] == "not-screened" and not v4["in_top15_shortlist"] and v4["s_cell"] == bool(s_cell_sightings), tid
                res_txt = "; ".join(f"IT{g}: " + "/".join(f"{k}{c[k]}" for k in ("same", "other", "unres") if c[k]) for g, c in v4["resolution_per_group"].items()) or "f-vector printed in no sighted group's table"
                sts_src = ("harness/COLLISION_PHASE2_RESULTS.md addendum 2026-09-04 (subagent #152): store-side screen of all 404 menu-sighted tetragonal-first types (collision_phase2_tetragonal_storeside.json; the hexagonal screen's rule, equivalence asserted 151/124/13; tetragonal counts COLLISION 177 / SURVIVOR 121 / UNRESOLVED 106 asserted): "
                           + (f"S-cell: reproduces {v4['n_p2_sightings']} printed row(s) at his printed point by pass P2 (= type-level SAME in schmitt_type_level_status) -> COLLISION (first-realization reframe)" if v4["s_cell"] else
                              (f"printed rows at its (group, f) per sighted group [same/other/unres]: {res_txt}; {len(v4['unstored_rows'])} unstored row(s) at its (group, f) were unresolved in v4 (listed in the JSON)" if sts == "UNRESOLVED" else
                               f"printed rows at its (group, f) per sighted group [same/other/unres]: {res_txt}; every printed row at its (group, f) reproduced as a different stored type, or the f-vector is absent from every sighted group's table -> SURVIVOR (catalog-relative, never novelty)"))
                           + "; outside the top-15 shortlist of TRIAGE_PHASE2_RESULT.md, so no pair was recomputed for it (catalog v3 said not-screened)")
                if sts == "UNRESOLVED":
                    # v5: the unstored rows were recomputed at the printed points with the documented conventions
                    v5 = tet_ov[tid]
                    sts = v5["status"]
                    assert sts in ("COLLISION", "SURVIVOR", "UNRESOLVED"), tid
                    rows_txt = "; ".join(f"IT{x['group']} b={x['b']} pt=({', '.join(x['pt'])}) [PDF p. {x['pdf_page']}] -> {x['verdict']}" + (f" (row cell `{x['row_cell_code_id']}`" + (f" = stored {x['row_cell_store_hit']})" if x.get("row_cell_store_hit") else ", not stored)") if x.get("row_cell_code_id") else "") for x in v5["rows"])
                    sts_src += (f"; [v5] harness/COLLISION_PHASE2_RESULTS.md addendum 2026-09-04 (subagent #154): its {len(v5['rows'])} unstored row(s) recomputed at the printed point with the documented setting conversion (collision_phase2_tetragonal_rows_recomputed.json md5 {rows_md5}; verdicts collision_phase2_tetragonal_unresolved_overlay.json md5 {ov_md5}): {rows_txt} -> "
                                + ("COLLISION (the type IS one of his printed cells; first-realization reframe)" if sts == "COLLISION" else
                                   ("SURVIVOR (every hung-on row reproduced as a different type; catalog-relative, never novelty)" if sts == "SURVIVOR" else
                                    "UNRESOLVED (a hung-on row could not be reproduced under any documented convention; listed in the overlay JSON)")))
        else:
            if eh["schmitt_printed_only"]:
                sts = "printed-only"
                sts_src = (f"phase2_hexagonal_types.json schmitt_printed_only=True: S-cell reproducing {len(h_cell_sightings)} printed trigonal/hexagonal row(s) at his printed point by pass P2, never reached by our menu; "
                           "outside the collision screen (COLLISION_PHASE2_HEX_RESULTS.md section 1 covered the 288 menu-sighted hexagonal-first types)")
            else:
                v3h = triage_hex[tid]
                sts = v3h["verdict"]
                sts_src = (f"harness/COLLISION_PHASE2_HEX_RESULTS.md section 1 store-side screen (288 menu-sighted hexagonal-first types; counts SURVIVOR 151 / COLLISION 124 / UNRESOLVED 13 asserted == collision_phase2_hex_results.json screen_counts and the doc line); "
                           f"per-type verdict = TRIAGE_PHASE2_HEX_RESULT.md full-table rank {v3h['rank']} of 288, re-derived here from the store and the digitization with the documented rule")
                if sts == "SURVIVOR":
                    sts_src += f"; survivor rank {survivors.index(tid) + 1} of 151 (= G4_PHASE2_HEX_RESULTS.md #)"
                if tid in coll_hex["post"]:
                    sts_src += f"; recomputed at every printed row of its (group, f) (doc sections 2-3): {coll_hex['post'][tid]}"
                if sts == "UNRESOLVED":
                    sts_src += f"; unresolved only at IT(180) rows; read-only re-run says: {resolved180.get(tid, 'not listed')} (store verdict stands)"
        assert sts in TS_VALUES
        families = sorted({s["system"] for s in cub_s + tet_s + hex_s})
        row = OrderedDict([
            ("catalog_id", catalog_id),
            ("type_id", tid),
            ("canon_code_sha256", hashlib.sha256(eh["canon_code"].encode("ascii")).hexdigest()),
            ("canon_code", eh["canon_code"]),
            ("first_sighting_system", family),
            ("first_sighting_family", family),
            ("first_sighting_crystal_system", sg[w["group"]]["crystal_system"] if w else None),
            ("systems_sighted", families),
            ("crystal_families_sighted", families),
            ("crystal_systems_sighted", sorted({s["crystal_system"] for s in cub_s + tet_s + hex_s})),
            ("witness_group", w["group"] if w else None),
            ("witness_group_symbol", (sg[w["group"]]["international_short"] if w else None)),
            ("witness_crystal_system", (sg[w["group"]]["crystal_system"] if w else None)),
            ("witness_point", list(wpt) if wpt else None),
            ("witness_kind", w["kind"] if w else None),
            ("witness_c_over_a", (w.get("b") if w else None)),
            ("witness_stratum_dim", w["stratum_dim"] if w else None),
            ("witness_site_stabilizer_order", w["stabilizer_order"] if w else None),
            ("witness_orbit_conventional", w["orbit_conventional"] if w else None),
            ("witness_orbit_primitive", w["orbit_primitive"] if w else None),
            ("witness_source", w_src),
            ("wyckoff_letter", wy[0] if wy else None),
            ("wyckoff_site_symmetry", wy[1] if wy else None),
            ("wyckoff_source", wy_src),
            ("f_vector", list(f)), ("V", f[0]), ("E", f[1]), ("F", f[2]),
            ("p_vector", p), ("p_vector_str", pvec_str(p)),
            ("aut_order", eh["aut_order"]),
            ("nonsimple_vertices_witness", w["nonsimple_vertices"] if w else None),
            ("degenerate_flag_witness", w["degenerate_flag"] if w else None),
            ("lattice_degenerate_witness", w["lattice_degenerate"] if w else None),
            ("float_superseded_witness", w["float_superseded"] if w else None),
            ("open_wall", ow[0] if ow else None),
            ("open_wall_source", ow[1] if ow else "not stored; no perturbation run on record for this type"),
            ("seeded", bool(eh.get("seeded"))),
            ("seed_source", eh.get("seed_source")),
            ("n_sightings_cubic", len(cub_s)), ("n_sightings_tetragonal", len(tet_s)),
            ("n_sightings_tetragonal_menu", len([s for s in tet_s if s["kind"] != "schmitt_printed"])),
            ("n_sightings_hexagonal", len(hex_s)),
            ("n_sightings_hexagonal_menu", len([s for s in hex_s if s["kind"] != "schmitt_printed"])),
            ("groups_sighted_cubic", groups_cubic),
            ("groups_sighted_tetragonal", groups_tet_all),
            ("groups_sighted_tetragonal_menu", groups_tet_menu),
            ("groups_sighted_hexagonal", groups_hex_all),
            ("groups_sighted_hexagonal_menu", groups_hex_menu),
            ("sighted_by_kinds_tetragonal", e2.get("sighted_by_kinds") if e2 else None),
            ("schmitt_printed_only_tetragonal", e2.get("schmitt_printed_only") if e2 else None),
            ("sighted_by_kinds_hexagonal", eh.get("sighted_by_kinds")),
            ("schmitt_printed_only_hexagonal", eh.get("schmitt_printed_only")),
            ("c_over_a_values_menu", [str(b) for b in b_menu]),
            ("c_over_a_values_all", [str(b) for b in b_all]),
            ("c_over_a_values_hexagonal_menu", [str(b) for b in hb_menu]),
            ("c_over_a_values_hexagonal_all", [str(b) for b in hb_all]),
            ("gate_G3", g3),
            ("gate_G4_certified", g4_status), ("gate_G4_pointer", g4),
            ("g4_status", g4_status_v2),
            ("g4_certificate_file", g4),
            ("g4_results_doc", g4_doc),
            ("g4_acceptance", g4_acc),
            ("g4_chiral_solid", g4_chiral),
            ("g4_chiral_solid_source", g4_chiral_src),
            ("g4_chiral_honeycomb", g4_hc),
            ("name", name), ("name_status", name_status),
            ("schmitt_fvector_flag_sighted_groups", fflag),
            ("schmitt_fvector_present_in_sighted_groups", f_present),
            ("schmitt_fvector_absent_in_sighted_groups", f_absent),
            ("schmitt_fvector_printed_anywhere_cubic", f_any_cubic),
            ("schmitt_fvector_printed_anywhere_tetragonal", f_any_tet),
            ("schmitt_fvector_printed_anywhere_hexagonal", f_any_hex),
            ("schmitt_type_level_status", type_level_status),
            ("schmitt_type_level_detail", type_level),
            ("schmitt_match_hexagonal", hmatch),
            ("novelty_wording", ("seeded classical type" if eh.get("seeded") else
                                 f"not matched against the records checked as of {SNAPSHOT}; f-vector agreement is not type identity; Schmitt's survey is a sampling")),
            # v3 columns (appended; every v1/v2 column above is unchanged)
            ("open_wall_verdict", o3["verdict"] if o3 else "not-computed"),
            ("open_wall_verdict_source", o3["source"] if o3 else "none"),
            ("open_wall_point_verdict", o3["point_verdict"] if o3 else None),
            ("open_wall_metric_verdict", o3["metric_verdict"] if o3 else None),
            ("open_wall_flags", o3["flags"] if o3 else None),
            ("open_wall_verdict_pointer", o3["pointer"] if o3 else "not computed: no perturbation run on record for this type (c1 covered the 7 cubic finalists; #148 the 165 G4-certified phase-2 cells)"),
            ("open_wall_scheme", o3["scheme"] if o3 else None),
            ("open_wall_scheme_date", o3["scheme_date"] if o3 else None),
            ("schmitt_type_status", sts),
            ("schmitt_type_status_source", sts_src),
            ("sightings", cub_s + tet_s + hex_s),
        ])
        rows.append(row)

    assert n_cub == 102 and n_tet == 789 and n_hex == 692 and len(rows) == 1583

    # --- summary ---------------------------------------------------------------
    per_group = defaultdict(lambda: Counter())
    for r in rows:
        for g in r["groups_sighted_cubic"]:
            per_group[g]["types_sighted"] += 1
        for g in r["groups_sighted_tetragonal"]:
            per_group[g]["types_sighted"] += 1
        for g in r["groups_sighted_tetragonal_menu"]:
            per_group[g]["types_sighted_menu"] += 1
        for g in r["groups_sighted_hexagonal"]:
            per_group[g]["types_sighted"] += 1
        for g in r["groups_sighted_hexagonal_menu"]:
            per_group[g]["types_sighted_menu"] += 1
        if r["witness_group"] is not None:
            per_group[r["witness_group"]]["types_first_here"] += 1
    is_tet = lambda r: r["first_sighting_system"] == "tetragonal"
    is_hex = lambda r: r["first_sighting_system"] == "hexagonal"
    is_cub = lambda r: r["first_sighting_system"] == "cubic"
    summary = OrderedDict([
        ("catalog_version", CATALOG_VERSION),
        ("n_types_total", len(rows)),
        ("n_types_cubic_first", n_cub),
        ("n_types_tetragonal_first", n_tet),
        ("n_types_hexagonal_first", n_hex),
        ("n_types_by_first_sighting_family", OrderedDict([("cubic", n_cub), ("tetragonal", n_tet), ("hexagonal", n_hex)])),
        ("n_types_by_first_sighting_crystal_system", OrderedDict(sorted(Counter(r["first_sighting_crystal_system"] or "none (seeded type without a phase-1 witness)" for r in rows).items()))),
        ("n_seeded", sum(1 for r in rows if r["seeded"])),
        ("n_seeded_never_sighted", sum(1 for r in rows if r["seeded"] and r["n_sightings_cubic"] + r["n_sightings_tetragonal"] + r["n_sightings_hexagonal"] == 0)),
        ("n_tetragonal_first_menu_sighted", sum(1 for r in rows if is_tet(r) and not r["schmitt_printed_only_tetragonal"])),
        ("n_tetragonal_first_schmitt_printed_only", sum(1 for r in rows if is_tet(r) and r["schmitt_printed_only_tetragonal"])),
        ("n_hexagonal_first_menu_sighted", sum(1 for r in rows if is_hex(r) and not r["schmitt_printed_only_hexagonal"])),
        ("n_hexagonal_first_schmitt_printed_only", sum(1 for r in rows if is_hex(r) and r["schmitt_printed_only_hexagonal"])),
        ("n_cubic_first_resighted_tetragonal", sum(1 for r in rows if is_cub(r) and r["n_sightings_tetragonal"] > 0)),
        ("n_cubic_first_resighted_tetragonal_menu", sum(1 for r in rows if is_cub(r) and r["n_sightings_tetragonal_menu"] > 0)),
        ("n_prior_resighted_hexagonal", sum(1 for r in rows if not is_hex(r) and r["n_sightings_hexagonal"] > 0)),
        ("n_prior_resighted_hexagonal_menu", sum(1 for r in rows if not is_hex(r) and r["n_sightings_hexagonal_menu"] > 0)),
        ("n_cubic_first_resighted_hexagonal", sum(1 for r in rows if is_cub(r) and r["n_sightings_hexagonal"] > 0)),
        ("n_tetragonal_first_resighted_hexagonal", sum(1 for r in rows if is_tet(r) and r["n_sightings_hexagonal"] > 0)),
        ("n_G4_certified_accepted", sum(1 for r in rows if r["gate_G4_certified"].startswith("yes"))),
        ("n_G4_provisional_tables_present", sum(1 for r in rows if r["gate_G4_certified"].startswith("tables present"))),
        ("g4_status_counts", OrderedDict((k, sum(1 for r in rows if r["g4_status"] == k)) for k in ("accepted-cubic", "certified-tetragonal", "certified-hexagonal", "none"))),
        ("g4_chiral_solid_counts", OrderedDict([
            ("chiral", sum(1 for r in rows if r["g4_chiral_solid"] is True)),
            ("achiral", sum(1 for r in rows if r["g4_chiral_solid"] is False)),
            ("not_recorded_in_certificate", sum(1 for r in rows if r["g4_status"] != "none" and r["g4_chiral_solid"] is None)),
            ("by_status", OrderedDict((k, OrderedDict([("chiral", sum(1 for r in rows if r["g4_status"] == k and r["g4_chiral_solid"] is True)),
                                                       ("achiral", sum(1 for r in rows if r["g4_status"] == k and r["g4_chiral_solid"] is False)),
                                                       ("not_recorded", sum(1 for r in rows if r["g4_status"] == k and r["g4_chiral_solid"] is None))]))
                                       for k in ("accepted-cubic", "certified-tetragonal", "certified-hexagonal"))),
        ])),
        ("g4_chiral_honeycomb_counts", OrderedDict([
            ("chiral", sum(1 for r in rows if r["g4_chiral_honeycomb"] is True)),
            ("achiral", sum(1 for r in rows if r["g4_chiral_honeycomb"] is False)),
        ])),
        ("n_named_program", sum(1 for r in rows if r["name_status"].startswith("named"))),
        ("n_held", sum(1 for r in rows if r["name_status"].startswith("HELD"))),
        ("n_descriptive_pending", sum(1 for r in rows if r["name_status"].startswith("descriptive"))),
        ("max_F_all", max(r["F"] for r in rows)),
        ("max_F_cubic_first", max(r["F"] for r in rows if is_cub(r))),
        ("max_F_tetragonal_menu", max(r["F"] for r in rows if is_tet(r) and not r["schmitt_printed_only_tetragonal"])),
        ("max_F_tetragonal_first", max(r["F"] for r in rows if is_tet(r))),
        ("max_F_hexagonal_menu", max(r["F"] for r in rows if is_hex(r) and not r["schmitt_printed_only_hexagonal"])),
        ("max_F_hexagonal_first", max(r["F"] for r in rows if is_hex(r))),
        ("n_distinct_fvectors", len({tuple(r["f_vector"]) for r in rows})),
        ("n_distinct_fvectors_cubic_first", len({tuple(r["f_vector"]) for r in rows if is_cub(r)})),
        ("n_distinct_fvectors_tetragonal_first", len({tuple(r["f_vector"]) for r in rows if is_tet(r)})),
        ("n_distinct_fvectors_hexagonal_first", len({tuple(r["f_vector"]) for r in rows if is_hex(r)})),
        ("schmitt_type_level", Counter(r["schmitt_type_level_status"].split(" ")[0] for r in rows)),
        ("schmitt_fvector_flag", Counter(r["schmitt_fvector_flag_sighted_groups"] for r in rows)),
        ("schmitt_match_hexagonal", OrderedDict([
            ("hexagonal_first_SURVIVOR", sum(1 for r in rows if is_hex(r) and r["schmitt_match_hexagonal"].startswith("SURVIVOR"))),
            ("hexagonal_first_COLLISION", sum(1 for r in rows if is_hex(r) and r["schmitt_match_hexagonal"].startswith("COLLISION"))),
            ("hexagonal_first_UNRESOLVED", sum(1 for r in rows if is_hex(r) and r["schmitt_match_hexagonal"].startswith("UNRESOLVED"))),
            ("hexagonal_first_S_cell_printed_only", sum(1 for r in rows if is_hex(r) and r["schmitt_match_hexagonal"].startswith("S-cell, printed-only"))),
            ("prior_resighted_in_family", sum(1 for r in rows if r["schmitt_match_hexagonal"].startswith("prior"))),
            ("no_hexagonal_sighting", sum(1 for r in rows if r["schmitt_match_hexagonal"].startswith("n/a"))),
        ])),
        ("per_group", OrderedDict((str(g), OrderedDict(sorted(per_group[g].items()))) for g in sorted(per_group))),
        ("per_system_types_sighted", OrderedDict([
            ("cubic", sum(1 for r in rows if "cubic" in r["systems_sighted"])),
            ("tetragonal", sum(1 for r in rows if "tetragonal" in r["systems_sighted"])),
            ("hexagonal", sum(1 for r in rows if "hexagonal" in r["systems_sighted"])),
        ])),
        ("per_crystal_system_types_sighted", OrderedDict((k, sum(1 for r in rows if k in r["crystal_systems_sighted"])) for k in ("cubic", "tetragonal", "trigonal", "hexagonal"))),
    ])
    # --- v3 summary blocks -------------------------------------------------------
    def fam_rows(f):
        return [r for r in rows if r["first_sighting_family"] == f]
    for r in rows:
        assert r["open_wall_verdict"] in OW_VERDICTS and r["open_wall_verdict_source"] in OW_SOURCES and r["schmitt_type_status"] in TS_VALUES, r["type_id"]
        assert (r["open_wall_verdict"] == "not-computed") == (r["open_wall_verdict_source"] == "none"), r["type_id"]
    summary["open_wall_verdict_counts"] = OrderedDict(
        (f, OrderedDict((v, sum(1 for r in fam_rows(f) if r["open_wall_verdict"] == v)) for v in OW_VERDICTS)) for f in FAMILIES)
    summary["open_wall_verdict_source_counts"] = OrderedDict(
        (f, OrderedDict((s, sum(1 for r in fam_rows(f) if r["open_wall_verdict_source"] == s)) for s in OW_SOURCES)) for f in FAMILIES)
    summary["schmitt_type_status_counts"] = OrderedDict(
        (f, OrderedDict((s, sum(1 for r in fam_rows(f) if r["schmitt_type_status"] == s)) for s in TS_VALUES)) for f in FAMILIES)
    summary["open_wall_x_schmitt_type_status"] = OrderedDict(
        (f, OrderedDict((v, OrderedDict((s, sum(1 for r in fam_rows(f) if r["open_wall_verdict"] == v and r["schmitt_type_status"] == s)) for s in TS_VALUES)) for v in OW_VERDICTS)) for f in FAMILIES)
    pool = OrderedDict()
    for f in FAMILIES:
        members = [r for r in fam_rows(f) if r["g4_status"] != "none" and r["open_wall_verdict"] == "OPEN" and r["name"] is None]
        pool[f] = OrderedDict([
            ("definition", "G4-certified (g4_status != none) AND open_wall_verdict == OPEN AND unnamed (name is null: no program / descriptive / HELD / literature / seed name)"),
            ("n_certified_open_unnamed", len(members)),
            ("n_certified", sum(1 for r in fam_rows(f) if r["g4_status"] != "none")),
            ("n_certified_open", sum(1 for r in fam_rows(f) if r["g4_status"] != "none" and r["open_wall_verdict"] == "OPEN")),
            ("n_certified_not_computed", sum(1 for r in fam_rows(f) if r["g4_status"] != "none" and r["open_wall_verdict"] == "not-computed")),
            ("catalog_ids", [r["catalog_id"] for r in members]),
            ("type_ids", [r["type_id"] for r in members]),
        ])
    summary["naming_pool"] = pool
    summary["naming_pool_note"] = ("Pool membership is catalog-relative: every member is 'not matched against the records checked as of 2026-09-04'; G5 diligence (print-only Engel / Koch exposure) "
                                   "still applies before any name; no name is proposed here. Asserted == PROGRAM_LEDGER 2026-09-04 14:10 ('13 tetragonal + 102 hexagonal').")
    summary["schmitt_type_status_tetragonal_storeside"] = OrderedDict([
        ("source", "v4: harness/collision_phase2_tetragonal_storeside.json (subagent #152, 2026-09-04; rule = COLLISION_PHASE2_HEX_RESULTS.md section 1 store-side rule re-implemented, hexagonal equivalence asserted 151/124/13; dated addendum in harness/COLLISION_PHASE2_RESULTS.md)"),
        ("json_md5", ss_md5),
        ("n_menu_sighted", ss["n_tetragonal_menu_sighted"]), ("n_s_cells", ss["n_tetragonal_s_cells"]),
        ("counts_pure_store_side_rule", OrderedDict(ss["counts_pure_store_side_rule"])),
        ("counts_with_recomputed_pairs_overlaid", OrderedDict(ss["counts_combined"])),
        ("counts_catalog_v3", OrderedDict(ss["counts_catalog_v3"])),
        ("transitions_v3_to_v4", OrderedDict(ss["transitions_v3_to_combined"])),
        ("shortlist_disagreements", ss["shortlist_disagreements"]),
        ("note", "the overlay = the 27 printed pairs recomputed in collision_phase2_check.py resolve their rows (SAME -> COLLISION; DIFFERENT on an unstored row -> row resolved); under the pure rule alone 5 of the 14 certified survivors and the 1 collision read UNRESOLVED because their worklist rows were unstored; [v5] the 106 UNRESOLVED of this block are settled in the block schmitt_type_status_tetragonal_unresolved_recomputed"),
    ])
    trans_v4_v5 = Counter((tet_ss[t]["status"], (tet_ov[t]["status"] if t in tet_ov else tet_ss[t]["status"])) for t in tet_ss)
    summary["schmitt_type_status_tetragonal_unresolved_recomputed"] = OrderedDict([
        ("source", "v5: harness/collision_phase2_tetragonal_unresolved_overlay.json + collision_phase2_tetragonal_rows_recomputed.json (subagent #154, 2026-09-04; script harness/collision_phase2_tetragonal_rows_recompute.py; dated addendum in harness/COLLISION_PHASE2_RESULTS.md): the 62 unstored printed rows behind the 106 v4-UNRESOLVED types recomputed at the printed points with the documented setting conversions of PHASE2_SCHMITT_ORIGIN_CHECK.md through the accepted phase-2 exact chain"),
        ("overlay_json_md5", ov_md5), ("rows_json_md5", rows_md5),
        ("n_rows_recomputed", rows_j["n_rows"]), ("row_status_counts", OrderedDict(rows_j["row_status_counts"])),
        ("rows_per_group", OrderedDict(rows_j["rows_per_group"])),
        ("n_cells_computed", sum(len(r["cells"]) for r in rows_j["rows"].values())),
        ("rows_with_documented_conventions_agreeing", sum(1 for r in rows_j["rows"].values() if r["documented_conventions_agree"])),
        ("rows_where_the_other_origin_or_enantiomorph_reading_reproduces_f", sum(1 for r in rows_j["rows"].values() if r["other_reading_reproduces_printed_f"])),
        ("row_cells_not_stored_under_any_id", sum(1 for r in rows_j["rows"].values() if r["code"] and not r["store_hit"])),
        ("row_cells_that_are_stored_types_outside_the_106", OrderedDict((k, len(v)) for k, v in rows_j["row_cells_that_are_stored_types_outside_the_106"].items())),
        ("counts_106", OrderedDict(ov["counts_106"])),
        ("counts_404_before_v4", OrderedDict(ov["counts_404_before_v4"])),
        ("counts_404_after_v5", OrderedDict(ov["counts_404_after_v5"])),
        ("transitions_v4_to_v5", OrderedDict((f"{a} -> {b}", n) for (a, b), n in sorted(trans_v4_v5.items()))),
        ("still_unresolved", ov["still_unresolved"]),
        ("secondary_hits", ov["secondary_hits"]),
        ("surprises", rows_j["surprises"]),
        ("rule", ov["rule"]),
        ("note", "row status REPRODUCED = printed f-vector reproduced under >= 1 documented convention with one canonical code across the reproducing conventions; the other origin / enantiomorph reading (printed point verbatim) was run and recorded for every two-origin / 95 / 96 row and never reproduced the printed f (it is exactly pass P2's quarantined run); the 14 certified survivors were never UNRESOLVED and are untouched; nothing was added to any store"),
    ])
    ow_counts = summary["open_wall_verdict_counts"]
    assert ow_counts["cubic"] == OrderedDict([("OPEN", 6), ("WALL", 1), ("ONE-SIDED", 0), ("not-computed", 95)]), ow_counts["cubic"]
    for fam in ("tetragonal", "hexagonal"):
        got = {k: v for k, v in ow_counts[fam].items() if k != "not-computed"}
        want = dict(wo["aggregate"][fam]["combined"])
        want.setdefault("ONE-SIDED", 0)
        assert got == want, (fam, got, want)
        assert ow_counts[fam]["not-computed"] == len(fam_rows(fam)) - wo["aggregate"][fam]["n"], fam
    assert ow_counts["tetragonal"]["OPEN"] == 13 and ow_counts["tetragonal"]["WALL"] == 1
    assert ow_counts["hexagonal"]["OPEN"] == 102 and ow_counts["hexagonal"]["WALL"] == 40 and ow_counts["hexagonal"]["ONE-SIDED"] == 9
    ts_counts = summary["schmitt_type_status_counts"]
    assert ts_counts["cubic"] == OrderedDict([("SURVIVOR", 0), ("COLLISION", 0), ("UNRESOLVED", 0), ("printed-only", 0), ("not-screened", 102)])
    assert ts_counts["tetragonal"] == OrderedDict([("SURVIVOR", 203), ("COLLISION", 201), ("UNRESOLVED", 0), ("printed-only", 385), ("not-screened", 0)]), ts_counts["tetragonal"]
    assert dict(ts_counts["tetragonal"]) == {**ov["counts_404_after_v5"], "printed-only": 385, "not-screened": 0}
    assert dict(summary["schmitt_type_status_tetragonal_unresolved_recomputed"]["transitions_v4_to_v5"]) == {"COLLISION -> COLLISION": 177, "SURVIVOR -> SURVIVOR": 121, "UNRESOLVED -> COLLISION": 24, "UNRESOLVED -> SURVIVOR": 82}
    for t, e in tet_screen.items():   # the 15 shortlist statuses are untouched by v5 (none was UNRESOLVED)
        assert next(r for r in rows if r["type_id"] == t)["schmitt_type_status"] == ("SURVIVOR" if e["n_same"] == 0 else "COLLISION"), t
    assert ts_counts["hexagonal"] == OrderedDict([("SURVIVOR", 151), ("COLLISION", 124), ("UNRESOLVED", 13), ("printed-only", 404), ("not-screened", 0)]), ts_counts["hexagonal"]
    assert pool["tetragonal"]["n_certified_open_unnamed"] == 13 and pool["hexagonal"]["n_certified_open_unnamed"] == 102, "naming pool != PROGRAM_LEDGER 2026-09-04 14:10"
    assert pool["cubic"]["n_certified_open_unnamed"] == 0 and pool["cubic"]["n_certified_not_computed"] == 5
    for f in ("tetragonal", "hexagonal"):
        assert all(r["schmitt_type_status"] == "SURVIVOR" for r in fam_rows(f) if r["type_id"] in pool[f]["type_ids"]), f
        assert pool[f]["n_certified_not_computed"] == 0, f

    for k, v in V1_SUMMARY.items():
        assert summary[k] == v, (k, summary[k], v)
    for k, v in V2_SUMMARY.items():
        assert summary[k] == v, (k, summary[k], v)
    assert summary["g4_chiral_solid_counts"]["chiral"] == V2_CHIRAL["solid_chiral"] and summary["g4_chiral_solid_counts"]["achiral"] == V2_CHIRAL["solid_achiral"]
    assert summary["g4_chiral_honeycomb_counts"] == OrderedDict([("chiral", V2_CHIRAL["honeycomb_chiral"]), ("achiral", V2_CHIRAL["honeycomb_achiral"])])
    for k, v in V2_HEXMATCH.items():
        assert summary["schmitt_match_hexagonal"][k] == v, (k, summary["schmitt_match_hexagonal"][k], v)
    assert summary["n_hexagonal_first_menu_sighted"] == hx["n_types_hexagonal_menu_sighted"] == 288
    assert summary["n_hexagonal_first_schmitt_printed_only"] == hx["n_types_hexagonal_schmitt_printed_only"] == 404
    assert summary["max_F_all"] == summary["max_F_hexagonal_first"] == hx["max_facets_stored"] == 34 or summary["max_F_all"] == 35
    assert summary["max_F_hexagonal_menu"] == hx["max_facets_from_our_menu"] == 24
    assert summary["g4_status_counts"] == OrderedDict([("accepted-cubic", 12), ("certified-tetragonal", 14), ("certified-hexagonal", 151), ("none", 1583 - 177)])
    assert summary["n_G4_provisional_tables_present"] == 0

    field_sources = OrderedDict([
        ("catalog_id", "assigned here: MINT-C### / MINT-T### / MINT-H### in phase2_hexagonal_types.json type_order (= phase2_types.json order for the first 891, then hexagonal first-sighting order); stable across re-runs; v1 ids unchanged"),
        ("type_id", "store key = sha1(canon_code)[:16] (sweep_phase1.py line 139; verified for all 1,583)"),
        ("canon_code", "types[id].canon_code (all three stores; identical for the shared ids)"),
        ("first_sighting_system / first_sighting_family", "phase2_hexagonal_types.json types[id].first_sighting_system, mapped to the crystal FAMILY name: 'cubic (phase 1 store)' -> cubic, 'tetragonal (phase 2)' -> tetragonal, 'hexagonal (phase 2 batch 2)' -> hexagonal (the hexagonal family = trigonal + hexagonal crystal systems, IT 143-194)"),
        ("first_sighting_crystal_system", "harness/spacegroups.json groups[witness_group].crystal_system (cubic / tetragonal / trigonal / hexagonal)"),
        ("systems_sighted / crystal_families_sighted", "families with >= 1 stored sighting (phase1 sightings -> cubic; phase2 -> tetragonal; hexagonal store -> hexagonal); 'systems_sighted' is the v1 name kept for compatibility"),
        ("crystal_systems_sighted", "spacegroups.json crystal_system of every sighted group (trigonal and hexagonal split)"),
        ("witness_*", "phase1 first_witness (cubic-first) / phase2 first_witness (tetragonal-first) / hexagonal store first_witness (hexagonal-first); seeded types have first_witness=null and use sightings[0]; 'b' field = c/a (hexagonal family: b = ||b3'||/||b1'|| = c/a in the ITA basis)"),
        ("witness_group_symbol / witness_crystal_system", "harness/spacegroups.json groups[].international_short / crystal_system (frozen G1 table)"),
        ("wyckoff_*", "NOT stored in any dedupe store; filled only for the 7 finalists from paper/wyckoff_check.txt (spglib 2.7.0) and the Laves cell from STATUS.md; null elsewhere"),
        ("f_vector / p_vector / aut_order", "types[id].f_vector / p_vector / aut_order (aut = combinatorial automorphism order of the canonical code)"),
        ("nonsimple_vertices / degenerate_flag / lattice_degenerate / float_superseded", "per-sighting store fields, reported for the witness sighting"),
        ("open_wall", "NOT a store field; from harness/round1_computations/c1_wall_open.json (7 cubic finalists) and collision_phase2_results.json perturbation block (3 tetragonal shortlist types); null = no perturbation run on record (the computed open/wall classification of all 165 certified phase-2 cells is agent #148's task, not yet on disk at this build) [v3 note: this v1/v2 column and its open_wall_source pointer are kept verbatim; the computed verdicts of all 172 cells with a run on record are in open_wall_verdict]"),
        ("sightings", "phase1 types[id].sightings (cubic) + phase2 types[id].sightings (tetragonal) + hexagonal store types[id].sightings (hexagonal family); phase 2 does NOT carry the phase-1 sightings of cubic-first types (phase1_sightings is a count only) and the hexagonal store carries only its own sightings of the 891 prior types (prior_sightings is a count only; asserted == the merged count here); per sighting 'crystal_system' is added from spacegroups.json; hexagonal P2 sightings carry printed_point_Bpp (his point as printed, B'' basis), conversion (H1 / H1+zflip), schmitt_primary_group, pdf_page"),
        ("schmitt_printed_only_tetragonal", "phase2 types[id].schmitt_printed_only (note: also True for one cubic-first type, 2001fe7ea92fd0ad, re-sighted in tetragonal groups only at his printed points)"),
        ("sighted_by_kinds_hexagonal / schmitt_printed_only_hexagonal", "hexagonal store types[id].sighted_by_kinds / schmitt_printed_only (for the 891 prior types the flag describes their HEXAGONAL sightings only; null kinds = no hexagonal sighting)"),
        ("n_sightings_hexagonal / n_sightings_hexagonal_menu / groups_sighted_hexagonal(_menu) / c_over_a_values_hexagonal_*", "hexagonal store types[id].sightings; 'menu' = kind != schmitt_printed (passes P1/P3/P4/P5); c/a values are the sightings' b field; the tetragonal c_over_a_values_* columns are unchanged from v1 (tetragonal sightings only)"),
        ("gate_G3", "store membership invariant (ANCHORS G3): every non-seeded stored type passed float->exact->canon agreement; seeded types are G2 seed-catalog entries"),
        ("gate_G4_certified / gate_G4_pointer", "v1 columns kept: existence of harness/g4_tables_<id>.json (11 accepted 2026-08-30), track4/g4_tables_laves17.json (accepted 2026-09-03), harness/g4p2_tables_<id>.json (14, accepted 2026-09-04 01:35), harness/g4p2hex_tables_<id>.json (151, accepted 2026-09-04 13:25); 'tables present, PROVISIONAL' no longer occurs"),
        ("g4_status", "accepted-cubic (11 cubic ladder + Laves track4) / certified-tetragonal (14; Gram ladder g4_certify_gram.py) / certified-hexagonal (151; g4_certify_hex.py) / none; every certificate set asserted == the ids in its results doc and, for the hexagonal batch, == the collision-screen survivors"),
        ("g4_certificate_file / g4_results_doc / g4_acceptance", "the V3 tables file (relative to paper_prep/MINT_plesiohedron/), the results document, and the main-session acceptance record (STATUS.md / PROGRAM_LEDGER.md dates)"),
        ("g4_chiral_solid", "V2 rung of the certificate: tetragonal from G4_PHASE2_RESULTS.md 'Isometry vs site vs aut summary' column 'solid'; hexagonal from harness/g4p2hex_cells/<id>.json sym.chiral asserted == the 'chiral?' column of G4_PHASE2_HEX_RESULTS.md; null for the 12 cubic certificates (the cubic ladder doc records no solid-chirality rung; TRACK4 records honeycomb chirality only) and for uncertified types"),
        ("g4_chiral_honeycomb", "derived from the certificate tables file itself: n_improper == 0 (every point operation of the honeycomb's symmetry group mod L is proper); present for all 177 certified types; null for uncertified types"),
        ("name / name_status", "publication/<id8>_<Name>/ folder names; seed_name for seeded types; STATUS.md for the two literature rediscoveries; no hexagonal-family type is named"),
        ("schmitt_fvector_*", "cubic: SCHMITT_FVECTORS in harness/triage_phase1.py (881 rows; 213 aliases 212), 386 rows independently re-keyed (harness/rekey_tables.json); tetragonal: harness/schmitt_tetragonal_tables.json (1,476 rows, single-pass visual + text-layer cross-check, NOT re-keyed); hexagonal family: harness/schmitt_hexagonal_tables.json (958 rows, 45 blocks, text-layer primary + 153-row visual cross-read, NOT re-keyed; enantiomorphic pairs share one printed table and both members get the same printed set here)"),
        ("schmitt_type_level_*", "harness/SCHMITT_COLLISION_RESULTS.md (21 pairs), harness/CROSS_GROUP_RESULTS.md (55 pairs), harness/collision_phase2_results.json (27 pairs), harness/collision_phase2_hex_results.json (26 pairs, top-10 hexagonal survivors), phase-2 and batch-2 P2 'schmitt_printed' sightings (type reproduces his printed cell), the read-only IT(180) re-run harness/phase2_hex_schmitt_180_check.json (46 rows, cells already stored), and the dedupe inference: a printed row reproduced by P2 and stored under a different id is a different type from this one"),
        ("schmitt_match_hexagonal", "hexagonal-first menu-sighted (288): store-side collision-screen verdict SURVIVOR/COLLISION/UNRESOLVED read from harness/TRIAGE_PHASE2_HEX_RESULT.md (full ranked table) and re-derived here from the store + digitization with the documented rule (asserted equal for all 288; counts asserted == collision_phase2_hex_results.json screen_counts); hexagonal-first printed-only (404): S-cell; prior types re-sighted in the family (43): f-vector flag only, NOT screened in this family; others: n/a"),
        ("novelty_wording", "fixed snapshot sentence (ANCHORS G5 amendment)"),
        # ---- v3 columns ----
        ("open_wall_verdict", "v3: OPEN / WALL / ONE-SIDED / not-computed. 7 cubic finalists: harness/round1_computations/c1_wall_open.json [].verdict (c1 round, run 2026-09-03; asserted == the v1/v2 open_wall head token); "
                              "165 G4-certified phase-2 cells (14 tetragonal + 151 hexagonal-family): harness/phase2/WALL_OPEN_PHASE2.json cells[].combined_verdict (agent #148 under the pre-registered scheme, accepted 2026-09-04 14:10; "
                              "file md5 asserted == the value stated in WALL_OPEN_PHASE2.md; per-family verdict counts asserted == the file's aggregate block; witness point / c/a / group / f / aut / stratum dim asserted == the stores; "
                              "the three top-3 tetragonal POINT verdicts asserted == collision_phase2_results.json 'perturbation'); every other type: not-computed (no perturbation run on record)"),
        ("open_wall_verdict_source", "v3: 'c1 cubic' (7) / 'phase2 #148' (165) / 'none' (1,411). The v2 column open_wall_source is untouched (it carries the v1/v2 pointer text of the open_wall column)"),
        ("open_wall_point_verdict / open_wall_metric_verdict / open_wall_flags", "v3: WALL_OPEN_PHASE2.json cells[].point_verdict / metric_verdict ('n/a' at stratum dim 0) and the true entries of cells[].flags (degenerate_flag_any, float_superseded_any, line_isolated, nonsimple_vertex, quarantine_any, stab_change_any; flags are never verdict inputs); c1 cells: point verdict = the verdict, metric 'n/a (cubic)', flags null (c1 records none)"),
        ("open_wall_verdict_pointer / open_wall_scheme / open_wall_scheme_date", "v3: file + record pointer with doc rank, POINT/METRIC split, wall directions, the previous heuristic label and its agreement flag, and the acceptance record; the scheme text (pre-registered 2026-09-04 in ANCHORS.md for phase 2; c1 round-1 scheme of 2026-09-03 for the cubic finalists) and its date"),
        ("schmitt_type_status", "v3: SURVIVOR / COLLISION / UNRESOLVED / printed-only / not-screened, from the two phase-2 collision screens. Tetragonal-first: harness/COLLISION_PHASE2_RESULTS.md (top-15 shortlist, 27 printed pairs; per target from collision_phase2_results.json: any 'SAME TYPE' pair = COLLISION, else SURVIVOR; asserted == the doc's 'Summary per shortlist type' lines; the 14 SURVIVORs = the 14 tetragonal certificates, 1 COLLISION cd4fb52572edcb73), "
                                "Schmitt-printed-only types (phase2 store flag, 385) = printed-only; [v4] the other 389 menu-sighted types (not-screened in v3) carry the store-side screen status of harness/collision_phase2_tetragonal_storeside.json (COLLISION_PHASE2_RESULTS.md addendum 2026-09-04: the hexagonal screen's rule applied to all 404 menu-sighted tetragonal types, hexagonal equivalence asserted 151/124/13, the 27 recomputed shortlist pairs overlaid; v4 tetragonal totals COLLISION 177 / SURVIVOR 121 / UNRESOLVED 106 / printed-only 385 / not-screened 0); "
                                "[v5] the 106 v4-UNRESOLVED types carry the status of harness/collision_phase2_tetragonal_unresolved_overlay.json (COLLISION_PHASE2_RESULTS.md addendum 2026-09-04, subagent #154: their 62 unstored printed rows recomputed at the printed points with the documented setting conversions, every row reproduced; any hung-on row SAME -> COLLISION (24), all DIFFERENT -> SURVIVOR (82); v5 tetragonal totals COLLISION 201 / SURVIVOR 203 / UNRESOLVED 0 / printed-only 385 / not-screened 0). "
                                "Hexagonal-first: harness/COLLISION_PHASE2_HEX_RESULTS.md section 1 store-side screen of the 288 menu-sighted types (counts asserted == collision_phase2_hex_results.json screen_counts and the doc line), per-type verdict from TRIAGE_PHASE2_HEX_RESULT.md re-derived from the store (as v2's schmitt_match_hexagonal); the 404 S-cell types = printed-only; top-10 survivors additionally recomputed at every printed row (doc sections 2-3, asserted == the JSON post block). "
                                "Cubic-first (102): not-screened by the phase-2 screens by construction (cubic-round verdicts stay in schmitt_type_level_*). SURVIVOR is catalog-relative ('not matched against the records checked as of 2026-09-04'), never novelty"),
        ("schmitt_type_status_source", "v3: the doc pointer, rank and pair counts behind schmitt_type_status, per type"),
    ])

    # cross-check the rekey (386 rows) against the ast-parsed cubic digitization
    for key, blk in rekey.items():
        if key == "_meta":
            continue
        g = int(key.split("_")[0])
        assert [tuple(r[0]) for r in blk["rows"]] == list(schmitt_cubic[g]), f"rekey vs triage digitization differ for {key}"
    n_cubic_rows = sum(len(v) for g, v in schmitt_cubic.items() if g != 213)
    n_tet_rows = sum(len(v) for v in {tet_block_of[g]: schmitt_tet[g] for g in schmitt_tet}.values())
    n_hex_rows = sum(len(v) for v in {hex_block_of[g]: schmitt_hex[g] for g in schmitt_hex}.values())
    assert n_tet_rows == 1476 and n_hex_rows == 958 == hex_meta["n_rows"] and len({hex_block_of[g] for g in schmitt_hex}) == 45 == hex_meta["n_blocks"]
    assert sorted(schmitt_hex) == HEX_GROUPS

    out = OrderedDict([
        ("title", "MINT plesiohedron combinatorial-type census (Track 3 catalog)"),
        ("build", BUILD_LABEL),
        ("catalog_version", CATALOG_VERSION),
        ("v1_reproducibility", "v1 (891 types, cubic + tetragonal) = git show 06e5d30:paper_prep/MINT_plesiohedron/catalog/build_catalog.py; v2 keeps every v1 column name and value for the 891 v1 types and asserts the v1 summary numbers unchanged"),
        ("v2_reproducibility", "v2 (1,583 types, hexagonal family + both phase-2 G4 batches) = git show 169ccb4:paper_prep/MINT_plesiohedron/catalog/build_catalog.py; v3 keeps every v1 and v2 column name, position and value (the open_wall / open_wall_source pair verbatim), appends columns and summary blocks only, and asserts the v1 and v2 summary numbers unchanged"),
        ("v3_reproducibility", "v3 (computed open/wall verdicts + type-level Schmitt status; tetragonal store-side rule not yet applied, 389 tetragonal not-screened) = git show e01618b:paper_prep/MINT_plesiohedron/catalog/build_catalog.py; v4 changes only the schmitt_type_status / schmitt_type_status_source values of the 389 tetragonal-first menu-sighted types that were not-screened in v3 (the 15 shortlist rows gain a v4 clause in the source text), the two summary blocks that count them, adds the summary block schmitt_type_status_tetragonal_storeside and the inputs entry collision_screen_tetragonal_storeside_v4, and asserts every other v1 / v2 / v3 summary number unchanged"),
        ("v4_reproducibility", "v4 (tetragonal store-side rule applied; 106 tetragonal UNRESOLVED) = git show 27e0083:paper_prep/MINT_plesiohedron/catalog/build_catalog.py; v5 changes only the schmitt_type_status / schmitt_type_status_source values of the 106 tetragonal-first menu-sighted types that were UNRESOLVED in v4 (24 -> COLLISION, 82 -> SURVIVOR; source text gains a [v5] clause), the two summary blocks that count them, adds the summary block schmitt_type_status_tetragonal_unresolved_recomputed and the inputs entry collision_screen_tetragonal_rows_recomputed_v5, and asserts every other v1 / v2 / v3 / v4 summary number unchanged (the 15 shortlist statuses and the 13 + 102 naming pool included)"),
        ("snapshot_date", SNAPSHOT),
        ("language_note", f"Every non-seeded type is 'not matched against the records checked as of {SNAPSHOT}'. "
                          "f-vector agreement with a printed Schmitt row is NOT type identity; absence from his tables is evidence, not proof; "
                          "his 2016 survey is a grid sampling, not an enumeration (ANCHORS.md G5 amendment). G4 certification is not novelty. The literature facet maximum is an observed 38, not a proven bound."),
        ("inputs", OrderedDict([
            ("phase1_types.json_sha256", p1_sha),
            ("phase2_store", p2_prov),
            ("phase2_hexagonal_store", hx_prov),
            ("schmitt_cubic_digitization_rows", n_cubic_rows),
            ("schmitt_cubic_rekeyed_rows", sum(len(b["rows"]) for k, b in rekey.items() if k != "_meta")),
            ("schmitt_tetragonal_digitization_rows", n_tet_rows),
            ("schmitt_tetragonal_meta_method", tet_meta.get("method")),
            ("schmitt_hexagonal_digitization_rows", n_hex_rows),
            ("schmitt_hexagonal_digitization_blocks", 45),
            ("schmitt_hexagonal_meta_method", hex_meta.get("method")),
            ("schmitt_hexagonal_shared_tables", hex_meta.get("shared_tables")),
            ("g4_certificate_sets", OrderedDict([("cubic_ladder", sorted(g4_cubic)), ("track4", sorted(g4_track4)),
                                                 ("tetragonal_gram_ladder", sorted(g4p2)), ("hexagonal_gram_ladder", sorted(g4p2hex))])),
            ("wall_open_phase2", OrderedDict([("file", "harness/phase2/WALL_OPEN_PHASE2.json"), ("md5", wo_md5), ("sha256", wo_sha), ("n_cells", wo["n_cells"]), ("n_crash", wo["n_crash"]),
                                              ("generated_by", wo["generated_by"]), ("pre_registration", wo["scheme"]["pre_registration"]),
                                              ("acceptance", "main-session fresh re-run 2026-09-04 14:10 (PROGRAM_LEDGER), JSON md5 identical")])),
            ("c1_wall_open", OrderedDict([("file", "harness/round1_computations/c1_wall_open.json"), ("sha256", sha256_file(C1_WALL)), ("n_cells", len(c1)),
                                          ("acceptance", "banked PROGRAM_LEDGER 2026-09-03 (shapes paper round 1 accepted)")])),
            ("collision_screen_tetragonal_storeside_v4", OrderedDict([("file", "harness/collision_phase2_tetragonal_storeside.json"), ("md5", ss_md5), ("sha256", hashlib.sha256(ss_raw).hexdigest()),
                                                                 ("doc", "harness/COLLISION_PHASE2_RESULTS.md addendum 2026-09-04 (subagent #152)"), ("n_types", len(tet_ss)), ("hexagonal_equivalence_counts", OrderedDict(he["counts_here"]))])),
            ("collision_screen_tetragonal_rows_recomputed_v5", OrderedDict([("overlay_file", "harness/collision_phase2_tetragonal_unresolved_overlay.json"), ("overlay_md5", ov_md5), ("overlay_sha256", hashlib.sha256(ov_raw).hexdigest()),
                                                                       ("rows_file", "harness/collision_phase2_tetragonal_rows_recomputed.json"), ("rows_md5", rows_md5), ("rows_sha256", hashlib.sha256(rows_raw).hexdigest()),
                                                                       ("script", "harness/collision_phase2_tetragonal_rows_recompute.py"), ("doc", "harness/COLLISION_PHASE2_RESULTS.md addendum 2026-09-04 (subagent #154)"),
                                                                       ("n_types", len(tet_ov)), ("n_rows", rows_j["n_rows"]), ("counts_106", OrderedDict(ov["counts_106"]))])),
            ("collision_screens_phase2", OrderedDict([("tetragonal", OrderedDict([("doc", "harness/COLLISION_PHASE2_RESULTS.md"), ("json", "harness/collision_phase2_results.json"), ("types_screened", len(tet_screen)), ("pairs", len(coll_tet["pairs"])), ("types_screened_store_side_v4", len(tet_ss)), ("types_unresolved_recomputed_v5", len(tet_ov))])),
                                                      ("hexagonal", OrderedDict([("doc", "harness/COLLISION_PHASE2_HEX_RESULTS.md"), ("json", "harness/collision_phase2_hex_results.json"), ("types_screened", len(triage_hex)), ("recomputed_pairs", len(coll_hex["results"]))]))])),
        ])),
        ("field_sources", field_sources),
        ("summary", summary),
        ("types", rows),
    ])
    # sightings (258,521 records) go to a sidecar so catalog.json stays small; canon_code stays inline.
    sightings = OrderedDict((r["type_id"], r.pop("sightings")) for r in rows)
    out["sightings_file"] = "catalog_sightings.json.gz  ({type_id: [sighting, ...]}; same order as 'types')"
    out["n_sightings_total"] = sum(len(v) for v in sightings.values())
    out["committed_forms_note"] = ("catalog.json (raw, > 5 MB in v2) and catalog.csv exceed the repo's 5 MB whitelist policy; "
                                   "catalog.json.gz / catalog.csv.gz (deterministic, mtime 0) are the committed forms, hashed in catalog.SHA256SUMS together with the raw files")

    def write_gz(path, data_bytes):
        # gzip with mtime=0 and no filename so re-runs are byte-identical
        with open(path, "wb") as raw_fh:
            with gzip.GzipFile(fileobj=raw_fh, mode="wb", compresslevel=9, mtime=0) as gz:
                gz.write(data_bytes)

    json_text = json.dumps(out, indent=1)
    with open(OUT_JSON, "w") as fh:
        fh.write(json_text)
    write_gz(OUT_JSON + ".gz", json_text.encode("utf-8"))
    write_gz(OUT_SIGHTINGS, json.dumps(sightings).encode("utf-8"))

    csv_cols = [c for c in rows[0].keys() if c not in ("canon_code", "sightings")]
    import io
    buf = io.StringIO()
    wtr = csv.writer(buf)
    wtr.writerow(csv_cols)
    for r in rows:
        wtr.writerow([json.dumps(r[c]) if isinstance(r[c], (list, dict)) else ("" if r[c] is None else r[c]) for c in csv_cols])
    csv_text = buf.getvalue()
    with open(OUT_CSV, "w", newline="") as fh:
        fh.write(csv_text)
    write_gz(OUT_CSV + ".gz", csv_text.encode("utf-8"))
    with open(os.path.join(HERE, "catalog.SHA256SUMS"), "w") as fh:
        for fn in ("catalog.json", "catalog.json.gz", "catalog.csv", "catalog.csv.gz", "catalog_sightings.json.gz"):
            fh.write(f"{fn}  sha256 {sha256_file(os.path.join(HERE, fn))}  ({os.path.getsize(os.path.join(HERE, fn))} bytes; {BUILD_LABEL})\n")

    print(f"catalog.json / catalog.csv (+ .gz forms, catalog.SHA256SUMS) written: {len(rows)} types (v{CATALOG_VERSION}); sightings sidecar {out['n_sightings_total']} records")
    for k, v in summary.items():
        if k != "per_group":
            print(f"  {k}: {v}")
    print("  per_group (types_first_here / types_sighted / types_sighted_menu[tet+hex]):")
    for g, c in summary["per_group"].items():
        print(f"    IT{g} {sg[int(g)]['international_short']}: first_here={c.get('types_first_here', 0)} sighted={c.get('types_sighted', 0)} menu={c.get('types_sighted_menu', '-')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
