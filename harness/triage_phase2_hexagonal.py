#!/usr/bin/env python
"""triage_phase2_hexagonal.py — deterministic triage of the Phase-2 batch-2
(hexagonal family, IT 143-194) MENU-sighted types into a G4 shortlist, plus the
store-side COLLISION SCREEN at Schmitt's printed points.

Inputs : phase2_hexagonal_types.json  (batch-2 store; regenerated from the .gz if absent; sha256
                                       verified against phase2_hexagonal_types.SHA256SUMS)
         schmitt_hexagonal_tables.json (digitization, text layer + visual cross-read, 2026-09-04)
Outputs: TRIAGE_PHASE2_HEX_RESULT.md, triage_phase2_hex_shortlist.json (worklist for the
         collision confirmation script collision_phase2_hex_check.py)
Model  : triage_phase2.py (batch 1; same features, weights and report layout). Differences: the
         prior store is cubic + tetragonal (891) and the Schmitt rows carry printed points in his
         B'' basis (the P2 sighting stores the printed point as printed_point_Bpp, so rows and
         sightings are keyed on the printed point verbatim, plus the conversion used).

SCHMITT FLAG (per sighted group, f-vector level, G5 wording) exactly as batch 1:
    P / Pb / A, resolution same / other / unres per printed row with the same (group, f), S-cell.
COLLISION SCREEN (task step 5, from the store): for every menu-sighted hexagonal type and every
sighted group, the type SURVIVES in that group iff its f-vector appears in no printed row of the
group, or every printed row with that (group, f-vector) reproduced (pass P2) as a DIFFERENT stored
type; a row that did not reproduce (quarantined) leaves the pair UNRESOLVED. A type is a
SURVIVOR iff it survives in every sighted group (no SAME anywhere, no unresolved pair);
SAME anywhere => reframe (first-realization, kill criterion). Survivors are ranked by the
triage score; the top-10 are re-confirmed by recomputation in collision_phase2_hex_check.py.

LANGUAGE: "not matched against the records checked as of 2026-09-04" ONLY — no novelty claims.
Deterministic: no timestamps in the body, stable sort keys, byte-identical across re-runs.
"""

import gzip
import hashlib
import json
import math
import os
import shutil
from collections import Counter, defaultdict
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.join(HERE, "phase2_hexagonal_types.json")
STORE_GZ = os.path.join(HERE, "phase2_hexagonal_types.json.gz")
STORE_SUMS = os.path.join(HERE, "phase2_hexagonal_types.SHA256SUMS")
DIGITIZED = os.path.join(HERE, "schmitt_hexagonal_tables.json")
OUT = os.path.join(HERE, "TRIAGE_PHASE2_HEX_RESULT.md")
OUT_JSON = os.path.join(HERE, "triage_phase2_hex_shortlist.json")

RUN_DATE = "2026-09-04"
SNAPSHOT = "2026-09-04"
SYSTEM = "hexagonal (phase 2 batch 2)"
TOP_N = 15
MAX_FACETS_KILL = 38
MENU_PASSES = {"P1", "P3", "P4", "P5"}

# Ranking weights — identical to triage_phase2.py (batch 1), stated for reproducibility.
W_FACET = 3.0
B_F_GE20 = 10.0
W_AUT = 4.0
W_STAB = 2.0
W_PNOV = 3.0
W_SIGHT = 1.5
W_SPECIALPOS = 1.5
W_VERT = 0.1
W_NB = 2.0
W_NGROUP = 1.0
B_SCHMITT_ABSENT = 5.0
PEN_THIN = -4.0
PEN_SCELL = -25.0


def pfmt(p):
    c = Counter(p)
    return " ".join(f"{g}^{c[g]}" for g in sorted(c))


def log2(x):
    return math.log2(x) if x > 0 else 0.0


def frac_key(strs):
    return tuple(Fraction(s) for s in strs)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_store():
    regenerated = False
    if not os.path.exists(STORE):
        with gzip.open(STORE_GZ, "rb") as src, open(STORE, "wb") as dst:
            shutil.copyfileobj(src, dst)
        regenerated = True
    expected = None
    if os.path.exists(STORE_SUMS):
        for line in open(STORE_SUMS):
            parts = line.split()
            if parts and parts[0].endswith("phase2_hexagonal_types.json") and "sha256" in parts:
                expected = parts[parts.index("sha256") + 1]
    actual = sha256_file(STORE)
    return regenerated, (expected is not None and actual == expected), actual, expected


def load_schmitt():
    dig = json.load(open(DIGITIZED))
    rows = []
    for key, blk in dig.items():
        if key == "_meta":
            continue
        for r in blk["rows"]:
            rows.append({"groups": list(blk["groups"]), "f": tuple(r["f"]), "b": r["b"],
                         "pt": list(r["pt"]), "pdf_page": r.get("pdf_page")})
    src = "schmitt_hexagonal_tables.json (text layer + visual cross-read of 153 rows, 2026-09-04)"
    note = ("text-layer parse cross-read visually on 153 of 958 rows (0 discrepancies), every row "
            "re-derived computationally in pass P2 (f-vector reproduced or quarantined), NOT "
            "independently re-keyed (G5 duty still owed) — flags provisional")
    return rows, src, note, dig["_meta"]["n_rows"]


def main():
    regenerated, sha_ok, sha_actual, sha_expected = ensure_store()
    store = json.load(open(STORE))
    types = store["types"]
    assert store["complete"], "store is not complete (budget stop) — resume the sweep first"

    schmitt_rows, schmitt_src, schmitt_note, n_meta_rows = load_schmitt()

    lines_sanity, kill_hits, problems = [], [], []

    lines_sanity.append(f"- phase2_hexagonal_types.json sha256 {sha_actual}: "
                        + ("MATCHES phase2_hexagonal_types.SHA256SUMS" if sha_ok
                           else f"MISMATCH/absent (expected {sha_expected})")
                        + (" [regenerated from .gz]" if regenerated else " [raw file present]"))
    if not sha_ok:
        problems.append("SHA256 MISMATCH on phase2_hexagonal_types.json")
    by_group_f = defaultdict(set)
    by_group_f_b = defaultdict(set)
    rows_by_group_f = defaultdict(list)
    n_euler_bad = 0
    for r in schmitt_rows:
        V, E, Fc = r["f"]
        if V - E + Fc != 2:
            n_euler_bad += 1
        for g in r["groups"]:
            by_group_f[g].add(r["f"])
            by_group_f_b[g].add((r["f"], Fraction(r["b"])))
            rows_by_group_f[(g, r["f"])].append(r)
    if n_euler_bad:
        problems.append(f"SCHMITT ROWS EULER FAIL: {n_euler_bad} rows")
    lines_sanity.append(f"- Schmitt hexagonal-family rows: {len(schmitt_rows)} rows over {len(by_group_f)} groups from "
                        f"{schmitt_src}; Euler on every row: {'PASS' if not n_euler_bad else 'FAIL'}; row count vs "
                        f"_meta {n_meta_rows}: {'MATCH' if len(schmitt_rows) == n_meta_rows else 'DISCREPANCY'}")

    for tid in sorted(types):
        t = types[tid]
        V, E, Fc = t["f_vector"]
        if V - E + Fc != 2:
            problems.append(f"EULER FAIL {tid}")
        if Fc > MAX_FACETS_KILL:
            kill_hits.append(f"KILL CRITERION {tid}: F={Fc} > {MAX_FACETS_KILL}")
        if len(t["p_vector"]) != Fc:
            problems.append(f"P-VECTOR LENGTH FAIL {tid}")
        if sum(t["p_vector"]) != 2 * E:
            problems.append(f"P-VECTOR EDGE SUM FAIL {tid}")
        for s in t["sightings"]:
            if t["aut_order"] % s["stabilizer_order"] != 0:
                problems.append(f"STAB|AUT FAIL {tid}: stab {s['stabilizer_order']} vs aut {t['aut_order']}")

    prior = sorted(tid for tid in types if types[tid]["first_sighting_system"] != SYSTEM)
    hexa = sorted(tid for tid in types if types[tid]["first_sighting_system"] == SYSTEM)
    sonly = sorted(tid for tid in hexa if types[tid]["schmitt_printed_only"])
    menu = sorted(tid for tid in hexa if not types[tid]["schmitt_printed_only"])
    for tid in menu:
        if not any(s["pass"] in MENU_PASSES for s in types[tid]["sightings"]):
            problems.append(f"MENU FLAG FAIL {tid}")
    for tid in sonly:
        if any(s["pass"] in MENU_PASSES for s in types[tid]["sightings"]):
            problems.append(f"S-ONLY FLAG FAIL {tid}")
    n_sight_total = sum(len(t["sightings"]) for t in types.values())
    lines_sanity.append(f"- Euler V-E+F=2 on all {len(types)} stored types: "
                        + ("ALL PASS" if not any(p.startswith('EULER') for p in problems) else "FAIL"))
    lines_sanity.append(f"- p-vector consistency (|p|=F, sum p = 2E) on all {len(types)} types: "
                        + ("ALL PASS" if not any(p.startswith('P-VECTOR') for p in problems) else "FAIL"))
    lines_sanity.append(f"- site-stabilizer divides aut on every stored sighting ({n_sight_total} sightings): "
                        + ("ALL PASS" if not any(p.startswith('STAB') for p in problems) else "FAIL"))
    maxF_store = max(t["f_vector"][2] for t in types.values())
    maxF_hex = max(types[t]["f_vector"][2] for t in hexa) if hexa else 0
    maxF_menu = max(types[t]["f_vector"][2] for t in menu) if menu else 0
    lines_sanity.append(f"- kill criterion (>{MAX_FACETS_KILL} facets): max stored facet count = {maxF_store} "
                        f"(hexagonal types: {maxF_hex}; from our menu: {maxF_menu}): "
                        + ("NO HITS" if not kill_hits else "HITS - QUARANTINE"))
    claim = (store["n_types_prior_store"], store["n_types_hexagonal_new"],
             store["n_types_hexagonal_menu_sighted"], store["n_types_hexagonal_schmitt_printed_only"])
    counts_ok = (len(prior), len(hexa), len(menu), len(sonly)) == claim
    lines_sanity.append(f"- recount: {len(prior)} prior-store + {len(hexa)} hexagonal = {len(types)} types; hexagonal "
                        f"split {len(menu)} menu-sighted + {len(sonly)} Schmitt-printed-only; store fields say "
                        f"{'/'.join(map(str, claim))}: " + ("MATCH" if counts_ok else "DISCREPANCY - reported, not forced"))
    prior_by_sys = Counter(types[t]["first_sighting_system"] for t in prior)
    lines_sanity.append("- prior store by system: " + ", ".join(f"{k}: {v}" for k, v in sorted(prior_by_sys.items())))
    lines_sanity.append(f"- menu/S-only flags consistent with stored pass labels for all {len(hexa)} hexagonal types: "
                        + ("PASS" if not any('FLAG FAIL' in p for p in problems) else "FAIL"))
    q = store["quarantines"]
    qc = Counter(x["reason"] for x in q)
    lines_sanity.append(f"- quarantines in the store: {len(q)} (" + ", ".join(f"{k}: {v}" for k, v in sorted(qc.items())) + ")"
                        + f"; (group,b) congruence purges: {len(store['group_b_quarantined'])}; Schmitt screen "
                        + json.dumps(store["schmitt_screen"], sort_keys=True))

    # --- P2 map: (group, printed point as printed, b) -> type id -----------------------------------
    p2_map = {}
    for tid, t in types.items():
        for s in t["sightings"]:
            if s["pass"] == "P2":
                p2_map[(s["group"], frac_key(s["printed_point_Bpp"]), Fraction(s["b"]))] = tid
    n_rows_resolved = sum(1 for r in schmitt_rows for g in r["groups"]
                          if (g, frac_key(r["pt"]), Fraction(r["b"])) in p2_map)
    n_row_evals = sum(len(r["groups"]) for r in schmitt_rows)
    lines_sanity.append(f"- P2 sightings keyed by (group, printed point, b): {len(p2_map)} stored cells; printed "
                        f"(row x group) evaluations resolved to a stored type: {n_rows_resolved} of {n_row_evals}")

    sym = {}
    for t in types.values():
        for s in t["sightings"]:
            sym[s["group"]] = s["group_symbol"]
    b_coarse = set(Fraction(b) for b in store["scan"]["b_coarse"])
    b_schmitt_used = set(Fraction(b) for b in store["scan"]["schmitt_b_used"])
    n_printed_b = len(store["scan"]["schmitt_b_all_digitized"])
    n_printed_b_swept = sum(1 for d in store["scan"]["schmitt_b_all_digitized"]
                            if Fraction(d["b"]) in b_coarse or Fraction(d["b"]) in b_schmitt_used)

    # --- Features + score -----------------------------------------------------------------------
    rows = []
    for tid in menu:
        t = types[tid]
        V, E, Fc = t["f_vector"]
        aut = t["aut_order"]
        sight_all = t["sightings"]
        sight_menu = [s for s in sight_all if s["pass"] in MENU_PASSES]
        sight_p2 = [s for s in sight_all if s["pass"] == "P2"]
        groups_all = sorted({s["group"] for s in sight_all})
        groups_menu = sorted({s["group"] for s in sight_menu})
        max_stab = max(s["stabilizer_order"] for s in sight_menu)
        min_dim = min(s["stratum_dim"] for s in sight_menu)
        n_sight = len(sight_menu)
        nov_gons = sorted({g for g in t["p_vector"] if (g % 2 == 1 and g >= 5) or g >= 7})
        fwm = sight_menu[0]
        bset = sorted({Fraction(s["b"]) for s in sight_menu})
        n_b = len(bset)
        orbit_b = defaultdict(set)
        for s in sight_menu:
            orbit_b[(s["group"], tuple(Fraction(x) % 1 for x in s["point"]))].add(Fraction(s["b"]))
        orbit_bmax = max(len(v) for v in orbit_b.values())
        passes = {s["pass"] for s in sight_menu}
        thin_reasons = []
        if n_b == 1:
            thin_reasons.append("1b")
        if passes == {"P5"}:
            thin_reasons.append("P5-only")
        if passes == {"P3"}:
            thin_reasons.append("P3-only")
        thin = bool(thin_reasons)
        ow = "open-likely" if orbit_bmax >= 3 else ("wall-suspect" if n_b == 1 else "indeterminate")
        b_kinds = []
        if any(b in b_coarse for b in bset):
            b_kinds.append("coarse")
        if any(b in b_schmitt_used for b in bset):
            b_kinds.append("schmittb")
        if any((b not in b_coarse and b not in b_schmitt_used) for b in bset):
            b_kinds.append("bisect")
        flags, resolution, collision = {}, {}, {}
        for g in groups_all:
            tbl = by_group_f.get(g)
            if tbl is None:
                flags[g] = "U"
                collision[g] = "no-table"
                continue
            if (V, E, Fc) not in tbl:
                flags[g] = "A"
                collision[g] = "absent"
                continue
            my_b = {Fraction(s["b"]) for s in sight_all if s["group"] == g}
            flags[g] = "Pb" if any(((V, E, Fc), b) in by_group_f_b[g] for b in my_b) else "P"
            res = Counter()
            for r in rows_by_group_f[(g, (V, E, Fc))]:
                hit = p2_map.get((g, frac_key(r["pt"]), Fraction(r["b"])))
                if hit is None:
                    res["unres"] += 1
                elif hit == tid:
                    res["same"] += 1
                else:
                    res["other"] += 1
            resolution[g] = res
            collision[g] = ("SAME" if res["same"] else ("unresolved" if res["unres"] else "different"))
        if all(v == "A" for v in flags.values()):
            schmitt_class = "ABSENT-all"
        elif any(v in ("P", "Pb") for v in flags.values()):
            schmitt_class = "present"
        else:
            schmitt_class = "UNKNOWN"
        scell = len(sight_p2) > 0
        if any(v == "SAME" for v in collision.values()) or scell:
            verdict = "COLLISION"
        elif any(v == "unresolved" for v in collision.values()):
            verdict = "UNRESOLVED"
        else:
            verdict = "SURVIVOR"
        score = (W_FACET * Fc + (B_F_GE20 if Fc >= 20 else 0.0) + W_AUT * log2(aut) + W_STAB * log2(max_stab)
                 + W_PNOV * min(3, len(nov_gons)) + W_SIGHT * log2(1 + n_sight) + W_SPECIALPOS * (3 - min_dim)
                 + W_VERT * V + W_NB * log2(n_b) + W_NGROUP * log2(len(groups_all))
                 + (B_SCHMITT_ABSENT if schmitt_class == "ABSENT-all" else 0.0)
                 + (PEN_THIN if thin else 0.0) + (PEN_SCELL if scell else 0.0))
        rows.append({
            "id": tid, "V": V, "E": E, "F": Fc, "aut": aut, "p": pfmt(t["p_vector"]),
            "groups": groups_all, "groups_menu": groups_menu, "max_stab": max_stab, "min_dim": min_dim,
            "n_sight": n_sight, "n_p2": len(sight_p2), "nov": nov_gons, "fwm": fwm,
            "bset": bset, "n_b": n_b, "orbit_bmax": orbit_bmax, "b_kinds": b_kinds,
            "thin": thin, "thin_reasons": thin_reasons, "ow": ow,
            "flags": flags, "res": resolution, "collision": collision, "verdict": verdict,
            "schmitt": schmitt_class, "scell": scell, "score": round(score, 2),
        })

    rows.sort(key=lambda r: (-r["score"], -r["F"], -r["aut"], r["id"]))
    rank_of = {r["id"]: i for i, r in enumerate(rows, 1)}
    by_witness = Counter(r["fwm"]["group"] for r in rows)
    by_sighted = Counter(g for r in rows for g in r["groups"])
    by_sighted_menu = Counter(g for r in rows for g in r["groups_menu"])
    by_scell = Counter(g for r in rows if r["scell"] for g in r["groups"])
    by_absent = Counter(g for r in rows for g, v in r["flags"].items() if v == "A")
    absent_all = [r for r in rows if r["schmitt"] == "ABSENT-all"]
    thin_rows = [r for r in rows if r["thin"]]
    scell_rows = [r for r in rows if r["scell"]]
    ow_counts = Counter(r["ow"] for r in rows)
    nb_hist = Counter(r["n_b"] for r in rows)
    verdicts = Counter(r["verdict"] for r in rows)
    survivors = [r for r in rows if r["verdict"] == "SURVIVOR"]
    shortlist = [r for r in rows if not r["scell"]][:TOP_N]

    def fmt_b(bs, cap=6):
        s = [str(b) for b in bs]
        return ", ".join(s[:cap]) + (f", ... (+{len(s) - cap})" if len(s) > cap else "")

    def fmt_flags(r):
        out = []
        for g in r["groups"]:
            v = r["flags"][g]
            if v in ("P", "Pb") and r["res"].get(g):
                res = r["res"][g]
                v += "[" + "/".join(f"{k}{res[k]}" for k in ("same", "other", "unres") if res[k]) + "]"
            out.append(f"{g}:{v}")
        return " ".join(out)

    def why(r):
        bits = [f"{r['F']} facets"]
        if r["aut"] > 1:
            bits.append(f"aut {r['aut']}")
        if r["nov"]:
            bits.append("faces incl. " + ",".join(f"{g}-gon" for g in r["nov"]))
        if r["min_dim"] <= 1:
            bits.append(f"special-position stratum (dim {r['min_dim']}, stab {r['max_stab']})")
        elif r["min_dim"] == 2:
            bits.append("plane stratum only")
        else:
            bits.append("general position only")
        bits.append(f"{r['n_b']} b-ratio(s) [{', '.join(r['b_kinds'])}], orbit-b max {r['orbit_bmax']} -> {r['ow']}")
        bits.append(f"{len(r['groups'])} group(s), {r['n_sight']} menu sighting(s)")
        if r["thin"]:
            bits.append("METRIC-THIN (" + ",".join(r["thin_reasons"]) + ")")
        if r["schmitt"] == "ABSENT-all":
            bits.append("Schmitt f-vec ABSENT in every sighted group's printed table")
        else:
            det = [f"{g}:{r['collision'][g]}" for g in r["groups"] if r["flags"][g] in ("P", "Pb")]
            bits.append("Schmitt f-vec present (" + ", ".join(det) + ")")
        bits.append("collision verdict " + r["verdict"])
        return "; ".join(bits)

    out = []
    out.append(f"# TRIAGE result — Phase-2 batch 2 (hexagonal family) MENU-sighted types -> G4 shortlist + collision screen ({RUN_DATE})\n")
    out.append("Script: `triage_phase2_hexagonal.py` (deterministic; model `triage_phase2.py`). Store: "
               "`phase2_hexagonal_types.json` (Phase-2 batch 2, run 2026-09-04; sha256 verified). Schmitt rows: "
               + schmitt_src + ". Gates: `../ANCHORS.md` G4 (NOT run here), G5 (NOT run here), KILL CRITERIA.\n")
    out.append(f"**LANGUAGE (G5): every type below is \"not matched against the records checked as of {SNAPSHOT}\". "
               "No novelty claim. The Schmitt column is f-vector-level evidence from his printed Sec. 2.2.3-2.2.4 tables "
               "(a grid SAMPLING, not an enumeration): \"A\" = absent there, \"P\"/\"Pb\" = present (same f-vector does "
               "NOT mean same type), \"S-cell\" = the type IS one of his printed cells (reproduced at his generating point "
               "in pass P2) => excluded from the shortlist by the kill criterion \"Schmitt-contains-candidate => reframe "
               "to first-realization\". COLLISION VERDICT per type: SURVIVOR = in every sighted group the f-vector is "
               "absent from the printed table or every printed row with that (group, f) reproduced as a DIFFERENT stored "
               "type; COLLISION = the type is one of his printed cells (S-cell / SAME); UNRESOLVED = some printed row with "
               "that (group, f) did not reproduce (quarantined) so no type-level statement is possible there.**\n")
    out.append(f"**SOURCE STATUS of the Schmitt flags: {schmitt_note}.**\n")
    out.append("## Sanity duties\n")
    out.extend(lines_sanity)
    if kill_hits:
        out.append("\n### KILL-CRITERION HITS\n")
        out.extend(f"- {k}" for k in kill_hits)
    if problems:
        out.append("\n### PROBLEMS (reported, not forced)\n")
        out.extend(f"- {p}" for p in problems)
    out.append("")
    out.append(f"## Headline counts (the {len(rows)} menu-sighted hexagonal types)\n")
    out.append(f"- Ranked: {len(rows)}. S-cell: {len(scell_rows)}; menu-only (never at a printed point): {len(rows) - len(scell_rows)}.")
    out.append(f"- Schmitt f-vector flag: ABSENT-all {len(absent_all)}; present (P/Pb in >= 1 sighted group) "
               f"{sum(1 for r in rows if r['schmitt'] == 'present')}; unknown {sum(1 for r in rows if r['schmitt'] == 'UNKNOWN')}.")
    out.append(f"- COLLISION SCREEN (store-side, all {len(rows)} types): SURVIVOR {verdicts['SURVIVOR']}, "
               f"COLLISION {verdicts['COLLISION']}, UNRESOLVED {verdicts['UNRESOLVED']}.")
    out.append(f"- Open/wall label (label only, no perturbation runs): open-likely {ow_counts['open-likely']}, "
               f"indeterminate {ow_counts['indeterminate']}, wall-suspect {ow_counts['wall-suspect']}.")
    out.append(f"- Metric-thin: {len(thin_rows)} (reasons: " + ", ".join(
        f"{k} {v}" for k, v in sorted(Counter(x for r in thin_rows for x in r['thin_reasons']).items())) + ").")
    out.append("- Distinct b-ratio histogram (#b: types): " + ", ".join(f"{k}: {v}" for k, v in sorted(nb_hist.items())) + ".")
    out.append(f"- Facet count: max {max(r['F'] for r in rows)}; F >= 20: {sum(1 for r in rows if r['F'] >= 20)}; "
               f"aut > 1: {sum(1 for r in rows if r['aut'] > 1)}; fixed-point witness (dim 0): "
               f"{sum(1 for r in rows if r['min_dim'] == 0)}; line (dim 1): {sum(1 for r in rows if r['min_dim'] == 1)}; "
               f"plane (dim 2): {sum(1 for r in rows if r['min_dim'] == 2)}; general only (dim 3): "
               f"{sum(1 for r in rows if r['min_dim'] == 3)}.")
    out.append(f"- Printed b-ratios swept by our menu: {n_printed_b_swept} of {n_printed_b} distinct printed values.")
    out.append("")
    out.append(f"## TOP-{TOP_N} G4 SHORTLIST (S-cell types excluded; rank in the full table in brackets)\n")
    for i, r in enumerate(shortlist, 1):
        fwp = "(" + ", ".join(r["fwm"]["point"]) + ")"
        out.append(f"{i}. `{r['id']}` [#{rank_of[r['id']]}] — **{r['fwm']['group']} {sym[r['fwm']['group']]}** at {fwp} "
                   f"b={r['fwm']['b']}, f=({r['V']}, {r['E']}, {r['F']}), p={r['p']}, aut={r['aut']}, "
                   f"b-ratios: {fmt_b(r['bset'])}, Schmitt {fmt_flags(r)} [score {r['score']}]  \n   {why(r)}")
    out.append("")
    out.append(f"## COLLISION-SCREEN SURVIVORS ({len(survivors)} of {len(rows)}; top 10 shown, all in the full table)\n")
    out.append("| # | id | witness group | c/a (b) | f-vector | p-vector | aut | #b | O/W label | Schmitt per group |")
    out.append("|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(survivors[:10], 1):
        out.append(f"| {i} | `{r['id']}` | {r['fwm']['group']} {sym[r['fwm']['group']]} ({', '.join(r['fwm']['point'])}) | "
                   f"{r['fwm']['b']} | ({r['V']}, {r['E']}, {r['F']}) | {r['p']} | {r['aut']} | {r['n_b']} | {r['ow']} | {fmt_flags(r)} |")
    out.append("")
    out.append("## Collision worklist for the top-10 survivors (recomputed independently by collision_phase2_hex_check.py)\n")
    out.append("Every printed row of a sighted group with the survivor's f-vector; P2 outcome from the store "
               "(`other` = a different stored type, id given; `unres` cannot occur for a survivor by definition).\n")
    out.append("| # | id | group | f-vector | printed b | printed point (B'') | PDF p. | P2 outcome |")
    out.append("|---|---|---|---|---|---|---|---|")
    worklist = []
    for i, r in enumerate(survivors[:10], 1):
        for g in r["groups"]:
            if r["flags"][g] not in ("P", "Pb"):
                continue
            for pr in sorted(rows_by_group_f[(g, (r["V"], r["E"], r["F"]))], key=lambda x: (Fraction(x["b"]), x["pt"])):
                hit = p2_map.get((g, frac_key(pr["pt"]), Fraction(pr["b"])))
                outcome = "unres" if hit is None else ("same" if hit == r["id"] else f"other `{hit}`")
                out.append(f"| {i} | `{r['id']}` | {g} {sym[g]} | ({r['V']}, {r['E']}, {r['F']}) | {pr['b']} | "
                           f"({', '.join(pr['pt'])}) | {pr['pdf_page']} | {outcome} |")
                worklist.append({"rank": i, "target": r["id"], "group": g, "fvec": [r["V"], r["E"], r["F"]],
                                 "b": pr["b"], "point_Bpp": pr["pt"], "pdf": pr["pdf_page"],
                                 "p2": "unres" if hit is None else ("same" if hit == r["id"] else "other"),
                                 "p2_id": hit})
    out.append("")
    out.append(f"## Full ranked table (all {len(rows)} menu-sighted hexagonal types)\n")
    out.append("witness = first MENU sighting (group, point, b); stab = max site-stabilizer over menu sightings; "
               "dim = min stratum; #b = distinct b-ratios (menu); ob = max distinct b on one orbit; sgt = menu sightings; "
               "grp = groups sighted; S = S-cell (P2 sightings count); thin; O/W label; Schmitt = per-group flag with "
               "P-resolution [same/other/unres]; verdict = collision-screen verdict.\n")
    out.append("| rank | id | f-vector | p-vector | aut | witness | stab | dim | #b | ob | sgt | grp | S | thin | O/W | Schmitt | verdict | score |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        fwp = "(" + ",".join(r["fwm"]["point"]) + ")"
        out.append(f"| {i} | `{r['id']}` | ({r['V']}, {r['E']}, {r['F']}) | {r['p']} | {r['aut']} "
                   f"| {r['fwm']['group']} {sym[r['fwm']['group']]} {fwp} b={r['fwm']['b']} | {r['max_stab']} | {r['min_dim']} "
                   f"| {r['n_b']} | {r['orbit_bmax']} | {r['n_sight']} | {len(r['groups'])} | {r['n_p2'] if r['scell'] else ''} "
                   f"| {','.join(r['thin_reasons'])} | {r['ow']} | {fmt_flags(r)} | {r['verdict']} | {r['score']} |")
    out.append("")
    out.append(f"## f-vectors ABSENT from every sighted group's printed Schmitt table ({len(absent_all)} of {len(rows)})\n")
    for r in absent_all:
        out.append(f"- #{rank_of[r['id']]} `{r['id']}` f=({r['V']}, {r['E']}, {r['F']}) p={r['p']} aut={r['aut']} "
                   f"— sighted in " + ", ".join(f"{g} {sym[g]}" for g in r["groups"])
                   + f" — #b {r['n_b']}, {r['ow']}" + (", METRIC-THIN" if r["thin"] else ""))
    out.append("")
    out.append(f"## Metric-thin list ({len(thin_rows)} of {len(rows)})\n")
    out.append("| rank | id | f-vector | aut | witness | b-ratio(s) | reasons | O/W | Schmitt |")
    out.append("|---|---|---|---|---|---|---|---|---|")
    for r in thin_rows:
        fwp = "(" + ",".join(r["fwm"]["point"]) + ")"
        out.append(f"| {rank_of[r['id']]} | `{r['id']}` | ({r['V']}, {r['E']}, {r['F']}) | {r['aut']} "
                   f"| {r['fwm']['group']} {sym[r['fwm']['group']]} {fwp} | {fmt_b(r['bset'], 4)} "
                   f"| {','.join(r['thin_reasons'])} | {r['ow']} | {r['schmitt']} |")
    out.append("")
    out.append(f"## S-cell types (menu-sighted AND reproduce one of Schmitt's printed cells: {len(scell_rows)})\n")
    out.append("| rank | id | f-vector | aut | P2 cells | groups |")
    out.append("|---|---|---|---|---|---|")
    for r in scell_rows:
        out.append(f"| {rank_of[r['id']]} | `{r['id']}` | ({r['V']}, {r['E']}, {r['F']}) | {r['aut']} | {r['n_p2']} "
                   f"| {' '.join(str(g) for g in r['groups'])} |")
    out.append("")
    out.append("## Per-group counts (menu-sighted hexagonal types)\n")
    out.append("| group | symbol | first menu witness here | sighted here (menu) | sighted here (any pass) | S-cell here | f-vec A here |")
    out.append("|---|---|---|---|---|---|---|")
    for g in sorted(by_sighted):
        out.append(f"| {g} | {sym[g]} | {by_witness.get(g, 0)} | {by_sighted_menu.get(g, 0)} | {by_sighted[g]} "
                   f"| {by_scell.get(g, 0)} | {by_absent.get(g, 0)} |")
    out.append("")
    out.append("## Ranking recipe (all weights explicit, deterministic; identical to batch 1)\n")
    out.append(f"score = {W_FACET}*F + {B_F_GE20}*[F>=20] + {W_AUT}*log2(aut) + {W_STAB}*log2(max stab) "
               f"+ {W_PNOV}*min(3, #face sizes odd>=5 or >=7) + {W_SIGHT}*log2(1+#menu sightings) "
               f"+ {W_SPECIALPOS}*(3 - min stratum dim) + {W_VERT}*V + {W_NB}*log2(#b) + {W_NGROUP}*log2(#groups) "
               f"+ {B_SCHMITT_ABSENT}*[Schmitt ABSENT-all] {PEN_THIN}*[metric-thin] {PEN_SCELL}*[S-cell]. "
               "Tie-break: F desc, aut desc, id asc.\n")
    out.append("## Honest limits\n")
    out.append(f"- Schmitt flags are PROVISIONAL: {schmitt_note}.")
    out.append("- The collision screen is TYPE-level only at Schmitt's printed representatives (one point per (group, "
               "f-vector)); a SURVIVOR verdict says his printed cell for that f-vector is a different type — his "
               "unprinted 14 TB may still contain ours (sampling, not enumeration). The top-10 survivors' pairs are "
               "re-confirmed by recomputation in collision_phase2_hex_check.py.")
    out.append("- OPEN vs WALL is a LABEL from stored sightings only; no perturbation runs here.")
    out.append(f"- #b counts menu sightings only; {n_printed_b - n_printed_b_swept} of {n_printed_b} printed b-ratios were never swept.")
    out.append("- Aut orders are combinatorial; no roundness / geometric symmetry / Burnside / Engel / Bernhard checks.")
    out.append("- Schmitt-printed-only types are not ranked; prior-store types re-sighted here are out of scope.")
    out.append("")
    open(OUT, "w").write("\n".join(out))
    json.dump({"snapshot": SNAPSHOT, "store_sha256": sha_actual,
               "shortlist": [r["id"] for r in shortlist],
               "survivors_ranked": [r["id"] for r in survivors],
               "top10_survivors": [{"rank": i, "id": r["id"], "group": r["fwm"]["group"], "point": r["fwm"]["point"],
                                    "b": r["fwm"]["b"], "f": [r["V"], r["E"], r["F"]], "aut": r["aut"], "ow": r["ow"],
                                    "collision": r["collision"]} for i, r in enumerate(survivors[:10], 1)],
               "worklist": worklist, "verdict_counts": dict(verdicts)},
              open(OUT_JSON, "w"), indent=1)
    print(f"wrote {OUT} and {OUT_JSON}")
    print(f"prior={len(prior)} hex={len(hexa)} menu={len(menu)} sonly={len(sonly)} problems={len(problems)} kill_hits={len(kill_hits)}")
    print(f"sha_ok={sha_ok} schmitt_rows={len(schmitt_rows)} p2_map={len(p2_map)} resolved={n_rows_resolved}/{n_row_evals}")
    print(f"verdicts={dict(verdicts)} scell={len(scell_rows)} absent_all={len(absent_all)} thin={len(thin_rows)} ow={dict(ow_counts)}")
    for i, r in enumerate(survivors[:10], 1):
        print(f"  surv{i:2d} [#{rank_of[r['id']]}] {r['id']} grp {r['fwm']['group']} {sym[r['fwm']['group']]} b={r['fwm']['b']} "
              f"f=({r['V']},{r['E']},{r['F']}) aut {r['aut']} #b {r['n_b']} {r['ow']} schmitt {fmt_flags(r)} score {r['score']}")
    if problems or kill_hits:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
