#!/usr/bin/env python
"""phase2_hex_schmitt_180_check.py — read-only diligence on the 46 batch-2
schmitt_fvec_mismatch quarantines (all in IT(180) P6_222; the 180/181 table's
normalizer remark reads "(only the normalizer for IT(181) but not for IT(180))",
i.e. the printed points belong to IT(181), the SECOND-listed member — the
pre-registered enantiomorph rule applied z -> -z only to the second-listed
group, so IT(180) ran the points verbatim and 46 of 69 rows failed).
Pattern: batch 1's phase2_schmitt_origin_check.py (read-only; nothing added to
the store). Each quarantined row is re-run with z -> -z (then H1) through the
accepted batch-2 chain; the printed f-vector must reproduce; the canonical
code is compared with the store (stored id or 'not stored'). The 13 triage
UNRESOLVED types are then resolved read-only against these cells.
Run: python3 phase2_hex_schmitt_180_check.py
Writes: PHASE2_HEX_SCHMITT_180_CHECK.md, phase2_hex_schmitt_180_check.json
"""
import hashlib, json, os, sys, time
from fractions import Fraction as F
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sweep_phase2_hexagonal as SH
STORE = os.path.join(HERE, "phase2_hexagonal_types.json")
SHORTLIST = os.path.join(HERE, "triage_phase2_hex_shortlist.json")

def sha(path):
    h = hashlib.sha256(); h.update(open(path, "rb").read()); return h.hexdigest()

def code_id(c):
    return hashlib.sha1(c.encode("ascii")).hexdigest()[:16]

t0 = time.time()
s0 = sha(STORE)
store = json.load(open(STORE)); types = store["types"]
code2type = {t["canon_code"]: tid for tid, t in types.items()}
q = [x for x in store["quarantines"] if x["reason"] == "schmitt_fvec_mismatch"]
assert all(x["group"] == 180 for x in q) and len(q) == 46, (len(q), {x["group"] for x in q})
rows = []
for x in q:
    # x['point'] is the ITA point after H1; recover the printed B'' point from the row table
    pass
tables = json.load(open(os.path.join(HERE, "schmitt_hexagonal_tables.json")))
blk = tables["180_181"]
printed = {(tuple(r["pt"]), r["b"]): r for r in blk["rows"]}
out = []
for x in q:
    fv = tuple(int(v) for v in x["detail"].split("printed (")[1].split(")")[0].split(","))
    # find the printed row: H1(pt) == x['point']
    cand = [r for (pt, b), r in printed.items() if b == x["b"] and
            [SH.frac_str(v) for v in SH.h1(tuple(F(s) for s in pt))] == x["point"] and tuple(r["f"]) == fv]
    assert len(cand) == 1, (x, cand)
    r = cand[0]
    p = SH.h1(SH.zflip(tuple(F(s) for s in r["pt"])))
    try:
        e = SH.evaluate(180, p, F(r["b"]), "check180")
        ok = tuple(e["fvec"]) == fv
        hit = code2type.get(e["code_str"])
        out.append({"printed_f": fv, "b": r["b"], "pt_Bpp": r["pt"], "pdf": r["pdf_page"], "conversion": "z->-z then H1",
                    "point_ITA": [SH.frac_str(v) for v in p], "exact_f": list(e["fvec"]), "reproduced": ok,
                    "p": SH.pvec_compact(e["pvec"]), "aut": e["aut"], "stab": e["stabilizer_order"],
                    "store_hit": hit, "code_id": code_id(e["code_str"]), "code": e["code_str"]})
    except SH.ChainError as exc:
        out.append({"printed_f": fv, "b": r["b"], "pt_Bpp": r["pt"], "pdf": r["pdf_page"], "conversion": "z->-z then H1",
                    "reproduced": False, "quarantine": f"{exc.reason}: {exc.detail}"})
n_ok = sum(1 for o in out if o["reproduced"])
# resolve the triage's UNRESOLVED types against these cells
sl = json.load(open(SHORTLIST))
unres_ids = [tid for tid in types if types[tid]["first_sighting_system"] == SH.SYSTEM
             and any(s["pass"] in {"P1", "P3", "P4", "P5"} for s in types[tid]["sightings"])]
cells_by_f = {}
for o in out:
    if o["reproduced"]:
        cells_by_f.setdefault(tuple(o["printed_f"]), []).append(o)
resolved = []
for tid in sorted(unres_ids):
    t = types[tid]
    if 180 not in {s["group"] for s in t["sightings"]}:
        continue
    fv = tuple(t["f_vector"])
    if fv not in cells_by_f:
        continue
    scell = any(s["pass"] == "P2" for s in t["sightings"])
    same = [o for o in cells_by_f[fv] if o["code"] == t["canon_code"]]
    # triage verdict class: UNRESOLVED iff not S-cell (S-cell types were already COLLISION in the triage)
    cls = "COLLISION (S-cell already)" if scell else "UNRESOLVED in the triage"
    resolved.append({"id": tid, "f": list(fv), "aut": t["aut_order"], "rows_180_with_f": len(cells_by_f[fv]),
                     "triage_class": cls, "same": len(same),
                     "verdict": ("SAME TYPE at a printed 180 row -> would be COLLISION (reframe)" if same
                                 else "DIFFERENT at every printed 180 row -> would be SURVIVOR (read-only; the 180 pair only)")})
n_unres = sum(1 for r in resolved if r["triage_class"].startswith("UNRESOLVED"))
s1 = sha(STORE)
L = ["# Batch-2 read-only check: the 46 IT(180) P6_222 Schmitt f-vector mismatches (2026-09-04)", "",
     f"Store `phase2_hexagonal_types.json` sha256 {s0} (unchanged after: {s0 == s1}); nothing added.",
     "Cause (Schmitt's own remark on the 180/181 table, PDF 114): the normalizer/basis given is \"only the normalizer for IT(181) but not for IT(180)\" — the printed points are IT(181)'s (the second-listed member); the pre-registered rule applied z -> -z only to the second-listed group, so IT(180) ran verbatim and 46 of 69 rows failed (the 23 that passed are z-flip-insensitive). IT(181) reproduced all 69 verbatim. Same pattern as 178/179 (remark names 178; 179 needed z -> -z on 77 of 97 rows) and as 95/96 in batch 1.", "",
     f"Result: **{n_ok} of {len(out)} quarantined rows reproduce the printed f-vector under z -> -z (then H1)**; "
     f"{sum(1 for o in out if o.get('store_hit'))} of those cells are already in the store, {sum(1 for o in out if o['reproduced'] and not o.get('store_hit'))} are not (read-only, not added).", "",
     "| printed f | b | printed point (B'') | PDF | point (ITA) | exact f | p | aut | stab | store hit |", "|---|---|---|---|---|---|---|---|---|---|"]
for o in out:
    if o["reproduced"]:
        L.append(f"| {o['printed_f']} | {o['b']} | ({', '.join(o['pt_Bpp'])}) | {o['pdf']} | ({', '.join(o['point_ITA'])}) | {tuple(o['exact_f'])} | {o['p']} | {o['aut']} | {o['stab']} | {o['store_hit'] or 'not stored'} |")
    else:
        L.append(f"| {o['printed_f']} | {o['b']} | ({', '.join(o['pt_Bpp'])}) | {o['pdf']} | - | FAIL | {o.get('quarantine') or o.get('exact_f')} | | | |")
L += ["", f"## Menu-sighted hexagonal types with an IT(180) sighting and an f-vector among these 46 rows ({len(resolved)}; "
      f"of which {n_unres} are the triage's UNRESOLVED types), resolved read-only", "",
      "| id | f | aut | printed 180 rows with this f | triage class | SAME | verdict |", "|---|---|---|---|---|---|---|"]
for r in resolved:
    L.append(f"| `{r['id']}` | {tuple(r['f'])} | {r['aut']} | {r['rows_180_with_f']} | {r['triage_class']} | {r['same']} | {r['verdict']} |")
L += ["", "Limits: read-only; the store's 46 quarantines stand as recorded (the sweep is not patched); these cells enter no count. "
      "Language: a DIFFERENT verdict is not novelty; snapshot language only.", f"", f"Wall {time.time() - t0:.0f} s."]
open(os.path.join(HERE, "PHASE2_HEX_SCHMITT_180_CHECK.md"), "w").write("\n".join(L) + "\n")
json.dump({"store_sha256": s0, "unchanged": s0 == s1, "rows": out, "resolved": resolved}, open(os.path.join(HERE, "phase2_hex_schmitt_180_check.json"), "w"), indent=1)
print(f"reproduced {n_ok}/{len(out)}; in store {sum(1 for o in out if o.get('store_hit'))}; types with 180 pairs: {len(resolved)} "
      f"({n_unres} triage-UNRESOLVED: {sum(1 for r in resolved if r['same'] and r['triage_class'].startswith('UNRESOLVED'))} SAME, "
      f"{sum(1 for r in resolved if not r['same'] and r['triage_class'].startswith('UNRESOLVED'))} DIFFERENT); store unchanged {s0 == s1}")
