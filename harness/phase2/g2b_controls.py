#!/usr/bin/env python
"""g2b_controls.py — GATE G2b (../../ANCHORS.md, block appended 2026-09-03):
metric controls for the Gram-metric path.

Pre-registered assertions (verbatim targets in ANCHORS G2b; nothing here was
tuned after seeing output — the run writes G2B_RESULT.md with PASS/FAIL per
assertion and FAIL is a valid deliverable):
  (a) P6/mmm #191 origin orbit (hexagonal lattice), c/a in {1/2, 1, 2} ->
      seed hexagonal_prism code, aut 24, f=(12,18,8), 0 non-simple vertices.
  (b) BCT lattice = origin orbit of I4/mmm #139 and I4 #79; c/a in
      {7/2, 2, 3/2} -> seed elongated_dodecahedron code, aut 16, exactly 2
      non-simple vertices; c/a in {1/2, 1, 7/5} -> seed truncated_octahedron
      code, aut 48. Source for the lattice: Schmitt 2016 printed p.29 (PDF
      p.34) IT(79) rows (18,28,12)@7/2 and (24,36,14)@1/2 at point (0,0,0);
      threshold c/a = sqrt2 derived analytically (the (0,0,+-c) facet exists
      iff a^2/(2c) + c/4 > c/2 iff c/a < sqrt2).
  (c) #221/#225/#229 origin orbits, Gram path with G = I: vertex sets,
      neighbor sets, p-vectors, codes identical to exact_cell.clip_cell and
      matching the catalog.
  (d) Schmitt tetragonal rows (printed pp.28-29 = PDF pp.33-34), points in
      the space-group coordinate system, b-ratio = c/a: exact f-vector must
      equal the printed one. IT(75) (10,15,7)@1/2 (2825/5652,-1/5652,0)
      [PRIMARY]; IT(76) (44,66,24)@797/1000 (20/333,44/999,0); IT(77)
      (28,42,16)@1/2 (539/5652,-187/5652,0).
  (e) on every cell: R^T G R = G for all ops of the group; float/exact
      agreement (facet count, p-vector, neighbor site sets) unless the float
      cell is degeneracy-flagged (exact supersedes, recorded); 4*rho2 <= D2
      in the G-norm.

Chain per cell: orbit.py (exact) -> sweep_voronoi_gram.sweep_gram (float
proposal, W=2, W=3 retry on window guard) -> exact_cell_gram.clip_cell_gram
(exact, certificate asserted) -> canon_code.canonical_code. Every orbit cell
is clipped exactly (orbits here are small).

Run:
  python3 g2b_controls.py
Writes: G2B_RESULT.md (this directory). Exit 0 iff every assertion passes.
"""
import json
import os
import sys
import time
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
HARNESS = os.path.dirname(HERE)
sys.path.insert(0, HARNESS)

import orbit                                           # noqa: E402
from canon_code import canonical_code                  # noqa: E402
from exact_cell import clip_cell                       # noqa: E402
import metric                                          # noqa: E402
from sweep_voronoi_gram import sweep_gram              # noqa: E402
from exact_cell_gram import clip_cell_gram             # noqa: E402

CATALOG = os.path.join(HARNESS, "seed_catalog.json")
ORIGIN = (F(0), F(0), F(0))

# Schmitt 2016 printed rows (visual read + pdftotext layer agree, 2026-09-03)
SCHMITT_ROWS = [
    # tag, group, printed f-vector (V,E,F), b-ratio c/a, point, printed page
    ("S75", 75, (10, 15, 7), F(1, 2), (F(2825, 5652), F(-1, 5652), F(0)), "p.28 (PDF 33)"),
    ("S76", 76, (44, 66, 24), F(797, 1000), (F(20, 333), F(44, 999), F(0)), "p.28 (PDF 33)"),
    ("S77", 77, (28, 42, 16), F(1, 2), (F(539, 5652), F(-187, 5652), F(0)), "p.29 (PDF 34)"),
]


def run_chain(entry, point, gram):
    """Full chain on one (group, point, Gram). Returns dict with orbit info,
    float cells, exact cells, codes, agreement flags, timing."""
    t0 = time.time()
    ob = orbit.orbit(entry, point)
    pts, period = orbit.scale_orbit(ob["points"])
    compat = metric.gram_compatible(entry, gram)
    W = 2
    while True:
        try:
            cells_f = sweep_gram(pts, period, gram, W=W, entry=entry)
            break
        except RuntimeError:
            W += 1
            if W > 4:
                raise
    cells_e = [clip_cell_gram(c, pts, period, gram) for c in pts]
    agree, superseded, cert = True, 0, True
    for c, e, f_ in zip(pts, cells_e, cells_f):
        nf = {tuple(c[k] + d[k] for k in range(3)) for d in f_["neighbor_deltas"]}
        ok = (e["facet_count"] == f_["facet_count"] and e["p_vector"] == f_["p_vector"]
              and nf == set(e["neighbors"]))
        if not ok:
            if f_["degenerate_flag"]:
                superseded += 1          # exact supersedes a flagged float cell
            else:
                agree = False
        cert = cert and 4 * e["rho2"] <= e["cutoff_D2"]
    codes = [canonical_code(e["facet_cycles"]) for e in cells_e]
    one = len({cd for cd, _ in codes}) == 1 and len({a for _, a in codes}) == 1
    e0 = cells_e[0]
    return {
        "orbit": ob, "pts": pts, "period": period, "W": W, "compat": compat,
        "cells_f": cells_f, "cells_e": cells_e, "agree": agree,
        "superseded": superseded, "cert": cert, "codes": codes, "one_code": one,
        "code": codes[0][0].decode("ascii"), "aut": codes[0][1],
        "fvec": (e0["n_vertices"], e0["n_edges"], e0["facet_count"]),
        "pvec": e0["p_vector"], "nonsimple": e0["nonsimple_vertices"],
        "flags": [c["degenerate_flag"] for c in cells_f],
        "D2": e0["cutoff_D2"], "rho2": e0["rho2"],
        "seconds": time.time() - t0,
    }


def main():
    res = []                                       # (assertion, ok, detail, seconds)

    def check(name, ok, detail="", secs=None):
        res.append((name, bool(ok), str(detail), secs))
        print(("PASS  " if ok else "FAIL  ") + name
              + ("  [" + str(detail) + "]" if detail else "")
              + (f"  ({secs:.2f}s)" if secs is not None else ""))
        return bool(ok)

    T0 = time.time()
    cat = {e["name"]: e for e in json.load(open(CATALOG))["entries"]}
    groups = orbit.load_groups()

    # ---------------- (a) hexagonal prism: P6/mmm #191 origin, c/a in {1/2,1,2}
    g = groups[191]
    for r in (F(1, 2), F(1), F(2)):
        G = metric.gram_hexagonal(r)
        R = run_chain(g, ORIGIN, G)
        ok = (R["orbit"]["n_conventional"] == 1 and R["compat"] and R["agree"]
              and R["cert"] and R["one_code"]
              and R["code"] == cat["hexagonal_prism"]["canon_code"]
              and R["aut"] == 24 and R["fvec"] == (12, 18, 8) and R["nonsimple"] == 0)
        check(f"(a) P6/mmm #191 origin orbit (hexagonal lattice), c/a={r}: "
              "code == seed hexagonal_prism, aut 24, f=(12,18,8), simple, "
              "R^T G R = G, float/exact agree, G-norm certificate",
              ok, f"orbit={R['orbit']['n_conventional']}, f={R['fvec']}, "
              f"p={R['pvec']}, aut={R['aut']}, nonsimple={R['nonsimple']}, "
              f"flags={R['flags']}, W={R['W']}, D2={R['D2']}, rho2={R['rho2']}",
              R["seconds"])

    # ---------------- (b) BCT lattice: #139 and #79 origin orbits
    for num in (139, 79):
        g = groups[num]
        for r, target, aut_exp, ns_exp in ((F(7, 2), "elongated_dodecahedron", 16, 2),
                                           (F(2), "elongated_dodecahedron", 16, 2),
                                           (F(3, 2), "elongated_dodecahedron", 16, 2),
                                           (F(1, 2), "truncated_octahedron", 48, 0),
                                           (F(1), "truncated_octahedron", 48, 0),
                                           (F(7, 5), "truncated_octahedron", 48, 0)):
            G = metric.gram_tetragonal(r)
            R = run_chain(g, ORIGIN, G)
            ok = (R["orbit"]["n_conventional"] == 2 and R["compat"] and R["agree"]
                  and R["cert"] and R["one_code"]
                  and R["code"] == cat[target]["canon_code"]
                  and R["aut"] == aut_exp and R["nonsimple"] == ns_exp
                  and R["fvec"] == tuple(cat[target]["f_vector"]))
            check(f"(b) {g['international_short']} #{num} origin orbit (BCT "
                  f"lattice), c/a={r}: code == seed {target}, aut {aut_exp}, "
                  f"{ns_exp} non-simple vertices, R^T G R = G, agree, certificate",
                  ok, f"orbit={R['orbit']['n_conventional']}, f={R['fvec']}, "
                  f"p={R['pvec']}, aut={R['aut']}, nonsimple={R['nonsimple']}, "
                  f"flags={R['flags']}, superseded={R['superseded']}, W={R['W']}",
                  R["seconds"])

    # ---------------- (c) cubic sanity through the Gram path with G = I
    for num, target in ((221, "cube"), (225, "rhombic_dodecahedron"),
                        (229, "truncated_octahedron")):
        g = groups[num]
        t0 = time.time()
        R = run_chain(g, ORIGIN, metric.gram_cubic())
        same = True
        for c, e in zip(R["pts"], R["cells_e"]):
            e_ref = clip_cell(c, R["pts"], R["period"])
            same = (same and e_ref["vertices"] == e["vertices"]
                    and set(e_ref["neighbors"]) == set(e["neighbors"])
                    and e_ref["p_vector"] == e["p_vector"]
                    and canonical_code(e_ref["facet_cycles"])[0].decode("ascii") == R["code"])
        ok = (same and R["compat"] and R["agree"] and R["cert"] and R["one_code"]
              and R["code"] == cat[target]["canon_code"]
              and R["aut"] == cat[target]["aut_order"])
        check(f"(c) {g['international_short']} #{num} origin orbit via Gram path "
              f"(G=I): vertices/neighbors/p-vector/code IDENTICAL to "
              f"exact_cell.clip_cell and == seed {target}",
              ok, f"f={R['fvec']}, aut={R['aut']}, nonsimple={R['nonsimple']}, "
              f"flags={R['flags']}, superseded={R['superseded']}",
              time.time() - t0)

    # ---------------- (d) Schmitt tetragonal rows
    for tag, num, fv, b, x, page in SCHMITT_ROWS:
        g = groups[num]
        G = metric.gram_tetragonal(b)
        R = run_chain(g, x, G)
        ok = (R["compat"] and R["agree"] and R["cert"] and R["one_code"]
              and R["fvec"] == fv)
        check(f"(d) {tag} Schmitt {g['international_short']} IT({num}) printed "
              f"{page}: f={fv} at b-ratio {b}, x={tuple(str(v) for v in x)} -> "
              "exact f-vector == printed, R^T G R = G, agree, certificate",
              ok, f"exact f={R['fvec']}, p={R['pvec']}, aut={R['aut']}, "
              f"general_position={R['orbit']['general_position']}, "
              f"orbit={R['orbit']['n_conventional']}, PERIOD={R['period']}, "
              f"nonsimple={R['nonsimple']}, flags={R['flags']}, "
              f"superseded={R['superseded']}, W={R['W']}, D2={R['D2']}",
              R["seconds"])

    total = time.time() - T0
    allpass = all(ok for _, ok, _, _ in res)
    write_result(res, allpass, total)
    print(f"\nG2b VERDICT: {'ALL ASSERTIONS PASS' if allpass else 'FAIL — phase 2 quarantined (ANCHORS G2b)'}"
          f"  total {total:.1f}s")
    return 0 if allpass else 1


def write_result(res, allpass, total):
    lines = [
        "# G2b result — metric controls (2026-09-03)",
        "",
        "Gate: `../../ANCHORS.md` block \"G2b - METRIC CONTROLS\" (pre-registered "
        "before this run). Pipeline under test: `orbit.py` -> "
        "`phase2/sweep_voronoi_gram.py` (float proposal; delegates to the accepted "
        "`sweep_voronoi.sweep` Gram hook after exact PD / R^T G R = G validation) "
        "-> `phase2/exact_cell_gram.py` (exact Fractions, G-norm certificate "
        "4*rho^2 <= D^2 with the coordinate-bound-complete candidate block) -> "
        "`canon_code.py`, compared against `seed_catalog.json` (G2, independent).",
        "",
        "Verdict: **" + ("G2b ALL ASSERTIONS PASS" if allpass
                         else "G2b FAILED — phase 2 quarantined") + "**"
        + f" (wall {total:.1f} s, single process)",
        "",
        "## Basis decision (recorded)",
        "",
        "Trigonal/hexagonal groups run in the ITA hexagonal basis of the frozen ops "
        "with the rational Gram [[1,-1/2,0],[-1/2,1,0],[0,0,(c/a)^2]] (cleared to "
        "integers). Schmitt's orthohexagonal C-centered basis (his App. B, printed "
        "pp. 171-172) is not needed under the Gram form and would require "
        "half-integer R (a re-freeze of G1 data). b-ratio = c/a = ||b3'||/||b1'|| "
        "(his p. 27).",
        "",
        "## Elongated-dodecahedron lattice (source)",
        "",
        "Body-centered tetragonal lattice with c/a > sqrt 2. Primary source: Schmitt "
        "2016, printed p. 29 (PDF p. 34), IT(79) = I4 table rows "
        "\"(18, 28, 12) | 7/2 | (0, 0, 0)\" and \"(24, 36, 14) | 1/2 | (0, 0, 0)\" "
        "(the origin orbit of I4 is the BCT lattice); he lists the (18,28,12) "
        "lattice cell as the \"hexarhombic dodecahedron\" in his IT(1) table (p. 27). "
        "Corroborated by Wikipedia \"Elongated dodecahedron\" (Wigner-Seitz cell of "
        "BCT for c/a > sqrt 2; retrieved 2026-09-03) and by the analytic threshold "
        "derived here: the (0,0,+-c) facet exists iff a^2/(2c) + c/4 > c/2, i.e. "
        "iff c/a < sqrt 2 (c/a = sqrt 2 is FCC).",
        "",
        "## Assertions (with per-assertion wall time)",
        "",
    ]
    for name, ok, detail, secs in res:
        lines.append(("- **PASS** " if ok else "- **FAIL** ") + name
                     + (f" — {detail}" if detail else "")
                     + (f" — {secs:.2f} s" if secs is not None else ""))
    lines += [
        "",
        "## Honest limits / deferrals",
        "",
        "- Aut orders are COMBINATORIAL map automorphism counts; geometric "
        "stabilizers (C6) remain the G4/V2 ladder.",
        "- c/a = sqrt 2 (the BCT -> FCC transition) is irrational and untested; the "
        "rationals 7/5 and 3/2 bracket it.",
        "- Schmitt rows are f-vector-level checks (his tables print f-vectors, not "
        "types); the exact cell's p-vector/aut are recorded but have no printed "
        "counterpart to compare with.",
        "- Orthorhombic Gram is provided (metric.gram_orthorhombic) but not gated; "
        "monoclinic/triclinic raise NotImplementedError by design (§2.1 deferral).",
        "- No hunt sweep was run in this step.",
        "",
        "## Commands run",
        "",
        "```",
        "PY=python3",
        "cd <repo>/harness/phase2",
        "$PY metric.py && $PY exact_cell_gram.py && $PY sweep_voronoi_gram.py  # selftests",
        "$PY g2b_controls.py      # this gate; writes G2B_RESULT.md",
        "```",
    ]
    open(os.path.join(HERE, "G2B_RESULT.md"), "w").write("\n".join(lines) + "\n")


if __name__ == "__main__":
    sys.exit(main())
