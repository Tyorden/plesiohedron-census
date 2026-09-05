#!/usr/bin/env python
"""R3 -- is Schmitt's printed IT(220) representative for f = (22, 35, 15) one of
the Satchelhedron's two wall neighbours on the 24d line?

Printed row (Schmitt 2016, printed p. 142, text layer):
    (22, 35, 15)   (-1/8, 55/2328, 437/3492)    52 090 897
IT(220) is single-origin and its operation table agrees with Schmitt's in the
identical setting, so the point is used as printed.  The chain is the frozen
exact chain (orbit -> exact clip -> canonical code); the run is accepted only
if the recomputed f-vector equals the printed one.  Compared against:
    A = stored type 0ee26ed471c923e2, (22,35,15) 3^4 5^10 8^1 (x < 0 on the line; sighted at x = 1/3),
    B = the unstored (22,35,15) 3^6 4^1 6^8 type, recomputed at (1/96, 0, 1/4) (0 < x < 1/12),
and, for completeness, against every stored (22,35,15) type of the sweep."""
import os, json
from fractions import Fraction as F
from common2 import *  # noqa

P = (F(-1, 8), F(55, 2328), F(437, 3492))
r = exact_cell_at(220, P)
assert r["f"] == (22, 35, 15), f"FVEC-MISMATCH: recomputed {r['f']} at the printed point"
A = TYPES["0ee26ed471c923e2"]
assert tuple(A["f_vector"]) == (22, 35, 15)
B = exact_cell_at(220, (F(1, 96), F(0), F(1, 4)))
assert B["f"] == (22, 35, 15) and pvec_compact(B["p"]) == "3^6 4^1 6^8"
S_ = exact_cell_at(220, (F(0), F(0), F(1, 4)))
assert S_["f"] == (16, 25, 11)
sameA = r["code"] == A["canon_code"]
sameB = r["code"] == B["code"]
others = {cid: e for cid, e in TYPES.items() if tuple(e["f_vector"]) == (22, 35, 15)}
match_stored = [cid for cid, e in others.items() if e["canon_code"] == r["code"]]
L = ["## R3 -- identity of Schmitt's printed IT(220) (22,35,15) representative", "",
     f"Printed point (-1/8, 55/2328, 437/3492), frequency 52 090 897 (printed p. 142). Recomputed through the frozen chain: f = {r['f']} (equals the printed f-vector; run accepted), "
     f"p = {pvec_compact(r['p'])}, aut = {r['aut']}, site-symmetry order = {r['stab']} ({'general position' if r['stab'] == 1 else 'special position'}), T = {r['T']}, non-simple vertices = {r['nonsimple']}, canonical-code id {code_id(r['code'])}.", "",
     "| comparison | f | p | aut | same type? |", "|---|---|---|---|---|",
     f"| A: wall neighbour x < 0, stored 0ee26ed471c923e2 | {tuple(A['f_vector'])} | {pvec_compact(A['p_vector'])} | {A['aut_order']} | {'YES' if sameA else 'NO'} |",
     f"| B: wall neighbour 0 < x < 1/12, recomputed at (1/96, 0, 1/4) | {B['f']} | {pvec_compact(B['p'])} | {B['aut']} | {'YES' if sameB else 'NO'} |"]
for cid, e in sorted(others.items()):
    L.append(f"| stored (22,35,15) type {cid} (first witness IT({e['first_witness']['group']}) {tuple(e['first_witness']['point'])}) | {tuple(e['f_vector'])} | {pvec_compact(e['p_vector'])} | {e['aut_order']} | {'YES' if e['canon_code'] == r['code'] else 'NO'} |")
verdict = ("It is the x < 0 neighbour (type A)." if sameA else "It is the x > 0 neighbour (type B)." if sameB else
           "It is NEITHER wall neighbour: a third (22,35,15) type in IT(220), " + ("also stored by the sweep as " + ", ".join(match_stored) if match_stored else "not stored by the sweep") + ".")
L += ["", "Verdict: " + verdict,
      f"The printed point has x = -1/8 (a lateral face of R220) and site-symmetry order {r['stab']}; it is not on the 24d line (y = 0, z = 1/4), and its frequency of 52 million grid points marks a three-dimensional type region. "
      "The (22,35,15) entry in Schmitt's IT(220) table therefore records a general-position type, and the two wall neighbours of the Satchelhedron share only its f-vector."]
open(os.path.join(HERE, "r3_neighbour_identity.md"), "w").write("\n".join(L) + "\n")
json.dump(dict(point=pt_str(P), f=r["f"], p=pvec_compact(r["p"]), aut=r["aut"], stab=r["stab"], code_id=code_id(r["code"]),
               same_as_A=sameA, same_as_B=sameB, stored_matches=match_stored), open(os.path.join(HERE, "r3_neighbour_identity.json"), "w"), indent=1)
print("\n".join(L))
