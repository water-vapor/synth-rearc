Both summary hints needed correction.

`arc2_sonnet45_summary.jsonl` is misleading and was discarded:
- it says the expansion is approximately the inner height in both directions
- the official examples instead require exact anisotropic target growth: add `2 * inner_height` to the surround height and `2 * inner_width` to the surround width

`arc2_opus46_summary.json` was useful as a starting point but is incomplete:
- it describes simple clipping at the grid edges
- the fifth official example shows a stricter centered-fit rule instead

Reliable rule:
- find the smaller inner rectangle and its color
- target a larger rectangle centered on the original figure, with height `outer_height + 2 * inner_height` and width `outer_width + 2 * inner_width`
- if that target would exceed the grid, shrink it symmetrically around the same center to the largest same-parity rectangle that fits
- fill that centered surround with the inner color
- repaint the original two-color figure on top
