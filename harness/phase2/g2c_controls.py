#!/usr/bin/env python
"""g2c_controls.py — GATE G2c (../../ANCHORS.md, block appended 2026-09-04
BEFORE any batch-2 computation): hexagonal-family controls for phase 2 batch 2.

Pre-registered assertions (verbatim targets in ANCHORS G2c; nothing here was
tuned after seeing output — the run writes G2C_RESULT.md with PASS/FAIL per
assertion and FAIL is a valid deliverable):
  (a) P6/mmm #191 origin orbit, c/a in {1/2, 1, 2} -> seed hexagonal_prism
      code, aut 24, f=(12,18,8), 0 non-simple vertices (re-run of G2b(a)).
  (b) R-3m #166 origin orbit on hexagonal axes = rhombohedral lattice
      (is_lattice True, 3 points/conventional cell). Brackets of the
      irrational transition values c/a = sqrt6 (FCC), sqrt6/2 (SC), sqrt6/4
      (BCC): {12/5, 5/2}, {6/5, 5/4}, {3/5, 5/8}; generic c/a in {1, 2, 3}
      with stability at c/a +- 1/24. Required: every cell is a seed-catalog
      parallelohedron (hexagonal_prism / elongated_dodecahedron /
      rhombic_dodecahedron / truncated_octahedron) with the seed's aut; the
      generic value's code is identical at c/a +- 1/24; stab | aut.
      Bracket sides are RECORDED (identical-on-both-sides is the prediction,
      not a requirement; a differing pair is recorded, not failed).
  (c) Schmitt trigonal/hexagonal printed rows S143, S147, S155, S166, S178,
      S194 (PDF 88/89/97/105/114/123): the exact cell at (group, b, point)
      must have the printed f-vector under ONE point convention for all six
      — H1 (points in his orthohexagonal basis B'', converted by x' = 2x'',
      y' = x''+y'', z' = z'') is tried first, then H0 (verbatim ITA), then
      the b-ratio alternative (c/a)^2 = 3 b^2 under H1/H0. The S178 row is
      also run in IT(179) (second enantiomorph): verbatim first, then
      z -> -z; the conversion that reproduces is recorded (required: one of
      them does).
  (d) On every cell: R^T G R = G for all ops of the group; float/exact
      agreement (facet count, p-vector, neighbor site sets) unless the float
      cell is degeneracy-flagged (exact supersedes, recorded); the G-norm
      certificate 4*rho^2 <= D^2; Euler; one canonical code over the orbit
      cells clipped; site-stabilizer order divides the combinatorial aut.

Chain per cell: orbit.py (exact) -> metric.gram_hexagonal(c/a) ->
sweep_voronoi_gram.sweep_gram (float proposal, W=2, W=3/4 retry) ->
exact_cell_gram.clip_cell_gram on cell 0 and on a second orbit cell (or
every cell when the orbit has <= 6 points) -> canon_code.canonical_code.

Run:
  python3 g2c_controls.py
Writes: G2C_RESULT.md (this directory). Exit 0 iff every required assertion
passes.
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
from sweep_phase1 import is_lattice                    # noqa: E402
import metric                                          # noqa: E402
from sweep_voronoi_gram import sweep_gram              # noqa: E402
from exact_cell_gram import clip_cell_gram             # noqa: E402

CATALOG = os.path.join(HARNESS, "seed_catalog.json")
TABLES = os.path.join(HARNESS, "schmitt_hexagonal_tables.json")
ORIGIN = (F(0), F(0), F(0))
PARALLELOHEDRA = ("hexagonal_prism", "elongated_dodecahedron",
                  "rhombic_dodecahedron", "truncated_octahedron")

# Schmitt 2016 printed rows (text layer + visual cross-read, 2026-09-04),
# points AS PRINTED (B'' coordinates under H1).
SCHMITT_ROWS = [
    # tag, group, printed f-vector (V,E,F), b-ratio, printed point, PDF page
    ("S143", 143, (8, 12, 6), F(3497, 1000), (F(1, 6), F(0), F(0)), 88),
    ("S147", 147, (10, 15, 7), F(3497, 1000), (F(33, 100), F(-1, 500), F(0)), 89),
    ("S155", 155, (48, 73, 27), F(797, 1000), (F(-193, 750), F(-53, 250), F(6, 125)), 97),
    ("S166", 166, (38, 58, 22), F(527, 1000), (F(-16, 375), F(-16, 125), F(31, 500)), 105),
    ("S178", 178, (64, 96, 34), F(163, 200), (F(32, 125), F(-19, 125), F(43, 1500)), 114),
    ("S194", 194, (18, 30, 14), F(797, 1000), (F(1, 3), F(0), F(1, 4)), 123),
]


def h1(p):
    """B'' -> ITA hexagonal basis: p' = X p'', X = [[2,0,0],[1,1,0],[0,0,1]]."""
    x, y, z = p
    return (2 * x, x + y, z)


def h0(p):
    return tuple(p)


def gram_b(b):
    return metric.gram_hexagonal(b)


def gram_b_alt(b):
    """b = ||b3''||/||b1''|| = c/(sqrt3 a): (c/a)^2 = 3 b^2, rational Gram."""
    G = ((F(1), F(-1, 2), F(0)), (F(-1, 2), F(1), F(0)), (F(0), F(0), 3 * b * b))
    return metric.scale_to_integers(G)[0]


def run_chain(entry, point, gram, n_exact=None):
    """Full chain on one (group, point, Gram)."""
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
    if n_exact is None:
        idx = list(range(len(pts))) if len(pts) <= 6 else sorted({0, len(pts) // 2})
    else:
        idx = list(range(min(n_exact, len(pts))))
    cells_e = {i: clip_cell_gram(pts[i], pts, period, gram) for i in idx}
    agree, superseded, cert, euler = True, 0, True, True
    for i in idx:
        e, f_, c = cells_e[i], cells_f[i], pts[i]
        nf = {tuple(c[k] + d[k] for k in range(3)) for d in f_["neighbor_deltas"]}
        ok = (e["facet_count"] == f_["facet_count"] and e["p_vector"] == f_["p_vector"]
              and nf == set(e["neighbors"]))
        if not ok:
            if f_["degenerate_flag"]:
                superseded += 1
            else:
                agree = False
        cert = cert and 4 * e["rho2"] <= e["cutoff_D2"]
        euler = euler and e["n_vertices"] - e["n_edges"] + e["facet_count"] == 2
    codes = [canonical_code(cells_e[i]["facet_cycles"]) for i in idx]
    one = len({cd for cd, _ in codes}) == 1 and len({a for _, a in codes}) == 1
    e0 = cells_e[idx[0]]
    aut = codes[0][1]
    return {
        "orbit": ob, "pts": pts, "period": period, "W": W, "compat": compat,
        "agree": agree, "superseded": superseded, "cert": cert, "euler": euler,
        "one_code": one, "code": codes[0][0].decode("ascii"), "aut": aut,
        "stab_divides": aut % ob["stabilizer_order"] == 0,
        "fvec": (e0["n_vertices"], e0["n_edges"], e0["facet_count"]),
        "pvec": e0["p_vector"], "nonsimple": e0["nonsimple_vertices"],
        "flags": [c["degenerate_flag"] for c in cells_f],
        "D2": e0["cutoff_D2"], "rho2": e0["rho2"], "n_exact": len(idx),
        "lattice": is_lattice(pts, period),
        "seconds": time.time() - t0,
    }


def invariants_ok(R):
    return (R["compat"] and R["agree"] and R["cert"] and R["euler"] and R["one_code"]
            and R["stab_divides"])


def main():
    res = []                                       # (assertion, ok, detail, seconds, required)
    notes = []

    def check(name, ok, detail="", secs=None, required=True):
        res.append((name, bool(ok), str(detail), secs, required))
        print(("PASS  " if ok else ("FAIL  " if required else "NOTE  ")) + name
              + ("  [" + str(detail) + "]" if detail else "")
              + (f"  ({secs:.2f}s)" if secs is not None else ""), flush=True)
        return bool(ok)

    T0 = time.time()
    cat = {e["name"]: e for e in json.load(open(CATALOG))["entries"]}
    code2name = {cat[n]["canon_code"]: n for n in cat}
    groups = orbit.load_groups()

    # ---------------- (a) hexagonal prism
    g = groups[191]
    for r in (F(1, 2), F(1), F(2)):
        R = run_chain(g, ORIGIN, gram_b(r))
        ok = (R["orbit"]["n_conventional"] == 1 and invariants_ok(R)
              and R["code"] == cat["hexagonal_prism"]["canon_code"]
              and R["aut"] == 24 and R["fvec"] == (12, 18, 8) and R["nonsimple"] == 0)
        check(f"(a) P6/mmm #191 origin orbit (hexagonal lattice), c/a={r}: code == seed "
              "hexagonal_prism, aut 24, f=(12,18,8), simple, invariants (d)",
              ok, f"orbit={R['orbit']['n_conventional']}, f={R['fvec']}, p={R['pvec']}, "
              f"aut={R['aut']}, nonsimple={R['nonsimple']}, flags={R['flags']}, W={R['W']}, "
              f"D2={R['D2']}, rho2={R['rho2']}", R["seconds"])

    # ---------------- (b) rhombohedral lattice: R-3m #166 origin orbit
    g = groups[166]
    R = run_chain(g, ORIGIN, gram_b(F(1)))
    check("(b) R-3m #166 origin orbit is a LATTICE with 3 points per conventional cell "
          "(rhombohedral, hexagonal axes)",
          R["lattice"] and R["orbit"]["n_conventional"] == 3,
          f"is_lattice={R['lattice']}, orbit={R['orbit']['n_conventional']}, "
          f"points={R['orbit']['points']}", R["seconds"])

    def par_name(R):
        return code2name.get(R["code"])

    brackets = [("FCC c/a=sqrt6~2.4495", F(12, 5), F(5, 2)),
                ("SC c/a=sqrt6/2~1.2247", F(6, 5), F(5, 4)),
                ("BCC c/a=sqrt6/4~0.6124", F(3, 5), F(5, 8))]
    for label, lo, hi in brackets:
        sides = []
        for r in (lo, hi):
            R = run_chain(g, ORIGIN, gram_b(r))
            nm = par_name(R)
            ok = (invariants_ok(R) and nm in PARALLELOHEDRA and R["aut"] == cat[nm]["aut_order"]
                  and R["fvec"] == tuple(cat[nm]["f_vector"]) and R["lattice"])
            sides.append((r, nm, R))
            check(f"(b) R-3m #166 lattice, bracket {label}, side c/a={r}: seed-catalog "
                  "parallelohedron with the seed's aut, invariants (d)",
                  ok, f"code -> {nm}, f={R['fvec']}, p={R['pvec']}, aut={R['aut']}, "
                  f"nonsimple={R['nonsimple']}, flags={R['flags']}, superseded={R['superseded']}, "
                  f"W={R['W']}", R["seconds"])
        same = sides[0][1] == sides[1][1] and sides[0][2]["code"] == sides[1][2]["code"]
        check(f"(b) bracket {label}: RECORDED sides {frac(sides[0][0])} -> {sides[0][1]}, "
              f"{frac(sides[1][0])} -> {sides[1][1]} ({'same code both sides' if same else 'DIFFERENT codes on the two sides'})",
              True, "prediction check only, recorded not required", None, required=False)
        notes.append(f"bracket {label}: {frac(sides[0][0])} -> {sides[0][1]}, "
                     f"{frac(sides[1][0])} -> {sides[1][1]}")
    for r in (F(1), F(2), F(3)):
        R = run_chain(g, ORIGIN, gram_b(r))
        nm = par_name(R)
        Rm = run_chain(g, ORIGIN, gram_b(r - F(1, 24)))
        Rp = run_chain(g, ORIGIN, gram_b(r + F(1, 24)))
        stable = Rm["code"] == R["code"] == Rp["code"]
        ok = (invariants_ok(R) and invariants_ok(Rm) and invariants_ok(Rp)
              and nm in PARALLELOHEDRA and R["aut"] == cat[nm]["aut_order"]
              and R["fvec"] == tuple(cat[nm]["f_vector"]) and stable and R["lattice"]
              and nm != "elongated_dodecahedron")
        check(f"(b) R-3m #166 lattice, generic c/a={r}: seed-catalog parallelohedron "
              f"(identified: {nm}), seed aut, STABLE at c/a +- 1/24, invariants (d)",
              ok, f"f={R['fvec']}, p={R['pvec']}, aut={R['aut']}, nonsimple={R['nonsimple']}, "
              f"stable={stable} (codes at -1/24: {par_name(Rm)}, +1/24: {par_name(Rp)}), "
              f"flags={R['flags']}, superseded={R['superseded']}",
              R["seconds"] + Rm["seconds"] + Rp["seconds"])

    # ---------------- (c) Schmitt rows: one convention for all
    tables = json.load(open(TABLES)) if os.path.exists(TABLES) else None
    conventions = [("H1 (B'' -> ITA: x'=2x'', y'=x''+y'', z'=z''), b = c/a", h1, gram_b),
                   ("H0 (verbatim ITA), b = c/a", h0, gram_b),
                   ("H1, b-alt (c/a)^2 = 3 b^2", h1, gram_b_alt),
                   ("H0, b-alt (c/a)^2 = 3 b^2", h0, gram_b_alt)]
    per_row = {}
    row_results = {}
    for tag, num, fv, b, x, page in SCHMITT_ROWS:
        g = groups[num]
        if tables is not None:
            blk = next(v for k, v in tables.items() if k != "_meta" and num in v["groups"])
            present = any(tuple(r["f"]) == fv and F(r["b"]) == b
                          and tuple(F(s) for s in r["pt"]) == tuple(x) and r["pdf_page"] == page
                          for r in blk["rows"])
            check(f"(c) {tag} row present verbatim in schmitt_hexagonal_tables.json (PDF {page})",
                  present, "", None)
        hits = []
        for label, conv, gf in conventions:
            xc = conv(x)
            G = gf(b)
            try:
                R = run_chain(g, xc, G)
            except Exception as exc:                        # noqa: BLE001
                hits.append((label, f"crash {type(exc).__name__}: {exc}"[:120], None))
                continue
            hits.append((label, R["fvec"], R))
            if R["fvec"] == fv and invariants_ok(R):
                per_row[tag] = label
                row_results[tag] = (label, R, xc)
                break
        detail = "; ".join(f"{lab}: f={fvv}" for lab, fvv, _ in hits)
        R = row_results.get(tag, (None, None, None))[1]
        extra = ""
        if R is not None:
            extra = (f" | exact f={R['fvec']}, p={R['pvec']}, aut={R['aut']}, "
                     f"stab={R['orbit']['stabilizer_order']}, orbit={R['orbit']['n_conventional']}, "
                     f"PERIOD={R['period']}, nonsimple={R['nonsimple']}, flags={R['flags']}, "
                     f"superseded={R['superseded']}, W={R['W']}, D2={R['D2']}, "
                     f"point_ITA={tuple(frac(v) for v in row_results[tag][2])}")
        check(f"(c) {tag} Schmitt {g['international_short']} IT({num}) PDF {page}: f={fv} at "
              f"b-ratio {b}, printed point {tuple(frac(v) for v in x)} -> exact f-vector == printed "
              f"under a documented convention, invariants (d)",
              tag in per_row, f"tried {detail}{extra}",
              sum(h[2]["seconds"] for h in hits if h[2] is not None))
    convs_used = sorted(set(per_row.values()))
    check("(c) ONE convention reproduces all six required rows",
          len(per_row) == len(SCHMITT_ROWS) and len(convs_used) == 1,
          f"conventions used: {convs_used}", None)
    # S178 in IT(179): verbatim then z -> -z
    tag, num, fv, b, x, page = SCHMITT_ROWS[4]
    if "S178" in row_results:
        conv = h1 if per_row["S178"].startswith("H1") else h0
        gf = gram_b_alt if "b-alt" in per_row["S178"] else gram_b
        g = groups[179]
        used, tried = None, []
        for lab, tf in (("verbatim", lambda p: p), ("z -> -z", lambda p: (p[0], p[1], -p[2]))):
            R = run_chain(g, conv(tf(x)), gf(b))
            tried.append((lab, R["fvec"], R["aut"]))
            if R["fvec"] == fv and invariants_ok(R):
                used = lab
                break
        check(f"(c) S178 row run in the second enantiomorph IT(179) P6_522: reproduces under "
              f"'verbatim' or 'z -> -z' (conversion recorded)",
              used is not None, f"used: {used}; tried {tried}", None)
        notes.append(f"IT(179) enantiomorph conversion for the S178 row: {used} (tried {tried})")

    total = time.time() - T0
    allpass = all(ok for _, ok, _, _, req in res if req)
    write_result(res, allpass, total, per_row, notes)
    print(f"\nG2c VERDICT: {'ALL REQUIRED ASSERTIONS PASS' if allpass else 'FAIL — batch 2 quarantined (ANCHORS G2c)'}"
          f"  total {total:.1f}s")
    return 0 if allpass else 1


def frac(x):
    x = F(x)
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def write_result(res, allpass, total, per_row, notes):
    lines = [
        "# G2c result — hexagonal-family controls (2026-09-04)",
        "",
        "Gate: `../../ANCHORS.md` block \"G2c - HEXAGONAL-FAMILY CONTROLS\" (pre-registered "
        "before this run). Pipeline under test: `orbit.py` -> `phase2/metric.py` "
        "(gram_hexagonal, R^T G R = G) -> `phase2/sweep_voronoi_gram.py` (float proposal) -> "
        "`phase2/exact_cell_gram.py` (exact Fractions, G-norm certificate 4*rho^2 <= D^2) -> "
        "`canon_code.py`, compared against `seed_catalog.json` (G2, independent) and Schmitt's "
        "printed trigonal/hexagonal rows (`schmitt_hexagonal_tables.json`). Accepted modules unmodified.",
        "",
        "Verdict: **" + ("G2c ALL REQUIRED ASSERTIONS PASS" if allpass
                         else "G2c FAILED — batch 2 quarantined") + "**"
        + f" (wall {total:.1f} s, single process)",
        "",
        "## Convention confirmed (recorded)",
        "",
        "Per required Schmitt row, the first documented convention under which the exact chain "
        "reproduced the printed f-vector:",
        "",
    ]
    for tag, lab in per_row.items():
        lines.append(f"- {tag}: {lab}")
    lines += ["", "Notes:", ""] + [f"- {n}" for n in notes] + [
        "",
        "## Assertions (with per-assertion wall time)",
        "",
    ]
    for name, ok, detail, secs, req in res:
        lines.append(("- **PASS** " if ok else ("- **FAIL** " if req else "- **NOTE** ")) + name
                     + (f" — {detail}" if detail else "")
                     + (f" — {secs:.2f} s" if secs is not None else ""))
    lines += [
        "",
        "## Honest limits / deferrals",
        "",
        "- Aut orders are COMBINATORIAL map automorphism counts; geometric stabilizers remain G4/V2.",
        "- The transition values c/a = sqrt6, sqrt6/2, sqrt6/4 are irrational and untested; the "
        "rational brackets record the code on each side only.",
        "- Schmitt rows are f-vector-level checks (his tables print f-vectors, not types).",
        "- Convention evidence: six printed rows (plus one enantiomorph re-run) — the P2 pass of "
        "the sweep runs every printed row and counts mismatches, which is the full-table test.",
        "- No hunt sweep runs in this step.",
        "",
        "## Commands run",
        "",
        "```",
        "PY=python3",
        "cd <repo>/harness/phase2",
        "$PY g2c_controls.py      # this gate; writes G2C_RESULT.md; exit 0 required",
        "```",
    ]
    open(os.path.join(HERE, "G2C_RESULT.md"), "w").write("\n".join(lines) + "\n")


if __name__ == "__main__":
    sys.exit(main())
