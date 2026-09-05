#!/usr/bin/env python3
"""
MINT Track 3 - verify_counts_independent.py  (v5, 2026-09-04)

INDEPENDENT RECOUNT. Shares no code with build_catalog.py (nothing imported from
it; its own loaders, its own hashing, its own parsing, its own counting), and
re-derives every summary number DIRECTLY from the three dedupe stores, the
certificate files on disk and the accepted results documents, then asserts
equality with what catalog.json claims. Exit 0 = every assertion held.

v1 (cubic + tetragonal, 891 types) = git show 06e5d30:paper_prep/MINT_plesiohedron/catalog/verify_counts_independent.py
v2 (hexagonal family + both phase-2 G4 batches, 1,583 types) = git show 169ccb4:paper_prep/MINT_plesiohedron/catalog/verify_counts_independent.py
v3 (open/wall verdicts + type-level Schmitt status, tetragonal top-15 only) = git show e01618b:paper_prep/MINT_plesiohedron/catalog/verify_counts_independent.py
v4 (tetragonal store-side rule; 106 tetragonal UNRESOLVED) = git show 27e0083:paper_prep/MINT_plesiohedron/catalog/verify_counts_independent.py
v5 (2026-09-04, subagent #154) re-derives, with its own loaders, the status of the
106 v4-UNRESOLVED tetragonal types from ../harness/collision_phase2_tetragonal_
rows_recomputed.json (the 62 recomputed rows: own keying of each row to the
type's own unstored-row list, own comparison of the recorded canonical code with
the store's, own check that every recorded cell's code id is the sha1 of its code
and that its f-vector equals the printed row's in the digitization) and asserts
equality with ../harness/collision_phase2_tetragonal_unresolved_overlay.json, with
the md5s stated in the COLLISION_PHASE2_RESULTS.md #154 addendum and the catalog,
and with every catalog row; the 15 shortlist statuses and the 13 + 102 pool are
asserted unchanged; tetragonal totals 201 / 203 / 0 asserted.
v4 (2026-09-04, subagent #152) re-derives, with its OWN implementation of the
store-side collision rule (no code shared with the harness script or the builder),
the hexagonal screen (must give 151/124/13 per type) and the tetragonal status of
all 404 menu-sighted tetragonal-first types from the stores + the digitizations +
the 27 recomputed pairs, asserts equality with ../harness/
collision_phase2_tetragonal_storeside.json (per type, pure rule and overlay), with
the md5 stated in the COLLISION_PHASE2_RESULTS.md addendum and the catalog, and with
every catalog row; the 15 shortlist statuses and the 13 + 102 pool are asserted
unchanged.
v3 (2026-09-04, subagent #150) adds, with its own loaders and no code shared
with build_catalog.py: the open/wall verdicts recounted per family from
../harness/phase2/WALL_OPEN_PHASE2.json (165 cells; md5 asserted to be the
value stated in WALL_OPEN_PHASE2.md) and ../harness/round1_computations/
c1_wall_open.json (7 cubic cells); the type-level Schmitt status recounted per
family from ../harness/collision_phase2_results.json (27 pairs -> 15 targets),
../harness/collision_phase2_hex_results.json + the triage table, and the
stores' schmitt_printed_only flags; the verdict x status cross-tab; and the
naming pool (certified by the files on disk AND OPEN by the verdict files AND
unnamed) asserted == 13 tetragonal + 102 hexagonal-family (PROGRAM_LEDGER
2026-09-04 14:10). Every per-row v3 value is compared, then the summary blocks.

Reads (read-only):
  ../harness/phase1_types.json
  ../harness/phase2_types.json.gz            (decompressed bytes hashed against
                                              ../harness/phase2_types.SHA256SUMS)
  ../harness/phase2_hexagonal_types.json.gz  (gz file AND decompressed bytes hashed
                                              against phase2_hexagonal_types.SHA256SUMS)
  ../harness/g4_tables_*.json, ../track4/g4_tables_laves17.json,
  ../harness/g4p2_tables_*.json, ../harness/g4p2hex_tables_*.json
  ../harness/G4_PHASE2_RESULTS.md, ../harness/G4_PHASE2_HEX_RESULTS.md (chirality)
  ../harness/TRIAGE_PHASE2_HEX_RESULT.md, ../harness/triage_phase2_hex_shortlist.json
  ../harness/phase2/WALL_OPEN_PHASE2.json (+ .md), ../harness/round1_computations/c1_wall_open.json   (v3)
  ../harness/collision_phase2_results.json, ../harness/COLLISION_PHASE2_RESULTS.md,                 (v3)
  ../harness/collision_phase2_hex_results.json, ../harness/COLLISION_PHASE2_HEX_RESULTS.md,         (v3)
  ../harness/collision_phase2_tetragonal_storeside.json, ../harness/schmitt_tetragonal_tables.json,
  ../harness/schmitt_hexagonal_tables.json                                                          (v4)
  ../publication/ (folder names = the only naming record)                                          (v3)
  ./catalog.json, ./catalog_sightings.json.gz, ./catalog.SHA256SUMS
Recounts: total types; per-family first-sighting counts; seeded; menu-sighted vs
Schmitt-printed-only (tetragonal and hexagonal); prior types re-sighted in later
families; per-group "types sighted" and "types first witnessed here"; max facet
counts; distinct f-vectors; per-type f-vector, p-vector, aut, groups sighted,
canonical-code id, witness; per-G4-status counts and pointer sets; chiral counts
(solid, from the two phase-2 results docs; honeycomb, from the tables files);
hexagonal screen verdict counts.
Run:  python3 verify_counts_independent.py
"""
import gzip
import hashlib
import json
import os
import re
import sys

D = os.path.dirname(os.path.abspath(__file__))
H = os.path.join(os.path.dirname(D), "harness")
T4 = os.path.join(os.path.dirname(D), "track4")

fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)
        print("  FAIL:", msg)
    return cond


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    # --- stores, loaded independently ---------------------------------------
    p1 = json.load(open(os.path.join(H, "phase1_types.json")))
    raw = gzip.open(os.path.join(H, "phase2_types.json.gz"), "rb").read()
    want = re.search(r"sha256\s+([0-9a-f]{64})", open(os.path.join(H, "phase2_types.SHA256SUMS")).read()).group(1)
    got = hashlib.sha256(raw).hexdigest()
    check(got == want, f"phase2 store sha256 {got} != {want}")
    p2 = json.loads(raw)
    sums_hx = open(os.path.join(H, "phase2_hexagonal_types.SHA256SUMS")).read().splitlines()
    want_raw = re.search(r"^phase2_hexagonal_types\.json\s+sha256\s+([0-9a-f]{64})", sums_hx[0]).group(1)
    want_gz = re.search(r"^phase2_hexagonal_types\.json\.gz\s+sha256\s+([0-9a-f]{64})", sums_hx[1]).group(1)
    check(sha(os.path.join(H, "phase2_hexagonal_types.json.gz")) == want_gz, "hexagonal store .gz sha256")
    raw_hx = gzip.open(os.path.join(H, "phase2_hexagonal_types.json.gz"), "rb").read()
    got_hx = hashlib.sha256(raw_hx).hexdigest()
    check(got_hx == want_raw == "7494c7b26114a68f1177158eb311a05546ba0b15cd5b1a27569c633858983a55", f"hexagonal store sha256 {got_hx} != {want_raw}")
    hx = json.loads(raw_hx)
    cat = json.load(open(os.path.join(D, "catalog.json")))
    sight = json.load(gzip.open(os.path.join(D, "catalog_sightings.json.gz"), "rt"))
    S = cat["summary"]
    crow = {r["type_id"]: r for r in cat["types"]}
    check(cat.get("catalog_version") == 5 and S.get("catalog_version") == 5, "catalog version 5")
    # the SHA256SUMS the builder wrote must match the files on disk
    for line in open(os.path.join(D, "catalog.SHA256SUMS")):
        fn, h = line.split()[0], line.split()[2]
        check(sha(os.path.join(D, fn)) == h, f"catalog.SHA256SUMS {fn}")

    # --- headline recount ------------------------------------------------------
    TH = hx["types"]
    T2 = p2["types"]
    cubic_first = [k for k, v in TH.items() if v["first_sighting_system"].startswith("cubic")]
    tet_first = [k for k, v in TH.items() if v["first_sighting_system"].startswith("tetragonal")]
    hex_first = [k for k, v in TH.items() if v["first_sighting_system"].startswith("hexagonal")]
    n_total = len(TH)
    print(f"total types {n_total}; cubic-first {len(cubic_first)}; tetragonal-first {len(tet_first)}; hexagonal-first {len(hex_first)}")
    check(n_total == len(cubic_first) + len(tet_first) + len(hex_first), "every type has a known first family")
    check(n_total == S["n_types_total"] == len(cat["types"]) == len(sight), "total")
    check(len(cubic_first) == S["n_types_cubic_first"] == len(p1["types"]), "cubic-first")
    check(len(tet_first) == S["n_types_tetragonal_first"], "tetragonal-first")
    check(len(hex_first) == S["n_types_hexagonal_first"] == hx["n_types_hexagonal_new"], "hexagonal-first")
    check(S["n_types_by_first_sighting_family"] == {"cubic": len(cubic_first), "tetragonal": len(tet_first), "hexagonal": len(hex_first)}, "by-family dict")
    check(sorted(cubic_first) == sorted(p1["types"]), "cubic-first id set == phase1 store")
    check(sorted(cubic_first + tet_first) == sorted(T2), "prior id set == phase2 store")
    check(hx["type_order"][:len(p2["type_order"])] == p2["type_order"], "type order prefix")
    check([r["type_id"] for r in cat["types"]] == hx["type_order"], "catalog order == hexagonal store order")
    ids_by_family = {"C": cubic_first, "T": tet_first, "H": hex_first}
    for k, r in crow.items():
        fam = r["catalog_id"][5]
        check(k in ids_by_family[fam], f"catalog_id family letter {k}")
    seeded = [k for k, v in TH.items() if v.get("seeded")]
    check(len(seeded) == S["n_seeded"] == sum(1 for v in p1["types"].values() if v.get("seeded")), "seeded")
    menu = [k for k in tet_first if not T2[k]["schmitt_printed_only"]]
    sonly = [k for k in tet_first if T2[k]["schmitt_printed_only"]]
    print(f"tetragonal-first: menu-sighted {len(menu)}, Schmitt-printed-only {len(sonly)}")
    check(len(menu) == S["n_tetragonal_first_menu_sighted"] == p2["n_types_tetragonal_menu_sighted"], "menu-sighted")
    check(len(sonly) == S["n_tetragonal_first_schmitt_printed_only"] == p2["n_types_tetragonal_schmitt_printed_only"], "schmitt-only")
    hmenu = [k for k in hex_first if not TH[k]["schmitt_printed_only"]]
    hsonly = [k for k in hex_first if TH[k]["schmitt_printed_only"]]
    print(f"hexagonal-first: menu-sighted {len(hmenu)}, Schmitt-printed-only {len(hsonly)}")
    check(len(hmenu) == S["n_hexagonal_first_menu_sighted"] == hx["n_types_hexagonal_menu_sighted"], "hex menu-sighted")
    check(len(hsonly) == S["n_hexagonal_first_schmitt_printed_only"] == hx["n_types_hexagonal_schmitt_printed_only"], "hex schmitt-only")
    for k in tet_first:
        kinds = {s["kind"] for s in T2[k]["sightings"]}
        check((kinds == {"schmitt_printed"}) == T2[k]["schmitt_printed_only"], f"flag vs kinds {k}")
    for k in hex_first:
        kinds = {s["kind"] for s in TH[k]["sightings"]}
        check((kinds == {"schmitt_printed"}) == TH[k]["schmitt_printed_only"], f"hex flag vs kinds {k}")
    resighted = [k for k in cubic_first if T2[k]["sightings"]]
    resighted_menu = [k for k in cubic_first if any(s["kind"] != "schmitt_printed" for s in T2[k]["sightings"])]
    print(f"cubic-first re-sighted in tetragonal groups: {len(resighted)} (by menu: {len(resighted_menu)})")
    check(len(resighted) == S["n_cubic_first_resighted_tetragonal"], "resighted")
    check(len(resighted_menu) == S["n_cubic_first_resighted_tetragonal_menu"], "resighted menu")
    prior_hx = [k for k in cubic_first + tet_first if TH[k]["sightings"]]
    prior_hx_menu = [k for k in cubic_first + tet_first if any(s["kind"] != "schmitt_printed" for s in TH[k]["sightings"])]
    print(f"prior types re-sighted in the hexagonal family: {len(prior_hx)} (by menu {len(prior_hx_menu)}; cubic-first {sum(1 for k in prior_hx if k in p1['types'])}, tetragonal-first {sum(1 for k in prior_hx if k not in p1['types'])})")
    check(len(prior_hx) == S["n_prior_resighted_hexagonal"], "prior resighted hex")
    check(len(prior_hx_menu) == S["n_prior_resighted_hexagonal_menu"], "prior resighted hex menu")
    check(sum(1 for k in prior_hx if k in p1["types"]) == S["n_cubic_first_resighted_hexagonal"], "cubic-first resighted hex")
    check(sum(1 for k in prior_hx if k not in p1["types"]) == S["n_tetragonal_first_resighted_hexagonal"], "tet-first resighted hex")
    never = [k for k in seeded if not p1["types"][k]["sightings"] and not T2[k]["sightings"] and not TH[k]["sightings"]]
    check(len(never) == S["n_seeded_never_sighted"], "seeded never sighted")

    # --- per-type recount --------------------------------------------------------
    per_group_sighted = {}
    per_group_first = {}
    maxF = 0
    fset = set()
    fam_sighted = {"cubic": 0, "tetragonal": 0, "hexagonal": 0}
    for k, v in TH.items():
        r = crow[k]
        f = v["f_vector"]
        maxF = max(maxF, f[2]); fset.add(tuple(f))
        check(r["f_vector"] == f and r["p_vector"] == v["p_vector"] and r["aut_order"] == v["aut_order"], f"f/p/aut {k}")
        check(r["F"] == f[2] and r["V"] == f[0] and r["E"] == f[1], f"V/E/F {k}")
        check(f[0] - f[1] + f[2] == 2 and len(v["p_vector"]) == f[2] and sum(v["p_vector"]) == 2 * f[1], f"Euler/p {k}")
        check(hashlib.sha1(v["canon_code"].encode()).hexdigest()[:16] == k, f"id {k}")
        check(r["canon_code"] == v["canon_code"], f"code {k}")
        if k in T2:
            check(T2[k]["canon_code"] == v["canon_code"] and T2[k]["f_vector"] == f, f"phase2 code/f {k}")
        cub = p1["types"][k]["sightings"] if k in p1["types"] else []
        tet = T2[k]["sightings"] if k in T2 else []
        hexs = v["sightings"]
        gc = sorted({s["group"] for s in cub}); gt = sorted({s["group"] for s in tet}); gh = sorted({s["group"] for s in hexs})
        check(r["groups_sighted_cubic"] == gc and r["groups_sighted_tetragonal"] == gt and r["groups_sighted_hexagonal"] == gh, f"groups {k}")
        check(r["n_sightings_cubic"] == len(cub) and r["n_sightings_tetragonal"] == len(tet) and r["n_sightings_hexagonal"] == len(hexs), f"n sightings {k}")
        check(r["n_sightings_hexagonal_menu"] == sum(1 for s in hexs if s["kind"] != "schmitt_printed"), f"n hex menu {k}")
        check(len(sight[k]) == len(cub) + len(tet) + len(hexs), f"sidecar sightings {k}")
        check([s["system"] for s in sight[k]] == ["cubic"] * len(cub) + ["tetragonal"] * len(tet) + ["hexagonal"] * len(hexs), f"sidecar families {k}")
        fams = sorted({x for x, n in (("cubic", len(cub)), ("tetragonal", len(tet)), ("hexagonal", len(hexs))) if n})
        check(r["crystal_families_sighted"] == fams == r["systems_sighted"], f"families {k}")
        for x in fams:
            fam_sighted[x] += 1
        for g in gc + gt + gh:
            per_group_sighted[g] = per_group_sighted.get(g, 0) + 1
        if k in p1["types"]:
            w = p1["types"][k]["first_witness"]
            if w is None and cub:
                w = cub[0]
        elif k in T2:
            w = T2[k]["first_witness"]
        else:
            w = v["first_witness"]
        if w is not None:
            per_group_first[w["group"]] = per_group_first.get(w["group"], 0) + 1
            check(r["witness_group"] == w["group"] and r["witness_point"] == w["point"], f"witness {k}")
        else:
            check(r["witness_group"] is None, f"witness null {k}")
    print(f"max F {maxF}; distinct f-vectors {len(fset)}")
    check(maxF == S["max_F_all"] == max(p2["max_facets_stored"], hx["max_facets_stored"]), "max F")
    check(len(fset) == S["n_distinct_fvectors"], "distinct f")
    check(max(p1["types"][k]["f_vector"][2] for k in cubic_first) == S["max_F_cubic_first"] == p1["max_facets_stored"], "max F cubic")
    check(max(T2[k]["f_vector"][2] for k in menu) == S["max_F_tetragonal_menu"] == p2["max_facets_from_our_menu"], "max F tet menu")
    check(max(TH[k]["f_vector"][2] for k in hmenu) == S["max_F_hexagonal_menu"] == hx["max_facets_from_our_menu"], "max F hex menu")
    check(max(TH[k]["f_vector"][2] for k in hex_first) == S["max_F_hexagonal_first"] == hx["max_facets_stored"], "max F hex first")
    check(len({tuple(TH[k]["f_vector"]) for k in hex_first}) == S["n_distinct_fvectors_hexagonal_first"], "distinct f hex-first")
    check(len({tuple(TH[k]["f_vector"]) for k in cubic_first}) == S["n_distinct_fvectors_cubic_first"], "distinct f cubic-first")
    check(len({tuple(TH[k]["f_vector"]) for k in tet_first}) == S["n_distinct_fvectors_tetragonal_first"], "distinct f tet-first")
    check(S["per_system_types_sighted"] == fam_sighted, f"per-family types sighted {fam_sighted}")
    print(f"per-family types sighted: {fam_sighted}")

    # --- per-group -----------------------------------------------------------------
    PG = S["per_group"]
    check(sorted(int(g) for g in PG) == sorted(per_group_sighted), "per-group key set")
    print("per group (IT: sighted / first-here):")
    line = []
    for g in sorted(per_group_sighted):
        c = PG[str(g)]
        check(c.get("types_sighted", 0) == per_group_sighted[g], f"group {g} sighted")
        check(c.get("types_first_here", 0) == per_group_first.get(g, 0), f"group {g} first here")
        line.append(f"{g}:{per_group_sighted[g]}/{per_group_first.get(g, 0)}")
    print("  " + " ".join(line))
    check(sum(per_group_first.get(g, 0) for g in range(143, 195)) == len(hex_first), "hex-first witnesses all in IT 143-194")
    # stores' own per-group summaries
    for gsum in p2["groups_summary"]:
        g = gsum["group"]
        n_tet = sum(1 for k in tet_first if any(s["group"] == g for s in T2[k]["sightings"]))
        n_cub = sum(1 for k in cubic_first if any(s["group"] == g for s in T2[k]["sightings"]))
        check(n_tet == gsum["types_tetragonal"] and n_cub == gsum["types_cubic_store"], f"phase2 groups_summary {g}")
    for gsum in p1["groups_summary"]:
        g = gsum["group"]
        n = sum(1 for k in cubic_first if any(s["group"] == g for s in p1["types"][k]["sightings"]))
        check(n == gsum["types_distinct"], f"phase1 groups_summary {g}")
    for gsum in hx["groups_summary"]:
        g = gsum["group"]
        n_h = sum(1 for k in hex_first if any(s["group"] == g for s in TH[k]["sightings"]))
        n_p = sum(1 for k in cubic_first + tet_first if any(s["group"] == g for s in TH[k]["sightings"]))
        check(n_h == gsum["types_hexagonal"] and n_p == gsum["types_prior_store"] and n_h + n_p == gsum["types_distinct"] == per_group_sighted.get(g, 0), f"hexagonal groups_summary {g}")

    # --- G4 pointers, statuses, chirality -----------------------------------------------
    def ids_on_disk(prefix):
        return {re.fullmatch(prefix + r"([0-9a-f]{16})\.json", f).group(1) for f in os.listdir(H) if re.fullmatch(prefix + r"([0-9a-f]{16})\.json", f)}
    g4 = ids_on_disk("g4_tables_")
    g4p2 = ids_on_disk("g4p2_tables_")
    g4hex = ids_on_disk("g4p2hex_tables_")
    check(os.path.exists(os.path.join(T4, "g4_tables_laves17.json")), "track4 laves tables present")
    st = {k: r["g4_status"] for k, r in crow.items()}
    acc_cubic = {k for k, s in st.items() if s == "accepted-cubic"}
    cert_tet = {k for k, s in st.items() if s == "certified-tetragonal"}
    cert_hex = {k for k, s in st.items() if s == "certified-hexagonal"}
    none_ = {k for k, s in st.items() if s == "none"}
    check(len(acc_cubic) + len(cert_tet) + len(cert_hex) + len(none_) == n_total, "g4_status values")
    check(g4 <= acc_cubic and len(acc_cubic) == len(g4) + 1 and (acc_cubic - g4) == {"8c69db9e84095469"}, "accepted-cubic = 11 cubic + Laves (track4)")
    check(cert_tet == g4p2 and len(g4p2) == 14, "certified-tetragonal == g4p2 files (14)")
    check(cert_hex == g4hex and len(g4hex) == 151, "certified-hexagonal == g4p2hex files (151)")
    check(all(k in tet_first for k in cert_tet) and all(k in hex_first for k in cert_hex) and all(k in cubic_first for k in acc_cubic), "certificate families")
    check(S["g4_status_counts"] == {"accepted-cubic": len(acc_cubic), "certified-tetragonal": len(cert_tet), "certified-hexagonal": len(cert_hex), "none": len(none_)}, "g4 status counts")
    check(S["n_G4_certified_accepted"] == len(acc_cubic) + len(cert_tet) + len(cert_hex) and S["n_G4_provisional_tables_present"] == 0, "G4 summary")
    for k, r in crow.items():
        if r["g4_status"] == "none":
            check(r["g4_certificate_file"] is None and r["g4_chiral_solid"] is None and r["g4_chiral_honeycomb"] is None and r["gate_G4_certified"] == "no", f"g4 none fields {k}")
        else:
            p = os.path.join(os.path.dirname(D), r["g4_certificate_file"])
            check(os.path.exists(p) and r["gate_G4_certified"].startswith("yes") and r["gate_G4_pointer"] == r["g4_certificate_file"], f"g4 pointer {k}")
            tab = json.load(open(p))
            check(r["g4_chiral_honeycomb"] == (tab["n_improper"] == 0), f"honeycomb chirality {k}")
    print(f"G4: accepted-cubic {len(acc_cubic)}, certified-tetragonal {len(cert_tet)}, certified-hexagonal {len(cert_hex)}, none {len(none_)}")
    # solid chirality, parsed here from the two results documents with this file's own regexes
    tet_chi = {}
    sec = open(os.path.join(H, "G4_PHASE2_RESULTS.md")).read().split("## Isometry vs site vs aut summary")[1].split("\n## ")[0]
    for m in re.finditer(r"`([0-9a-f]{16})`[^\n]*\| (chiral|achiral) \|", sec):
        tet_chi[m.group(1)] = m.group(2) == "chiral"
    hex_chi = {}
    sec = open(os.path.join(H, "G4_PHASE2_HEX_RESULTS.md")).read().split("## Summary table")[1].split("\n## ")[0]
    for m in re.finditer(r"`([0-9a-f]{16})`[^\n]*\| PASS \| (chiral|achiral) \|", sec):
        hex_chi[m.group(1)] = m.group(2) == "chiral"
    check(set(tet_chi) == g4p2 and set(hex_chi) == g4hex, "chirality tables cover the certificate sets")
    for k in g4p2:
        check(crow[k]["g4_chiral_solid"] == tet_chi[k], f"tet chirality {k}")
    for k in g4hex:
        check(crow[k]["g4_chiral_solid"] == hex_chi[k], f"hex chirality {k}")
    for k in acc_cubic:
        check(crow[k]["g4_chiral_solid"] is None, f"cubic chirality not recorded {k}")
    n_chi = sum(tet_chi.values()) + sum(hex_chi.values())
    n_achi = len(tet_chi) + len(hex_chi) - n_chi
    hc = S["g4_chiral_solid_counts"]
    check(hc["chiral"] == n_chi and hc["achiral"] == n_achi and hc["not_recorded_in_certificate"] == len(acc_cubic), "chiral solid counts")
    check(hc["by_status"]["certified-tetragonal"] == {"chiral": sum(tet_chi.values()), "achiral": len(tet_chi) - sum(tet_chi.values()), "not_recorded": 0}, "tet chiral by status")
    check(hc["by_status"]["certified-hexagonal"] == {"chiral": sum(hex_chi.values()), "achiral": len(hex_chi) - sum(hex_chi.values()), "not_recorded": 0}, "hex chiral by status")
    n_hchi = sum(1 for k in acc_cubic | cert_tet | cert_hex if crow[k]["g4_chiral_honeycomb"])
    check(S["g4_chiral_honeycomb_counts"] == {"chiral": n_hchi, "achiral": len(acc_cubic | cert_tet | cert_hex) - n_hchi}, "honeycomb chiral counts")
    print(f"chiral solids (where recorded): tetragonal {sum(tet_chi.values())}/{len(tet_chi)}, hexagonal {sum(hex_chi.values())}/{len(hex_chi)}; chiral honeycombs {n_hchi}/{len(acc_cubic | cert_tet | cert_hex)}")

    # --- hexagonal screen verdicts --------------------------------------------------------
    shortlist = json.load(open(os.path.join(H, "triage_phase2_hex_shortlist.json")))
    surv = set(shortlist["survivors_ranked"])
    check(shortlist["store_sha256"] == got_hx and surv == g4hex, "survivors == certified-hexagonal")
    verd = {}
    sec = open(os.path.join(H, "TRIAGE_PHASE2_HEX_RESULT.md")).read().split("## Full ranked table")[1].split("\n## ")[0]
    for line_ in sec.splitlines():
        m = re.match(r"^\| \d+ \| `([0-9a-f]{16})` \|", line_)
        if m:
            verd[m.group(1)] = [c.strip() for c in line_.strip().strip("|").split("|")][16]
    check(set(verd) == set(hmenu), "triage table covers the menu-sighted hexagonal-first types")
    cnt = {v: sum(1 for x in verd.values() if x == v) for v in ("SURVIVOR", "COLLISION", "UNRESOLVED")}
    check({k for k, v in verd.items() if v == "SURVIVOR"} == surv, "SURVIVOR set")
    for k, v in verd.items():
        check(crow[k]["schmitt_match_hexagonal"].startswith(v), f"schmitt_match_hexagonal {k}")
    for k in hsonly:
        check(crow[k]["schmitt_match_hexagonal"].startswith("S-cell, printed-only"), f"printed-only match {k}")
    for k in prior_hx:
        check(crow[k]["schmitt_match_hexagonal"].startswith("prior"), f"prior match {k}")
    for k in set(TH) - set(prior_hx) - set(hex_first):
        check(crow[k]["schmitt_match_hexagonal"].startswith("n/a"), f"n/a match {k}")
    sm = S["schmitt_match_hexagonal"]
    check(sm["hexagonal_first_SURVIVOR"] == cnt["SURVIVOR"] and sm["hexagonal_first_COLLISION"] == cnt["COLLISION"] and sm["hexagonal_first_UNRESOLVED"] == cnt["UNRESOLVED"], "screen counts")
    check(sm["hexagonal_first_S_cell_printed_only"] == len(hsonly) and sm["prior_resighted_in_family"] == len(prior_hx) and sm["no_hexagonal_sighting"] == n_total - len(hsonly) - len(prior_hx) - len(hmenu), "match-status counts")
    print(f"hexagonal screen: {cnt}; printed-only {len(hsonly)}; prior re-sighted {len(prior_hx)}")

    # --- v3: open/wall verdicts, recounted from the raw verdict files (own loaders) -------------
    wo_raw = open(os.path.join(H, "phase2", "WALL_OPEN_PHASE2.json"), "rb").read()
    wo = json.loads(wo_raw)
    md5 = hashlib.md5(wo_raw).hexdigest()
    md_txt = open(os.path.join(H, "phase2", "WALL_OPEN_PHASE2.md")).read()
    check(("md5 = `%s`" % md5) in md_txt, "WALL_OPEN_PHASE2.json md5 == the value stated in WALL_OPEN_PHASE2.md")
    check(wo["n_cells"] == len(wo["cells"]) == 165 and wo["n_crash"] == 0 and wo["regression_ok"] is True, "WALL_OPEN: 165 cells, 0 crashes, regression ok")
    check(wo["stores"]["phase2_types.json_sha256"] == got and wo["stores"]["phase2_hexagonal_types.json_sha256"] == got_hx and wo["stores"]["sha256_unchanged_after_run"] is True, "WALL_OPEN store hashes")
    wcell = {c["id"]: c for c in wo["cells"]}
    check(set(wcell) == g4p2 | g4hex, "WALL_OPEN ids == the 165 phase-2 certificate files")
    check({k for k, c in wcell.items() if c["family"] == "tetragonal"} == g4p2 and {k for k, c in wcell.items() if c["family"] == "hexagonal"} == g4hex, "WALL_OPEN families")
    for k, c in wcell.items():
        w = T2[k]["first_witness"] if k in g4p2 else TH[k]["first_witness"]
        check(c["witness_point"] == "(" + ", ".join(w["point"]) + ")" and c["c_over_a"] == w["b"] and c["IT"] == w["group"] and c["base_f"] == TH[k]["f_vector"], f"WALL_OPEN witness {k}")
    c1 = json.load(open(os.path.join(H, "round1_computations", "c1_wall_open.json")))
    c1v = {r["id"]: r["verdict"] for r in c1}
    check(len(c1v) == 7 and set(c1v) <= acc_cubic and not (set(c1v) & set(wcell)), "c1: 7 accepted-cubic cells, disjoint from phase 2")
    fam_of = {}
    for k in cubic_first:
        fam_of[k] = "cubic"
    for k in tet_first:
        fam_of[k] = "tetragonal"
    for k in hex_first:
        fam_of[k] = "hexagonal"
    VERD = ("OPEN", "WALL", "ONE-SIDED", "not-computed")
    exp_v, exp_src = {}, {}
    for k in TH:
        if k in wcell:
            exp_v[k], exp_src[k] = wcell[k]["combined_verdict"], "phase2 #148"
        elif k in c1v:
            exp_v[k], exp_src[k] = c1v[k], "c1 cubic"
        else:
            exp_v[k], exp_src[k] = "not-computed", "none"
        check(exp_v[k] in VERD, f"verdict value {k}")
    for k, r in crow.items():
        check(r["open_wall_verdict"] == exp_v[k] and r["open_wall_verdict_source"] == exp_src[k], f"open_wall_verdict {k}")
        if k in wcell:
            c = wcell[k]
            check(r["open_wall_point_verdict"] == c["point_verdict"] and r["open_wall_metric_verdict"] == c["metric_verdict"]
                  and r["open_wall_flags"] == sorted(f_ for f_, v in c["flags"].items() if v), f"open_wall point/metric/flags {k}")
            check(r["open_wall_scheme_date"].startswith("2026-09-04") and "1/1536" in r["open_wall_scheme"] and "1/3072" in r["open_wall_scheme"]
                  and "WALL_OPEN_PHASE2.json" in r["open_wall_verdict_pointer"] and md5 in r["open_wall_verdict_pointer"], f"scheme / pointer {k}")
        elif k in c1v:
            check(r["open_wall_point_verdict"] == c1v[k] and r["open_wall"] is not None and r["open_wall"].split()[0] == c1v[k]
                  and r["open_wall_scheme_date"].startswith("2026-09-03") and "c1_wall_open.json" in r["open_wall_verdict_pointer"], f"c1 verdict vs v2 open_wall {k}")
        else:
            check(r["open_wall_point_verdict"] is None and r["open_wall_flags"] is None and r["open_wall_scheme"] is None and r["open_wall_scheme_date"] is None, f"not-computed fields {k}")
    vc = {f_: {v: 0 for v in VERD} for f_ in ("cubic", "tetragonal", "hexagonal")}
    for k in TH:
        vc[fam_of[k]][exp_v[k]] += 1
    for f_ in vc:
        check(dict(S["open_wall_verdict_counts"][f_]) == vc[f_], f"open_wall_verdict_counts {f_}")
        src_c = {"c1 cubic": 0, "phase2 #148": 0, "none": 0}
        for k in TH:
            if fam_of[k] == f_:
                src_c[exp_src[k]] += 1
        check(dict(S["open_wall_verdict_source_counts"][f_]) == src_c, f"open_wall_verdict_source_counts {f_}")
    for f_ in ("tetragonal", "hexagonal"):
        agg = dict(wo["aggregate"][f_]["combined"])
        agg.setdefault("ONE-SIDED", 0)
        check({v: n for v, n in vc[f_].items() if v != "not-computed"} == agg, f"verdict counts vs WALL_OPEN aggregate {f_}")
    check(vc["tetragonal"] == {"OPEN": 13, "WALL": 1, "ONE-SIDED": 0, "not-computed": len(tet_first) - 14}, "tetragonal verdict counts (PROGRAM_LEDGER 2026-09-04 14:10)")
    check(vc["hexagonal"] == {"OPEN": 102, "WALL": 40, "ONE-SIDED": 9, "not-computed": len(hex_first) - 151}, "hexagonal verdict counts (PROGRAM_LEDGER 2026-09-04 14:10)")
    check(vc["cubic"] == {"OPEN": 6, "WALL": 1, "ONE-SIDED": 0, "not-computed": len(cubic_first) - 7}, "cubic c1 verdict counts")
    print("open/wall verdicts per family:", vc)

    # --- v3: type-level Schmitt status, recounted from the screen files -------------------------
    ct = json.load(open(os.path.join(H, "collision_phase2_results.json")))
    check(ct["store_sha256"] == got, "collision_phase2_results store hash")
    tgt, same = {}, set()
    for p in ct["pairs"]:
        check(p["verdict"] in ("SAME TYPE", "DIFFERENT TYPE"), f"pair verdict {p['pair']}")
        tgt[p["target"]] = tgt.get(p["target"], 0) + 1
        if p["verdict"] == "SAME TYPE":
            same.add(p["target"])
    check(len(ct["pairs"]) == 27 and len(tgt) == 15 and set(tgt) <= set(menu), "tetragonal screen: 27 pairs / 15 menu-sighted targets")
    check(set(tgt) - same == g4p2 and len(same) == 1, "tetragonal SURVIVORs == the 14 certificates; 1 COLLISION")
    md_t = open(os.path.join(H, "COLLISION_PHASE2_RESULTS.md")).read()
    for k in tgt:
        want = "COLLISION" if k in same else "survives this screen"
        check(re.search(r"^- rank \d+ `%s`: %s" % (k, want), md_t, re.M) is not None, f"COLLISION_PHASE2_RESULTS.md summary line {k}")
    ch = json.load(open(os.path.join(H, "collision_phase2_hex_results.json")))
    check(ch["store_sha256_before"] == ch["store_sha256_after"] == got_hx and dict(ch["screen_counts"]) == cnt, "hex screen_counts == triage-table recount")
    md_h = open(os.path.join(H, "COLLISION_PHASE2_HEX_RESULTS.md")).read()
    check(f"Verdicts: SURVIVOR {cnt['SURVIVOR']}, COLLISION {cnt['COLLISION']}, UNRESOLVED {cnt['UNRESOLVED']} of {len(hmenu)} menu-sighted types" in md_h, "COLLISION_PHASE2_HEX_RESULTS.md section-1 counts line")
    check(set(ch["post"]) == set(shortlist["survivors_ranked"][:10]) and all(v.startswith("SURVIVES") for v in ch["post"].values()), "hex top-10 post-screen block")
    # --- v4: the store-side collision rule, re-implemented here (own code), hexagonal first then tetragonal ---
    from fractions import Fraction as Fr

    def rule(types_, tables_path, ids, point_field, mod1):
        tabs = json.load(open(tables_path))
        printed = {}
        for key, blk in tabs.items():
            if key == "_meta":
                continue
            for r in blk["rows"]:
                for g in blk["groups"]:
                    printed.setdefault((g, tuple(r["f"])), []).append((tuple(Fr(x) % 1 if mod1 else Fr(x) for x in r["pt"]), Fr(r["b"])))
        cells = {}
        for k, t in types_.items():
            for s in t["sightings"]:
                if s["pass"] == "P2":
                    cells[(s["group"], tuple(Fr(x) % 1 if mod1 else Fr(x) for x in s[point_field]), Fr(s["b"]))] = k
        out, unres_rows = {}, {}
        for k in ids:
            t = types_[k]
            f = tuple(t["f_vector"])
            scell = any(s["pass"] == "P2" for s in t["sightings"])
            same_ = False
            ur = []
            for g in sorted({s["group"] for s in t["sightings"]}):
                for pt_key, b_key in printed.get((g, f), []):
                    hit = cells.get((g, pt_key, b_key))
                    if hit is None:
                        ur.append((g, pt_key, b_key))
                    elif hit == k:
                        same_ = True
            out[k] = "COLLISION" if (scell or same_) else ("UNRESOLVED" if ur else "SURVIVOR")
            unres_rows[k] = ur
        return out, unres_rows
    hex_rule, _ = rule(TH, os.path.join(H, "schmitt_hexagonal_tables.json"), hmenu, "printed_point_Bpp", False)
    check({v: sum(1 for x in hex_rule.values() if x == v) for v in ("SURVIVOR", "COLLISION", "UNRESOLVED")} == cnt == {"SURVIVOR": 151, "COLLISION": 124, "UNRESOLVED": 13}
          and all(hex_rule[k] == verd[k] for k in hmenu), "own re-implementation of the store-side rule reproduces the hexagonal screen (151/124/13, per type)")
    tet_pure, tet_unres = rule(T2, os.path.join(H, "schmitt_tetragonal_tables.json"), menu, "point", True)
    tet_status = {}
    for k in menu:
        if tet_pure[k] == "COLLISION" or k in same:
            tet_status[k] = "COLLISION"
            continue
        done = {(p["group"], tuple(Fr(x) % 1 for x in p["point"]), Fr(p["b"])) for p in ct["pairs"] if p["target"] == k and p["verdict"] == "DIFFERENT TYPE"}
        tet_status[k] = "UNRESOLVED" if [u for u in tet_unres[k] if u not in done] else "SURVIVOR"
    ss_raw = open(os.path.join(H, "collision_phase2_tetragonal_storeside.json"), "rb").read()
    ss = json.loads(ss_raw)
    ss_md5 = hashlib.md5(ss_raw).hexdigest()
    check(ss["store_tetragonal_sha256"] == got and ss["store_hexagonal_sha256"] == got_hx, "storeside JSON store hashes")
    check(set(ss["verdicts"]) == set(menu) and all(ss["verdicts"][k]["status"] == tet_status[k] and ss["verdicts"][k]["status_pure_store_side_rule"] == tet_pure[k] for k in menu),
          "storeside JSON per-type verdicts == own re-derivation (pure rule and overlay)")
    tsc = {v: sum(1 for x in tet_status.values() if x == v) for v in ("SURVIVOR", "COLLISION", "UNRESOLVED")}
    check(tsc == dict(ss["counts_combined"]) == {"COLLISION": 177, "SURVIVOR": 121, "UNRESOLVED": 106}, f"tetragonal store-side counts {tsc}")
    check(sum(1 for k in menu if tet_pure[k] == "COLLISION") == 176 == sum(1 for k in menu if any(s["pass"] == "P2" for s in T2[k]["sightings"])), "176 S-cells, all COLLISION under the pure rule")
    check(all(tet_status[k] == ("COLLISION" if k in same else "SURVIVOR") for k in tgt), "the 15 shortlist statuses unchanged under the store-side rule + overlay")
    check(("md5 %s" % ss_md5) in md_t and S["schmitt_type_status_tetragonal_storeside"]["json_md5"] == ss_md5 and cat["inputs"]["collision_screen_tetragonal_storeside_v4"]["md5"] == ss_md5,
          "storeside JSON md5 == the addendum's and the catalog's stated value")
    check(dict(S["schmitt_type_status_tetragonal_storeside"]["counts_with_recomputed_pairs_overlaid"]) == tsc
          and dict(S["schmitt_type_status_tetragonal_storeside"]["counts_pure_store_side_rule"]) == {v: sum(1 for x in tet_pure.values() if x == v) for v in ("SURVIVOR", "COLLISION", "UNRESOLVED")}, "catalog summary storeside block")
    print("tetragonal store-side (own re-derivation): pure", {v: sum(1 for x in tet_pure.values() if x == v) for v in ("SURVIVOR", "COLLISION", "UNRESOLVED")}, "overlaid", tsc)
    # --- v5: the 106 UNRESOLVED settled by the recomputed rows (own keying, own code comparison) ---
    rr_raw = open(os.path.join(H, "collision_phase2_tetragonal_rows_recomputed.json"), "rb").read()
    rr = json.loads(rr_raw)
    rr_md5 = hashlib.md5(rr_raw).hexdigest()
    ov_raw = open(os.path.join(H, "collision_phase2_tetragonal_unresolved_overlay.json"), "rb").read()
    ov = json.loads(ov_raw)
    ov_md5 = hashlib.md5(ov_raw).hexdigest()
    check(ov["rows_file_md5"] == rr_md5 and ov["storeside_json_md5"] == ss_md5 == rr["storeside_json_md5"], "v5 overlay points at the rows file and the storeside JSON on disk")
    check(ov["store_sha256"] == got == rr["store_sha256_before"] == rr["store_sha256_after"], "v5 files ran on the verified store, unchanged")
    check(("md5 %s" % rr_md5) in md_t and ("md5 %s" % ov_md5) in md_t, "v5 JSON md5s stated in the COLLISION_PHASE2_RESULTS.md #154 addendum (or its CORRECTION paragraph)")
    # content equality with the #154 addendum's tables (own parsing): 62 row lines, 106 type lines
    sec154 = md_t.split("## Addendum 2026-09-04 (subagent #154")[1].split("\n### CORRECTION")[0]
    md_rows154 = {}
    for line_ in sec154.split("### Row-level results")[1].split("### Type-level verdicts")[0].splitlines():
        cells_ = [c.strip() for c in line_.strip().strip("|").split("|")]
        if len(cells_) == 18 and cells_[0].isdigit():
            mm = re.search(r"`([0-9a-f]{16})`", cells_[13])
            md_rows154[(int(cells_[1].split()[0]), Fr(cells_[2]), tuple(Fr(x) for x in cells_[3].strip("()").split(",")))] = (cells_[6].strip("*"), mm.group(1) if mm else None)
    md_types154 = {m.group(1): m.group(2) for m in re.finditer(r"^\| `([0-9a-f]{16})` \| .* \| \*\*(\w+)\*\* \|$", sec154.split("### Type-level verdicts")[1], re.M)}
    check(len(md_types154) == 106 and md_types154 == {k_: v_["status"] for k_, v_ in ov["verdicts"].items()}, "addendum type table == overlay JSON (106 verdicts)")
    check("wall_seconds" not in rr and not any("secs" in c for r in rr["rows"].values() for c in r["cells"]), "no timing field inside the hashed rows JSON")
    tabs_t = json.load(open(os.path.join(H, "schmitt_tetragonal_tables.json")))
    printed_rows_t = {}
    for key, blk in tabs_t.items():
        if key == "_meta":
            continue
        for r in blk["rows"]:
            for g in blk["groups"]:
                printed_rows_t[(g, Fr(r["b"]), tuple(Fr(x) for x in r["pt"]))] = (tuple(r["f"]), r["pdf_page"])
    rows_k = {}
    for r in rr["rows"].values():
        k5 = (r["group"], Fr(r["b"]), tuple(Fr(x) for x in r["pt_printed"]))
        check(k5 in printed_rows_t and printed_rows_t[k5][0] == tuple(r["f_printed"]) and printed_rows_t[k5][1] == r["pdf_page"], f"v5 row cites a digitized row {k5}")
        check(r["status"] == "REPRODUCED" and tuple(r["f"]) == tuple(r["f_printed"]) and hashlib.sha1(r["code"].encode()).hexdigest()[:16] == r["code_id"], f"v5 row reproduced / code id {k5}")
        check(all(c["documented"] is False or not c["ok"] or c["f"] != r["f_printed"] or c["code"] == r["code"] for c in r["cells"]), f"v5 documented conventions agree {k5}")
        check(not any((not c["documented"]) and c["ok"] and c["f"] == r["f_printed"] for c in r["cells"]), f"v5 other reading never reproduces f {k5}")
        rows_k[k5] = r
    check(len(rows_k) == 62 == rr["n_rows"], "62 recomputed rows")
    check(len(md_rows154) == 62 and set(md_rows154) == set(rows_k) and all(md_rows154[k5] == ("REPRODUCED", rows_k[k5]["code_id"]) for k5 in rows_k), "addendum row table == rows JSON (62 rows: status, code id)")
    status5 = dict(tet_status)
    n5 = {"COLLISION": 0, "SURVIVOR": 0, "UNRESOLVED": 0}
    unres4 = [k for k in menu if tet_status[k] == "UNRESOLVED"]
    check(len(unres4) == 106 and set(unres4) == set(ov["verdicts"]), "overlay covers exactly the 106 v4-UNRESOLVED types")
    for k in unres4:
        hung = [(g, pt_key, b_key) for (g, pt_key, b_key) in tet_unres[k]]
        verd5 = []
        for g, pt_key, b_key in hung:
            m = [r for (g2, b2, pt2), r in rows_k.items() if g2 == g and b2 == b_key and tuple(x % 1 for x in pt2) == pt_key]
            check(len(m) == 1, f"v5 exactly one recomputed row for {k} {g} {b_key}")
            verd5.append("SAME TYPE" if m and m[0]["code"] == T2[k]["canon_code"] else "DIFFERENT TYPE")
        status5[k] = "COLLISION" if "SAME TYPE" in verd5 else "SURVIVOR"
        n5[status5[k]] += 1
        check(ov["verdicts"][k]["status"] == status5[k] and [x["verdict"] for x in ov["verdicts"][k]["rows"]] == verd5, f"v5 overlay verdict {k}")
    check(n5 == dict(ov["counts_106"]) == {"COLLISION": 24, "SURVIVOR": 82, "UNRESOLVED": 0} or (n5["UNRESOLVED"] == 0 and n5 == {**dict(ov["counts_106"]), "UNRESOLVED": 0}), f"the 106 -> {n5}")
    check(n5 == {"COLLISION": 24, "SURVIVOR": 82, "UNRESOLVED": 0}, "the 106 -> 24 COLLISION / 82 SURVIVOR / 0 UNRESOLVED")
    tsc5 = {v: sum(1 for x in status5.values() if x == v) for v in ("SURVIVOR", "COLLISION", "UNRESOLVED")}
    check(tsc5 == dict(ov["counts_404_after_v5"]) == {"COLLISION": 201, "SURVIVOR": 203, "UNRESOLVED": 0}, f"tetragonal v5 counts {tsc5}")
    check(all(status5[k] == ("COLLISION" if k in same else "SURVIVOR") for k in tgt) and not (set(tgt) & set(unres4)), "the 15 shortlist statuses unchanged by v5")
    RC = S["schmitt_type_status_tetragonal_unresolved_recomputed"]
    check(RC["overlay_json_md5"] == ov_md5 and RC["rows_json_md5"] == rr_md5 and cat["inputs"]["collision_screen_tetragonal_rows_recomputed_v5"]["overlay_md5"] == ov_md5
          and cat["inputs"]["collision_screen_tetragonal_rows_recomputed_v5"]["rows_md5"] == rr_md5, "v5 md5s in the catalog summary block and inputs")
    check(dict(RC["counts_106"]) == {k_: v_ for k_, v_ in n5.items() if v_} and dict(RC["counts_404_after_v5"]) == tsc5 and RC["still_unresolved"] == []
          and dict(RC["transitions_v4_to_v5"]) == {"COLLISION -> COLLISION": 177, "SURVIVOR -> SURVIVOR": 121, "UNRESOLVED -> COLLISION": 24, "UNRESOLVED -> SURVIVOR": 82}, "catalog summary v5 block")
    print("tetragonal v5 (own re-derivation): the 106 ->", n5, "; 404 ->", tsc5)
    STAT = ("SURVIVOR", "COLLISION", "UNRESOLVED", "printed-only", "not-screened")
    exp_s = {}
    for k in cubic_first:
        exp_s[k] = "not-screened"
    for k in tet_first:
        exp_s[k] = "printed-only" if T2[k]["schmitt_printed_only"] else status5[k]
    for k in hex_first:
        exp_s[k] = "printed-only" if TH[k]["schmitt_printed_only"] else verd[k]
    for k, r in crow.items():
        check(r["schmitt_type_status"] == exp_s[k], f"schmitt_type_status {k}")
        if k in tgt:
            check(f"rank {ct['pairs'][[p['target'] for p in ct['pairs']].index(k)]['rank']} of 15" in r["schmitt_type_status_source"], f"schmitt_type_status_source rank {k}")
        elif k in menu:
            check("addendum 2026-09-04" in r["schmitt_type_status_source"], f"schmitt_type_status_source v4 pointer {k}")
            if k in unres4:
                check("[v5]" in r["schmitt_type_status_source"] and "subagent #154" in r["schmitt_type_status_source"] and rr_md5 in r["schmitt_type_status_source"], f"schmitt_type_status_source v5 pointer {k}")
    sc = {f_: {s: 0 for s in STAT} for f_ in vc}
    for k in TH:
        sc[fam_of[k]][exp_s[k]] += 1
    for f_ in sc:
        check(dict(S["schmitt_type_status_counts"][f_]) == sc[f_], f"schmitt_type_status_counts {f_}")
    check(sc["tetragonal"] == {"SURVIVOR": 203, "COLLISION": 201, "UNRESOLVED": 0, "printed-only": len(sonly), "not-screened": 0}, "tetragonal status counts (v5)")
    check(sc["hexagonal"] == {"SURVIVOR": cnt["SURVIVOR"], "COLLISION": cnt["COLLISION"], "UNRESOLVED": cnt["UNRESOLVED"], "printed-only": len(hsonly), "not-screened": 0}, "hexagonal status counts")
    check(sc["cubic"] == {"SURVIVOR": 0, "COLLISION": 0, "UNRESOLVED": 0, "printed-only": 0, "not-screened": len(cubic_first)}, "cubic status counts")
    print("type status per family:", sc)
    for f_ in vc:
        xt = {v: {s: 0 for s in STAT} for v in VERD}
        for k in TH:
            if fam_of[k] == f_:
                xt[exp_v[k]][exp_s[k]] += 1
        got_xt = {v: dict(S["open_wall_x_schmitt_type_status"][f_][v]) for v in VERD}
        check(got_xt == xt, f"cross-tab {f_}")
        print(f"cross-tab {f_}:", {v: {s: n for s, n in d.items() if n} for v, d in xt.items()})

    # --- v3: naming pool = certified (files on disk) AND OPEN (verdict files) AND unnamed --------
    pub = os.path.join(os.path.dirname(D), "publication")
    named8 = {f_[:8] for f_ in os.listdir(pub) if re.fullmatch(r"[0-9a-f]{8}_.+", f_) and os.path.isdir(os.path.join(pub, f_))}
    check(len(named8) == 7, "7 publication folders")
    certified = acc_cubic | cert_tet | cert_hex
    for f_ in vc:
        members = [k for k in hx["type_order"] if fam_of[k] == f_ and k in certified and exp_v[k] == "OPEN" and crow[k]["name"] is None]
        if f_ != "cubic":
            all_cert_open = [k for k in hx["type_order"] if fam_of[k] == f_ and k in certified and exp_v[k] == "OPEN"]
            check(members == all_cert_open and not any(k[:8] in named8 or TH[k].get("seeded") for k in all_cert_open), f"pool = every certified OPEN cell, none named by folder or seed {f_}")
            check(all(exp_s[k] == "SURVIVOR" for k in members), f"pool members SURVIVOR {f_}")
        else:
            check(all(crow[k]["name"] is not None for k in hx["type_order"] if fam_of[k] == "cubic" and k in certified and exp_v[k] == "OPEN"), "every OPEN accepted-cubic cell carries a name or marker")
        P_ = S["naming_pool"][f_]
        check(P_["n_certified_open_unnamed"] == len(members) and P_["type_ids"] == members and P_["catalog_ids"] == [crow[k]["catalog_id"] for k in members], f"naming pool {f_}")
        check(P_["n_certified"] == sum(1 for k in TH if fam_of[k] == f_ and k in certified) and P_["n_certified_open"] == sum(1 for k in TH if fam_of[k] == f_ and k in certified and exp_v[k] == "OPEN")
              and P_["n_certified_not_computed"] == sum(1 for k in TH if fam_of[k] == f_ and k in certified and exp_v[k] == "not-computed"), f"naming pool sub-counts {f_}")
    check(len(S["naming_pool"]["tetragonal"]["type_ids"]) == 13 and len(S["naming_pool"]["hexagonal"]["type_ids"]) == 102 and len(S["naming_pool"]["cubic"]["type_ids"]) == 0,
          "naming pool 13 tetragonal + 102 hexagonal (PROGRAM_LEDGER 2026-09-04 14:10)")
    print("naming pool (certified AND OPEN AND unnamed):", {f_: len(S["naming_pool"][f_]["type_ids"]) for f_ in vc})

    # --- named records unchanged ---------------------------------------------------------
    named = {k for k, r in crow.items() if r["name_status"].startswith("named")}
    check(named == {"8cf50403cf88c455", "2de0a21129cabe90"}, "named = Satchelhedron + Ordenhedron")
    check(crow["8cf50403cf88c455"]["f_vector"] == [16, 25, 11] and crow["8cf50403cf88c455"]["aut_order"] == 4
          and crow["8cf50403cf88c455"]["witness_group"] == 220 and crow["8cf50403cf88c455"]["witness_point"] == ["0", "0", "1/4"], "Satchelhedron record")
    check(crow["2de0a21129cabe90"]["f_vector"] == [20, 33, 15] and crow["2de0a21129cabe90"]["aut_order"] == 1
          and crow["2de0a21129cabe90"]["witness_group"] == 201 and crow["2de0a21129cabe90"]["witness_point"] == ["1/8", "1/6", "5/12"], "Ordenhedron record")
    check(not any(r["name"] for k, r in crow.items() if k in hex_first), "no hexagonal-family type is named")

    print(f"\n{len(fails)} failures")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
