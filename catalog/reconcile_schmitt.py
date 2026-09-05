#!/usr/bin/env python3
"""
MINT Track 3 - reconcile_schmitt.py  (v5, 2026-09-04)

f-VECTOR-LEVEL reconciliation of the catalog (catalog.json, built by
build_catalog.py) against Schmitt 2016's printed per-group tables, cubic,
tetragonal and (v2) the trigonal/hexagonal family separately. For every space
group g of the system:

  (a) OURS-IN-HIS : our types sighted in g (by OUR sweep menu) whose f-vector is
                    printed in his table for g;
  (b) OURS-NOT-HIS: our menu f-vectors in g that his table for g does not print;
  (c) HIS-NOT-OURS: his printed rows for g at whose f-vector our MENU found no
                    type in g - the coverage gap of OUR sweep, stated as such.

"Menu" = the program's own sample points (phase 1: every cubic orbit; phase 2
and batch 2: passes P1/P3/P4/P5). Pass P2 evaluated his printed points
themselves, which trivially reproduces his rows, so P2 sightings are reported
SEPARATELY (column "his rows reproduced at his own point") and never counted as
coverage.

VERSION NOTE. v1 (subagent #141, accepted 2026-09-04) covered cubic + tetragonal
and wrote RECONCILIATION.md from scratch. v2 keeps RECONCILIATION.md APPEND-ONLY:
the text above the marker "## v2 (2026-09-04)" is preserved byte for byte from
the file on disk, the cubic and tetragonal reconciliations are recomputed from
the v2 catalog and ASSERTED equal to the headline numbers in that preserved
text, and a dated v2 section (hexagonal family) is appended. v1 behaviour =
    git show 06e5d30:paper_prep/MINT_plesiohedron/catalog/reconcile_schmitt.py

v3 (2026-09-04, subagent #150) keeps the file APPEND-ONLY one level further:
everything above the marker "## v3 (2026-09-04)" (= the v1 text + the v2
section) is preserved byte for byte from the file on disk; the v1 and v2
sections are still regenerated from the (v3) catalog and ASSERTED equal to the
preserved text; then a dated v3 section is appended: the cross-tab of the two
v3 catalog columns (open_wall_verdict x schmitt_type_status) per family, the
naming-pool count (certified AND OPEN AND unnamed) asserted == 13 tetragonal +
102 hexagonal-family (PROGRAM_LEDGER 2026-09-04 14:10), the certified cells
outside the pool, and the v3 limits. v2 behaviour =
    git show 169ccb4:paper_prep/MINT_plesiohedron/catalog/reconcile_schmitt.py

v4 (2026-09-04, subagent #152) keeps the file APPEND-ONLY one level further:
everything above the marker "## v4 (2026-09-04)" (= v1 text + v2 section + v3
section) is preserved byte for byte from the file on disk (v1 + v2 still
regenerated from the v4 catalog and asserted equal; the v3 section is kept
verbatim as the pre-rule record, since its tetragonal cross-tab is superseded);
then a dated v4 section is appended: the cross-tab with the tetragonal family
under the store-side rule (COLLISION_PHASE2_RESULTS.md addendum 2026-09-04),
the v3 -> v4 status transitions, the pool (asserted still 13 + 102) and the
v4 limits. v3 behaviour =
    git show e01618b:paper_prep/MINT_plesiohedron/catalog/reconcile_schmitt.py

v5 (2026-09-04, subagent #154) keeps the file APPEND-ONLY one level further:
everything above the marker "## v5 (2026-09-04)" (= v1 text + v2 + v3 + v4
sections) is preserved byte for byte (v1 + v2 still regenerated from the v5
catalog and asserted equal; the v3 and v4 sections are kept verbatim as the
pre-recomputation record: the v4 tetragonal column 'UNRESOLVED 106' is
superseded); then a dated v5 section is appended: the cross-tab with the 106
v4-UNRESOLVED tetragonal types settled by the recomputation of their 62
unstored printed rows (COLLISION_PHASE2_RESULTS.md addendum 2026-09-04, #154),
the v4 -> v5 status transitions, the pool (asserted still 13 + 102) and the
v5 limits. v4 behaviour =
    git show 27e0083:paper_prep/MINT_plesiohedron/catalog/reconcile_schmitt.py

WORDING RULE (ANCHORS.md G5 amendment): an f-vector match is NOT type identity;
absence from his table is evidence, not proof; his survey is a grid sampling,
not an enumeration. Nothing here is a novelty claim.

Inputs (read-only): catalog.json + catalog_sightings.json.gz (this folder);
harness/triage_phase1.py (SCHMITT_FVECTORS, ast-parsed),
harness/schmitt_tetragonal_tables.json, harness/schmitt_hexagonal_tables.json,
harness/phase2_hex_schmitt_180_check.json (46 IT(180) rows reproduced read-only).
Outputs: RECONCILIATION.md (v1 text preserved + v2 section), reconciliation_cubic.csv,
reconciliation_tetragonal.csv, reconciliation_hexagonal.csv, reconciliation_summary.json.
"""

import ast
import csv
import gzip
import json
import os
import re
import sys
from collections import Counter, OrderedDict, defaultdict
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
HARNESS = os.path.join(ROOT, "harness")
CATALOG = os.path.join(HERE, "catalog.json")
TRIAGE1 = os.path.join(HARNESS, "triage_phase1.py")
TET_TABLES = os.path.join(HARNESS, "schmitt_tetragonal_tables.json")
HEX_TABLES = os.path.join(HARNESS, "schmitt_hexagonal_tables.json")
HEX180 = os.path.join(HARNESS, "phase2_hex_schmitt_180_check.json")
SG_PATH = os.path.join(HARNESS, "spacegroups.json")
RECON_MD = os.path.join(HERE, "RECONCILIATION.md")

SNAPSHOT = "2026-09-04"
V2_MARK = "## v2 (2026-09-04): hexagonal family (IT 143-194)"
V3_MARK = "## v3 (2026-09-04): computed open/wall verdicts x type-level Schmitt status"
V4_MARK = "## v4 (2026-09-04): tetragonal store-side status folded in (both phase-2 families under one rule)"
V5_MARK = "## v5 (2026-09-04): the 62 unstored tetragonal rows recomputed; the 106 UNRESOLVED settled (no tetragonal UNRESOLVED left)"
OW_VERDICTS = ("OPEN", "WALL", "ONE-SIDED", "not-computed")
TS_VALUES = ("SURVIVOR", "COLLISION", "UNRESOLVED", "printed-only", "not-screened")
FAMILIES = ("cubic", "tetragonal", "hexagonal")
CUBIC = list(range(195, 231))
TETRA = list(range(75, 143))
HEXA = list(range(143, 195))


def load_cubic_tables():
    src = open(TRIAGE1).read()
    for node in ast.parse(src).body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "SCHMITT_FVECTORS" for t in node.targets):
            fv = ast.literal_eval(node.value)
            break
    else:
        sys.exit("SCHMITT_FVECTORS not found")
    assert "SCHMITT_FVECTORS[213] = SCHMITT_FVECTORS[212]" in src
    fv[213] = fv[212]
    rows = {g: [dict(f=tuple(r), b=None, pt=None, block=("212_213" if g in (212, 213) else str(g))) for r in v] for g, v in fv.items()}
    return rows


def load_block_tables(path):
    d = json.load(open(path))
    rows = {}
    for key, blk in d.items():
        if key == "_meta":
            continue
        for g in blk["groups"]:
            rows[g] = [dict(f=tuple(r["f"]), b=r["b"], pt=tuple(r["pt"]), block=key, pdf_page=r.get("pdf_page")) for r in blk["rows"]]
    return rows


def fstr(f):
    return f"({f[0]},{f[1]},{f[2]})"


def reconcile(system, groups, his_rows, types, sg, readonly_rows=None):
    """Return per-group records and (group,f)-level rows.
    readonly_rows: {(group, b, pt): stored_id} for printed rows reproduced only by a
    read-only re-run whose cell IS in the store (v2: the 46 IT(180) rows)."""
    readonly_rows = readonly_rows or {}
    # our sightings per group
    ours_menu = defaultdict(lambda: defaultdict(set))   # g -> f -> {type_id}
    ours_p2 = defaultdict(lambda: defaultdict(set))
    ours_menu_b = defaultdict(lambda: defaultdict(set))  # g -> f -> {b}
    for t in types:
        f = tuple(t["f_vector"])
        for s in t["sightings"]:
            if s["system"] != system:
                continue
            g = s["group"]
            if s["kind"] == "schmitt_printed":
                ours_p2[g][f].add(t["type_id"])
            else:
                ours_menu[g][f].add(t["type_id"])
                if s.get("c_over_a"):
                    ours_menu_b[g][f].add(Fraction(s["c_over_a"]))
    per_group = []
    flat = []
    tot = Counter()
    metric = system in ("tetragonal", "hexagonal")
    for g in groups:
        his = his_rows.get(g, [])
        his_f = {}
        for r in his:
            his_f.setdefault(r["f"], []).append(r)
        our_f = set(ours_menu[g])
        a = sorted(our_f & set(his_f))
        b = sorted(our_f - set(his_f))
        c = sorted(set(his_f) - our_f)
        # (c) split: his rows reproduced by P2 at his own point (type stored) vs read-only
        # reproduction with the cell already stored (v2, IT(180)) vs not stored at all
        c_p2 = [f for f in c if f in ours_p2[g]]
        c_ro = [f for f in c if f not in ours_p2[g] and any((g, r["b"], r["pt"]) in readonly_rows for r in his_f[f])]
        c_none = [f for f in c if f not in ours_p2[g] and f not in c_ro]
        n_types_a = sum(len(ours_menu[g][f]) for f in a)
        n_types_b = sum(len(ours_menu[g][f]) for f in b)
        n_rows_c = sum(len(his_f[f]) for f in c)
        # same-c/a matches (metric families only)
        a_same_b = 0
        if metric:
            for f in a:
                his_bs = {Fraction(r["b"]) for r in his_f[f]}
                if his_bs & ours_menu_b[g][f]:
                    a_same_b += 1
        rec = OrderedDict([
            ("group", g), ("symbol", sg[g]["international_short"]),
            ("his_rows", len(his)), ("his_distinct_f", len(his_f)),
            ("our_menu_types", len({tid for f in our_f for tid in ours_menu[g][f]})),
            ("our_menu_distinct_f", len(our_f)),
            ("a_fvec_matched", len(a)), ("a_our_types_at_matched_f", n_types_a),
            ("a_matched_at_same_c_over_a", a_same_b if metric else None),
            ("b_our_f_absent_from_his_table", len(b)), ("b_our_types_at_absent_f", n_types_b),
            ("c_his_f_not_reached_by_our_menu", len(c)), ("c_his_rows_not_reached", n_rows_c),
            ("c_of_which_reproduced_by_P2_at_his_point", len(c_p2)),
            ("c_of_which_reproduced_read_only_cell_stored", len(c_ro) if system == "hexagonal" else None),
            ("c_of_which_no_stored_type_at_all", len(c_none)),
            ("his_f_coverage_by_our_menu", (f"{len(a)}/{len(his_f)}" if his_f else "n/a")),
        ])
        per_group.append(rec)
        for k in ("his_rows", "his_distinct_f", "a_fvec_matched", "a_our_types_at_matched_f", "b_our_f_absent_from_his_table",
                  "b_our_types_at_absent_f", "c_his_f_not_reached_by_our_menu", "c_his_rows_not_reached",
                  "c_of_which_reproduced_by_P2_at_his_point", "c_of_which_no_stored_type_at_all"):
            tot[k] += rec[k]
        if metric:
            tot["a_matched_at_same_c_over_a"] += a_same_b
        if system == "hexagonal":
            tot["c_of_which_reproduced_read_only_cell_stored"] += len(c_ro)
        for f in sorted(set(his_f) | our_f):
            status = ("a_ours_in_his" if f in a else ("b_ours_not_his" if f in b else
                      ("c_his_not_ours_P2_reproduced" if f in c_p2 else
                       ("c_his_not_ours_readonly_reproduced_cell_stored" if f in c_ro else "c_his_not_ours_not_stored"))))
            rec_flat = OrderedDict([
                ("system", system), ("group", g), ("symbol", sg[g]["international_short"]),
                ("f_vector", fstr(f)), ("status", status),
                ("our_menu_type_ids", ";".join(sorted(ours_menu[g][f]))),
                ("our_P2_type_ids", ";".join(sorted(ours_p2[g][f]))),
                ("our_menu_c_over_a", ";".join(str(x) for x in sorted(ours_menu_b[g][f]))),
                ("his_row_count", len(his_f.get(f, []))),
                ("his_b_ratios", ";".join(r["b"] for r in his_f.get(f, []) if r["b"])),
                ("his_points", ";".join("(" + ",".join(r["pt"]) + ")" for r in his_f.get(f, []) if r["pt"])),
                ("his_block", his_f[f][0]["block"] if f in his_f else ""),
            ])
            if system == "hexagonal":
                rec_flat["readonly_180_stored_ids"] = ";".join(sorted({readonly_rows[(g, r["b"], r["pt"])] for r in his_f.get(f, []) if (g, r["b"], r["pt"]) in readonly_rows}))
            flat.append(rec_flat)
    return per_group, flat, tot


def parse_v1_headline(v1_text, system_heading):
    """Pull the bold headline numbers of a preserved v1 section: his pairs, (a), (b), (c)."""
    sec = v1_text.split(f"## {system_heading} (")[1].split("\n## ")[0]
    his = int(re.search(r"his distinct \(group, f\) pairs: \*\*(\d+)\*\*", sec).group(1))
    a = int(re.search(r"\(a\) ours-in-his: \*\*(\d+)\*\*", sec).group(1))
    b = int(re.search(r"\(b\) ours-not-his: \*\*(\d+)\*\*", sec).group(1))
    c = int(re.search(r"\(c\) his-not-ours: \*\*(\d+)\*\*", sec).group(1))
    return dict(his_distinct_f=his, a_fvec_matched=a, b_our_f_absent_from_his_table=b, c_his_f_not_reached_by_our_menu=c)


def main():
    cat = json.load(open(CATALOG))
    assert cat.get("catalog_version") == 5, "reconcile v5 needs catalog.json v5 (v4 script = git show 27e0083:...)"
    types = cat["types"]
    sightings = json.load(gzip.open(os.path.join(HERE, "catalog_sightings.json.gz"), "rt"))
    assert list(sightings) == [t["type_id"] for t in types]
    for t in types:
        t["sightings"] = sightings[t["type_id"]]
    sg = {g["number"]: g for g in json.load(open(SG_PATH))["groups"]}
    cubic_rows = load_cubic_tables()
    tet_rows = load_block_tables(TET_TABLES)
    hex_rows = load_block_tables(HEX_TABLES)
    n_cubic_rows = sum(len(v) for g, v in cubic_rows.items() if g != 213)
    n_tet_rows = sum(len(v) for k, v in {r[0]["block"]: r for r in tet_rows.values()}.items())
    n_hex_rows = sum(len(v) for k, v in {r[0]["block"]: r for r in hex_rows.values()}.items())
    assert n_cubic_rows == 881, n_cubic_rows
    assert n_tet_rows == 1476, n_tet_rows
    assert n_hex_rows == 958, n_hex_rows
    assert len({r[0]["block"] for r in hex_rows.values()}) == 45 and sorted(hex_rows) == HEXA
    # Euler on every printed row
    for rows in (cubic_rows, tet_rows, hex_rows):
        for g, v in rows.items():
            for r in v:
                assert r["f"][0] - r["f"][1] + r["f"][2] == 2, (g, r)
    # the 46 IT(180) rows reproduced read-only (z -> -z then H1), cells already stored
    h180 = json.load(open(HEX180))
    assert h180["unchanged"] is True and len(h180["rows"]) == 46
    readonly180 = {(180, r["b"], tuple(r["pt_Bpp"])): r["store_hit"] for r in h180["rows"] if r["reproduced"] and r["store_hit"]}
    assert len(readonly180) == 46
    assert all(any(r["b"] == b and r["pt"] == pt for r in hex_rows[180]) for (_, b, pt) in readonly180), "180 read-only rows not all in the 180/181 table"

    # --- the preserved v1 text (append-only) ---------------------------------
    existing = open(RECON_MD).read()
    preserved = existing.split("\n" + V5_MARK)[0]      # v1 text + v2 + v3 + v4 sections, byte for byte
    assert ("\n" + V3_MARK) in preserved and ("\n" + V4_MARK) in preserved, "v3 / v4 section missing from RECONCILIATION.md"
    preserved_v12 = preserved.split("\n" + V3_MARK)[0]  # v1 text + v2 section (regenerated below and asserted equal)
    v1_text = existing.split("\n" + V2_MARK)[0]
    if not v1_text.endswith("\n"):
        v1_text += "\n"
    assert "## Cubic (36 groups; his rows 881)" in v1_text and "## Tetragonal (68 groups; his rows 1476)" in v1_text, "v1 sections missing from RECONCILIATION.md"

    results = {}
    for system, groups, his, ro in (("cubic", CUBIC, cubic_rows, None), ("tetragonal", TETRA, tet_rows, None), ("hexagonal", HEXA, hex_rows, readonly180)):
        per_group, flat, tot = reconcile(system, groups, his, types, sg, ro)
        results[system] = dict(per_group=per_group, flat=flat, tot=tot)
        with open(os.path.join(HERE, f"reconciliation_{system}.csv"), "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(flat[0].keys()))
            w.writeheader()
            for r in flat:
                w.writerow(r)
    # v2 catalog reproduces the v1 cubic / tetragonal headline numbers exactly
    for system, heading in (("cubic", "Cubic"), ("tetragonal", "Tetragonal")):
        want = parse_v1_headline(v1_text, heading)
        got = {k: results[system]["tot"][k] for k in want}
        assert got == want, (system, got, want)

    # distinct f-vector level (whole system)
    def system_fsets(system, his):
        his_f = {r["f"] for g, v in his.items() for r in v}
        our_f = {tuple(t["f_vector"]) for t in types if any(s["system"] == system and s["kind"] != "schmitt_printed" for s in t["sightings"])}
        our_f_any = {tuple(t["f_vector"]) for t in types if any(s["system"] == system for s in t["sightings"])}
        return his_f, our_f, our_f_any
    sys_level = {}
    for system, his in (("cubic", cubic_rows), ("tetragonal", tet_rows), ("hexagonal", hex_rows)):
        his_f, our_f, our_f_any = system_fsets(system, his)
        if system == "hexagonal":
            by_id = {t["type_id"]: t for t in types}
            our_f_any = our_f_any | {tuple(by_id[i]["f_vector"]) for i in readonly180.values()}
        sys_level[system] = OrderedDict([
            ("his_distinct_fvectors_whole_system", len(his_f)),
            ("our_menu_distinct_fvectors_whole_system", len(our_f)),
            ("shared", len(his_f & our_f)),
            ("ours_menu_not_in_any_of_his_tables_for_the_system", sorted(fstr(f) for f in our_f - his_f)),
            ("his_not_reached_by_our_menu_anywhere_in_the_system", len(his_f - our_f)),
            ("his_not_reached_even_counting_P2", len(his_f - our_f_any)),
        ])
    # the hexagonal family: the same f-vector set is also compared with the OTHER two families
    hex_his_f = {r["f"] for v in hex_rows.values() for r in v}
    cub_his_f = {r["f"] for g, v in cubic_rows.items() if g != 213 for r in v}
    tet_his_f = {r["f"] for v in tet_rows.values() for r in v}
    hex_first_f = {tuple(t["f_vector"]) for t in types if t["first_sighting_system"] == "hexagonal"}
    hex_first_menu_f = {tuple(t["f_vector"]) for t in types if t["first_sighting_system"] == "hexagonal" and not t["schmitt_printed_only_hexagonal"]}
    cross = OrderedDict([
        ("his_hexagonal_family_distinct_f", len(hex_his_f)),
        ("of_which_also_printed_in_his_cubic_tables", len(hex_his_f & cub_his_f)),
        ("of_which_also_printed_in_his_tetragonal_tables", len(hex_his_f & tet_his_f)),
        ("of_which_printed_in_no_cubic_or_tetragonal_table", len(hex_his_f - cub_his_f - tet_his_f)),
        ("our_hexagonal_first_distinct_f", len(hex_first_f)),
        ("our_hexagonal_first_menu_distinct_f", len(hex_first_menu_f)),
        ("our_hexagonal_first_menu_f_printed_in_no_table_of_any_family", sorted(fstr(f) for f in hex_first_menu_f - hex_his_f - cub_his_f - tet_his_f)),
        ("our_hexagonal_first_menu_f_printed_in_no_hexagonal_family_table", sorted(fstr(f) for f in hex_first_menu_f - hex_his_f)),
    ])

    # finalists + named cells + the top-10 hexagonal survivors: cross-family scan
    finalists = ["8cf50403cf88c455", "2de0a21129cabe90", "c4ea3f32fdd6dc51", "f98a3ee5675fc121",
                 "ceb70631e274e727", "359beee832567a71", "aa6b0077c3234d24"]
    by_id = {t["type_id"]: t for t in types}
    fin_rows = []
    for tid in finalists:
        t = by_id[tid]
        f = tuple(t["f_vector"])
        hex_hits = [(g, r["b"], "(" + ",".join(r["pt"]) + ")", r.get("pdf_page")) for g, v in hex_rows.items() for r in v if r["f"] == f]
        stored = []
        for g, b, pt, page in hex_hits:
            ids = {tt["type_id"] for tt in types for s in tt["sightings"] if s["system"] == "hexagonal" and s["group"] == g and s["kind"] == "schmitt_printed" and tuple(tt["f_vector"]) == f}
            stored.append((g, sorted(ids)))
        fin_rows.append(OrderedDict([("type_id", tid), ("name", t["name"]), ("group", t["witness_group"]), ("f", fstr(f)),
                                     ("own_group_table", "present" if t["witness_group"] in t["schmitt_fvector_present_in_sighted_groups"] else "ABSENT"),
                                     ("printed_in_hexagonal_groups", hex_hits),
                                     ("hexagonal_rows_with_stored_P2_cell", stored),
                                     ("type_level", t["schmitt_type_level_status"])]))
    def survivor_rank(t):
        m = re.search(r"survivor rank (\d+) of 151", t["schmitt_match_hexagonal"])
        return int(m.group(1)) if m else None
    top_hex = [t for t in types if t["first_sighting_system"] == "hexagonal" and survivor_rank(t) is not None]
    assert len(top_hex) == 151 and sorted(survivor_rank(t) for t in top_hex) == list(range(1, 152))
    top_hex = sorted(top_hex, key=survivor_rank)[:10]
    top_rows = []
    for t in top_hex:
        f = tuple(t["f_vector"])
        own = t["witness_group"]
        top_rows.append(OrderedDict([
            ("type_id", t["type_id"]), ("rank", survivor_rank(t)),
            ("group", own), ("symbol", sg[own]["international_short"]), ("c_over_a", t["witness_c_over_a"]), ("f", fstr(f)), ("aut", t["aut_order"]),
            ("own_group_table", "present" if own in t["schmitt_fvector_present_in_sighted_groups"] else "ABSENT"),
            ("other_hex_groups_printing_f", [g for g in t["schmitt_fvector_printed_anywhere_hexagonal"] if g != own]),
            ("cubic_groups_printing_f", t["schmitt_fvector_printed_anywhere_cubic"]),
            ("tetragonal_groups_printing_f", t["schmitt_fvector_printed_anywhere_tetragonal"]),
            ("g4", t["g4_status"]), ("chiral_solid", t["g4_chiral_solid"]),
            ("type_level", t["schmitt_type_level_status"]),
        ]))

    summary = OrderedDict([
        ("snapshot", SNAPSHOT),
        ("version", 2),
        ("printed_rows", {"cubic": n_cubic_rows, "tetragonal": n_tet_rows, "hexagonal": n_hex_rows}),
        ("totals", {s: dict(results[s]["tot"]) for s in results}),
        ("system_level", sys_level),
        ("hexagonal_cross_family_fvectors", cross),
        ("finalists_hexagonal_scan", fin_rows),
        ("top10_hexagonal_survivors", top_rows),
    ])
    # v3 blocks (copied from the v3 catalog summary; recounted independently by verify_counts_independent.py)
    S3 = cat["summary"]
    summary["v5_open_wall_verdict_counts"] = S3["open_wall_verdict_counts"]
    summary["v5_schmitt_type_status_counts"] = S3["schmitt_type_status_counts"]
    summary["v5_open_wall_x_schmitt_type_status"] = S3["open_wall_x_schmitt_type_status"]
    summary["v5_naming_pool"] = S3["naming_pool"]
    summary["v5_schmitt_type_status_tetragonal_storeside"] = S3["schmitt_type_status_tetragonal_storeside"]
    summary["v5_schmitt_type_status_tetragonal_unresolved_recomputed"] = S3["schmitt_type_status_tetragonal_unresolved_recomputed"]
    json.dump(summary, open(os.path.join(HERE, "reconciliation_summary.json"), "w"), indent=1, default=str)

    # ---------------- RECONCILIATION.md: v1 text preserved + v2 section ----------------
    L = []
    L.append(V2_MARK + "\n")
    L.append(f"Appended by `catalog/reconcile_schmitt.py` v2 from `catalog/catalog.json` v2 (1,583 types; snapshot {SNAPSHOT}); deterministic. "
             "Everything above this heading is the v1 text (cubic + tetragonal), preserved verbatim; v2 recomputed both from the v2 catalog and asserted the four headline numbers of each equal (his pairs / (a) / (b) / (c)). "
             "Trigonal + hexagonal tables: `harness/schmitt_hexagonal_tables.json` (958 rows in 45 printed blocks, Sec. 2.2.3-2.2.4, PDF pp. 86-123; text layer primary, 153 rows visually cross-read, NOT independently re-keyed - G5 duty owed, agent #147 in progress). "
             "Every printed row passed Euler V-E+F=2 here. The wording rule of the v1 preamble binds every line below: an f-vector match is NOT type identity; absence is evidence, not proof; his survey is a grid sampling; (c) is a coverage gap of OUR sweep.\n")
    L.append("### Definitions specific to this family\n")
    L.append("- **Shared tables**: seven enantiomorphic pairs print ONE table each (144/145, 151/153, 152/154, 169/170, 171/172, 178/179, 180/181); both members get the printed set here, our sightings are per group. "
             "For 180/181 Schmitt's normalizer remark ('only the normalizer for IT(181) but not for IT(180)') means the printed points belong to IT(181): pass P2 reproduced all 69 rows in IT(181) verbatim (conversion H1) and 23 of them in IT(180); the other 46 reproduce in IT(180) only under z -> -z then H1, established by the read-only re-run `harness/phase2_hex_schmitt_180_check.py` with every one of the 46 cells already in the store. "
             "Those 46 rows are reported as a third (c) sub-split, **'(c) read-only, cell stored'**, never as coverage.\n"
             "- **Our menu** (batch 2) = passes P1 (grid x 13 coarse c/a), P3 (5 printed b-ratios x grid: 3497/1000, 797/1000, 4/5, 527/1000, 7/8), P4 (1/24 line orbits), P5 (c/a bisection); pass P2 = his printed points (converted from his B'' basis by x' = 2x'', y' = x''+y'', z' = z''; second enantiomorphs verbatim then z -> -z).\n"
             "- **b-ratio** = ||b3'||/||b1'|| = c/a in the ITA hexagonal basis; '(a) same c/a' counts matched (group, f) pairs where at least one of his printed b-ratios for that f equals one our menu sampled.\n")
    tot = results["hexagonal"]["tot"]
    pg = results["hexagonal"]["per_group"]
    sl = sys_level["hexagonal"]
    L.append(f"### Hexagonal family ({len(pg)} groups; his rows {n_hex_rows})\n")
    L.append("Headline (sums over groups; a (group, f-vector) pair counts once per group):\n")
    L.append(f"- his distinct (group, f) pairs: **{tot['his_distinct_f']}** ({tot['his_rows']} (group, row) pairs from {n_hex_rows} printed rows; a shared table is counted once per group it serves)")
    L.append(f"- (a) ours-in-his: **{tot['a_fvec_matched']}** (group, f) pairs, carrying **{tot['a_our_types_at_matched_f']}** of our (type, group) sightings-by-menu; of these {tot['a_matched_at_same_c_over_a']} pairs match at a c/a value we also sampled")
    L.append(f"- (b) ours-not-his: **{tot['b_our_f_absent_from_his_table']}** (group, f) pairs, carrying **{tot['b_our_types_at_absent_f']}** of our (type, group) menu sightings")
    L.append(f"- (c) his-not-ours: **{tot['c_his_f_not_reached_by_our_menu']}** (group, f) pairs = {tot['c_his_rows_not_reached']} printed rows our menu never reached in that group "
             f"(coverage gap of our sweep); of these {tot['c_of_which_reproduced_by_P2_at_his_point']} have his cell stored via P2 at his own point, {tot['c_of_which_reproduced_read_only_cell_stored']} are IT(180) rows reproduced read-only with the cell already stored, and {tot['c_of_which_no_stored_type_at_all']} have no stored type at all")
    L.append(f"- whole-family distinct f-vectors: his {sl['his_distinct_fvectors_whole_system']}, our menu {sl['our_menu_distinct_fvectors_whole_system']}, shared {sl['shared']}; "
             f"ours not printed in ANY trigonal/hexagonal table: {len(sl['ours_menu_not_in_any_of_his_tables_for_the_system'])} "
             f"({', '.join(sl['ours_menu_not_in_any_of_his_tables_for_the_system']) or 'none'}); his f-vectors unreached by our menu anywhere in the family: {sl['his_not_reached_by_our_menu_anywhere_in_the_system']} (even counting P2 and the read-only 180 rows: {sl['his_not_reached_even_counting_P2']})")
    L.append(f"- across families: of his {cross['his_hexagonal_family_distinct_f']} trigonal/hexagonal f-vectors, {cross['of_which_also_printed_in_his_cubic_tables']} are also printed in a cubic table and {cross['of_which_also_printed_in_his_tetragonal_tables']} in a tetragonal table; {cross['of_which_printed_in_no_cubic_or_tetragonal_table']} appear in this family only. "
             f"Our {cross['our_hexagonal_first_distinct_f']} hexagonal-first f-vectors ({cross['our_hexagonal_first_menu_distinct_f']} from our menu): menu f-vectors printed in no table of any family: {len(cross['our_hexagonal_first_menu_f_printed_in_no_table_of_any_family'])} "
             f"({', '.join(cross['our_hexagonal_first_menu_f_printed_in_no_table_of_any_family']) or 'none'}); printed in no trigonal/hexagonal table: {len(cross['our_hexagonal_first_menu_f_printed_in_no_hexagonal_family_table'])} ({', '.join(cross['our_hexagonal_first_menu_f_printed_in_no_hexagonal_family_table']) or 'none'}).\n")
    L.append("Per group (full (group, f)-level table in `reconciliation_hexagonal.csv`):\n")
    cols = ["group", "symbol", "his_rows", "his_distinct_f", "our_menu_types", "our_menu_distinct_f", "a_fvec_matched", "a_our_types_at_matched_f", "a_matched_at_same_c_over_a",
            "b_our_f_absent_from_his_table", "b_our_types_at_absent_f", "c_his_f_not_reached_by_our_menu", "c_of_which_reproduced_by_P2_at_his_point",
            "c_of_which_reproduced_read_only_cell_stored", "c_of_which_no_stored_type_at_all", "his_f_coverage_by_our_menu"]
    short = {"group": "IT", "symbol": "symbol", "his_rows": "his rows", "his_distinct_f": "his f", "our_menu_types": "our types (menu)", "our_menu_distinct_f": "our f (menu)",
             "a_fvec_matched": "(a) f matched", "a_our_types_at_matched_f": "(a) our types", "a_matched_at_same_c_over_a": "(a) same c/a",
             "b_our_f_absent_from_his_table": "(b) our f absent", "b_our_types_at_absent_f": "(b) our types", "c_his_f_not_reached_by_our_menu": "(c) his f unreached",
             "c_of_which_reproduced_by_P2_at_his_point": "(c) stored via P2", "c_of_which_reproduced_read_only_cell_stored": "(c) read-only, cell stored",
             "c_of_which_no_stored_type_at_all": "(c) not stored", "his_f_coverage_by_our_menu": "coverage a/his"}
    L.append("| " + " | ".join(short[c] for c in cols) + " |")
    L.append("|" + "---|" * len(cols))
    for r in pg:
        L.append("| " + " | ".join(str(r[c]) for c in cols) + " |")
    L.append("")
    L.append("### The seven cubic finalists and the two named cells: trigonal/hexagonal f-vector scan\n")
    L.append("Same purpose as the v1 cross-system table (own-group absence is the paper's criterion; a same-f-vector row elsewhere says nothing about type identity until the exact code is compared). The type-level column is the v2 catalog's, which now also carries the hexagonal dedupe inference.\n")
    L.append("| type | name | IT | f | own-group table | trigonal/hexagonal rows printing f (IT, c/a, point as printed in B'', PDF p.) | his cell stored (P2)? | type-level status (v2) |")
    L.append("|---|---|---|---|---|---|---|---|")
    for r in fin_rows:
        hx = "; ".join(f"IT{g} b={b} {pt} p.{pg_}" for g, b, pt, pg_ in r["printed_in_hexagonal_groups"]) or "none"
        st = "; ".join(f"IT{g}: {', '.join(ids) if ids else 'NOT stored'}" for g, ids in r["hexagonal_rows_with_stored_P2_cell"]) or "n/a"
        L.append(f"| `{r['type_id']}` | {r['name']} | {r['group']} | {r['f']} | {r['own_group_table']} | {hx} | {st} | {r['type_level']} |")
    L.append("")
    L.append("### The top-10 hexagonal-family collision-screen survivors (all G4-certified 2026-09-04)\n")
    L.append("Rank = survivor rank among the 151 (triage_phase2_hex_shortlist.json survivors_ranked = the # column of G4_PHASE2_HEX_RESULTS.md); all ten were re-confirmed DIFFERENT by exact recomputation at every printed row of their (group, f) (COLLISION_PHASE2_HEX_RESULTS.md, 26 pairs). "
             "Own-group table = whether his table for the first-witness group prints the f-vector at all. No name is proposed for any of them.\n")
    L.append("| rank | type | IT | c/a | f | aut | own-group table | other trigonal/hexagonal groups printing f | cubic groups printing f | tetragonal groups printing f | G4 | solid chiral | type-level status |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in top_rows:
        L.append(f"| {r['rank']} | `{r['type_id']}` | {r['group']} {r['symbol']} | {r['c_over_a']} | {r['f']} | {r['aut']} | {r['own_group_table']} | {', '.join(str(g) for g in r['other_hex_groups_printing_f']) or 'none'} | "
                 f"{', '.join(str(g) for g in r['cubic_groups_printing_f']) or 'none'} | {', '.join(str(g) for g in r['tetragonal_groups_printing_f']) or 'none'} | {r['g4']} | {r['chiral_solid']} | {r['type_level']} |")
    L.append("")
    L.append("### Limits (v2)\n")
    L.append("- f-vector level only; type-level facts live in the catalog's `schmitt_type_level_*` and `schmitt_match_hexagonal` columns (store-side screen of all 288 menu-sighted hexagonal-first types: 151 SURVIVOR / 124 COLLISION / 13 UNRESOLVED; the 13 are unresolved only at IT(180) rows, and the read-only re-run finds all 13 DIFFERENT there - recorded, store verdict stands).\n"
             "- The trigonal/hexagonal digitization is single-pass (text layer + 153-row visual cross-read), not an independent re-key; every row was, however, run through the exact chain by pass P2 (1,230 verbatim + 46 read-only = 1,276/1,276 reproduce their printed f-vector).\n"
             "- Our batch-2 menu sampled 13 coarse c/a values plus 5 of his 38 printed b-ratios (9 of 38 reached in total); (c) on this side is dominated by metric under-sampling, as in the tetragonal batch.\n"
             "- The 43 prior (cubic-/tetragonal-first) types re-sighted in this family were NOT collision-screened here; their hexagonal status is f-vector level only.\n"
             "- No frequency column is printed in these tables.\n")
    v12_text = v1_text + "\n" + "\n".join(L) + "\n"
    assert v12_text == preserved_v12, "the v1 + v2 text regenerated from the v5 catalog differs from the preserved text on disk (append-only violated)"

    # ---------------- v5 section: open/wall verdict x type-level Schmitt status, tetragonal UNRESOLVED settled ----------------
    by_id = {t["type_id"]: t for t in types}
    xt = S3["open_wall_x_schmitt_type_status"]
    pool = S3["naming_pool"]
    assert pool["tetragonal"]["n_certified_open_unnamed"] == 13 and pool["hexagonal"]["n_certified_open_unnamed"] == 102
    V = []
    SS = S3["schmitt_type_status_tetragonal_storeside"]
    RC = S3["schmitt_type_status_tetragonal_unresolved_recomputed"]
    assert dict(RC["counts_404_after_v5"]) == {k: S3["schmitt_type_status_counts"]["tetragonal"][k] for k in ("COLLISION", "SURVIVOR", "UNRESOLVED")}
    assert RC["still_unresolved"] == [] and dict(RC["row_status_counts"]) == {"REPRODUCED": 62}
    V.append(V5_MARK + "\n")
    V.append(f"Appended by `catalog/reconcile_schmitt.py` v5 from `catalog/catalog.json` v5 (1,583 types; snapshot {SNAPSHOT}); deterministic. "
             "Everything above this heading is the v1 text + the v2, v3 and v4 sections, preserved byte for byte (asserted for v1 + v2 by regeneration from the v5 catalog; the v3 and v4 sections are the pre-recomputation record and are kept verbatim: the v4 tetragonal column 'UNRESOLVED 106' is superseded below); v4 of this script = `git show 27e0083:paper_prep/MINT_plesiohedron/catalog/reconcile_schmitt.py`. "
             "Sources of the two columns cross-tabulated here: `harness/phase2/WALL_OPEN_PHASE2.json` (computed open/wall verdicts of the 165 G4-certified phase-2 cells at their stored first witness; agent #148; accepted 2026-09-04 14:10, JSON md5 6b257c551f6fb275dfabb03e992f57c2), "
             "`harness/round1_computations/c1_wall_open.json` (the 7 cubic finalists), `harness/COLLISION_PHASE2_RESULTS.md` (tetragonal top-15 shortlist, 27 printed pairs; ADDENDUM 2026-09-04 #152 = the store-side rule over all 404 menu-sighted tetragonal types, `collision_phase2_tetragonal_storeside.json`; ADDENDUM 2026-09-04 #154 = the 62 unstored printed rows behind the 106 UNRESOLVED recomputed at the printed points with the documented setting conversions, "
             f"`collision_phase2_tetragonal_rows_recomputed.json` md5 {RC['rows_json_md5']} + `collision_phase2_tetragonal_unresolved_overlay.json` md5 {RC['overlay_json_md5']}) and `harness/COLLISION_PHASE2_HEX_RESULTS.md` (store-side screen of the 288 menu-sighted hexagonal-first types; top-10 recomputed at the printed points). "
             "Wording, stated once: OPEN = the type holds on the tested neighbourhood of its first witness at finite steps (point 1/1536, metric 1/3072 relative), never an interval proof; WALL = the witness sits on a transition (both sides of some direction change); ONE-SIDED = some side changes but no direction on both sides (a short neighbourhood, not a wall); "
             "SURVIVOR = not matched at the printed representatives checked (records checked as of 2026-09-04), never novelty; COLLISION = the type reproduces one of his printed cells (first-realization reframe); printed-only = an S-cell never reached by our menu; not-screened = outside both phase-2 screens (all cubic-first types by construction; no tetragonal-first type). "
             "A wall cell is excluded from the naming pool because its witness sits on a transition; nothing here proposes a name.\n")
    V.append("### Cross-tab per family: open_wall_verdict (rows) x schmitt_type_status (columns)\n")
    for fam in FAMILIES:
        n_fam = sum(1 for t in types if t["first_sighting_family"] == fam)
        vc = S3["open_wall_verdict_counts"][fam]
        sc = S3["schmitt_type_status_counts"][fam]
        V.append(f"**{fam}-first** ({n_fam} types; verdicts " + ", ".join(f"{v} {vc[v]}" for v in OW_VERDICTS) + "; statuses " + ", ".join(f"{s} {sc[s]}" for s in TS_VALUES) + "):\n")
        V.append("| verdict \\ status | " + " | ".join(TS_VALUES) + " | total |")
        V.append("|" + "---|" * (len(TS_VALUES) + 2))
        for v in OW_VERDICTS:
            row = xt[fam][v]
            V.append(f"| {v} | " + " | ".join(str(row[s]) for s in TS_VALUES) + f" | {sum(row[s] for s in TS_VALUES)} |")
        V.append("| total | " + " | ".join(str(sum(xt[fam][v][s] for v in OW_VERDICTS)) for s in TS_VALUES) + f" | {n_fam} |")
        V.append("")
    V.append("### Tetragonal type-level status, v4 -> v5 (the 62 unstored printed rows behind the 106 UNRESOLVED recomputed)\n")
    V.append(f"Source: {RC['source']}; overlay JSON md5 {RC['overlay_json_md5']}, rows JSON md5 {RC['rows_json_md5']}. Rule (stated once): {RC['rule']} "
             f"Rows: {RC['n_rows_recomputed']} recomputed ({RC['n_cells_computed']} cells: every documented convention of the group plus the other origin / enantiomorph reading, recorded), status counts {dict(RC['row_status_counts'])}; "
             f"documented conventions agree on the code in {RC['rows_with_documented_conventions_agreeing']}/62 rows; the other reading reproduces the printed f in {RC['rows_where_the_other_origin_or_enantiomorph_reading_reproduces_f']}/62 (it is pass P2's quarantined run); "
             f"{RC['row_cells_not_stored_under_any_id']} row cells are stored under no id (types our menu never sampled; read-only, not added); row cells that are stored types outside the 106: {dict(RC['row_cells_that_are_stored_types_outside_the_106'])}.\n")
    V.append("| count | SURVIVOR | COLLISION | UNRESOLVED |")
    V.append("|---|---|---|---|")
    for lab, key in (("catalog v3 (top-15 recomputation only; not-screened = " + str(SS['counts_catalog_v3'].get('not-screened', 0)) + ")", "counts_catalog_v3"), ("pure store-side rule", "counts_pure_store_side_rule"), ("v4 = rule + recomputed shortlist pairs overlaid", "counts_with_recomputed_pairs_overlaid")):
        c = SS[key]
        V.append(f"| {lab} | {c.get('SURVIVOR', 0)} | {c.get('COLLISION', 0)} | {c.get('UNRESOLVED', 0)} |")
    c = RC["counts_106"]
    V.append(f"| the 106 v4-UNRESOLVED after recomputation | {c.get('SURVIVOR', 0)} | {c.get('COLLISION', 0)} | {c.get('UNRESOLVED', 0)} |")
    c = RC["counts_404_after_v5"]
    V.append(f"| v5 = v4 + the 106 settled | {c.get('SURVIVOR', 0)} | {c.get('COLLISION', 0)} | {c.get('UNRESOLVED', 0)} |")
    V.append("")
    V.append("Transitions v4 -> v5 over the 404 menu-sighted tetragonal-first types: " + "; ".join(f"{k}: {n}" for k, n in RC["transitions_v4_to_v5"].items()) + f". Still UNRESOLVED: {len(RC['still_unresolved'])}. Secondary hits (a type's code equal to the cell of a row it does not hang on; no status effect): {len(RC['secondary_hits'])}. "
             "The 385 Schmitt-printed-only tetragonal types stay printed-only; the 102 cubic-first types stay not-screened (scope fact); the 15 shortlist statuses and the 14 certified survivors are untouched (none was UNRESOLVED).\n")
    if RC["surprises"]:
        V.append("Recorded facts from the recomputation (no status effect): " + " ".join(f"({i}) {s}" for i, s in enumerate(RC["surprises"], 1)) + "\n")
    V.append("### Naming pool = G4-certified AND open_wall_verdict OPEN AND unnamed, per family\n")
    cub_open_named = [t for t in types if t["first_sighting_family"] == "cubic" and t["g4_status"] != "none" and t["open_wall_verdict"] == "OPEN"]
    cub_nc = [t for t in types if t["first_sighting_family"] == "cubic" and t["g4_status"] != "none" and t["open_wall_verdict"] == "not-computed"]
    V.append(f"- cubic: **{pool['cubic']['n_certified_open_unnamed']}** of {pool['cubic']['n_certified']} accepted-cubic types: the {len(cub_open_named)} OPEN cells (c1) all carry a name or a marker already (" +
             "; ".join(f"`{t['type_id']}` {t['name']} [{t['name_status'].split(' (')[0]}]" for t in cub_open_named) +
             f"); the Satchelhedron is the cubic WALL cell; {len(cub_nc)} accepted-cubic types have no perturbation run on record (" + ", ".join(f"`{t['type_id']}`" for t in cub_nc) + ").")
    for fam in ("tetragonal", "hexagonal"):
        p = pool[fam]
        V.append(f"- {fam}: **{p['n_certified_open_unnamed']}** of {p['n_certified']} certified ({p['n_certified_open']} OPEN, {p['n_certified'] - p['n_certified_open']} WALL / ONE-SIDED, {p['n_certified_not_computed']} not computed); every member is a SURVIVOR of its family's screen and carries no name. Members (catalog id = type id): " +
                 ", ".join(f"{c} = `{t}`" for c, t in zip(p["catalog_ids"], p["type_ids"])) + ".")
    V.append(f"- Pool check: {pool['tetragonal']['n_certified_open_unnamed']} tetragonal + {pool['hexagonal']['n_certified_open_unnamed']} hexagonal-family = {pool['tetragonal']['n_certified_open_unnamed'] + pool['hexagonal']['n_certified_open_unnamed']}, "
             "equal to PROGRAM_LEDGER 2026-09-04 14:10 ('13 tetragonal + 102 hexagonal'); asserted in build_catalog.py and recounted from the raw verdict / screen / certificate files by verify_counts_independent.py. "
             "Pool membership is catalog-relative; G5 diligence (print-only Engel / Koch exposure) still applies before any name. The certified phase-2 cells outside the pool (WALL / ONE-SIDED) are tabulated in the v4 section above; nothing about them changed in v5.\n")
    V.append("### Limits (v5)\n")
    V.append("- Every verdict is for the stored FIRST witness of the type only (one point, one c/a); a type OPEN here may have other sightings on a wall, and a WALL witness does not preclude an open region of the same type elsewhere.\n"
             "- Finite steps: point 1/48, 1/96 halved to 1/1536; metric c/a(1 +- 1/96, 1/192) halved to 1/3072 (relative, so coarser than 1/96 absolute for the five cells with c/a > 2, stated in WALL_OPEN_PHASE2.md); OPEN is 'holds on the tested neighbourhood', ONE-SIDED is a short neighbourhood, neither is an interval proof.\n"
             f"- Tetragonal type-level status (v5): COLLISION {RC['counts_404_after_v5'].get('COLLISION', 0)} (the {SS['n_s_cells']} S-cells + the shortlist's cd4fb52572edcb73 + the {RC['counts_106'].get('COLLISION', 0)} v4-UNRESOLVED types whose recomputed hung-on row IS the type) / SURVIVOR {RC['counts_404_after_v5'].get('SURVIVOR', 0)} / UNRESOLVED {RC['counts_404_after_v5'].get('UNRESOLVED', 0)} of the 404 menu-sighted types. "
             "Every printed row at a menu-sighted type's (group, f) has now been reproduced by the exact chain (stored by pass P2, recomputed for the 27 shortlist pairs, or recomputed here for the 62 unstored rows), so SURVIVOR is type-level at every printed representative of the type's (group, f) pairs; it remains catalog-relative: his tables print ONE point per (group, f) from a grid sampling. The tetragonal digitization is a single visual pass, text-layer cross-checked, not re-keyed; the setting conversions are the machine-verified ones of PHASE2_SCHMITT_ORIGIN_CHECK.md (every printed row of each group reproduces under them; here 62/62 again).\n"
             "- Cubic-first types are not-screened by the two phase-2 screens by construction; their cubic-round verdicts (SCHMITT_COLLISION_RESULTS.md, CROSS_GROUP_RESULTS.md) stay in schmitt_type_level_*. Two of the 62 recomputed rows are cubic-store types (recorded above), a cross-system fact and not a status change.\n"
             "- No new digitization, perturbation or certificate was computed here; the section only cross-tabulates accepted and staged records (the #154 recomputation is provisional until the main-session re-run). Snapshot wording throughout.\n")
    with open(RECON_MD, "w") as fh:
        fh.write(preserved + "\n" + "\n".join(V) + "\n")
    print("RECONCILIATION.md (v1 + v2 + v3 + v4 text preserved byte for byte + v5 section) + CSVs written")
    for fam in FAMILIES:
        print(f"v5 cross-tab {fam}:", {v: {s: n for s, n in xt[fam][v].items() if n} for v in OW_VERDICTS})
    print("v5 naming pool:", {fam: pool[fam]["n_certified_open_unnamed"] for fam in FAMILIES})
    print("v5 tetragonal transitions v4 -> v5:", dict(RC["transitions_v4_to_v5"]))
    for system in ("cubic", "tetragonal", "hexagonal"):
        print(system, dict(results[system]["tot"]))
        print(" ", {k: v for k, v in sys_level[system].items() if k != "ours_menu_not_in_any_of_his_tables_for_the_system"}, "ours-not-in-any:", sys_level[system]["ours_menu_not_in_any_of_his_tables_for_the_system"])
    print("cross-family:", dict(cross))
    for r in fin_rows:
        print(r["type_id"], r["name"], r["f"], r["own_group_table"], "hex:", r["printed_in_hexagonal_groups"], r["hexagonal_rows_with_stored_P2_cell"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
