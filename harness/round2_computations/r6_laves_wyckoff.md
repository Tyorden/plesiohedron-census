## R6 -- Wyckoff letters of the Laves-graph type sightings (spglib 2.7.0 on the frozen orbits)

| group | point | site-symmetry order (frozen ops) | orbit / conventional cell | orbit / primitive cell | Wyckoff (ITA, from multiplicity and site order) | site symmetry | spglib symmetry of the point set | same canonical code |
|---|---|---|---|---|---|---|---|---|
| IT(199) I2_13 | (1/8, 1/8, 1/8) | 3 | 8 | 4 | 8a | .3. | IT(214) I4_132 | yes |
| IT(199) I2_13 | (1/8, 3/8, 5/8) | 3 | 8 | 4 | 8a | .3. | IT(214) I4_132 | yes |
| IT(212) P4_332 | (1/8, 3/8, 5/8) | 3 | 8 | 8 | 8c | .3. | IT(214) I4_132 | yes |
| IT(213) P4_132 | (1/8, 1/8, 1/8) | 3 | 8 | 8 | 8c | .3. | IT(214) I4_132 | yes |
| IT(214) I4_132 | (1/8, 1/8, 1/8) | 6 | 8 | 4 | 8a | .32 | IT(214) I4_132 | yes |
| IT(214) I4_132 | (1/8, 3/8, 5/8) | 6 | 8 | 4 | 8b | .32 | IT(214) I4_132 | yes |

Reading: every sighting is an eight-point orbit per conventional cell (the vertex set of one Laves graph). In IT(212) P4_332 the sighted orbit is 8c at (1/8, 3/8, 5/8), site symmetry .3.; in IT(213) P4_132 it is 8c at (1/8, 1/8, 1/8); in IT(199) I2_13 it is 8a (.3.); in IT(214) I4_132 both (1/8, 1/8, 1/8) and (1/8, 3/8, 5/8) are eight-point orbits with site symmetry .32 (8a and 8b). The four-point orbits 4a/4b of IT(212)/IT(213) (site symmetry .32) were not among the sightings of this type. spglib on each eight-point set returns I4_132 (the point set's own symmetry), which is why the letters are read from the generating group's position list.
