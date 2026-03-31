The task decomposes the input into 5x5 motif panels separated by full `6` rows and columns.

Panels are ordered by a shape-only key:
- lower vertical placement first, measured by `uppermost + lowermost`
- then motifs that reach the panel's right edge
- then the right-to-left foreground column-count profile

When every panel shares the same vertical center, the ordered motifs are concatenated horizontally.
Otherwise they are stacked vertically.

The generator mirrors the official distribution with two families:
- middle-band motifs that all share the same vertical center and therefore produce horizontal outputs
- mixed bottom/full-height/top motifs that produce vertical outputs
