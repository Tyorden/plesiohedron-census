## C2 -- full isometry group of each solid (centre-free) and the honeycomb hands

Method: all aut map automorphisms enumerated from the canonical code; an automorphism is an isometry iff its vertex permutation preserves all pairwise squared distances (exact); the affine map is then solved, asserted orthogonal, det and site-fixing recorded. Honeycomb columns come from the banked g4 tables (det of each point operation in the lattice basis; the hand of a translation class is the det of any operation carrying class 0 to it, asserted consistent).

| cell | aut (reversing) | Isom | Isom+ | improper isometries | Isom fixing site | site sym | solid | ops (improper) | T | classes of the other hand |
|---|---|---|---|---|---|---|---|---|---|---|
| S | 4 (2) | 2 | 2 | 0 | 2 | 2 | chiral | 24 (12) | 12 | 6 |
| O | 1 (0) | 1 | 1 | 0 | 1 | 1 | chiral | 24 (12) | 24 | 12 |
| P11 | 2 (1) | 2 | 1 | 1 | 2 | 2 | achiral | 48 (24) | 24 | n/a (achiral solid) |
| P7 | 4 (2) | 1 | 1 | 0 | 1 | 1 | chiral | 48 (24) | 48 | 24 |
| H212 | 3 (0) | 3 | 3 | 0 | 3 | 3 | chiral | 24 (0) | 8 | 0 |
| H230 | 4 (2) | 2 | 2 | 0 | 2 | 2 | chiral | 48 (24) | 24 | 12 |
| H214 | 2 (0) | 2 | 2 | 0 | 2 | 2 | chiral | 24 (0) | 12 | 0 |

Findings: for every cell |Isom| equals the site-symmetry order and every isometry of the solid fixes its Voronoi site, so the about-site stabilizer certified in G4/V2 IS the full isometry group of the solid, and since the site-symmetry operations of G are isometries of the cell (V2 containment), Isom(cell) = site group of G. Consequence for the honeycomb: an isometry of the tiling carries the cell to some cell; composing with the element of G that carries it back gives an isometry of the solid, hence an element of G; so the full symmetry group of every honeycomb here is exactly G. Solids: P11 has one improper isometry (the site mirror) and is achiral; the other six have no improper isometry and are chiral as solids. In an achiral honeycomb (S, O, P7, H230) each improper operation carries the solid-chiral cell to its mirror image (a direct congruence would compose to an improper isometry of the cell), and the hand count above shows exactly half the translation classes of each hand. In the chiral honeycombs (H212, H214) every class has the same hand.
