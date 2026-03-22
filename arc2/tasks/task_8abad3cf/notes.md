`arc2_sonnet45_summary.jsonl` was discarded for this task. It describes the puzzle as extracting rectangular regions, but the official examples are governed by non-background color frequencies instead.

`arc2_opus46_summary.json` was a useful starting point, but one detail is wrong: the optional singleton does not go at the top-left of the embedded secondary square. In the official examples it lands at the bottom-left corner of the left panel, with one background column separating it from the secondary square.

Corrected rule:
- Ignore background color `7`.
- Sort the remaining colors by frequency.
- The most frequent color has a square count `n^2`; it becomes a solid `n x n` block on the right.
- The second color has a square count `m^2`; it becomes an `m x m` block in the lower part of a `7`-background panel on the left.
- If a third color exists, it is always a singleton and becomes the bottom-left cell of that left panel.
