#!/usr/bin/env python
"""canon_code.py — rotation-system canonical planar code (design doc §1.4).

Input: the facet vertex cycles of a convex 3-polytope, all consistently
oriented (CCW seen from outside — exactly what exact_cell.clip_cell emits).
By Steinitz the graph is planar and 3-connected, so the rotation system
determines the embedding up to reflection. The canonical code is the
lexicographic minimum, over all 2E starting darts and BOTH orientations
(4E dart-rooted traversals — the mirror sweep), of a BFS vertex-labeling code
driven by the rotation system.

Rotation system from face cycles: darts are ordered vertex pairs (a,b); with a
consistent orientation each dart lies in exactly ONE face cycle (asserted —
this catches inconsistently oriented input, design §6 risk 6). With
phi(dart) = next dart in its face cycle, the vertex rotation is
sigma((v,w)) = phi((w,v)), a dart out of v; sigma's orbits are the vertices.

Automorphism order for free: map automorphisms (reflections included) act
FREELY on (dart, orientation) pairs and permute the code-minimizing pairs
transitively, so the number of pairs attaining the minimum equals
|Aut+-(map)| — for a chiral map the minimum is attained in one orientation
sweep only (count = |Aut+| = |Aut+-|), for an amphichiral map in both
(count = 2|Aut+| = |Aut+-|). Returned as aut_order.

Cost: O(E) per traversal, 4E traversals, E <= ~114 (design §1.4) — well under
a millisecond per cell.
"""


def rotation_system(face_cycles):
    """Build sigma and sigma^-1 from consistently oriented face cycles."""
    phi = {}
    for cyc in face_cycles:
        k = len(cyc)
        assert k >= 3 and len(set(cyc)) == k, f"bad face cycle {cyc}"
        for i in range(k):
            d = (cyc[i], cyc[(i+1) % k])
            assert d not in phi, \
                f"dart {d} in two faces: cycles not consistently oriented"
            phi[d] = (cyc[(i+1) % k], cyc[(i+2) % k])
    for (a, b) in phi:
        assert (b, a) in phi, f"edge {{{a},{b}}} on only one face: not closed"
    sigma = {(v, w): phi[(w, v)] for (v, w) in phi}
    sigma_inv = {d2: d1 for d1, d2 in sigma.items()}
    return sigma, sigma_inv


def _code(start, rot, n):
    """BFS canonical labeling code from a root dart under rotation `rot`.

    Root vertex gets label 0; at each vertex the outgoing darts are listed in
    rotation order starting from the entry dart (for the root: the start dart);
    unlabeled endpoints get the next label. The per-vertex label sequences,
    concatenated in BFS order, are the code."""
    label = {start[0]: 0}
    order = [start[0]]
    entry = {start[0]: start}
    code = []
    i = 0
    while i < len(order):
        x = order[i]; i += 1
        d0 = entry[x]
        d = d0
        row = []
        while True:
            w = d[1]
            if w not in label:
                label[w] = len(order)
                order.append(w)
                entry[w] = (w, x)
            row.append(label[w])
            d = rot[d]
            if d == d0:
                break
        code.append(tuple(row))
    assert len(order) == n, "graph not connected"
    return tuple(code)


def canonical_code(face_cycles):
    """Return (canon_code_bytes, aut_order) for the polyhedral map."""
    sigma, sigma_inv = rotation_system(face_cycles)
    n = len({v for cyc in face_cycles for v in cyc})
    best = None
    count = 0
    for rot in (sigma, sigma_inv):
        for d in sigma:                       # same dart set for both
            c = _code(d, rot, n)
            if best is None or c < best:
                best, count = c, 1
            elif c == best:
                count += 1
    return repr(best).encode("ascii"), count


if __name__ == "__main__":
    # Full unit tests live in test_canon.py (required deliverable); this is a
    # smoke check only: tetrahedron, faces CCW from outside.
    tet = [[0, 1, 2], [0, 2, 3], [0, 3, 1], [1, 3, 2]]
    code, aut = canonical_code(tet)
    assert aut == 24, aut                     # S4, incl. reflections
    print("canon_code.py smoke: tetrahedron aut_order=24 PASS "
          "(run test_canon.py for the full suite)")
