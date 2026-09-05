#!/usr/bin/env python
"""R1 -- roundness of the classical lattice Voronoi cells, the Josehedron and
the Laves-graph cell under BOTH conventions used in the paper:
  (a) volume / volume of the site-centred circumsphere (radius^2 = max |v - site|^2),
  (b) volume / volume of the smallest sphere enclosing the vertex set.
Bernhard's stated convention (arXiv:2604.07160, p. 6, verbatim in RESULTS):
"fills ~47.98% of the volume of its outer circumsphere", with the cube at
~36.76% and the rhombic dodecahedron and the maximal hexagonal prism inscribed
in a unit sphere at ~47.75%; the Josehedron is "therefore, by a small margin,
the 'roundest' SFPH known to date".  Exact rational volumes and squared radii
where the cell is rational (all but the hexagonal prisms, which are done in
closed form); one float division per percentage.  Deterministic."""
import json, os, sys, math
from fractions import Fraction as F
from common2 import *  # noqa
from exact_cell import clip_cell  # noqa: E402
sys.path.insert(0, os.path.join(HARNESS, "..", "publication"))
from build_packages import JOSE_BASE, JOSE_PERIOD  # noqa: E402

rows = []   # (name, convention note, vol, rho2_site, mes_r2, coincide, closed form site, closed form mes)


def lattice_cell(name, base, period, closed):
    ec = clip_cell((0, 0, 0), base, period)
    assert 4 * ec["rho2"] <= ec["cutoff_D"] ** 2
    verts = [tuple(F(x) for x in v) for v in ec["vertices"]]
    vol = cell_volume(ec)
    c, r2, _ = mes(verts)
    rows.append(dict(name=name, f=(ec["n_vertices"], sum(len(x) for x in ec["facet_cycles"]) // 2, ec["facet_count"]),
                     p=pvec_compact(ec["p_vector"]), vol=vol, rho2=ec["rho2"], mes_r2=r2, mes_c=c,
                     coincide=(tuple(c) == (0, 0, 0) and r2 == ec["rho2"]), closed=closed))
    return ec


# --- the three lattice cells (Voronoi cells of the P, F, I cubic lattices; G2 controls)
lattice_cell("cube (P lattice)", [(0, 0, 0)], 2, "2/(sqrt3 pi)")
lattice_cell("rhombic dodecahedron (F lattice)", [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)], 2, "3/(2 pi)")
lattice_cell("truncated octahedron (I lattice)", [(0, 0, 0), (1, 1, 1)], 2, "24/(5 sqrt5 pi)")

# --- elongated dodecahedron: the seed-catalog member (g2_seed_catalog.py published vertices), exact hull
ED = [(0, 0, 3), (0, 0, -3)] + [(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-2, 2)] \
     + [(x, 0, z) for x in (-2, 2) for z in (-1, 1)] + [(0, y, z) for y in (-2, 2) for z in (-1, 1)]
EDv = [tuple(F(x) for x in v) for v in ED]
vol, faces = hull_volume(EDv)
assert len(faces) == 12 and len(EDv) == 18
rho2 = max(dot(v, v) for v in EDv)
c, r2, _ = mes(EDv)
rows.append(dict(name="elongated dodecahedron (seed member, elongation e=1)", f=(18, 28, 12),
                 p=pvec_compact(sorted(len(on) for on in faces.values())), vol=vol, rho2=rho2, mes_r2=r2, mes_c=c,
                 coincide=(tuple(c) == (0, 0, 0) and r2 == rho2), closed="8/(9 pi)"))
# the whole elongation family: vertices (0,0,+-(2+e)), (+-1,+-1,+-(1+e)), (+-2,0,+-e), (0,+-2,+-e), e >= 0;
# vol = 16 + 16 e, rho^2 = (2+e)^2, ratio(e) = 12 (1+e) / (pi (2+e)^3), derivative sign = -(1+2e) < 0:
# the ratio decreases from the rhombic dodecahedron value 3/(2 pi) at e = 0.  Checked numerically below.
fam = [(e, 12 * (1 + e) / (math.pi * (2 + e) ** 3)) for e in (0, 0.25, 0.5, 1, 2)]
assert all(fam[i][1] > fam[i + 1][1] for i in range(len(fam) - 1))
assert abs(fam[0][1] - 3 / (2 * math.pi)) < 1e-15 and abs(fam[3][1] - float(vol) / (4 / 3 * math.pi * 27)) < 1e-12

# --- hexagonal prisms (closed form; regular hexagon side s, height h, all 12 vertices cospherical, R^2 = s^2 + h^2/4)
#   Bernhard's: the maximal-volume prism inscribed in a unit sphere: h = 2/sqrt3, s^2 = 2/3, V = 2, ratio = 3/(2 pi).
#   Equilateral (h = s): ratio = 9 sqrt3 / (5 sqrt5 pi).
prism_max = 3 / (2 * math.pi)
prism_eq = 9 * math.sqrt(3) / (5 * math.sqrt(5) * math.pi)
# check the maximal prism by calculus: V(h) = (3 sqrt3 / 2) (1 - h^2/4) h on the unit sphere, V'(h) = 0 at h = 2/sqrt3
h = 2 / math.sqrt(3); assert abs((3 * math.sqrt(3) / 2) * (1 - h * h / 4) * h - 2.0) < 1e-12
assert all((3 * math.sqrt(3) / 2) * (1 - t * t / 4) * t <= 2.0 + 1e-12 for t in [k / 1000 for k in range(1, 2000)])

# --- Josehedron (Bernhard's 12 integer generating points, period 8) and the Laves-graph cell (IT(214) 8a)
jec = clip_cell(JOSE_BASE[0], JOSE_BASE, JOSE_PERIOD)
assert 4 * jec["rho2"] <= jec["cutoff_D"] ** 2
jv = [tuple(F(x) for x in v) for v in jec["vertices"]]
c, r2, _ = mes(jv)
rows.append(dict(name="Josehedron (control; Bernhard prints ~47.98%)", f=(jec["n_vertices"], sum(len(x) for x in jec["facet_cycles"]) // 2, jec["facet_count"]),
                 p=pvec_compact(jec["p_vector"]), vol=cell_volume(jec), rho2=jec["rho2"], mes_r2=r2, mes_c=c,
                 coincide=(tuple(c) == tuple(F(x) for x in jec["center"]) and r2 == jec["rho2"]), closed=None))
lav = exact_cell_at(214, (F(1, 8), F(1, 8), F(1, 8)))
assert lav["f"] == (30, 45, 17)
lv = [tuple(F(x) for x in v) for v in lav["ec"]["vertices"]]
c, r2, _ = mes(lv)
rows.append(dict(name="Laves-graph cell (IT(214) 8a, (30,45,17))", f=lav["f"], p=pvec_compact(lav["p"]), vol=cell_volume(lav["ec"]),
                 rho2=lav["ec"]["rho2"], mes_r2=r2, mes_c=c,
                 coincide=(tuple(c) == tuple(F(x) for x in lav["ec"]["center"]) and r2 == lav["ec"]["rho2"]), closed=None))

# --- report
BERN = 47.98
L = ["## R1 -- roundness of classical cells under both conventions", "",
     "Bernhard's convention (arXiv:2604.07160, p. 6, PDF text layer, verbatim): \"The Josehedron fills ~47.98% of the volume of its outer circumsphere. "
     "This is slightly superior to another SFPH, the rhombic dodecahedron at ~47.75%, though the latter has 16 vertices. The cube, in comparison, only occupies ~36.76% of its circumsphere. "
     "The maximal hexagonal prism (also an SFPH, and a suspected candidate by reddit user \"st3f-ping\") inscribed in a unit sphere occupies ~47.75%. "
     "The Josehedron is therefore, by a small margin, the \"roundest\" SFPH known to date.\" "
     "Earlier on the same page his outer circumsphere is the sphere through the farthest vertices about the cell's centre (Fig. 4, R2), and for the regular dodecahedron he writes \"its circumsphere (the sphere through all vertices)\". "
     "For every cell below the site-centred sphere and the smallest enclosing sphere coincide (the symmetry group of each cell fixes only its centre), so the two conventions agree and the values are Bernhard's.", "",
     "| cell | f | p | vol | rho^2 (site) | r^2 (MES) | coincide | roundness (site) | roundness (MES) | closed form |", "|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    L.append(f"| {r['name']} | {r['f']} | {r['p']} | {frac_str(r['vol'])} | {frac_str(r['rho2'])} | {frac_str(r['mes_r2'])} | {'YES' if r['coincide'] else 'NO'} | "
             f"{pct(r['vol'], r['rho2']):.4f}% | {pct(r['vol'], r['mes_r2']):.4f}% | {r['closed'] or '-'} |")
L.append(f"| hexagonal prism, maximal inscribed (Bernhard's; h/s = sqrt2) | (12,18,8) | 4^6 6^2 | closed form | | | YES | {100*prism_max:.4f}% | {100*prism_max:.4f}% | 3/(2 pi) |")
L.append(f"| hexagonal prism, equilateral (h = s) | (12,18,8) | 4^6 6^2 | closed form | | | YES | {100*prism_eq:.4f}% | {100*prism_eq:.4f}% | 9 sqrt3/(5 sqrt5 pi) |")
L += ["", "Elongated dodecahedron family (vertices (0,0,+-(2+e)), (+-1,+-1,+-(1+e)), (+-2,0,+-e), (0,+-2,+-e), e >= 0): vol = 16(1+e), rho^2 = (2+e)^2, "
      "ratio = 12(1+e)/(pi (2+e)^3), strictly decreasing in e from 3/(2 pi) = 47.75% at e = 0 (the rhombic dodecahedron); the seed member is e = 1.", ""]
to = next(r for r in rows if r["name"].startswith("truncated"))
tov = pct(to["vol"], to["rho2"])
L.append(f"Finding: the truncated octahedron (the Voronoi cell of the body-centred cubic lattice, the paper's gate-G2 control) fills {tov:.4f}% of its circumsphere "
         f"under Bernhard's convention, above the Josehedron's {pct(rows[4]['vol'], rows[4]['rho2']):.4f}%. The cube ({pct(rows[0]['vol'], rows[0]['rho2']):.4f}%), rhombic dodecahedron "
         f"({pct(rows[1]['vol'], rows[1]['rho2']):.4f}%) and maximal hexagonal prism ({100*prism_max:.4f}%) reproduce his printed 36.76%, 47.75%, 47.75%, which fixes the convention. "
         f"Bernhard's text restricts the comparison to the cells he names; it does not exclude lattice Voronoi cells by any stated rule, and the truncated octahedron appears in his own Table 1 as the Voronoi cell of several minimal-surface point sets.")
assert tov > BERN
open(os.path.join(HERE, "r1_roundness_classical.md"), "w").write("\n".join(L) + "\n")
json.dump([dict(name=r["name"], f=r["f"], p=r["p"], vol=frac_str(r["vol"]), rho2=frac_str(r["rho2"]), mes_r2=frac_str(r["mes_r2"]),
                coincide=r["coincide"], round_site=round(pct(r["vol"], r["rho2"]), 4), round_mes=round(pct(r["vol"], r["mes_r2"]), 4), closed=r["closed"]) for r in rows]
          + [dict(name="hexagonal prism, maximal inscribed", round_site=round(100 * prism_max, 4), round_mes=round(100 * prism_max, 4), closed="3/(2 pi)"),
             dict(name="hexagonal prism, equilateral", round_site=round(100 * prism_eq, 4), round_mes=round(100 * prism_eq, 4), closed="9 sqrt3/(5 sqrt5 pi)")],
          open(os.path.join(HERE, "r1_roundness_classical.json"), "w"), indent=1)
print("\n".join(L))
