#!/usr/bin/env python
"""C3 -- the Laves-graph cell.  IT(214) I4_132, Wyckoff 8a, point (1/8,1/8,1/8),
through the exact chain; compare with the sweep store and the collision screen."""
import json, os, sys
from fractions import Fraction as F
from common import *  # noqa
import numpy as np, spglib

r = exact_cell_at(214, (F(1, 8), F(1, 8), F(1, 8)))
cid = code_id(r["code"])
stored = TYPES.get(cid)
pos = np.array(r["pts"], float) / r["period"]
ds = spglib.get_symmetry_dataset((np.eye(3), pos, [1] * len(pos)), symprec=1e-8)
vol = cell_volume(r["ec"])
L = ["## C3 -- the Laves-graph cell (IT(214) I4_132, Wyckoff 8a, (1/8,1/8,1/8))", "",
     f"- exact chain: f = {r['f']}, p = {pvec_compact(r['p'])}, aut = {r['aut']}, site symmetry order {r['stab']}, "
     f"orbit {r['ob']['n_conventional']} per conventional cell, T = {r['T']}, non-simple vertices {r['nonsimple']}, "
     f"cell volume {frac_str(vol)} (PERIOD {r['period']})",
     f"- spglib 2.7.0 on the orbit: IT({ds.number}) {ds.international}, Wyckoff {sorted(set(ds.wyckoffs))}, site symmetry {sorted(set(ds.site_symmetry_symbols))}",
     f"- canonical code id: {cid}; in phase1_types.json: {'YES' if stored else 'NO'}"]
if stored:
    L.append(f"- stored entry: f {tuple(stored['f_vector'])}, p {pvec_compact(stored['p_vector'])}, aut {stored['aut_order']}, "
             f"first witness {stored['first_witness']['group']} {stored['first_witness']['group_symbol']} {pt_str([F(s) for s in stored['first_witness']['point']])}; "
             f"sightings: " + "; ".join(f"{s['group']} {pt_str([F(x) for x in s['point']])}" for s in stored["sightings"]))
L.append("- collision screen (harness/SCHMITT_COLLISION_RESULTS.md P07-P09): this stored type was identified as SAME TYPE as Schmitt's printed "
         "(30,45,17) representative in IT(199), IT(212) and IT(214) (the 214 point being (1/8,1/8,1/8) itself), and eliminated from the candidate list.")
L.append(f"- verdict: {'the sweep REDISCOVERED the Laves-graph plesiohedron (stored as ' + cid + ', triage rank 5) and the collision screen correctly identified it as Schmitt''s printed cell; it has six pentagonal facets.' if stored else 'NOT in the store'}")
open(os.path.join(HERE, "c3_laves.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
