`arc2_opus46_summary.json` was consistent with the official examples and useful as a starting hypothesis.

`arc2_sonnet45_summary.jsonl` was rejected. It claims the task cyclically rotates the three horizontal bands and swaps colors `1` and `2`, but the official examples preserve each 3x3 tile exactly and only reorder the nine tiles.

Correct rule:
- Remove the zero separator rows and columns to isolate the nine 3x3 tiles.
- Count the number of `2` cells in each tile.
- Sort the tiles from fewest `2`s to most `2`s.
- Place the sorted tiles back into the 3x3 layout from right to left within each row, keeping the zero separators unchanged.
