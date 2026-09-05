#!/usr/bin/env python
"""C5 (side check for reviewer Q9) -- Bernhard's published Josehedron generating
points (Table 4 minima, integer mod 8, verbatim from build_packages.JOSE_BASE)
through spglib and the exact chain: space group, Wyckoff letter, site symmetry,
and the canonical code compared with the banked Josehedron seed."""
import os, sys
from fractions import Fraction as F
from common import *  # noqa
import numpy as np, spglib
sys.path.insert(0, os.path.join(HARNESS, "..", "publication"))
from build_packages import JOSE_BASE, JOSE_PERIOD  # noqa
pos = np.array(JOSE_BASE, float) / JOSE_PERIOD
ds = spglib.get_symmetry_dataset((np.eye(3), pos, [1] * len(pos)), symprec=1e-8)
ec = clip_cell(JOSE_BASE[0], JOSE_BASE, JOSE_PERIOD)
code, aut = canonical_code(ec["facet_cycles"])
cid = code_id(code.decode("ascii")); ent = TYPES.get(cid)
# the same orbit regenerated from the frozen IT(220) operations at the 12a point
p12a = tuple(F(x) for x in JOSE_BASE[0]) 
r = exact_cell_at(220, [F(x, JOSE_PERIOD) for x in JOSE_BASE[0]])
L = ["## C5 -- Bernhard's Josehedron generating orbit: group and Wyckoff label", "",
     f"- spglib 2.7.0 on Bernhard's 12 integer points (mod 8): IT({ds.number}) {ds.international}, Wyckoff {sorted(set(ds.wyckoffs))}, site symmetry {sorted(set(ds.site_symmetry_symbols))}, origin shift {np.round(ds.origin_shift, 6).tolist()}",
     f"- exact cell from those points: f {(ec['n_vertices'], sum(len(c) for c in ec['facet_cycles'])//2, ec['facet_count'])}, p {pvec_compact(ec['p_vector'])}, aut {aut}; code id {cid} = stored seed '{ent['seed_name'] if ent else None}'",
     f"- orbit of the point {pt_str([F(x, JOSE_PERIOD) for x in JOSE_BASE[0]])} under the frozen IT(220) operations: {r['ob']['n_conventional']} points per conventional cell, site symmetry order {r['stab']}, T = {r['T']}; its cell has code id {code_id(r['code'])} ({'SAME' if r['code'] == code.decode('ascii') else 'DIFFERENT'} as Bernhard's cell), f {r['f']}, p {pvec_compact(r['p'])}",
     f"- point set identity: frozen-orbit points {'EQUAL' if sorted(r['pts']) == sorted(tuple(int(x * r['period'] / JOSE_PERIOD) for x in q) for q in JOSE_BASE) or set(r['pts']) == set(tuple(x * (r['period'] // JOSE_PERIOD) for x in q) for q in JOSE_BASE) else 'DIFFER from'} Bernhard's points (after rescaling to PERIOD {r['period']})"]
open(os.path.join(HERE, "c5_josehedron_wyckoff.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
