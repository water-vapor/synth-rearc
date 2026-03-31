Rule summary:

- Treat each nonzero, non-`5` connected component as a motif with one distinguished geometric center cell.
- The `5` cells form a single 8-connected connector graph.
- Find the two diameter terminals of that connector graph.
- For each terminal, choose the locally attached motif with the smallest terminal-contact footprint.
- Keep only those two motifs.
- Each kept motif keeps its outer color and replaces its center color with the center color of the motif whose outer color matches the kept motif's original center color.
- All other motifs disappear; the `5` connector remains unchanged.

Generator summary:

- Sample one of six canonical layout families distilled from the official examples.
- Recolor motifs with fresh non-`5` colors and random one-step center mappings.
- Render canonical input/output grids explicitly, then apply a random global dihedral transform.
