`arc2_opus46_summary.json` matched the official examples and I used it as the starting hypothesis.

`arc2_sonnet45_summary.jsonl` was discarded. Its "gravity by column" explanation fails on the official pairs:
- In training example 2, the `1` rectangle moves from the upper-left to the far right in the output.
- In training example 3, the small `1` shape on the right edge moves to the far left in the output.

The consistent rule is: treat `7` as background, ignore any connected non-background object whose bounding box spans the whole grid, sort the remaining connected objects by increasing size, normalize each one, and repack them side-by-side along the bottom of an all-`7` grid.
