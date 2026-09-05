# Schmitt IT(220) f=(12,22,12) vs Josehedron — exact type comparison (2026-08-28)

Pipeline: orbit.py (frozen G1 spacegroups.json) -> sweep_voronoi (float, W=2) -> exact_cell (Fractions) -> canon_code. Source table: Schmitt 2016 printed p. 141 (references/Schmitt_2016_dissertation.pdf), point x=(143/1746, 289/3492, 295/3492), frequency 46.

```
Josehedron reference: f-vectors [(12, 22, 12)], p-vectors [(3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4)], aut=4, code_len=163
Schmitt point orbit under IT(220): n_conventional=48, general_position=True, stabilizer_order=1
scaled PERIOD=3492, 48 points/conventional cell
Schmitt cell: f-vectors [(12, 22, 12)], p-vectors [(3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5)], aut=1, code_len=163

VERDICT: NO MATCH — same f-vector, different combinatorial type. The Josehedron's type is NOT identified in Schmitt's in-text IT(220) table at this point; absence remains evidence, not proof.
```
