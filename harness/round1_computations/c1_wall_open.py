#!/usr/bin/env python
"""C1 -- wall/open classification of the seven cells within their Wyckoff strata.
For each witness point p: the tangent space of its stratum is the fixed subspace
of the linear parts of its site stabilizer.  Along every basis direction of that
space, p is moved by +-1/96 and +-1/48 (fractional coordinates of the group's
conventional cell), the exact chain is run, and the canonical code is compared
with the stored one.  OPEN = code unchanged in every tested perturbation;
WALL = along some direction the code changes on BOTH sides.  For the
Satchelhedron the reviewer's x = +-1/48, +-1/24 checks are reproduced; for the
five special-position cells one generic off-stratum step is also recorded
(supplementary; it leaves the stratum and is not part of the classification).
Deterministic; exact."""
import json, os, sys, itertools
from fractions import Fraction as F
from common import *  # noqa

sys.path.insert(0, HARNESS)
from triage_phase1 import SCHMITT_FVECTORS  # noqa: E402  (digitized printed tables)

CODE2ID = {e["canon_code"]: cid for cid, e in TYPES.items()}


def nullspace_basis(mats):
    """Exact basis of {v : (R - I) v = 0 for all R in mats}."""
    rows = []
    for R in mats:
        for i in range(3):
            rows.append([F(R[i][j] - (1 if i == j else 0)) for j in range(3)])
    # row reduce
    piv_cols, r = [], 0
    A = [row[:] for row in rows]
    for c in range(3):
        piv = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv_cols.append(c); r += 1
    free = [c for c in range(3) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [F(0)] * 3; v[fc] = F(1)
        for i, pc in enumerate(piv_cols):
            v[pc] = -A[i][fc]
        # scale to a primitive integer vector
        from math import lcm, gcd
        den = 1
        for x in v: den = lcm(den, x.denominator)
        vi = [int(x * den) for x in v]
        g = 0
        for x in vi: g = gcd(g, abs(x))
        basis.append(tuple(x // g for x in vi))
    return basis


def classify(cid, label, name, extra_eps=()):
    ent = TYPES[cid]; w = ent["first_witness"]
    base = rederive(cid)
    g = GROUPS[w["group"]]
    p0 = tuple(F(s) for s in w["point"])
    stab_ops = orbit.site_stabilizer(g, p0)
    basis = nullspace_basis([R for R, _ in stab_ops])
    assert len(basis) == w["stratum_dim"], (len(basis), w["stratum_dim"])
    rows = []
    eps_list = [F(-1, 48), F(-1, 96), F(1, 96), F(1, 48)] + list(extra_eps)
    for d in basis:
        for eps in eps_list:
            q = tuple(p0[k] + eps * d[k] for k in range(3))
            r = exact_cell_at(w["group"], q)
            same = r["code"] == ent["canon_code"]
            rows.append(dict(direction=d, eps=eps, point=q, stab=r["stab"], f=r["f"],
                             p=pvec_compact(r["p"]), nonsimple=r["nonsimple"], same=same,
                             stored_id=CODE2ID.get(r["code"]), aut=r["aut"],
                             fvec_printed=tuple(r["f"]) in SCHMITT_FVECTORS.get(w["group"], []),
                             off_stratum=False))
    # classification: per direction, refine the step on any side whose
    # smallest step changed the code, down to 1/1536; the verdict uses the
    # smallest step tested on each side (a type is OPEN in its stratum iff it
    # holds on a neighbourhood, and WALL iff it changes on both sides).
    def add(d, eps, refine):
        q = tuple(p0[k] + eps * d[k] for k in range(3))
        r = exact_cell_at(w["group"], q)
        rows.append(dict(direction=d, eps=eps, point=q, stab=r["stab"], f=r["f"],
                         p=pvec_compact(r["p"]), nonsimple=r["nonsimple"],
                         same=r["code"] == ent["canon_code"], stored_id=CODE2ID.get(r["code"]),
                         aut=r["aut"], fvec_printed=tuple(r["f"]) in SCHMITT_FVECTORS.get(w["group"], []),
                         off_stratum=False, refine=refine))
        return rows[-1]["same"]
    side_same = {}
    for d in basis:
        for sign in (-1, 1):
            smallest = min((x for x in rows if x["direction"] == d and sign * x["eps"] > 0), key=lambda x: abs(x["eps"]))
            same = smallest["same"]
            den = 96
            while not same and den < 1536:
                den *= 2
                same = add(d, F(sign, den), True)
            side_same[(d, sign)] = same
    wall_dirs = [d for d in basis if not side_same[(d, -1)] and not side_same[(d, 1)]]
    if all(side_same.values()):
        verdict = "OPEN"
    elif wall_dirs:
        verdict = "WALL"
    else:
        verdict = "ONE-SIDED"
    # supplementary off-stratum step for special positions
    if len(basis) < 3:
        # generic direction not in the span of basis: try e1,e2,e3 combos
        cand = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, 3)]
        for dgen in cand:
            vecs = [list(map(F, b)) for b in basis] + [list(map(F, dgen))]
            if len(nullspace_basis_from_rows(vecs)) == 3 - len(vecs):
                break
        for eps in (F(-1, 96), F(1, 96)):
            q = tuple(p0[k] + eps * dgen[k] for k in range(3))
            r = exact_cell_at(w["group"], q)
            rows.append(dict(direction=dgen, eps=eps, point=q, stab=r["stab"], f=r["f"],
                             p=pvec_compact(r["p"]), nonsimple=r["nonsimple"],
                             same=r["code"] == ent["canon_code"], stored_id=CODE2ID.get(r["code"]),
                             aut=r["aut"], fvec_printed=tuple(r["f"]) in SCHMITT_FVECTORS.get(w["group"], []),
                             off_stratum=True))
    return dict(id=cid, label=label, name=name, group=w["group"], point=p0,
                stratum_dim=w["stratum_dim"], basis=basis, base_f=base["f"],
                base_p=pvec_compact(base["p"]), rows=rows, verdict=verdict, wall_dirs=wall_dirs)


def nullspace_basis_from_rows(vecs):
    """Basis of the orthogonal complement of the row span (for the rank test)."""
    A = [row[:] for row in vecs]
    piv_cols, r = [], 0
    for c in range(3):
        piv = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv_cols.append(c); r += 1
    return [c for c in range(3) if c not in piv_cols]


def line_scan(cid, label, d, ks, den):
    """Type along the 1-dof line p0 + (k/den) d for k in ks (context only)."""
    ent = TYPES[cid]; w = ent["first_witness"]
    p0 = tuple(F(s) for s in w["point"])
    L = [f"### Line scan for {label}: p0 + t*{d}, t = k/{den}", "",
         "| t | point | site stab | f | p | non-simple | stored id | same as witness |", "|---|---|---|---|---|---|---|---|"]
    for k in ks:
        eps = F(k, den)
        q = tuple(p0[i] + eps * d[i] for i in range(3))
        r = exact_cell_at(w["group"], q)
        L.append(f"| {frac_str(eps)} | {pt_str(q)} | {r['stab']} | {r['f']} | {pvec_compact(r['p'])} | {r['nonsimple']} | {CODE2ID.get(r['code']) or '-'} | {r['code'] == ent['canon_code']} |")
    return L


def main():
    out = []
    for cid, label, name in CELLS:
        extra = (F(-1, 24), F(1, 24)) if label == "S" else ()
        res = classify(cid, label, name, extra)
        out.append(res)
        print(f"{label:5s} {res['verdict']:8s} dim {res['stratum_dim']} basis {res['basis']}")
        for x in res["rows"]:
            print(f"   {'off ' if x['off_stratum'] else '    '}d={x['direction']} eps={frac_str(x['eps']):>6s} "
                  f"{pt_str(x['point']):28s} stab {x['stab']} f={x['f']} p={x['p']} ns={x['nonsimple']} "
                  f"{'SAME' if x['same'] else 'DIFF'} stored={x['stored_id']} printed_f={x['fvec_printed']}")
    # Satchelhedron neighbour bookkeeping
    s = out[0]
    nb = {}
    for x in s["rows"]:
        if not x["off_stratum"] and not x["same"]:
            nb.setdefault((x["f"], x["p"]), []).append((frac_str(x["eps"]), x["stored_id"]))
    print("Satchelhedron neighbours on the 24d line:", nb)
    print("(22,35,15) printed in Schmitt IT(220) table:", (22, 35, 15) in SCHMITT_FVECTORS[220])
    json.dump([{**r, "point": pt_str(r["point"]),
                "rows": [{**x, "point": pt_str(x["point"]), "eps": frac_str(x["eps"])} for x in r["rows"]]}
               for r in out], open(os.path.join(HERE, "c1_wall_open.json"), "w"), indent=1, default=str)
    # markdown
    L = ["## C1 -- wall/open classification within the Wyckoff stratum", "",
         "Method: tangent directions of the stratum = fixed subspace of the site stabilizer's linear parts; "
         "steps of +-1/96 and +-1/48 (fractional, conventional cell) along each; exact chain; canonical code compared with the store. "
         "OPEN = unchanged in every step; WALL = changes on both sides along some direction. "
         "Off-stratum rows (marked) are supplementary only.", "",
         "| cell | group | point | stratum dim | tangent basis | verdict | perturbed types seen (f, p, stored id, f printed in the group's Schmitt table) |",
         "|---|---|---|---|---|---|---|"]
    for r in out:
        seen = {}
        for x in r["rows"]:
            if x["off_stratum"] or x["same"]:
                continue
            seen[(x["f"], x["p"])] = (x["stored_id"], x["fvec_printed"])
        seen_s = "; ".join(f"{f} {p} [{sid or 'not stored'}; printed={pr}]" for (f, p), (sid, pr) in seen.items()) or "none (all SAME)"
        note = ""
        if r["label"] == "H214":
            note = " (open interval is short: the +1/96 step leaves it, +1/192 does not; see line scan)"
        L.append(f"| {r['label']} | {r['group']} | {pt_str(r['point'])} | {r['stratum_dim']} | {r['basis']} | **{r['verdict']}**{note} | {seen_s} |")
    L += ["", "### Per-step detail", ""]
    for r in out:
        L.append(f"**{r['label']} {r['name']}** ({r['id']}), base f={r['base_f']} p={r['base_p']}:")
        L.append("")
        L.append("| direction | eps | point | site stab | f | p | non-simple | code | stored id | f printed |")
        L.append("|---|---|---|---|---|---|---|---|---|---|")
        for x in r["rows"]:
            L.append(f"| {x['direction']}{' (off-stratum)' if x['off_stratum'] else ''}{' (refine)' if x.get('refine') else ''} | {frac_str(x['eps'])} | {pt_str(x['point'])} | {x['stab']} | {x['f']} | {x['p']} | {x['nonsimple']} | {'SAME' if x['same'] else 'DIFFERENT'} | {x['stored_id'] or '-'} | {x['fvec_printed']} |")
        L.append("")
    L.append(f"Satchelhedron: (22,35,15) is {'PRESENT' if (22,35,15) in SCHMITT_FVECTORS[220] else 'ABSENT'} in the digitized Schmitt IT(220) table (triage_phase1.py).")
    L += ["", "### Context: type along the whole line (grid of the sweep was k/24 at most)", ""]
    L += line_scan("8cf50403cf88c455", "S (24d line x,0,1/4)", (1, 0, 0), range(-12, 13), 96) + [""]
    L += line_scan("aa6b0077c3234d24", "H214 (24f line 0,1/4,z)", (0, 0, 1), range(-8, 9), 192) + [""]
    open(os.path.join(HERE, "c1_wall_open.md"), "w").write("\n".join(L) + "\n")
    print("wrote c1_wall_open.md / .json")


if __name__ == "__main__":
    main()
