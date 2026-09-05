#!/usr/bin/env python3
"""Diff the blind re-key (schmitt_hexagonal_rekey.json, agent #147) against the
accepted digitization (schmitt_hexagonal_tables.json, agent #143).

Match key per row: (block, b-ratio, generating point) as exact Fractions.
Reports: row-count per block, f-vector differences on matched keys, keys present
in one file only (which also catches b-ratio / point differences), page-number
differences, and header-fact differences (normalizer, grid points, bounds).
Read-only on both inputs.
"""
import json, re, sys
from fractions import Fraction
from collections import Counter

H = "<repo>/harness/"
REKEY = json.load(open(H + "schmitt_hexagonal_rekey.json"))
ACC = json.load(open(H + "schmitt_hexagonal_tables.json"))


def F(s):
    return Fraction(str(s).replace("−", "-").strip())


def rekey_rows():
    out = {}
    for b in REKEY["blocks"]:
        bid = b["block"].replace("/", "_")
        out[bid] = [((F(r["b_ratio"]), tuple(F(p) for p in r["point"])),
                     tuple(r["f_vector"]), r["pdf_page"], r["idx"]) for r in b["rows"]]
    return out


def find_rows(block):
    for k, v in block.items():
        if isinstance(v, list) and v and isinstance(v[0], dict) and "f" in v[0] and "b" in v[0]:
            return v
    raise KeyError("no row list in block")


def acc_rows():
    out = {}
    for bid, blk in ACC.items():
        if bid.startswith("_"):
            continue
        rows = find_rows(blk)
        out[bid] = [((F(r["b"]), tuple(F(p) for p in r["pt"])), tuple(r["f"]),
                     r.get("pdf_page"), i + 1) for i, r in enumerate(rows)]
    return out


R, A = rekey_rows(), acc_rows()
report = []
n_fv = n_only_r = n_only_a = n_page = n_count = 0
tot_r = sum(len(v) for v in R.values())
tot_a = sum(len(v) for v in A.values())
report.append(f"blocks: rekey {len(R)} / accepted {len(A)}; rows: rekey {tot_r} / accepted {tot_a}")
if set(R) != set(A):
    report.append(f"BLOCK SET DIFFERS: only rekey {sorted(set(R)-set(A))}; only accepted {sorted(set(A)-set(R))}")

for bid in sorted(set(R) | set(A), key=lambda s: int(s.split("_")[0])):
    r, a = R.get(bid, []), A.get(bid, [])
    if len(r) != len(a):
        n_count += 1
        report.append(f"[{bid}] ROW COUNT rekey {len(r)} vs accepted {len(a)}")
    rk = Counter(k for k, *_ in r)
    ak = Counter(k for k, *_ in a)
    # duplicates of the same key within a file (legit when Schmitt prints one point twice)
    for k, c in rk.items():
        if c > 1:
            report.append(f"[{bid}] note: key {fmt(k)} appears {c}x in rekey")
    for k, c in ak.items():
        if c > 1:
            report.append(f"[{bid}] note: key {fmt(k)} appears {c}x in accepted")
    rmap = {}
    for k, fv, pg, idx in r:
        rmap.setdefault(k, []).append((fv, pg, idx))
    amap = {}
    for k, fv, pg, idx in a:
        amap.setdefault(k, []).append((fv, pg, idx))
    for k in rmap:
        if k not in amap:
            for fv, pg, idx in rmap[k]:
                n_only_r += 1
                report.append(f"[{bid}] ONLY IN REKEY  row {idx} PDF {pg}: f={fv} b={fmt_b(k[0])} pt={fmt_pt(k[1])}")
    for k in amap:
        if k not in rmap:
            for fv, pg, idx in amap[k]:
                n_only_a += 1
                report.append(f"[{bid}] ONLY IN ACCEPTED row {idx} PDF {pg}: f={fv} b={fmt_b(k[0])} pt={fmt_pt(k[1])}")
    for k in rmap:
        if k in amap:
            rf = sorted(x[0] for x in rmap[k]); af = sorted(x[0] for x in amap[k])
            if rf != af:
                n_fv += 1
                report.append(f"[{bid}] F-VECTOR DIFF at b={fmt_b(k[0])} pt={fmt_pt(k[1])}: rekey {rf} vs accepted {af} (rekey row {rmap[k][0][2]} PDF {rmap[k][0][1]})")
            rp = sorted(x[1] for x in rmap[k]); ap = sorted(x[1] for x in amap[k])
            if rp != ap:
                n_page += 1
                report.append(f"[{bid}] PAGE DIFF at b={fmt_b(k[0])} pt={fmt_pt(k[1])}: rekey {rp} vs accepted {ap}")
    # order check: same sequence of keys?
    if len(r) == len(a) and [k for k, *_ in r] != [k for k, *_ in a]:
        report.append(f"[{bid}] note: same row set but different ORDER")


def fmt_b(b):
    return f"{b.numerator}/{b.denominator}" if b.denominator != 1 else str(b.numerator)


def fmt_pt(p):
    return "(" + ",".join(fmt_b(x) for x in p) + ")"


def fmt(k):
    return f"b={fmt_b(k[0])} pt={fmt_pt(k[1])}"


# header facts: normalizer string and grid points / bounds, normalized for whitespace and symbols
def norm(s):
    s = str(s).replace("≤", "<=").replace("−", "-").replace("̄", "")
    s = re.sub(r"\s+", " ", s)
    s = s.replace("P 1 6/mmm", "P^1 6/mmm").replace("P 1 622", "P^1 622").replace("P 1 -31m", "P^1 -31m")
    s = s.replace("P 6/mmm", "P6/mmm").replace("P 62 22", "P6_2 22").replace("- 1/3", "-1/3")
    return s.strip()


hdr = []
for b in REKEY["blocks"]:
    bid = b["block"].replace("/", "_")
    if bid not in ACC:
        continue
    acc = ACC[bid]
    notes = " ".join(b["notes"])
    m = re.search(r"Normalizer: (.*?)(?:\.? Reduced|; so the)", notes)
    my_norm = norm(m.group(1)) if m else "?"
    their_norm = norm(acc.get("normalizer", "")).split(" ; so")[0].split("; so")[0].strip()
    if my_norm.split(" (only")[0] != their_norm.split(" (only")[0]:
        hdr.append(f"[{bid}] NORMALIZER: rekey '{my_norm}' vs accepted '{their_norm}'")
    if "(only the normalizer for" in notes:
        mo = re.search(r"\(only the normalizer for IT\((\d+)\) but not for IT\((\d+)\)\)", notes)
        to = re.search(r"\(only the normalizer for IT\((\d+)\) but not for IT\((\d+)\)\)", str(acc.get("normalizer", "")))
        if not to or mo.groups() != to.groups():
            hdr.append(f"[{bid}] ONLY-FOR remark: rekey {mo.groups() if mo else None} vs accepted {to.groups() if to else None}")
    g = re.search(r"(?:uses|used) (1 ?[0-9]{3} ?[0-9]{3}) (?:grid )?points", notes)
    my_grid = g.group(1).replace(" ", "") if g else "?"
    if my_grid != str(acc.get("grid_points", "")).replace(" ", ""):
        hdr.append(f"[{bid}] GRID POINTS: rekey {my_grid} vs accepted {acc.get('grid_points')}")
    ub = re.search(r"Upper bound on number of facets: (.*?)\. (?:Remarks|Metrical)", notes)
    my_ub = norm(ub.group(1)) if ub else "?"
    their_ub = norm(acc.get("upper_bound", "")).rstrip(".")
    if my_ub.rstrip(".") != their_ub:
        hdr.append(f"[{bid}] UPPER BOUND: rekey '{my_ub}' vs accepted '{their_ub}'")

print("\n".join(report))
print("--- header facts ---")
print("\n".join(hdr) if hdr else "no normalizer / only-for / grid / upper-bound differences")
print("--- summary ---")
print(f"row-count diffs {n_count}; f-vector diffs {n_fv}; only-in-rekey {n_only_r}; only-in-accepted {n_only_a}; page diffs {n_page}; header diffs {len(hdr)}")
