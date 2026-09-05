#!/usr/bin/env python
"""triage_phase2.py — deterministic triage of the Phase-2 (tetragonal) MENU-sighted types into a G4 shortlist.

Inputs : phase2_types.json      (Phase-2 batch-1 store, 2026-09-03; regenerated from phase2_types.json.gz if absent;
                                 sha256 verified against phase2_types.SHA256SUMS)
         schmitt_tetragonal_tables.json          (VISUAL digitization of Schmitt Sec. 2.2.2, 2026-09-04; preferred)
         schmitt_tetragonal_rows_harvested.json  (text-layer harvest used by the sweep; fallback + cross-check)
Output : TRIAGE_PHASE2_RESULT.md
Model  : triage_phase1.py (feature logic + report format), extended with b-ratio features.
Gates  : ../ANCHORS.md G4/G5 + KILL CRITERIA. LANGUAGE: "not matched against catalog snapshot of 2026-09-03"
         ONLY — no novelty claims. Schmitt ch.2 is a sampling survey: absence from his printed tables is
         evidence, not proof.

SCHMITT FLAG (per sighted group, f-vector level, G5 wording):
    P  : the type's f-vector appears in Schmitt's printed table for that sighted group at SOME b-ratio
         => a TYPE-LEVEL check is required at G5 (same f-vector != same type).
    Pb : as P, and at least one printed row with that f-vector is at a b-ratio at which WE sighted the
         type in that group (tighter coincidence, still f-vector level).
    A  : the f-vector does NOT appear in his printed table for that sighted group => stronger candidate;
         still only snapshot language.
  Resolution of a P/Pb cell (cheap, from the stored P2 sightings): every printed row was run through our
  pipeline at his generating point (pass P2). For each printed row with the same (group, f-vector):
    same   : that printed cell reproduced as THIS type (type-level match with his printed representative);
    other  : it reproduced as a DIFFERENT stored type (his printed representative for this f-vector is a
             different combinatorial type; his unprinted data may still contain ours — sampling, not proof);
    unres  : the row was not stored (origin-choice-2 / second-enantiomorph rows quarantined in the sweep and
             re-run read-only in PHASE2_SCHMITT_ORIGIN_CHECK, or the two order_cycle rows) => must be
             re-run with the shifted setting before any verdict.
  S-cell : the type has >= 1 P2 sighting at all, i.e. it IS one of Schmitt's printed cells (type level).
           Such types are shown in the ranked table but EXCLUDED from the TOP-15 shortlist: by the KILL
           CRITERIA, "Schmitt-contains-candidate => reframe to first-realization", they are not G4 material.

SOURCE STATUS OF THE FLAGS: schmitt_tetragonal_tables.json is a SINGLE-PASS visual transcription
(diffed 0-discrepancy against the text layer, NOT an independent second re-key). Flags are provisional
until that G5 re-key. If the digitization file is absent the script falls back to the text-layer harvest
and labels the flags text-layer-provisional.

b-RATIO FEATURES (menu sightings only, i.e. passes P1/P3/P4/P5; P2 sightings excluded as in PHASE2_RESULT):
    #b        : number of distinct b-ratio values at which the type was sighted.
    orbit-b   : max over orbits (group, point) of the number of distinct b at which the SAME orbit gave the type.
    O/W label : open-likely   if orbit-b >= 3  (same orbit persists across >= 3 metric values);
                wall-suspect  if #b == 1       (single metric value; could be a transition wall);
                indeterminate otherwise.        LABEL ONLY — no perturbation runs here.
    thin      : metric-thin flag with reasons: 1b (exactly one b), P5-only (seen only at bisection midpoints),
                P3-only (seen only at Schmitt's non-grid b-ratios). Interesting but fragile.

Deterministic: no timestamps in the body, stable sort keys, byte-identical across re-runs on the same inputs.
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
STORE = os.path.join(HERE, "phase2_types.json")
STORE_GZ = os.path.join(HERE, "phase2_types.json.gz")
STORE_SUMS = os.path.join(HERE, "phase2_types.SHA256SUMS")
DIGITIZED = os.path.join(HERE, "schmitt_tetragonal_tables.json")
HARVESTED = os.path.join(HERE, "schmitt_tetragonal_rows_harvested.json")
OUT = os.path.join(HERE, "TRIAGE_PHASE2_RESULT.md")

RUN_DATE = "2026-09-04"        # fixed label, not a timestamp
CATALOG_SNAPSHOT = "2026-09-03"
TOP_N = 15

# Claims to recount against (PHASE2_RESULT.md headline / STATUS 2026-09-04 (early)).
CLAIM_CUBIC, CLAIM_TET, CLAIM_MENU, CLAIM_SONLY = 102, 789, 404, 385
CLAIM_SCHMITT_ROWS = 1476

SEEDED_GONS = {3, 4, 6}         # face sizes of the seeded classics (as in triage_phase1)
MAX_FACETS_KILL = 38            # observed literature max (Schmitt 2016 sampling; ANCHORS amendment: observed, not proven)
MENU_PASSES = {"P1", "P3", "P4", "P5"}

# ---------------------------------------------------------------------------
# Ranking weights (all documented; deterministic). Phase-1 weights kept where the feature is the same;
# corridor / 220-230 bonuses do not apply (no pre-registered tetragonal corridor); b-ratio terms are new.
# ---------------------------------------------------------------------------
W_FACET = 3.0           # per facet (task: 20+ notable; observed literature max 38)
B_F_GE20 = 10.0         # bonus if F >= 20
W_AUT = 4.0             # * log2(combinatorial aut order)
W_STAB = 2.0            # * log2(max site-stabilizer order over menu sightings)
W_PNOV = 3.0            # * min(3, #distinct face sizes that are odd or >= 7)  (5,7,9,... and 7,8,9,...)
W_SIGHT = 1.5           # * log2(1 + #menu sightings)
W_SPECIALPOS = 1.5      # * (3 - min stratum_dim over menu sightings)  (fixed point > line > plane > general)
W_VERT = 0.1            # * vertex count (mild)
W_NB = 2.0              # * log2(#distinct b-ratios)   (metric robustness)
W_NGROUP = 1.0          # * log2(#distinct groups sighted)
B_SCHMITT_ABSENT = 5.0  # f-vector absent from EVERY sighted group's printed table (snapshot evidence only)
PEN_THIN = -4.0         # metric-thin (fragile sighting)
PEN_SCELL = -25.0       # type reproduces one of Schmitt's printed cells (type-level: he has it)


def pfmt(p):
    c = Counter(p)
    return " ".join(f"{g}^{c[g]}" for g in sorted(c))


def log2(x):
    return math.log2(x) if x > 0 else 0.0


def frac_key(strs):
    """Exact rational key for a point, reduced mod 1 (sightings and printed rows may differ by lattice shifts)."""
    return tuple(Fraction(s) % 1 for s in strs)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_store():
    """Regenerate the raw store from the .gz if absent; return (regenerated, sha_ok, sha_actual, sha_expected)."""
    regenerated = False
    if not os.path.exists(STORE):
        with gzip.open(STORE_GZ, "rb") as src, open(STORE, "wb") as dst:
            shutil.copyfileobj(src, dst)
        regenerated = True
    expected = None
    with open(STORE_SUMS) as fh:
        for line in fh:
            parts = line.split()
            if "phase2_types.json" in parts[:1] and "sha256" in parts:
                expected = parts[parts.index("sha256") + 1]
            elif len(parts) >= 2 and len(parts[0]) == 64 and parts[1].endswith("phase2_types.json"):
                expected = parts[0]
    actual = sha256_file(STORE)
    return regenerated, (expected is not None and actual == expected), actual, expected


def load_schmitt():
    """Return (rows, source_label, provisional_note, digitized_meta_checks).
    rows: list of dicts {groups: [..], f: (V,E,F), b: str, pt: [..], pdf_page: int|None}."""
    harv = None
    if os.path.exists(HARVESTED):
        with open(HARVESTED) as fh:
            harv = json.load(fh)
    if os.path.exists(DIGITIZED):
        with open(DIGITIZED) as fh:
            dig = json.load(fh)
        rows = []
        for key, blk in dig.items():
            if key == "_meta":
                continue
            for r in blk["rows"]:
                rows.append({"groups": list(blk["groups"]), "f": tuple(r["f"]), "b": r["b"],
                             "pt": list(r["pt"]), "pdf_page": r.get("pdf_page")})
        src = "schmitt_tetragonal_tables.json (VISUAL digitization, single pass, 2026-09-04)"
        note = ("visual single-pass + text-layer cross-checked (0 row discrepancies, re-verified below), NOT "
                "independently re-keyed (G5 duty still owed) — flags provisional")
        # cross-check against the text-layer harvest, row for row (multiset of (groups, f, b, pt mod 1))
        xcheck = None
        if harv is not None:
            def ms(rs, gkey, fkey, bkey, pkey):
                return Counter((tuple(r[gkey]), tuple(r[fkey]), str(Fraction(r[bkey])), frac_key(r[pkey])) for r in rs)
            a = ms(rows, "groups", "f", "b", "pt")
            b = ms(harv["rows"], "groups", "f_vector", "b_ratio", "point")
            only_a = sum((a - b).values())
            only_b = sum((b - a).values())
            # flag invariance: the P/Pb/A flag depends only on (group, f, b); compare that projection too
            fa = {(g, tuple(r["f"]), str(Fraction(r["b"]))) for r in rows for g in r["groups"]}
            fb = {(g, tuple(r["f_vector"]), str(Fraction(r["b_ratio"]))) for r in harv["rows"] for g in r["groups"]}
            xcheck = (len(rows), len(harv["rows"]), only_a, only_b, len(fa ^ fb))
        return rows, src, note, xcheck
    # fallback
    rows = [{"groups": list(r["groups"]), "f": tuple(r["f_vector"]), "b": r["b_ratio"], "pt": list(r["point"]),
             "pdf_page": None} for r in harv["rows"]]
    src = "schmitt_tetragonal_rows_harvested.json (pdftotext text layer; visual digitization NOT found)"
    note = "text-layer-provisional: pdftotext harvest, not visually verified"
    return rows, src, note, None


def main():
    regenerated, sha_ok, sha_actual, sha_expected = ensure_store()
    with open(STORE) as fh:
        store = json.load(fh)
    types = store["types"]

    schmitt_rows, schmitt_src, schmitt_note, xcheck = load_schmitt()

    lines_sanity = []
    kill_hits = []
    problems = []

    # --- Sanity 0: inputs -----------------------------------------------------
    lines_sanity.append(f"- phase2_types.json sha256 {sha_actual}: "
                        + ("MATCHES phase2_types.SHA256SUMS" if sha_ok else f"MISMATCH (expected {sha_expected})")
                        + (" [regenerated from phase2_types.json.gz]" if regenerated else " [raw file present]"))
    if not sha_ok:
        problems.append("SHA256 MISMATCH on phase2_types.json")
    # Schmitt rows self-check
    by_group_f = defaultdict(set)          # group -> set of f-vectors printed
    by_group_f_b = defaultdict(set)        # group -> set of (f, b as Fraction)
    rows_by_group_f = defaultdict(list)    # (group, f) -> list of rows
    n_euler_bad = 0
    for r in schmitt_rows:
        V, E, F = r["f"]
        if V - E + F != 2:
            n_euler_bad += 1
        for g in r["groups"]:
            by_group_f[g].add(r["f"])
            by_group_f_b[g].add((r["f"], Fraction(r["b"])))
            rows_by_group_f[(g, r["f"])].append(r)
    if n_euler_bad:
        problems.append(f"SCHMITT ROWS EULER FAIL: {n_euler_bad} rows")
    lines_sanity.append(f"- Schmitt tetragonal rows: {len(schmitt_rows)} rows over {len(by_group_f)} groups from {schmitt_src}; "
                        f"Euler V-E+F=2 on every row: {'PASS' if not n_euler_bad else 'FAIL'}; "
                        f"row count vs claim {CLAIM_SCHMITT_ROWS}: {'MATCH' if len(schmitt_rows) == CLAIM_SCHMITT_ROWS else 'DISCREPANCY'}")
    if xcheck is not None:
        n_d, n_h, oa, ob, fdiff = xcheck
        lines_sanity.append(f"- Digitization vs text-layer harvest, row-for-row multiset on (groups, f, b, point mod 1): "
                            f"{n_d} vs {n_h} rows, {oa} only in digitization, {ob} only in harvest: "
                            + ("IDENTICAL" if oa == 0 and ob == 0 else "DIFFER (reported, not forced)")
                            + f". Flag-relevant projection (group, f, b): {fdiff} symmetric-difference entries => the "
                            "Schmitt P/Pb/A flags below are " + ("IDENTICAL under either source (visual tables used as primary)."
                                                                  if fdiff == 0 else "NOT identical across sources (visual tables used)."))
        if fdiff:
            problems.append(f"SCHMITT FLAG PROJECTION DIFFERS across sources: {fdiff}")
        if oa or ob:
            problems.append(f"SCHMITT DIGITIZATION vs HARVEST DIFFER: {oa} / {ob}")

    # --- Sanity 1-3: store checks --------------------------------------------
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
                    f"(group {s['group']}, point {tuple(s['point'])}, b={s['b']})")

    cubic = sorted(tid for tid in types if types[tid]["first_sighting_system"].startswith("cubic"))
    tet = sorted(tid for tid in types if not types[tid]["first_sighting_system"].startswith("cubic"))
    sonly = sorted(tid for tid in tet if types[tid]["schmitt_printed_only"])
    menu = sorted(tid for tid in tet if not types[tid]["schmitt_printed_only"])
    # menu-sighted must have >= 1 non-P2 sighting; S-only must have none
    for tid in menu:
        if not any(s["pass"] in MENU_PASSES for s in types[tid]["sightings"]):
            problems.append(f"MENU FLAG FAIL {tid}: flagged menu-sighted but has no P1/P3/P4/P5 sighting")
    for tid in sonly:
        if any(s["pass"] in MENU_PASSES for s in types[tid]["sightings"]):
            problems.append(f"S-ONLY FLAG FAIL {tid}: flagged Schmitt-only but has a menu sighting")
    cubic_sonly = [tid for tid in cubic if types[tid]["schmitt_printed_only"]]
    n_sight_total = sum(len(t["sightings"]) for t in types.values())
    lines_sanity.append(f"- Euler V-E+F=2: checked for all {len(types)} stored types: "
                        + ("ALL PASS" if not any(p.startswith('EULER') for p in problems) else "FAIL"))
    lines_sanity.append(f"- p-vector consistency (|p|=F and sum(p)=2E) for all {len(types)} types: "
                        + ("ALL PASS" if not any(p.startswith('P-VECTOR') for p in problems) else "FAIL"))
    lines_sanity.append(f"- site-stabilizer divides aut, every stored sighting ({n_sight_total} sightings): "
                        + ("ALL PASS" if not any(p.startswith('STAB') for p in problems) else "FAIL"))
    maxF_store = max(t["f_vector"][2] for t in types.values())
    maxF_menu = max(types[tid]["f_vector"][2] for tid in menu)
    lines_sanity.append(f"- kill criterion (>{MAX_FACETS_KILL} facets): max stored facet count = {maxF_store} "
                        f"(from our menu: {maxF_menu}): " + ("NO HITS" if not kill_hits else "HITS - QUARANTINE"))
    counts_ok = (len(cubic), len(tet), len(menu), len(sonly)) == (CLAIM_CUBIC, CLAIM_TET, CLAIM_MENU, CLAIM_SONLY)
    lines_sanity.append(f"- recount: {len(cubic)} cubic-store + {len(tet)} tetragonal = {len(types)} types; tetragonal split "
                        f"{len(menu)} menu-sighted + {len(sonly)} Schmitt-printed-only; store fields say "
                        f"{store['n_types_cubic_store']}/{store['n_types_tetragonal_new']}/"
                        f"{store['n_types_tetragonal_menu_sighted']}/{store['n_types_tetragonal_schmitt_printed_only']}; "
                        f"PHASE2_RESULT/STATUS claim {CLAIM_CUBIC}/{CLAIM_TET}/{CLAIM_MENU}/{CLAIM_SONLY}: "
                        + ("MATCH" if counts_ok else "DISCREPANCY - reported, not forced"))
    lines_sanity.append(f"- menu/S-only flags consistent with stored pass labels for all {len(tet)} tetragonal types: "
                        + ("PASS" if not any(p.endswith('FLAG FAIL') or 'FLAG FAIL' in p for p in problems) else "FAIL"))
    if cubic_sonly:
        lines_sanity.append(f"- note: {len(cubic_sonly)} cubic-store type(s) carry schmitt_printed_only=True "
                            f"(re-sighted in tetragonal groups only at his printed points; not part of the 385): "
                            + ", ".join(f"`{tid}` f=({','.join(map(str, types[tid]['f_vector']))})" for tid in cubic_sonly))

    # --- P2 map: (group, point mod 1, b) -> type id (which stored type each printed cell reproduced as) ------
    p2_map = {}
    for tid, t in types.items():
        for s in t["sightings"]:
            if s["pass"] == "P2":
                p2_map[(s["group"], frac_key(s["point"]), Fraction(s["b"]))] = tid
    n_rows_resolved = 0
    for r in schmitt_rows:
        for g in r["groups"]:
            if (g, frac_key(r["pt"]), Fraction(r["b"])) in p2_map:
                n_rows_resolved += 1
    lines_sanity.append(f"- P2 sightings keyed by (group, printed point mod 1, b): {len(p2_map)} stored cells; "
                        f"printed (row x group) evaluations resolved to a stored type: {n_rows_resolved} "
                        f"(PHASE2_RESULT: 1215 reproduced of 1641 evaluations)")

    sym = {}
    for t in types.values():
        for s in t["sightings"]:
            sym[s["group"]] = s["group_symbol"]

    b_coarse = set(Fraction(b) for b in store["scan"]["b_coarse"])
    b_schmitt_used = set(Fraction(b) for b in store["scan"]["schmitt_b_used"])

    # --- Features + score --------------------------------------------------------
    rows = []
    for tid in menu:
        t = types[tid]
        V, E, F = t["f_vector"]
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
        fw = t["first_witness"]
        # menu first witness = earliest stored menu sighting (sightings are in run order)
        fwm = sight_menu[0]

        bset = sorted({Fraction(s["b"]) for s in sight_menu})
        n_b = len(bset)
        orbit_b = defaultdict(set)
        for s in sight_menu:
            orbit_b[(s["group"], frac_key(s["point"]))].add(Fraction(s["b"]))
        orbit_bmax = max(len(v) for v in orbit_b.values())
        best_orbit = min((k for k, v in orbit_b.items() if len(v) == orbit_bmax))
        passes = {s["pass"] for s in sight_menu}
        thin_reasons = []
        if n_b == 1:
            thin_reasons.append("1b")
        if passes == {"P5"}:
            thin_reasons.append("P5-only")
        if passes == {"P3"}:
            thin_reasons.append("P3-only")
        thin = bool(thin_reasons)
        if orbit_bmax >= 3:
            ow = "open-likely"
        elif n_b == 1:
            ow = "wall-suspect"
        else:
            ow = "indeterminate"
        b_kinds = []
        if any(b in b_coarse for b in bset):
            b_kinds.append("coarse")
        if any(b in b_schmitt_used for b in bset):
            b_kinds.append("schmittb")
        if any((b not in b_coarse and b not in b_schmitt_used) for b in bset):
            b_kinds.append("bisect")

        # Schmitt flag per sighted group (all groups where the type was seen, menu or P2)
        flags = {}
        resolution = {}   # group -> Counter(same/other/unres)
        for g in groups_all:
            tbl = by_group_f.get(g)
            if tbl is None:
                flags[g] = "U"
                continue
            if (V, E, F) not in tbl:
                flags[g] = "A"
                continue
            my_b = {Fraction(s["b"]) for s in sight_all if s["group"] == g}
            flags[g] = "Pb" if any(((V, E, F), b) in by_group_f_b[g] for b in my_b) else "P"
            res = Counter()
            for r in rows_by_group_f[(g, (V, E, F))]:
                hit = p2_map.get((g, frac_key(r["pt"]), Fraction(r["b"])))
                if hit is None:
                    res["unres"] += 1
                elif hit == tid:
                    res["same"] += 1
                else:
                    res["other"] += 1
            resolution[g] = res
        if all(v == "A" for v in flags.values()):
            schmitt_class = "ABSENT-all"
        elif any(v in ("P", "Pb") for v in flags.values()):
            schmitt_class = "present"
        else:
            schmitt_class = "UNKNOWN"
        scell = len(sight_p2) > 0

        score = (W_FACET * F
                 + (B_F_GE20 if F >= 20 else 0.0)
                 + W_AUT * log2(aut)
                 + W_STAB * log2(max_stab)
                 + W_PNOV * min(3, len(nov_gons))
                 + W_SIGHT * log2(1 + n_sight)
                 + W_SPECIALPOS * (3 - min_dim)
                 + W_VERT * V
                 + W_NB * log2(n_b)
                 + W_NGROUP * log2(len(groups_all))
                 + (B_SCHMITT_ABSENT if schmitt_class == "ABSENT-all" else 0.0)
                 + (PEN_THIN if thin else 0.0)
                 + (PEN_SCELL if scell else 0.0))

        rows.append({
            "id": tid, "V": V, "E": E, "F": F, "aut": aut, "p": pfmt(t["p_vector"]),
            "groups": groups_all, "groups_menu": groups_menu, "max_stab": max_stab, "min_dim": min_dim,
            "n_sight": n_sight, "n_p2": len(sight_p2), "nov": nov_gons, "fw": fw, "fwm": fwm,
            "bset": bset, "n_b": n_b, "orbit_bmax": orbit_bmax, "best_orbit": best_orbit, "b_kinds": b_kinds,
            "thin": thin, "thin_reasons": thin_reasons, "ow": ow,
            "flags": flags, "res": resolution, "schmitt": schmitt_class, "scell": scell,
            "score": round(score, 2),
        })

    rows.sort(key=lambda r: (-r["score"], -r["F"], -r["aut"], r["id"]))
    rank_of = {r["id"]: i for i, r in enumerate(rows, 1)}

    # --- Aggregates ---------------------------------------------------------------
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
            pres = [g for g in r["groups"] if r["flags"][g] in ("P", "Pb")]
            det = []
            for g in pres:
                res = r["res"][g]
                det.append(f"{g}:" + ("other" if res["other"] and not res["unres"] else
                                     "unres" if res["unres"] else "same"))
            bits.append("Schmitt f-vec present (" + ", ".join(det) + ") -> G5 type-level check")
        return "; ".join(bits)

    # --- Emit ---------------------------------------------------------------------
    out = []
    out.append(f"# TRIAGE result — Phase-2 (tetragonal) MENU-sighted types -> G4 shortlist ({RUN_DATE})\n")
    out.append("Script: `triage_phase2.py` (deterministic; byte-identical across re-runs on the same inputs; model "
               "`triage_phase1.py`). Store: `phase2_types.json` (Phase-2 batch 1, run 2026-09-03; sha256 verified). "
               "Schmitt rows: " + schmitt_src + ". Gates: `../ANCHORS.md` G4 (finalist certificates), G5 (novelty "
               "diligence — NOT run here) and KILL CRITERIA.\n")
    out.append(f"**LANGUAGE (G5): every type below is \"not matched against the catalog snapshot of {CATALOG_SNAPSHOT}\". "
               "No novelty claim. The Schmitt column is f-vector-level evidence from his printed Sec. 2.2.2 tables "
               "(a 351-CPU-year grid SAMPLING, not an enumeration): \"A\" = absent there (stronger candidate, still only "
               "snapshot language), \"P\"/\"Pb\" = present (same f-vector does NOT mean same type — the Josehedron/"
               "Schmitt-220 pair proves this — so a G5 type-level check is required; Pb = present at a b-ratio at which "
               "we sighted the type in that group). \"S-cell\" = the type IS one of his printed cells (reproduced at his "
               "generating point in pass P2): type-level match, excluded from the shortlist by the kill criterion "
               "\"Schmitt-contains-candidate => reframe to first-realization\".**\n")
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

    out.append("## Headline counts (the 404 menu-sighted tetragonal types)\n")
    out.append(f"- Ranked: {len(rows)}. S-cell (type reproduces one of Schmitt's printed cells): {len(scell_rows)}; "
               f"menu-only (never at a printed point): {len(rows) - len(scell_rows)}.")
    out.append(f"- Schmitt f-vector flag: ABSENT-all {len(absent_all)}; present (P/Pb in >= 1 sighted group) "
               f"{sum(1 for r in rows if r['schmitt'] == 'present')}; unknown {sum(1 for r in rows if r['schmitt'] == 'UNKNOWN')}.")
    n_absent_menuonly = sum(1 for r in absent_all if not r["scell"])
    out.append(f"- ABSENT-all and menu-only: {n_absent_menuonly}.")
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
    out.append("")

    out.append(f"## TOP-{TOP_N} G4 SHORTLIST (S-cell types excluded; rank in the full table in brackets)\n")
    for i, r in enumerate(shortlist, 1):
        fwp = "(" + ", ".join(r["fwm"]["point"]) + ")"
        out.append(f"{i}. `{r['id']}` [#{rank_of[r['id']]}] — **{r['fwm']['group']} {sym[r['fwm']['group']]}** at {fwp} "
                   f"b={r['fwm']['b']}, f=({r['V']}, {r['E']}, {r['F']}), p={r['p']}, aut={r['aut']}, "
                   f"b-ratios: {fmt_b(r['bset'])}, Schmitt {fmt_flags(r)} [score {r['score']}]  \n   {why(r)}")
    out.append("")

    out.append("## Collision screen worklist for the shortlist (what to run first once the digitization is accepted)\n")
    out.append("For each shortlisted type flagged P/Pb: the printed rows in that group with the same f-vector, and how "
               "each reproduced in pass P2 (`other` = a different stored type, id given; `unres` = row not stored in the "
               "sweep — the two-origin / second-enantiomorph groups — re-run with the shifted setting first; `same` "
               "cannot occur here by construction). A-flagged shortlist types have no printed row to collide with.\n")
    out.append("| # | id | group | f-vector | printed b | printed point | PDF p. | P2 outcome |")
    out.append("|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(shortlist, 1):
        for g in r["groups"]:
            if r["flags"][g] not in ("P", "Pb"):
                continue
            for pr in sorted(rows_by_group_f[(g, (r["V"], r["E"], r["F"]))], key=lambda x: (Fraction(x["b"]), x["pt"])):
                hit = p2_map.get((g, frac_key(pr["pt"]), Fraction(pr["b"])))
                outcome = ("unres (not stored; re-run shifted)" if hit is None else
                           ("same" if hit == r["id"] else f"other `{hit}`"))
                out.append(f"| {i} | `{r['id']}` | {g} {sym[g]} | ({r['V']}, {r['E']}, {r['F']}) | {pr['b']} | "
                           f"({', '.join(pr['pt'])}) | {pr['pdf_page'] if pr['pdf_page'] is not None else '-'} | {outcome} |")
    out.append("")

    out.append("## Full ranked table (all 404 menu-sighted tetragonal types)\n")
    out.append("witness = first MENU sighting (group, point, b); stab = max site-stabilizer over menu sightings; "
               "dim = min stratum (0 fixed point / 1 line / 2 plane / 3 general); #b = distinct b-ratios (menu); "
               "ob = max distinct b on one orbit; sgt = menu sightings; grp = groups sighted (all passes); "
               "S = S-cell (P2 sightings count); thin = metric-thin reasons; O/W = open/wall label; "
               "Schmitt = per group flag with P-resolution [same/other/unres counts].\n")
    out.append("| rank | id | f-vector | p-vector | aut | witness | stab | dim | #b | ob | sgt | grp | S | thin | O/W | Schmitt | score |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        fwp = "(" + ",".join(r["fwm"]["point"]) + ")"
        out.append(f"| {i} | `{r['id']}` | ({r['V']}, {r['E']}, {r['F']}) | {r['p']} | {r['aut']} "
                   f"| {r['fwm']['group']} {sym[r['fwm']['group']]} {fwp} b={r['fwm']['b']} | {r['max_stab']} | {r['min_dim']} "
                   f"| {r['n_b']} | {r['orbit_bmax']} | {r['n_sight']} | {len(r['groups'])} | {r['n_p2'] if r['scell'] else ''} "
                   f"| {','.join(r['thin_reasons'])} | {r['ow']} | {fmt_flags(r)} | {r['score']} |")
    out.append("")

    out.append(f"## f-vectors ABSENT from every sighted group's printed Schmitt table ({len(absent_all)} of {len(rows)})\n")
    out.append("Sorted by rank. His grid sampled these groups without printing this f-vector (evidence, not proof); "
               "S-cell cannot occur here (an S-cell type reproduces a printed row, hence is P in that group).\n")
    for r in absent_all:
        out.append(f"- #{rank_of[r['id']]} `{r['id']}` f=({r['V']}, {r['E']}, {r['F']}) p={r['p']} aut={r['aut']} "
                   f"— sighted in " + ", ".join(f"{g} {sym[g]}" for g in r["groups"])
                   + f" — #b {r['n_b']}, {r['ow']}" + (", METRIC-THIN" if r["thin"] else ""))
    out.append("")

    out.append(f"## Metric-thin list ({len(thin_rows)} of {len(rows)})\n")
    out.append("1b = exactly one b-ratio value; P5-only = seen only at bisection midpoints; P3-only = seen only at "
               "Schmitt's non-grid b-ratios. Interesting but fragile: a single metric value can be a transition wall.\n")
    out.append("| rank | id | f-vector | aut | witness | b-ratio(s) | reasons | O/W | Schmitt |")
    out.append("|---|---|---|---|---|---|---|---|---|")
    for r in thin_rows:
        fwp = "(" + ",".join(r["fwm"]["point"]) + ")"
        out.append(f"| {rank_of[r['id']]} | `{r['id']}` | ({r['V']}, {r['E']}, {r['F']}) | {r['aut']} "
                   f"| {r['fwm']['group']} {sym[r['fwm']['group']]} {fwp} | {fmt_b(r['bset'], 4)} "
                   f"| {','.join(r['thin_reasons'])} | {r['ow']} | {r['schmitt']} |")
    out.append("")

    out.append(f"## S-cell types (menu-sighted AND reproduce one of Schmitt's printed cells: {len(scell_rows)})\n")
    out.append("Type-level matches with his printed representatives; excluded from the shortlist. Listed compactly.\n")
    out.append("| rank | id | f-vector | aut | P2 cells | groups |")
    out.append("|---|---|---|---|---|---|")
    for r in scell_rows:
        out.append(f"| {rank_of[r['id']]} | `{r['id']}` | ({r['V']}, {r['E']}, {r['F']}) | {r['aut']} | {r['n_p2']} "
                   f"| {' '.join(str(g) for g in r['groups'])} |")
    out.append("")

    out.append("## Per-group counts (menu-sighted tetragonal types)\n")
    out.append("| group | symbol | first menu witness here | sighted here (menu) | sighted here (any pass) | S-cell here | f-vec A here |")
    out.append("|---|---|---|---|---|---|---|")
    for g in sorted(by_sighted):
        out.append(f"| {g} | {sym[g]} | {by_witness.get(g, 0)} | {by_sighted_menu.get(g, 0)} | {by_sighted[g]} "
                   f"| {by_scell.get(g, 0)} | {by_absent.get(g, 0)} |")
    out.append("")

    out.append("## Ranking recipe (all weights explicit, deterministic)\n")
    out.append(f"score = {W_FACET}*F + {B_F_GE20}*[F>=20] + {W_AUT}*log2(aut) + {W_STAB}*log2(max stab) "
               f"+ {W_PNOV}*min(3, #face sizes odd>=5 or >=7) + {W_SIGHT}*log2(1+#menu sightings) "
               f"+ {W_SPECIALPOS}*(3 - min stratum dim) + {W_VERT}*V + {W_NB}*log2(#b) + {W_NGROUP}*log2(#groups) "
               f"+ {B_SCHMITT_ABSENT}*[Schmitt ABSENT-all] {PEN_THIN}*[metric-thin] {PEN_SCELL}*[S-cell]. "
               "Tie-break: F desc, aut desc, id asc. Shortlist = top-15 among non-S-cell rows. Weights are triage "
               "judgment, not measurements; they are stated so the ranking is reproducible and criticizable.\n")

    out.append("## Honest limits\n")
    out.append(f"- Schmitt flags are PROVISIONAL: {schmitt_note}. Any G5 verdict that leans on a specific P/A cell must "
               "first re-read that printed page (PDF page given in the worklist).")
    out.append("- The Schmitt cross-check is F-VECTOR level (his tables print one representative point per f-vector); "
               "the P-resolution column only says how HIS PRINTED representative reproduced in our pipeline. `other` "
               "means his printed cell for that f-vector is a different type than ours — his unprinted 14 TB may still "
               "contain ours (sampling, not enumeration; SCHMITT_DATA_RECOVERY_2026-08-28.md). `unres` rows (origin-choice-2 "
               "groups 85,86,88,125,126,129,130,133,134,137,138,141,142 and second-enantiomorph 95/96, plus the two "
               "order_cycle rows) were re-run read-only in PHASE2_SCHMITT_ORIGIN_CHECK.md but NOT stored, so their "
               "types are unknown to this triage.")
    out.append("- OPEN vs WALL is a LABEL from stored sightings only (same orbit persisting across >= 3 b-values vs a "
               "single b-value); no perturbation or interval computation was run. A wall-suspect type may be open in "
               "the point direction; an open-likely label is not a certificate.")
    out.append("- #b counts menu sightings only (P1/P3/P4/P5); the sweep ran 13 coarse + 5 Schmitt + bisection "
               "b-values, so #b is bounded by the menu, and 51 of 56 printed b-ratios were never swept.")
    out.append("- Aut orders are combinatorial map automorphism counts; geometric stabilizer certification is G4/V2, "
               "not claimed. Roundness, Wyckoff letters, polyform counts (G4 Burnside), Engel-1981 and Bernhard "
               "cross-checks are NOT computed here.")
    out.append("- The 385 Schmitt-printed-only types are not ranked (his cells, not our hunt) and the 19 cubic-store "
               "types re-sighted in tetragonal groups are out of scope here (phase-1 triage covers them).")
    out.append("- The ranking weights are stated judgment calls; re-ranking is one `triage_phase2.py` edit away and "
               "does not touch the store.")
    out.append("")

    with open(OUT, "w") as fh:
        fh.write("\n".join(out))

    print(f"wrote {OUT}")
    print(f"cubic={len(cubic)} tet={len(tet)} menu={len(menu)} sonly={len(sonly)} problems={len(problems)} kill_hits={len(kill_hits)}")
    print(f"sha_ok={sha_ok} schmitt_rows={len(schmitt_rows)} xcheck={xcheck} p2_map={len(p2_map)} resolved_rows={n_rows_resolved}")
    print(f"scell={len(scell_rows)} absent_all={len(absent_all)} (menu-only {n_absent_menuonly}) "
          f"thin={len(thin_rows)} ow={dict(ow_counts)}")
    for i, r in enumerate(shortlist, 1):
        print(f"  top{i:2d} [#{rank_of[r['id']]}] {r['id']} grp {r['fwm']['group']} {sym[r['fwm']['group']]} "
              f"f=({r['V']},{r['E']},{r['F']}) aut {r['aut']} #b {r['n_b']} ob {r['orbit_bmax']} {r['ow']} "
              f"schmitt {fmt_flags(r)} score {r['score']}")
    if problems or kill_hits:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
