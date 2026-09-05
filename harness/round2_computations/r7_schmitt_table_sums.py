#!/usr/bin/env python
"""R7 -- do Schmitt's printed per-group frequencies sum to his printed grid-point
counts?  For every cubic group block of the dissertation (Sec. 2.2.5, text layer
extracted with pdftotext -layout from the archived PDF) the rows
    (V, E, F)   (generating grid point)   frequency
are parsed, the frequencies summed, and the sum compared with the block's
"We used N grid points in the approximating grid".  A shortfall means grid
points whose f-vector is not printed in the table.  Also re-counts the rows per
group against the 881-row digitization (triage_phase1.py).  Deterministic."""
import os, re, subprocess, json, sys
from common2 import *  # noqa
from triage_phase1 import SCHMITT_FVECTORS  # noqa: E402

PDF = os.path.join(HARNESS, "..", "references", "Schmitt_2016_dissertation.pdf")
txt = subprocess.run(["/opt/homebrew/bin/pdftotext", "-layout", PDF, "-"], capture_output=True, text=True, check=True).stdout
lines = txt.splitlines()
hdr = re.compile(r"Space group type \([\d, ]+\); IT\((\d+)\) = ")
used = re.compile(r"We used ([\d ]+?) grid points in the approximating")
row = re.compile(r"\((\d+), (\d+), (\d+)\)\s+\(([^)]*)\)\s+([\d][\d ]*?)\s*$")
blocks = {}
cur = None
for ln in lines:
    m = hdr.search(ln)
    if m:
        n = int(m.group(1))
        if 195 <= n <= 230:
            cur = n; blocks[cur] = dict(used=None, rows=[])
        else:
            cur = None
        continue
    if cur is None:
        continue
    m = used.search(ln)
    if m:
        blocks[cur]["used"] = int(m.group(1).replace(" ", "")); continue
    m = row.search(ln)
    if m:
        f = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
        blocks[cur]["rows"].append((f, m.group(4).replace(" ", ""), int(m.group(5).replace(" ", ""))))
# IT(213) shares IT(212)'s block
L = ["## R7 -- Schmitt's printed frequencies versus his printed grid-point counts (36 cubic groups)", "",
     "| group | grid points printed | rows | sum of printed frequencies | shortfall | shortfall % | rows == digitization |", "|---|---|---|---|---|---|---|"]
out = {}
tot_rows = 0
for n in sorted(blocks):
    b = blocks[n]
    s = sum(r[2] for r in b["rows"])
    short = (b["used"] - s) if b["used"] is not None else None
    digit = len(SCHMITT_FVECTORS[n])
    fset = sorted(set(r[0] for r in b["rows"]))
    same_rows = (fset == sorted(SCHMITT_FVECTORS[n]))
    tot_rows += len(b["rows"])
    out[n] = dict(used=b["used"], rows=len(b["rows"]), sum=s, shortfall=short, digitization_match=same_rows)
    L.append(f"| IT({n}){' (=213)' if n == 212 else ''} | {b['used']:,} | {len(b['rows'])} | {s:,} | {short:,} | {100*short/b['used']:.3f}% | {'yes' if same_rows else 'NO'} |")
tot_rows += len(blocks[212]["rows"])   # the digitization counts IT(213) as a copy of IT(212)
L += ["", f"Rows parsed: {tot_rows} counting IT(213) as a copy of IT(212) (the digitization has {sum(len(v) for v in SCHMITT_FVECTORS.values())}). "
      f"Blocks whose f-vector sets differ from the digitization: {[n for n, o in out.items() if not o['digitization_match']] or 'none'}."]
bad = {n: o for n, o in out.items() if o["shortfall"]}
L.append(f"Groups with a shortfall (printed frequencies do not exhaust the printed grid): {sorted(bad)}; groups where they match exactly: {len(out) - len(bad)} of {len(out)}.")
if 201 in bad:
    L.append(f"IT(201): {out[201]['shortfall']:,} of {out[201]['used']:,} grid points ({100*out[201]['shortfall']/out[201]['used']:.2f}%) carry no printed f-vector. "
             "The Ordenhedron's type region, estimated in R5 at about half of a cube of side 1/12 about its generating point, is about 3% of the reduced domain R201 (volume 1/96) "
             "if that box is representative; the shortfall and that estimate are of the same order. Nothing more is inferred here.")
open(os.path.join(HERE, "r7_schmitt_table_sums.md"), "w").write("\n".join(L) + "\n")
json.dump(out, open(os.path.join(HERE, "r7_schmitt_table_sums.json"), "w"), indent=1)
print("\n".join(L))
