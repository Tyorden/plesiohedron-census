#!/usr/bin/env python3
"""collision_phase2_tetragonal_storeside.py — STORE-SIDE collision screen of ALL
404 menu-sighted tetragonal-first types under the hexagonal screen's rule
(2026-09-04, subagent #152, Claude Fable 5.1; consistency task, no new
mathematics; AI-drafted, main-session re-run required before acceptance).

WHY. collision_phase2_hex_check.py section 1 gave every menu-sighted
hexagonal-first type a schmitt_type_status (SURVIVOR / COLLISION / UNRESOLVED)
by a STORE-SIDE rule; the tetragonal screen (collision_phase2_check.py) only
recomputed the 27 printed pairs of the top-15 shortlist, so 389 menu-sighted
tetragonal types carried "not-screened" in catalog v3 although 176 of them are
S-cells (catalog/STATUS.md v3 finding 3). This script applies the SAME rule to
the tetragonal family so both families carry the same semantics.

THE RULE (re-implemented verbatim from collision_phase2_hex_check.py lines
115-139; the hexagonal script imports sweep_phase2_hexagonal, which needs the
venv's numpy, so the rule is re-implemented here as a pure function and its
equivalence is ASSERTED by running it on the hexagonal family first: it must
reproduce SURVIVOR 151 / COLLISION 124 / UNRESOLVED 13 and the per-type verdict
of every one of the 288 rows of TRIAGE_PHASE2_HEX_RESULT.md):
  per menu-sighted type T with f-vector f, sighted (any pass) in groups G(T):
    COLLISION  iff T has a P2 sighting at all (S-cell: T IS one of Schmitt's
               printed cells) OR some printed row (g, f) with g in G(T)
               reproduced in pass P2 as T itself (SAME);
    else UNRESOLVED iff some printed row (g, f), g in G(T), has NO stored P2
               cell (the row was quarantined / not stored), so no type-level
               statement is possible for that pair;
    else SURVIVOR (in every sighted group f is absent from the printed table,
               or every printed row with that (group, f) reproduced as a
               DIFFERENT stored type).
  Row <-> stored cell matching: hexagonal family exactly as the hexagonal
  script (group, printed_point_Bpp, b); tetragonal family exactly as
  triage_phase2.py (group, point mod 1, b) — the tetragonal store keeps the
  printed point verbatim in `point` (no printed_point_Bpp field) and the
  triage's frac_key reduces both sides mod 1.

OVERLAY (tetragonal only, recorded separately from the pure rule): the 27
printed pairs recomputed in collision_phase2_check.py resolve their rows —
a pair recomputed SAME TYPE makes its target COLLISION (the one known case,
cd4fb52572edcb73 at IT(134), an unstored two-origin row); a pair recomputed
DIFFERENT TYPE on an unstored row removes that row from the target's unresolved
set. Without the overlay the 14 certified survivors whose worklist had `unres`
rows would read UNRESOLVED under the pure rule; with it they read SURVIVOR, as
COLLISION_PHASE2_RESULTS.md states. Both verdicts are written per type.

Read-only: both stores are sha256-verified (phase2_types.json.gz decompressed
bytes == phase2_types.SHA256SUMS 71685b9a...; phase2_hexagonal_types.json.gz
decompressed == 7494c7b2...); nothing is added to any store.

LANGUAGE (G5, once): SURVIVOR is catalog-relative ("not matched against the
records checked as of 2026-09-04"), never novelty; Schmitt's tables print ONE
representative per (group, f-vector) from a grid sampling.

Run (plain python3, seconds, foreground):
  python3 <repo>/harness/collision_phase2_tetragonal_storeside.py
Writes: collision_phase2_tetragonal_storeside.json (sorted keys, deterministic;
md5 printed) and APPENDS a dated addendum to COLLISION_PHASE2_RESULTS.md once
(skipped if the addendum heading is already present).
Exit 0 iff the hexagonal equivalence assertion held, the 15 shortlist statuses
equal the doc's summary lines, and the stores were unchanged.
"""
import gzip
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter, OrderedDict, defaultdict
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
TET_GZ = os.path.join(HERE, "phase2_types.json.gz")
TET_RAW = os.path.join(HERE, "phase2_types.json")
TET_SUMS = os.path.join(HERE, "phase2_types.SHA256SUMS")
HEX_GZ = os.path.join(HERE, "phase2_hexagonal_types.json.gz")
HEX_SUMS = os.path.join(HERE, "phase2_hexagonal_types.SHA256SUMS")
TET_TABLES = os.path.join(HERE, "schmitt_tetragonal_tables.json")
HEX_TABLES = os.path.join(HERE, "schmitt_hexagonal_tables.json")
HEX_SHORTLIST = os.path.join(HERE, "triage_phase2_hex_shortlist.json")
HEX_TRIAGE_MD = os.path.join(HERE, "TRIAGE_PHASE2_HEX_RESULT.md")
HEX_COLL_JSON = os.path.join(HERE, "collision_phase2_hex_results.json")
TET_COLL_JSON = os.path.join(HERE, "collision_phase2_results.json")
TET_COLL_MD = os.path.join(HERE, "COLLISION_PHASE2_RESULTS.md")
OUT_JSON = os.path.join(HERE, "collision_phase2_tetragonal_storeside.json")

RUN_DATE = "2026-09-04"
SNAPSHOT = "2026-09-04"
MENU_PASSES = {"P1", "P3", "P4", "P5"}          # as collision_phase2_hex_check.py
TET_FIRST = "tetragonal (phase 2)"
HEX_FIRST = "hexagonal (phase 2 batch 2)"
HEX_EXPECTED = {"SURVIVOR": 151, "COLLISION": 124, "UNRESOLVED": 13}
ADDENDUM_HEAD = "## Addendum 2026-09-04 (subagent #152, Claude Fable 5.1): store-side rule applied to all 404 menu-sighted tetragonal types"

RULE_TEXT = ("SURVIVOR = in every sighted group the f-vector is absent from the printed table or every printed row with that "
             "(group, f) reproduced (P2) as a different stored type; COLLISION = the type reproduces one of his printed cells "
             "(S-cell / SAME); UNRESOLVED = a printed row with that (group, f) was not stored (quarantined in the sweep), so no "
             "type-level statement is possible for that pair. Rows are matched to stored P2 cells by (group, printed point, "
             "b-ratio): exact printed_point_Bpp in the hexagonal store, point mod 1 in the tetragonal store (triage_phase2.py "
             "frac_key; the tetragonal store keeps the printed point verbatim in `point`).")


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_store(gz_path, sums_path, raw_path=None):
    """Decompress the committed .gz, hash the bytes against the SHA256SUMS raw line."""
    want = re.search(r"sha256\s+([0-9a-f]{64})", open(sums_path).read()).group(1)
    raw = gzip.open(gz_path, "rb").read()
    got = sha256_bytes(raw)
    assert got == want, f"{os.path.basename(gz_path)}: decompressed sha256 {got} != {want}"
    raw_note = "raw .json absent"
    if raw_path and os.path.exists(raw_path):
        with open(raw_path, "rb") as fh:
            raw_sha = hashlib.sha256(fh.read()).hexdigest()
        assert raw_sha == want, f"{os.path.basename(raw_path)}: sha256 {raw_sha} != {want}"
        raw_note = "raw .json present, sha256 matches"
    return json.loads(raw), got, raw_note


def load_rows(path):
    """Printed rows of a block-keyed digitization: [{groups, f, b, pt, pdf}]."""
    tables = json.load(open(path))
    rows = []
    for key, blk in tables.items():
        if key == "_meta":
            continue
        for r in blk["rows"]:
            rows.append({"groups": list(blk["groups"]), "f": tuple(r["f"]), "b": r["b"],
                         "pt": list(r["pt"]), "pdf": r["pdf_page"]})
    return rows


def key_exact(strs):
    return tuple(F(s) for s in strs)


def key_mod1(strs):
    return tuple(F(s) % 1 for s in strs)


def store_side_rule(types, rows, menu_ids, sighting_point_field, keyfn):
    """collision_phase2_hex_check.py lines 115-139, generic in the point field / key.

    Returns (verdict: {tid: status}, detail: {tid: {...}}). `detail` records the
    S-cell flag and, per sighted group with the f-vector printed, the counts of
    printed rows that reproduced as this type (same) / another stored type
    (other) / were not stored (unres), plus the unstored rows themselves.
    """
    by_group_f = defaultdict(set)
    rows_by_gf = defaultdict(list)
    for r in rows:
        for g in r["groups"]:
            by_group_f[g].add(r["f"])
            rows_by_gf[(g, r["f"])].append(r)
    p2_map = {}
    for tid, t in types.items():
        for s in t["sightings"]:
            if s["pass"] == "P2":
                p2_map[(s["group"], keyfn(s[sighting_point_field]), F(s["b"]))] = tid
    verdict, detail = {}, {}
    for tid in sorted(menu_ids):
        t = types[tid]
        fv = tuple(t["f_vector"])
        groups = sorted({s["group"] for s in t["sightings"]})
        scell = any(s["pass"] == "P2" for s in t["sightings"])
        same = unres = False
        res = OrderedDict()
        unres_rows = []
        for g in groups:
            if fv not in by_group_f.get(g, set()):
                continue
            c = Counter()
            for r in rows_by_gf[(g, fv)]:
                hit = p2_map.get((g, keyfn(r["pt"]), F(r["b"])))
                if hit is None:
                    unres = True
                    c["unres"] += 1
                    unres_rows.append(OrderedDict([("group", g), ("b", r["b"]), ("pt", r["pt"]), ("pdf_page", r["pdf"])]))
                elif hit == tid:
                    same = True
                    c["same"] += 1
                else:
                    c["other"] += 1
            res[str(g)] = OrderedDict((k, c[k]) for k in ("same", "other", "unres"))
        verdict[tid] = "COLLISION" if (same or scell) else ("UNRESOLVED" if unres else "SURVIVOR")
        detail[tid] = OrderedDict([
            ("f_vector", list(fv)), ("groups_sighted", groups), ("s_cell", scell),
            ("n_p2_sightings", sum(1 for s in t["sightings"] if s["pass"] == "P2")),
            ("same_by_row", same), ("resolution_per_group", res), ("unstored_rows", unres_rows),
        ])
    return verdict, detail, len(p2_map)


def parse_hex_triage_verdicts():
    out = {}
    in_table = False
    for line in open(HEX_TRIAGE_MD):
        if line.startswith("## Full ranked table"):
            in_table = True
            continue
        if in_table and line.startswith("## "):
            break
        m = re.match(r"^\| (\d+) \| `([0-9a-f]{16})` \|", line)
        if in_table and m:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            assert len(cells) == 18, (len(cells), line[:80])
            out[m.group(2)] = cells[16]
    return out


def parse_tet_doc_summary():
    out = {}
    for line in open(TET_COLL_MD):
        m = re.match(r"^- rank (\d+) `([0-9a-f]{16})`: (survives this screen|COLLISION)", line)
        if m:
            out[m.group(2)] = "SURVIVOR" if m.group(3).startswith("survives") else "COLLISION"
    return out


def main():
    t0 = time.time()
    # ---- stores (read-only, sha-verified) --------------------------------------
    tet, tet_sha, tet_raw_note = load_store(TET_GZ, TET_SUMS, TET_RAW)
    hx, hex_sha, _ = load_store(HEX_GZ, HEX_SUMS)
    assert tet_sha.startswith("71685b9a") and hex_sha.startswith("7494c7b2")
    T2, TH = tet["types"], hx["types"]

    # ---- 1. EQUIVALENCE on the hexagonal family (must reproduce 151/124/13) ------
    hex_rows = load_rows(HEX_TABLES)
    hex_menu = [tid for tid, t in TH.items() if t["first_sighting_system"] == HEX_FIRST
                and any(s["pass"] in MENU_PASSES for s in t["sightings"])]
    assert len(hex_menu) == 288 and set(hex_menu) == {tid for tid, t in TH.items() if t["first_sighting_system"] == HEX_FIRST and not t["schmitt_printed_only"]}
    hv, hd, n_hex_p2 = store_side_rule(TH, hex_rows, hex_menu, "printed_point_Bpp", key_exact)
    hc = dict(Counter(hv.values()))
    sl = json.load(open(HEX_SHORTLIST))
    assert sl["store_sha256"] == hex_sha
    hj = json.load(open(HEX_COLL_JSON))
    assert hj["store_sha256_before"] == hj["store_sha256_after"] == hex_sha
    triage_v = parse_hex_triage_verdicts()
    assert len(triage_v) == 288
    hex_equiv = OrderedDict([
        ("counts_here", OrderedDict(sorted(hc.items()))),
        ("counts_expected", OrderedDict(sorted(HEX_EXPECTED.items()))),
        ("counts_match_expected", hc == HEX_EXPECTED),
        ("counts_match_shortlist_json", hc == dict(sl["verdict_counts"])),
        ("counts_match_collision_hex_json", hc == dict(hj["screen_counts"])),
        ("survivors_ranked_match", [tid for tid in sl["survivors_ranked"] if hv.get(tid) == "SURVIVOR"] == sl["survivors_ranked"]
         and sorted(sl["survivors_ranked"]) == sorted(tid for tid, v in hv.items() if v == "SURVIVOR")),
        ("per_type_match_triage_table", all(hv[tid] == triage_v[tid] for tid in hex_menu)),
        ("n_types", len(hex_menu)), ("n_p2_cells_keyed", n_hex_p2),
    ])
    assert all(v is True for k, v in hex_equiv.items() if k.endswith("match") or k.endswith("match_expected")
               or k.endswith("match_shortlist_json") or k.endswith("match_collision_hex_json") or k.endswith("match_triage_table")), hex_equiv
    print(f"HEX EQUIVALENCE: {hc} == {HEX_EXPECTED}; per-type == triage table for all 288: PASS")

    # ---- 2. the rule on all 404 menu-sighted tetragonal types -------------------
    tet_rows = load_rows(TET_TABLES)
    assert len(tet_rows) == 1476
    tet_menu = [tid for tid, t in T2.items() if t["first_sighting_system"] == TET_FIRST
                and any(s["pass"] in MENU_PASSES for s in t["sightings"])]
    assert len(tet_menu) == 404 and set(tet_menu) == {tid for tid, t in T2.items() if t["first_sighting_system"] == TET_FIRST and not t["schmitt_printed_only"]}
    tv, td, n_tet_p2 = store_side_rule(T2, tet_rows, tet_menu, "point", key_mod1)
    assert n_tet_p2 == 1215, n_tet_p2            # TRIAGE_PHASE2_RESULT.md: 1215 stored cells
    # exact (no mod 1) keying, information only: how many verdicts would differ
    tv_exact, _, _ = store_side_rule(T2, tet_rows, tet_menu, "point", key_exact)
    n_exact_differs = sum(1 for tid in tet_menu if tv_exact[tid] != tv[tid])
    pure_counts = dict(Counter(tv.values()))
    n_scell = sum(1 for tid in tet_menu if td[tid]["s_cell"])
    assert n_scell == 176, n_scell               # TRIAGE_PHASE2_RESULT.md headline

    # ---- 3. overlay: the 27 recomputed pairs of collision_phase2_check.py --------
    cj = json.load(open(TET_COLL_JSON))
    assert cj["store_sha256"] == tet_sha
    pairs = cj["pairs"]
    assert len(pairs) == 27 and len({p["target"] for p in pairs}) == 15
    resolved = defaultdict(list)                 # tid -> rows resolved DIFFERENT by recomputation
    same_by_recomp = defaultdict(list)
    for p in pairs:
        assert p["verdict"] in ("SAME TYPE", "DIFFERENT TYPE"), p["pair"]
        if p["verdict"] == "SAME TYPE":
            same_by_recomp[p["target"]].append(p["pair"])
        elif p["p2"] == "unres":
            resolved[p["target"]].append(OrderedDict([("pair", p["pair"]), ("group", p["group"]), ("b", p["b"]), ("pt", list(p["point"]))]))
    combined = {}
    for tid in tet_menu:
        d = td[tid]
        if tv[tid] == "COLLISION" or tid in same_by_recomp:
            combined[tid] = "COLLISION"
            continue
        res_keys = {(r["group"], tuple(F(x) % 1 for x in r["pt"]), F(r["b"])) for r in resolved.get(tid, [])}
        still_unres = [r for r in d["unstored_rows"] if (r["group"], tuple(F(x) % 1 for x in r["pt"]), F(r["b"])) not in res_keys]
        combined[tid] = "UNRESOLVED" if still_unres else "SURVIVOR"
    comb_counts = dict(Counter(combined.values()))

    # ---- 4. consistency with COLLISION_PHASE2_RESULTS.md (15 shortlist targets) --
    doc = parse_tet_doc_summary()
    assert len(doc) == 15
    shortlist_disagreements = [OrderedDict([("type", tid), ("doc", doc[tid]), ("combined", combined[tid]), ("pure_rule", tv[tid])])
                               for tid in doc if combined[tid] != doc[tid]]
    survivors14 = sorted(tid for tid, v in doc.items() if v == "SURVIVOR")
    assert len(survivors14) == 14 and doc["cd4fb52572edcb73"] == "COLLISION"
    for tid in doc:
        assert not td[tid]["s_cell"], tid          # the shortlist excluded S-cells
    # catalog v3 said not-screened for the 389 non-shortlist menu types
    v3_status = {tid: (doc[tid] if tid in doc else "not-screened") for tid in tet_menu}
    transitions = Counter((v3_status[tid], combined[tid]) for tid in tet_menu)
    changed = [tid for tid in tet_menu if v3_status[tid] != combined[tid]]
    same_prev_ok = all(combined[tid] == v3_status[tid] for tid in doc)

    # ---- 5. write JSON (sorted keys, deterministic) -------------------------------
    verdicts = OrderedDict()
    for tid in sorted(tet_menu):
        d = td[tid]
        verdicts[tid] = OrderedDict([
            ("status", combined[tid]),
            ("status_pure_store_side_rule", tv[tid]),
            ("status_catalog_v3", v3_status[tid]),
            ("s_cell", d["s_cell"]), ("n_p2_sightings", d["n_p2_sightings"]),
            ("f_vector", d["f_vector"]), ("groups_sighted", d["groups_sighted"]),
            ("resolution_per_group", d["resolution_per_group"]),
            ("unstored_rows", d["unstored_rows"]),
            ("rows_resolved_different_by_recomputation", resolved.get(tid, [])),
            ("pairs_recomputed_same", same_by_recomp.get(tid, [])),
            ("in_top15_shortlist", tid in doc),
            ("shortlist_doc_status", doc.get(tid)),
        ])
    out = OrderedDict([
        ("generated_by", "harness/collision_phase2_tetragonal_storeside.py (subagent #152, Claude Fable 5.1), " + RUN_DATE),
        ("snapshot", SNAPSHOT),
        ("rule_text", RULE_TEXT),
        ("rule_source", "collision_phase2_hex_check.py lines 115-139 (store-side screen), re-implemented as a pure function; equivalence asserted on the hexagonal family"),
        ("overlay_text", "tetragonal only: the 27 printed pairs recomputed in collision_phase2_check.py (collision_phase2_results.json) resolve their rows: SAME TYPE -> COLLISION; DIFFERENT TYPE on an unstored (`unres`) row removes that row from the type's unresolved set; `other` pairs are already resolved by the store"),
        ("store_tetragonal_sha256", tet_sha), ("store_tetragonal_raw_note", tet_raw_note),
        ("store_hexagonal_sha256", hex_sha),
        ("hexagonal_equivalence", hex_equiv),
        ("n_tetragonal_menu_sighted", len(tet_menu)),
        ("n_tetragonal_s_cells", n_scell),
        ("n_tetragonal_p2_cells_keyed", n_tet_p2),
        ("n_tetragonal_verdicts_differing_under_exact_point_keying", n_exact_differs),
        ("counts_pure_store_side_rule", OrderedDict(sorted(pure_counts.items()))),
        ("counts_combined", OrderedDict(sorted(comb_counts.items()))),
        ("counts_catalog_v3", OrderedDict(sorted(Counter(v3_status.values()).items()))),
        ("transitions_v3_to_combined", OrderedDict((f"{a} -> {b}", n) for (a, b), n in sorted(transitions.items()))),
        ("n_types_changed_vs_catalog_v3", len(changed)),
        ("shortlist_disagreements", shortlist_disagreements),
        ("survivors_certified_14_all_SURVIVOR", all(combined[t] == "SURVIVOR" for t in survivors14)),
        ("known_collision_stays", combined["cd4fb52572edcb73"] == "COLLISION"),
        ("verdicts", verdicts),
    ])
    with open(OUT_JSON, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
        fh.write("\n")
    md5 = md5_file(OUT_JSON)

    # ---- 6. append-only addendum to COLLISION_PHASE2_RESULTS.md --------------------
    existing = open(TET_COLL_MD).read()
    appended = False
    if ADDENDUM_HEAD not in existing:
        L = ["", ADDENDUM_HEAD, "",
             f"Script: `collision_phase2_tetragonal_storeside.py` (plain python3, wall {time.time() - t0:.0f} s). Stores read-only and sha256-verified: "
             f"`phase2_types.json.gz` decompressed {tet_sha} ({tet_raw_note}); `phase2_hexagonal_types.json.gz` decompressed {hex_sha}. "
             "Rows: `schmitt_tetragonal_tables.json` (1476). Output: `collision_phase2_tetragonal_storeside.json` (sorted keys, deterministic; "
             f"md5 {md5}).", "",
             "**Rule (the hexagonal screen's store-side rule, COLLISION_PHASE2_HEX_RESULTS.md section 1, re-implemented as a pure function):** " + RULE_TEXT, "",
             f"- Equivalence assertion (run FIRST, on the 288 menu-sighted hexagonal-first types): {hc} == the hexagonal screen's "
             f"{HEX_EXPECTED}; per-type verdict equal to TRIAGE_PHASE2_HEX_RESULT.md's full table for all 288; survivor ranking identical. PASS.",
             f"- Tetragonal, PURE rule over the {len(tet_menu)} menu-sighted types ({n_tet_p2} stored P2 cells keyed by (group, point mod 1, b) as in triage_phase2.py; "
             f"exact keying would change {n_exact_differs} verdict(s)): " + ", ".join(f"{k} {v}" for k, v in sorted(pure_counts.items())) + f"; S-cells {n_scell}.",
             "- Overlay (this document's 27 recomputed pairs resolve their rows: SAME -> COLLISION; DIFFERENT on an unstored row -> that row resolved): "
             + ", ".join(f"{k} {v}" for k, v in sorted(comb_counts.items())) + ".",
             "- Against catalog v3 (15 shortlist statuses + 389 not-screened): " + "; ".join(f"{k}: {v}" for k, v in sorted(((f"{a} -> {b}", n) for (a, b), n in transitions.items()))) + ".",
             f"- Shortlist consistency: the 15 'Summary per shortlist type' lines above vs the combined status: {len(shortlist_disagreements)} disagreement(s)"
             + ("" if not shortlist_disagreements else " — " + "; ".join(f"`{d['type']}` doc {d['doc']} / combined {d['combined']}" for d in shortlist_disagreements))
             + f". The 14 certified survivors are SURVIVOR: {all(combined[t] == 'SURVIVOR' for t in survivors14)}; `cd4fb52572edcb73` stays COLLISION: {combined['cd4fb52572edcb73'] == 'COLLISION'}.",
             "- Under the PURE rule the certified survivors whose worklist had `unres` rows read UNRESOLVED (their unstored two-origin / second-enantiomorph / IT(80) rows); "
             "the recomputation above resolved exactly those rows, which is why the combined status is the catalog's. Every other UNRESOLVED type has an unstored printed row "
             "at its (group, f) that no recomputation has touched (listed per type in the JSON) — no verdict is claimed for those pairs.",
             "- LANGUAGE (G5): SURVIVOR = 'not matched against the records checked as of " + SNAPSHOT + "', never novelty; COLLISION = the type reproduces one of his printed cells (first-realization reframe).",
             "- No new mathematics: no cell was computed; nothing was added to any store (sha256 unchanged). Digitization caveat as above (single visual pass, text-layer cross-checked, not re-keyed).",
             ""]
        with open(TET_COLL_MD, "a") as fh:
            fh.write("\n".join(L))
        appended = True

    print(f"TETRAGONAL pure rule: {pure_counts}; S-cells {n_scell}; exact-keying differs {n_exact_differs}")
    print(f"TETRAGONAL combined:  {comb_counts}")
    print(f"transitions v3 -> combined: {dict(transitions)}")
    print(f"shortlist disagreements: {len(shortlist_disagreements)} {shortlist_disagreements}")
    print(f"JSON {OUT_JSON} md5 {md5}; addendum appended: {appended}; wall {time.time() - t0:.1f} s")
    ok = (hex_equiv["counts_match_expected"] and hex_equiv["per_type_match_triage_table"] and not shortlist_disagreements
          and same_prev_ok and out["survivors_certified_14_all_SURVIVOR"] and out["known_collision_stays"])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
