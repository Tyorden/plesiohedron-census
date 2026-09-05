#!/usr/bin/env python
"""R6 -- Wyckoff position and orbit size of each sighting of the Laves-graph
type 8c69db9e84095469 (f = (30,45,17)) in phase1_types.json, from the site-symmetry
order and orbit size under the GENERATING group (ITA position lists for IT(199),
IT(212), IT(213), IT(214), hard-coded below), with spglib 2.7.0 run on the point
set only to report its full symmetry group (the point set is the vertex set of a
Laves graph and has symmetry I4_132 whichever subgroup generated it, so spglib
cannot return the subgroup's letter).  Answers referee Q6."""
# ITA Wyckoff positions with multiplicity, site-symmetry order and symbol
ITA = {199: [("a", 8, 3, ".3."), ("b", 12, 2, "2.."), ("c", 24, 1, "1")],
       212: [("a", 4, 6, ".32"), ("b", 4, 6, ".32"), ("c", 8, 3, ".3."), ("d", 12, 2, "..2"), ("e", 24, 1, "1")],
       213: [("a", 4, 6, ".32"), ("b", 4, 6, ".32"), ("c", 8, 3, ".3."), ("d", 12, 2, "..2"), ("e", 24, 1, "1")],
       214: [("a", 8, 6, ".32"), ("b", 8, 6, ".32"), ("c", 12, 4, "2.22"), ("d", 12, 4, "-4.."), ("e", 16, 3, ".3."),
             ("f", 24, 2, "2.."), ("g", 24, 2, "..2"), ("h", 24, 2, "..2"), ("i", 48, 1, "1")]}


def letter(group, n_conv, stab, pts):
    c = [w for w in ITA[group] if w[1] == n_conv and w[2] == stab]
    if group == 214 and len(c) == 2:   # 8a contains (1/8,1/8,1/8); 8b contains (7/8,7/8,7/8)
        c = [w for w in c if (w[0] == "a") == ((F(1, 8), F(1, 8), F(1, 8)) in pts)]
    assert len(c) == 1, (group, n_conv, stab, c)
    return c[0]

import os, json
from fractions import Fraction as F
import numpy as np, spglib
from common2 import *  # noqa
import orbit  # noqa: E402

ent = TYPES["8c69db9e84095469"]
assert tuple(ent["f_vector"]) == (30, 45, 17)
L = ["## R6 -- Wyckoff letters of the Laves-graph type sightings (spglib 2.7.0 on the frozen orbits)", "",
     "| group | point | site-symmetry order (frozen ops) | orbit / conventional cell | orbit / primitive cell | Wyckoff (ITA, from multiplicity and site order) | site symmetry | spglib symmetry of the point set | same canonical code |",
     "|---|---|---|---|---|---|---|---|---|"]
out = []
for s in ent["sightings"]:
    p = tuple(F(x) for x in s["point"])
    r = exact_cell_at(s["group"], p)
    same = r["code"] == ent["canon_code"]
    pos = np.array([[float(x) for x in q] for q in r["ob"]["points"]])
    ds = spglib.get_symmetry_dataset((np.eye(3), pos, [1] * len(pos)), symprec=1e-8)
    assert ds.number == 214, ds.number    # the point set itself has the full symmetry I4_132 in every case
    w = letter(s["group"], r["ob"]["n_conventional"], r["stab"], set(r["ob"]["points"]))
    out.append(dict(group=s["group"], point=pt_str(p), stab=r["stab"], n_conv=r["ob"]["n_conventional"], n_prim=r["T"],
                    spglib=f"IT({ds.number}) {ds.international}", wyckoff=f"{w[1]}{w[0]}", sitesym=w[3], same=same))
    L.append(f"| IT({s['group']}) {s['group_symbol']} | {pt_str(p)} | {r['stab']} | {r['ob']['n_conventional']} | {r['T']} | {w[1]}{w[0]} | {w[3]} | IT({ds.number}) {ds.international} | {'yes' if same else 'NO'} |")
assert all(o["same"] and o["n_conv"] == 8 for o in out)
L += ["", "Reading: every sighting is an eight-point orbit per conventional cell (the vertex set of one Laves graph). In IT(212) P4_332 the sighted orbit is 8c at (1/8, 3/8, 5/8), site symmetry .3.; "
      "in IT(213) P4_132 it is 8c at (1/8, 1/8, 1/8); in IT(199) I2_13 it is 8a (.3.); in IT(214) I4_132 both (1/8, 1/8, 1/8) and (1/8, 3/8, 5/8) are eight-point orbits with site symmetry .32 (8a and 8b). "
      "The four-point orbits 4a/4b of IT(212)/IT(213) (site symmetry .32) were not among the sightings of this type. spglib on each eight-point set returns I4_132 (the point set's own symmetry), which is why the letters are read from the generating group's position list."]
open(os.path.join(HERE, "r6_laves_wyckoff.md"), "w").write("\n".join(L) + "\n")
json.dump(out, open(os.path.join(HERE, "r6_laves_wyckoff.json"), "w"), indent=1)
print("\n".join(L))
