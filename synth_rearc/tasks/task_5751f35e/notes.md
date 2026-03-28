`arc2_opus46_summary.json` was useful only as a rough starting point. The official examples show a stricter and slightly richer pattern than that summary states.

The stable rule is:

- each nonzero color belongs to one centered nested region
- for each color, take the smallest grid-centered rectangle that contains that color's clues
- fill those centered rectangles largest to smallest so inner colors overwrite outer ones
- keep `0` outside the outermost reconstructed rectangle when the outer rectangle does not span the whole grid

This correction matters on training pair 2, where the `2` clues do not reach the bottom edge of the final `6x6` region. A plain per-color bounding box would recover only a `5x6` rectangle, but the official output restores the full centered region.
