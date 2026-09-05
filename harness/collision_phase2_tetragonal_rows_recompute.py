#!/usr/bin/env python
"""collision_phase2_tetragonal_rows_recompute.py — recompute, with the ACCEPTED
phase-2 exact chain, the 62 unstored Schmitt printed rows on which the 106
UNRESOLVED tetragonal type statuses of collision_phase2_tetragonal_storeside.json
hang, and settle those 106 statuses (2026-09-04, subagent #154, Claude Fable 5.1;
AI-drafted, main-session re-run required before acceptance).

WHY. COLLISION_PHASE2_RESULTS.md addendum (subagent #152): under the store-side
rule 106 menu-sighted tetragonal-first types read UNRESOLVED because a printed
row at their (group, f) was NOT stored by the sweep's pass P2 (quarantined as
schmitt_fvec_mismatch in the two-origin groups and the second enantiomorphs,
where Schmitt's coordinates are in another setting, or as the IT(80) order_cycle
crash). Those rows were never recomputed with the documented setting
conversions. This script does exactly what collision_phase2_check.py did for the
7 `unres` rows of the top-15 shortlist, for all 62 rows.

PER ROW (group g, printed b, printed point X; PDF page cited from
schmitt_tetragonal_tables.json): every DOCUMENTED convention of the group is run
(PHASE2_SCHMITT_ORIGIN_CHECK.md, machine-verified on ALL printed rows of each
group): origin-choice-2 groups -> p_ours = X + s for EVERY shift s that
reproduced all rows (primary = the check's best_shift, the others as robustness
alternatives; collision_phase2_check.conversions_for reproduced verbatim); second
enantiomorphs 95/96 -> the primary z -> -z and the other signed-axis transforms
that reproduced all rows; IT(80) -> none (printed point verbatim; the row crashed
on the float facet-ordering proposal, now the exact order_cycle fallback). In
addition the OTHER origin / enantiomorph reading — the printed point taken
verbatim in our setting (origin choice 1 / first-enantiomorph coordinates) — is
run and RECORDED for every two-origin / 95 / 96 row; it is not a documented
conversion (pass P2 already ran it and quarantined the row), so it cannot
establish the row's cell, but if it reproduced the printed f-vector with a
different code that is reported as a surprise. Chain per cell:
sweep_phase2_tetragonal.evaluate (orbit -> Gram(b) -> float proposal -> exact clip
with 4*rho^2 <= D^2 asserted on cell 0 AND a second orbit cell, Euler,
float/exact agreement, orbit congruence, stab | aut). A row is REPRODUCED iff the
printed f-vector comes back under >= 1 documented convention and every documented
convention that reproduces it gives ONE canonical code; otherwise QUARANTINE
(f-vectors / chain errors obtained are recorded) — or AMBIGUOUS if two documented
conventions reproduce f with different codes (treated as quarantine).

PER TYPE (the 106 UNRESOLVED): its canonical code is compared with the code of
every row it hangs on (the storeside JSON's unstored_rows): any SAME ->
COLLISION (decisive: the type IS one of his printed cells; first-realization
reframe); every row REPRODUCED and DIFFERENT -> SURVIVOR (catalog-relative, never
novelty: "not matched against the records checked as of 2026-09-04"); any row
quarantined and no SAME -> stays UNRESOLVED (listed). Secondary check, recorded
separately: does any type's code equal the cell of a row it does NOT hang on
(a printed cell of the type in a group where our menu never sighted it)?

READ-ONLY: phase2_types.json / .gz sha256 71685b9a... verified before and after;
no cell computed here is added to any store. The storeside JSON is verified by
md5 (64cc7bb82e85164914d7ec441cfc1304, the value stated in the #152 addendum).

Run (from harness/, foreground, seconds):
  nice -n 10 python3 \
      collision_phase2_tetragonal_rows_recompute.py
Writes: collision_phase2_tetragonal_rows_recomputed.json (every computed cell;
sorted keys; md5 printed), collision_phase2_tetragonal_unresolved_overlay.json
(the 106 verdicts; sorted keys; md5 printed) and APPENDS a dated addendum to
COLLISION_PHASE2_RESULTS.md once (skipped if its heading is already present).
Exit 0 iff every row got a status, the stores were unchanged, and the two
previously recomputed rows (Q14 IT(86), Q24 IT(80)) reproduce their codes.
"""
import hashlib
import json
import os
import signal
import sys
import time
from collections import Counter, OrderedDict
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sweep_phase2_tetragonal as S2                  # noqa: E402
from collision_phase2_check import conversions_for, code_id, pt_str, frac_str   # noqa: E402

STORE = os.path.join(HERE, "phase2_types.json")
STORE_GZ = os.path.join(HERE, "phase2_types.json.gz")
SHA_FILE = os.path.join(HERE, "phase2_types.SHA256SUMS")
TABLES = os.path.join(HERE, "schmitt_tetragonal_tables.json")
ORIGIN_JSON = os.path.join(HERE, "phase2_schmitt_origin_check.json")
SS_JSON = os.path.join(HERE, "collision_phase2_tetragonal_storeside.json")
CHECK_JSON = os.path.join(HERE, "collision_phase2_results.json")
OUT_MD = os.path.join(HERE, "COLLISION_PHASE2_RESULTS.md")
OUT_ROWS = os.path.join(HERE, "collision_phase2_tetragonal_rows_recomputed.json")
OUT_OVERLAY = os.path.join(HERE, "collision_phase2_tetragonal_unresolved_overlay.json")
SS_MD5_EXPECTED = "64cc7bb82e85164914d7ec441cfc1304"
TIMEOUT_S = 600
RUN_DATE = "2026-09-04"
SNAPSHOT = "2026-09-04"
ADDENDUM_HEAD = ("## Addendum 2026-09-04 (subagent #154, Claude Fable 5.1): the 62 unstored printed rows recomputed "
                 "with the documented conventions; the 106 UNRESOLVED tetragonal statuses settled")
TWO_ORIGIN = {85, 86, 88, 125, 126, 129, 130, 133, 134, 137, 138, 141, 142}
ENANTIO_SECOND = {95, 96}


class RowTimeout(Exception):
    pass


def _alarm(signum, frame):
    raise RowTimeout()


def md5_file(path):
    return hashlib.md5(open(path, "rb").read()).hexdigest()


def sha256_file(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def store_sha_expected():
    return next(t for t in open(SHA_FILE).read().split()
                if len(t) == 64 and all(c in "0123456789abcdef" for c in t))


def all_conventions(group, origin):
    """[(label, fn, documented)] — collision_phase2_check.conversions_for (documented,
    primary first) + the other origin / enantiomorph reading (identity, recorded only)."""
    out = [(lab, fn, True) for lab, fn in conversions_for(group, origin)]
    if group in TWO_ORIGIN:
        out.append(("other origin reading: origin choice 1, printed point verbatim (no shift; = pass P2's run, quarantined)", lambda p: p, False))
    elif group in ENANTIO_SECOND:
        out.append(("other enantiomorph reading: first-member coordinates verbatim (identity; = pass P2's run, quarantined)", lambda p: p, False))
    return out


def one_cell(group, Xc, b):
    """One evaluation -> (record, seconds); never raises on ChainError / crash.
    NO timing inside the record: the JSON must be byte-identical across runs
    (CORRECTION 2026-09-04: the first version carried per-cell `secs` and a
    top-level `wall_seconds`, which made both JSON md5s run-dependent)."""
    t0 = time.time()
    try:
        r = S2.evaluate(group, Xc, F(b), "collision_phase2_rows")
    except S2.ChainError as exc:
        return OrderedDict([("ok", False), ("error", f"ChainError {exc.reason}: {exc.detail}"[:200])]), time.time() - t0
    except Exception as exc:                       # crash: recorded, never silent
        return OrderedDict([("ok", False), ("error", f"crash {type(exc).__name__}: {exc}"[:200])]), time.time() - t0
    return OrderedDict([
        ("ok", True), ("f", list(r["fvec"])), ("p", S2.pvec_compact(r["pvec"])), ("aut", r["aut"]),
        ("stab", r["stabilizer_order"]), ("orbit_conventional", r["orbit_conventional"]), ("period", r["period"]),
        ("nonsimple", r["nonsimple"]), ("cutoff_D2", r["cutoff_D2"]), ("congruence_checked", r["congruence_checked"]),
        ("code", r["code_str"]), ("code_id", code_id(r["code_str"])),
    ]), time.time() - t0


def main():
    t_all = time.time()
    # ---- stores / inputs, sha-verified --------------------------------------------
    want = store_sha_expected()
    sha_before = sha256_file(STORE)
    assert sha_before == want and sha_before.startswith("71685b9a"), (sha_before, want)
    import gzip
    assert hashlib.sha256(gzip.open(STORE_GZ, "rb").read()).hexdigest() == want, "phase2_types.json.gz != SHA256SUMS"
    store = json.load(open(STORE))
    types = store["types"]
    code2type = {v["canon_code"]: k for k, v in types.items()}
    assert len(code2type) == len(types)
    origin = json.load(open(ORIGIN_JSON))
    ss_md5 = md5_file(SS_JSON)
    assert ss_md5 == SS_MD5_EXPECTED, ss_md5
    ss = json.load(open(SS_JSON))
    assert ss["store_tetragonal_sha256"] == want
    verdicts = ss["verdicts"]
    unresolved = sorted(t for t, v in verdicts.items() if v["status"] == "UNRESOLVED")
    assert len(unresolved) == 106, len(unresolved)
    assert not any(verdicts[t]["in_top15_shortlist"] for t in unresolved)
    certified14 = sorted(t for t, v in verdicts.items() if v["in_top15_shortlist"] and v["shortlist_doc_status"] == "SURVIVOR")
    assert len(certified14) == 14 and not (set(certified14) & set(unresolved)), "a certified survivor is UNRESOLVED?"
    # the 62 rows and the types hanging on each
    tables = json.load(open(TABLES))
    row_lookup = {}
    for key, blk in tables.items():
        if key == "_meta":
            continue
        for g in blk["groups"]:
            for r in blk["rows"]:
                row_lookup[(g, r["b"], tuple(r["pt"]))] = (tuple(r["f"]), r["pdf_page"])
    rows = OrderedDict()
    for t in unresolved:
        for r in verdicts[t]["unstored_rows"]:
            k = (r["group"], r["b"], tuple(r["pt"]))
            assert k in row_lookup, ("row not in the digitization", k)
            f_printed, pdf = row_lookup[k]
            assert pdf == r["pdf_page"] and f_printed == tuple(verdicts[t]["f_vector"]), (k, t)
            rows.setdefault(k, OrderedDict([("group", k[0]), ("symbol", S2.GROUPS[k[0]]["international_short"]), ("b", k[1]),
                                            ("pt_printed", list(k[2])), ("pdf_page", pdf), ("printed_page", pdf - 5),
                                            ("f_printed", list(f_printed)), ("types_hanging", [])]))
            rows[k]["types_hanging"].append(t)
    assert len(rows) == 62, len(rows)
    assert Counter(k[0] for k in rows) == Counter({141: 15, 142: 8, 88: 6, 86: 5, 95: 5, 96: 5, 133: 4, 130: 3, 134: 3, 138: 3, 137: 2, 126: 2, 80: 1})

    # ---- 1. recompute every row under every convention -----------------------------
    old = signal.signal(signal.SIGALRM, _alarm)
    results = OrderedDict()
    row_secs = {}                                  # timings live in the run log only, never in the hashed JSON
    try:
        for i, (k, row) in enumerate(rows.items(), 1):
            g, b, pt = k
            X = tuple(F(s) for s in pt)
            convs = all_conventions(g, origin)
            cells = []
            signal.alarm(TIMEOUT_S)
            timed_out = False
            row_secs[k] = 0.0
            try:
                for lab, fn, documented in convs:
                    Xc = fn(X)
                    c, dt = one_cell(g, Xc, b)
                    row_secs[k] += dt
                    c = OrderedDict([("convention", lab), ("documented", documented), ("point_ours", pt_str(Xc))] + list(c.items()))
                    if c["ok"]:
                        c["reproduces_printed_f"] = c["f"] == row["f_printed"]
                        c["store_hit"] = code2type.get(c["code"])
                        c["store_hit_status_v4"] = (verdicts[c["store_hit"]]["status"] if c["store_hit"] in verdicts else
                                                    ("printed-only" if c["store_hit"] and types[c["store_hit"]]["schmitt_printed_only"] else
                                                     ("cubic-first" if c["store_hit"] else None)))
                    cells.append(c)
            except RowTimeout:
                timed_out = True
            finally:
                signal.alarm(0)
            doc_repro = [c for c in cells if c["documented"] and c["ok"] and c["reproduces_printed_f"]]
            codes = sorted({c["code"] for c in doc_repro})
            if timed_out:
                status = "TIMEOUT-DEFERRED"
            elif not doc_repro:
                status = "QUARANTINE"
            elif len(codes) > 1:
                status = "AMBIGUOUS"
            else:
                status = "REPRODUCED"
            primary = doc_repro[0] if doc_repro else None
            other = [c for c in cells if not c["documented"]]
            other_repro = [c for c in other if c["ok"] and c["reproduces_printed_f"]]
            res = OrderedDict(row)
            res.update([
                ("status", status),
                ("n_conventions_run", len(cells)),
                ("n_documented_reproducing", len(doc_repro)),
                ("documented_conventions_agree", len(codes) <= 1),
                ("convention_used", primary["convention"] if primary else None),
                ("point_ours", primary["point_ours"] if primary else None),
                ("f", primary["f"] if primary else None), ("p", primary["p"] if primary else None),
                ("aut", primary["aut"] if primary else None), ("stab", primary["stab"] if primary else None),
                ("period", primary["period"] if primary else None),
                ("code", primary["code"] if primary else None), ("code_id", primary["code_id"] if primary else None),
                ("store_hit", primary["store_hit"] if primary else None),
                ("store_hit_status_v4", primary["store_hit_status_v4"] if primary else None),
                ("f_vectors_obtained", sorted({tuple(c["f"]) for c in cells if c["ok"]})),
                ("other_reading_reproduces_printed_f", bool(other_repro)),
                ("other_reading_code_equal", (other_repro[0]["code"] == primary["code"]) if (other_repro and primary) else None),
                ("cells", cells),
            ])
            results[k] = res
            print(f"[{i:2d}/62] IT({g}) {res['symbol']} b={b} pt=({', '.join(pt)}) f_printed={tuple(row['f_printed'])} -> {status} "
                  f"code={res['code_id']} hit={res['store_hit']} ({res['store_hit_status_v4']}) p={res['p']} aut={res['aut']} "
                  f"conv={len(cells)} docrepro={len(doc_repro)} other_repro={bool(other_repro)} hang={len(row['types_hanging'])} [{row_secs[k]:.2f}s, log only]", flush=True)
    finally:
        signal.signal(signal.SIGALRM, old)

    # regression: rows already recomputed by collision_phase2_check.py must give the same code
    cj = json.load(open(CHECK_JSON))
    assert cj["store_sha256"] == want
    regress = []
    for p in cj["pairs"]:
        if p["p2"] != "unres":
            continue
        k = (p["group"], p["b"], tuple(p["point"]))
        if k in results:
            same_code = results[k]["code"] == p["code"]
            regress.append(OrderedDict([("pair", p["pair"]), ("group", p["group"]), ("b", p["b"]), ("pt", list(p["point"])),
                                        ("code_id_check", code_id(p["code"])), ("code_id_here", results[k]["code_id"]), ("equal", same_code)]))
    assert len(regress) == 2 and all(r["equal"] for r in regress), regress

    # ---- 2. verdicts for the 106 UNRESOLVED types -----------------------------------
    row_by_key = results
    all_row_codes = {res["code"]: k for k, res in results.items() if res["code"]}
    overlay = OrderedDict()
    secondary_hits = []
    for t in unresolved:
        ent = types[t]
        per_row = []
        any_same = any_quar = False
        for r in verdicts[t]["unstored_rows"]:
            k = (r["group"], r["b"], tuple(r["pt"]))
            res = row_by_key[k]
            if res["status"] != "REPRODUCED":
                any_quar = True
                per_row.append(OrderedDict([("group", k[0]), ("b", k[1]), ("pt", list(k[2])), ("pdf_page", res["pdf_page"]),
                                            ("row_status", res["status"]), ("verdict", "QUARANTINED-ROW")]))
                continue
            same = res["code"] == ent["canon_code"]
            any_same |= same
            per_row.append(OrderedDict([("group", k[0]), ("b", k[1]), ("pt", list(k[2])), ("pdf_page", res["pdf_page"]),
                                        ("row_status", "REPRODUCED"), ("convention", res["convention_used"]),
                                        ("row_cell_code_id", res["code_id"]), ("row_cell_store_hit", res["store_hit"]),
                                        ("verdict", "SAME TYPE" if same else "DIFFERENT TYPE")]))
        status = "COLLISION" if any_same else ("UNRESOLVED" if any_quar else "SURVIVOR")
        # secondary: the type's code equals the cell of a row it does not hang on
        hang_keys = {(r["group"], r["b"], tuple(r["pt"])) for r in verdicts[t]["unstored_rows"]}
        sec = [list(k) for k, res in results.items() if res["code"] == ent["canon_code"] and k not in hang_keys]
        sec = [[k[0], k[1], list(k[2])] for k in ((x[0], x[1], x[2]) for x in sec)]
        if sec:
            secondary_hits.append(OrderedDict([("type", t), ("status_primary_rule", status), ("rows_not_hung_on_with_this_cell", sec)]))
        overlay[t] = OrderedDict([
            ("status", status), ("status_v4", "UNRESOLVED"),
            ("f_vector", ent["f_vector"]), ("groups_sighted", verdicts[t]["groups_sighted"]),
            ("g4_certified", False), ("rows", per_row),
            ("n_rows", len(per_row)), ("n_same", sum(1 for x in per_row if x["verdict"] == "SAME TYPE")),
            ("n_different", sum(1 for x in per_row if x["verdict"] == "DIFFERENT TYPE")),
            ("n_quarantined_rows", sum(1 for x in per_row if x["verdict"] == "QUARANTINED-ROW")),
            ("secondary_hit_rows", sec),
        ])
    counts_after_106 = OrderedDict(sorted(Counter(v["status"] for v in overlay.values()).items()))
    before = OrderedDict(ss["counts_combined"])
    after = OrderedDict([("COLLISION", before["COLLISION"] + counts_after_106.get("COLLISION", 0)),
                         ("SURVIVOR", before["SURVIVOR"] + counts_after_106.get("SURVIVOR", 0)),
                         ("UNRESOLVED", counts_after_106.get("UNRESOLVED", 0))])
    assert sum(after.values()) == 404
    row_status_counts = OrderedDict(sorted(Counter(r["status"] for r in results.values()).items()))
    surprises = []
    for k, res in results.items():
        if res["other_reading_reproduces_printed_f"]:
            surprises.append(f"IT({k[0]}) b={k[1]} pt=({', '.join(k[2])}): the OTHER (verbatim) reading also reproduces the printed f "
                             f"(code equal to the documented convention's: {res['other_reading_code_equal']})")
        if res["status"] != "REPRODUCED":
            surprises.append(f"IT({k[0]}) b={k[1]} pt=({', '.join(k[2])}): {res['status']} — f-vectors obtained {res['f_vectors_obtained']}; "
                             + "; ".join(f"{c['convention'][:40]}: {c.get('error') or c['f']}" for c in res["cells"]))
        if not res["documented_conventions_agree"]:
            surprises.append(f"IT({k[0]}) b={k[1]} pt=({', '.join(k[2])}): documented conventions disagree on the code")
    # row cells that are stored types OUTSIDE the 106: classified, never silently dropped.
    #   COLLISION / printed-only = an S-cell reproducing one more printed row (expected: that is what an S-cell is);
    #   cubic-first = a cubic-store type at a printed tetragonal point (cross-system fact; cubic-first types are
    #   not-screened by the phase-2 screens by construction); SURVIVOR = would contradict the v4 status (a surprise).
    non_unres_hits = [(k, res["store_hit"], res["store_hit_status_v4"]) for k, res in results.items()
                      if res["store_hit"] and res["store_hit_status_v4"] != "UNRESOLVED"]
    hits_expected = [(k, h, s) for k, h, s in non_unres_hits if s in ("COLLISION", "printed-only")]
    hits_cubic_first = [(k, h, s) for k, h, s in non_unres_hits if s == "cubic-first"]
    hits_survivor = [(k, h, s) for k, h, s in non_unres_hits if s == "SURVIVOR"]
    assert len(hits_expected) + len(hits_cubic_first) + len(hits_survivor) == len(non_unres_hits)
    for k, hit, st in hits_survivor:
        surprises.append(f"IT({k[0]}) b={k[1]} pt=({', '.join(k[2])}): row cell = stored type {hit} whose v4 status is SURVIVOR "
                         "(a printed cell of a type that reads SURVIVOR: contradicts v4; recorded, status outside the 106 not changed here)")
    for k, hit, st in hits_cubic_first:
        surprises.append(f"IT({k[0]}) b={k[1]} pt=({', '.join(k[2])}): row cell = cubic-first store type {hit} "
                         f"(f {tuple(results[k]['f'])}, p {results[k]['p']}, aut {results[k]['aut']}): a cubic-store type IS Schmitt's printed representative "
                         "at this tetragonal row (cross-system fact; cubic-first types are not-screened by the phase-2 screens by construction; recorded only)")
    for s in secondary_hits:
        surprises.append(f"type {s['type']} ({s['status_primary_rule']} by its hung-on rows) also equals the recomputed cell of a row it does not hang on "
                         f"(a printed cell of the type in a group where our menu never sighted it): {s['rows_not_hung_on_with_this_cell']}; no status effect")
    sha_after = sha256_file(STORE)
    assert sha_after == sha_before == want, "STORE CHANGED"

    def rk(k):
        return f"IT{k[0]}|b={k[1]}|pt=({','.join(k[2])})"

    # ---- 3. write JSONs (sorted keys) ---------------------------------------------------
    rows_out = OrderedDict([
        ("generated_by", "harness/collision_phase2_tetragonal_rows_recompute.py (subagent #154, Claude Fable 5.1), " + RUN_DATE),
        ("snapshot", SNAPSHOT),
        ("chain", "sweep_phase2_tetragonal.evaluate (accepted phase-2 modules phase2/metric.py, phase2/sweep_voronoi_gram.py, phase2/exact_cell_gram.py; exact order_cycle fallback); certificate asserted per cell"),
        ("conventions", "PHASE2_SCHMITT_ORIGIN_CHECK.md via collision_phase2_check.conversions_for (two-origin groups: every shift reproducing all rows, primary = best_shift; 95/96: z -> -z primary + the other transforms reproducing all rows; IT(80): verbatim) plus the other origin / enantiomorph reading (identity) recorded, not counted"),
        ("row_status_rule", "REPRODUCED = printed f reproduced under >= 1 documented convention and all reproducing documented conventions give one canonical code; AMBIGUOUS = they disagree (treated as quarantine); QUARANTINE = no documented convention reproduces the printed f (f-vectors / chain errors listed); TIMEOUT-DEFERRED = 600 s cap"),
        ("store_sha256_before", sha_before), ("store_sha256_after", sha_after),
        ("storeside_json_md5", ss_md5),
        ("n_rows", len(results)), ("row_status_counts", row_status_counts),
        ("rows_per_group", OrderedDict(sorted((str(g), n) for g, n in Counter(k[0] for k in results).items()))),
        ("regression_vs_collision_phase2_check", regress),
        ("row_cells_that_are_stored_types_outside_the_106", OrderedDict([
            ("expected_S_cell_hits_COLLISION_or_printed_only", [OrderedDict([("row", rk(k)), ("type", h), ("status_v4", s)]) for k, h, s in hits_expected]),
            ("cubic_first_hits", [OrderedDict([("row", rk(k)), ("type", h), ("status_v4", s)]) for k, h, s in hits_cubic_first]),
            ("SURVIVOR_hits", [OrderedDict([("row", rk(k)), ("type", h), ("status_v4", s)]) for k, h, s in hits_survivor]),
        ])),
        ("surprises", surprises),
        ("timing_note", "no timing field is stored in this file (run log only), so the file is byte-identical across runs; CORRECTION 2026-09-04: the first run's file carried per-cell secs and wall_seconds"),
        ("rows", OrderedDict((rk(k), res) for k, res in results.items())),
    ])
    with open(OUT_ROWS, "w") as fh:
        json.dump(rows_out, fh, indent=1, sort_keys=True)
        fh.write("\n")
    rows_md5 = md5_file(OUT_ROWS)
    overlay_out = OrderedDict([
        ("generated_by", rows_out["generated_by"]), ("snapshot", SNAPSHOT),
        ("rule", "per UNRESOLVED type (collision_phase2_tetragonal_storeside.json status UNRESOLVED): compare its canonical code with the recomputed cell of every printed row it hangs on (unstored_rows): any SAME TYPE -> COLLISION (the type reproduces one of his printed cells; first-realization reframe); every row REPRODUCED and DIFFERENT TYPE -> SURVIVOR ('not matched against the records checked as of 2026-09-04', never novelty); any row not REPRODUCED and no SAME -> UNRESOLVED"),
        ("rows_file", os.path.basename(OUT_ROWS)), ("rows_file_md5", rows_md5),
        ("storeside_json_md5", ss_md5), ("store_sha256", sha_before),
        ("n_types", len(overlay)),
        ("counts_106", counts_after_106),
        ("counts_404_before_v4", before), ("counts_404_after_v5", after),
        ("certified_14_untouched", certified14),
        ("secondary_hits", secondary_hits),
        ("still_unresolved", [t for t, v in overlay.items() if v["status"] == "UNRESOLVED"]),
        ("verdicts", overlay),
    ])
    with open(OUT_OVERLAY, "w") as fh:
        json.dump(overlay_out, fh, indent=1, sort_keys=True)
        fh.write("\n")
    overlay_md5 = md5_file(OUT_OVERLAY)

    # ---- 4. addendum (append-only, once) ---------------------------------------------------
    existing = open(OUT_MD).read()
    appended = False
    if ADDENDUM_HEAD not in existing:
        L = ["", ADDENDUM_HEAD, "",
             f"Script: `collision_phase2_tetragonal_rows_recompute.py` (venv python, single process, wall {time.time() - t_all:.0f} s). Store `phase2_types.json` read-only, sha256 {sha_before} before and after (= `phase2_types.SHA256SUMS`; .gz decompressed equal). "
             f"Inputs: `collision_phase2_tetragonal_storeside.json` (md5 {ss_md5}; its 106 UNRESOLVED types and their `unstored_rows` = the 62 rows below), `schmitt_tetragonal_tables.json` (row citations; PDF page = printed + 5), `phase2_schmitt_origin_check.json` (conventions). "
             "Chain: `sweep_phase2_tetragonal.evaluate` (accepted phase-2 modules; exact order_cycle fallback), certificate asserted per cell. "
             f"Outputs: `collision_phase2_tetragonal_rows_recomputed.json` (every computed cell: {sum(len(r['cells']) for r in results.values())} cells over 62 rows; sorted keys; md5 {rows_md5}) and "
             f"`collision_phase2_tetragonal_unresolved_overlay.json` (the 106 verdicts; sorted keys; md5 {overlay_md5}).", "",
             "**Conventions (PHASE2_SCHMITT_ORIGIN_CHECK.md, each verified on ALL printed rows of its group; `collision_phase2_check.conversions_for` reused verbatim):** two-origin groups: p_ours = p_his + s for every shift s that reproduced all rows (primary = best_shift); "
             "second enantiomorphs 95/96: z -> -z primary, the other signed-axis transforms as robustness alternatives; IT(80): printed point verbatim. The OTHER reading (printed point verbatim in our setting for two-origin / 95 / 96 rows = what pass P2 ran and quarantined) was run and recorded per row but never counted. "
             "Row status: REPRODUCED = printed f under >= 1 documented convention with one canonical code across the reproducing conventions; else QUARANTINE (f-vectors obtained listed) / AMBIGUOUS. "
             "Type verdict (per the 106 UNRESOLVED): any hung-on row SAME -> COLLISION; all hung-on rows REPRODUCED and DIFFERENT -> SURVIVOR; any hung-on row not REPRODUCED and no SAME -> UNRESOLVED.", "",
             f"- Rows: {len(results)} recomputed; status counts {dict(row_status_counts)}; documented conventions agree on the code in {sum(1 for r in results.values() if r['documented_conventions_agree'])}/62 rows; "
             f"the other (verbatim) reading reproduces the printed f in {sum(1 for r in results.values() if r['other_reading_reproduces_printed_f'])}/62 rows (expected 0: those runs are exactly the P2 quarantines). "
             f"Regression: the two rows already recomputed for the shortlist (Q14 IT(86), Q24 IT(80)) give the same codes here.",
             f"- Types: the 106 UNRESOLVED -> {', '.join(f'{k} {v}' for k, v in counts_after_106.items())}. Tetragonal menu-sighted totals (404): before (v4) {', '.join(f'{k} {v}' for k, v in before.items())}; after {', '.join(f'{k} {v}' for k, v in after.items())}. "
             f"The 14 certified survivors were never UNRESOLVED and are untouched (asserted); `cd4fb52572edcb73` stays COLLISION.",
             f"- Secondary check (a type's code equal to the cell of a row it does NOT hang on): {len(secondary_hits)} case(s)" + ("." if not secondary_hits else ": " + "; ".join(f"`{s['type']}` ({s['status_primary_rule']} by its hung-on rows) at {s['rows_not_hung_on_with_this_cell']}; no status effect" for s in secondary_hits)),
             f"- Row cells that are stored types OUTSIDE the 106 (statuses not changed here): {len(non_unres_hits)} = {len(hits_expected)} S-cells already COLLISION / printed-only (expected: an S-cell reproducing one more printed row"
             + (": " + ", ".join(f"IT({k[0]}) b={k[1]} -> `{h}` ({s})" for k, h, s in hits_expected) if hits_expected else "") + f") + {len(hits_cubic_first)} cubic-first store types (cross-system fact, not-screened by construction"
             + (": " + ", ".join(f"IT({k[0]}) b={k[1]} pt=({', '.join(k[2])}) -> `{h}` f {tuple(results[k]['f'])} p `{results[k]['p']}` aut {results[k]['aut']}" for k, h, s in hits_cubic_first) if hits_cubic_first else "") + f") + {len(hits_survivor)} SURVIVOR types (would contradict v4"
             + (": " + ", ".join(f"IT({k[0]}) b={k[1]} -> `{h}`" for k, h, s in hits_survivor) if hits_survivor else "") + f"); row cells stored under no id: {sum(1 for r in results.values() if r['code'] and not r['store_hit'])} (types the menu never sampled; read-only, not added).",
             f"- Surprises recorded: {len(surprises)}" + ("." if not surprises else "\n" + "\n".join(f"  - {s}" for s in surprises)),
             "- LANGUAGE (G5): SURVIVOR = 'not matched against the records checked as of " + SNAPSHOT + "', never novelty (Schmitt prints ONE representative per (group, f) from a grid sampling); COLLISION = the type reproduces one of his printed cells (first-realization reframe). "
             "Digitization caveat as above (single visual pass, text-layer cross-checked, not re-keyed); every row below cites its PDF page.",
             "", "### Row-level results (62 rows)", "",
             "| # | IT | b | printed point | PDF p. (printed) | printed f | status | convention used | point in our setting | f | p | aut | stab | code id / store hit (v4 status) | conv. agree | other reading reproduces f | types hanging | secs |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for i, (k, r) in enumerate(results.items(), 1):
            hit = f"`{r['code_id']}`" + (f" = stored `{r['store_hit']}` ({r['store_hit_status_v4']})" if r["store_hit"] else " (not stored)") if r["code_id"] else "-"
            L.append(f"| {i} | {k[0]} {r['symbol']} | {k[1]} | ({', '.join(k[2])}) | {r['pdf_page']} ({r['printed_page']}) | {tuple(r['f_printed'])} | **{r['status']}** | {r['convention_used'] or '-'} | {r['point_ours'] or '-'} | "
                     f"{tuple(r['f']) if r['f'] else '-'} | {('`' + r['p'] + '`') if r['p'] else '-'} | {r['aut'] if r['aut'] is not None else '-'} | {r['stab'] if r['stab'] is not None else '-'} | {hit} | "
                     f"{'YES (%d)' % r['n_documented_reproducing'] if r['documented_conventions_agree'] else 'NO'} | {r['other_reading_reproduces_printed_f']} | {len(r['types_hanging'])} | {round(row_secs[k], 1)} |")
        L += ["", "### Type-level verdicts (106 types)", "",
              "| type | f | groups sighted | rows hung on: IT b -> verdict (row cell id) | verdict |", "|---|---|---|---|---|"]
        for t, v in overlay.items():
            rs = "; ".join(f"IT{x['group']} {x['b']} -> {x['verdict']}" + (f" (`{x['row_cell_code_id']}`)" if x.get("row_cell_code_id") else "") for x in v["rows"])
            L.append(f"| `{t}` | {tuple(v['f_vector'])} | {v['groups_sighted']} | {rs} | **{v['status']}** |")
        L += ["", f"Still UNRESOLVED after this pass: {len(overlay_out['still_unresolved'])}" + ("." if not overlay_out["still_unresolved"] else " — " + ", ".join(f"`{t}`" for t in overlay_out["still_unresolved"]) + "."), ""]
        with open(OUT_MD, "a") as fh:
            fh.write("\n".join(L))
        appended = True
    correction = False
    if ADDENDUM_HEAD in existing and not (("md5 %s" % rows_md5) in existing and ("md5 %s" % overlay_md5) in existing):
        # the addendum above was written by a run whose JSON md5s are not the current ones: append a dated
        # correction (never edit the old text). Content is asserted identical in the correction itself.
        C = ["", f"### CORRECTION {time.strftime('%Y-%m-%d %H:%M %Z')} (subagent #154): stable md5s", "",
             f"The md5s stated in the #154 addendum text above were RUN-DEPENDENT: the first version of the rows JSON carried a top-level `wall_seconds` and a per-cell `secs`, and the overlay JSON referenced the rows file by that changing md5, so the main-session re-run produced different hashes with identical verdict content. "
             f"Timings were moved to the run log (no timing field in either JSON), and the two files are now byte-identical across runs. STABLE md5s: `collision_phase2_tetragonal_rows_recomputed.json` md5 {rows_md5}; `collision_phase2_tetragonal_unresolved_overlay.json` md5 {overlay_md5}. "
             f"Content unchanged: rows {dict(row_status_counts)}; the 106 -> {', '.join(f'{k} {v}' for k, v in counts_after_106.items())}; 404 after: {', '.join(f'{k} {v}' for k, v in after.items())}; the row-level and type-level tables above are the content of record and are asserted equal to the JSONs by build_catalog.py and verify_counts_independent.py (v5).", ""]
        with open(OUT_MD, "a") as fh:
            fh.write("\n".join(C))
        correction = True

    print(f"ROWS: {dict(row_status_counts)}; the 106 -> {dict(counts_after_106)}; 404 before {dict(before)} after {dict(after)}")
    print(f"secondary hits {len(secondary_hits)}; non-UNRESOLVED store hits {len(non_unres_hits)}; surprises {len(surprises)}")
    for s in surprises:
        print("  SURPRISE:", s)
    print(f"rows JSON md5 {rows_md5}; overlay JSON md5 {overlay_md5}; addendum appended: {appended}; correction appended: {correction}; store sha unchanged: {sha_after == want}; wall {time.time() - t_all:.1f} s (log only)")
    ok = all(r["status"] in ("REPRODUCED", "QUARANTINE", "AMBIGUOUS", "TIMEOUT-DEFERRED") for r in results.values()) and sha_after == want
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
