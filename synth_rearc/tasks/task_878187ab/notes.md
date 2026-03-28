# 878187ab notes

The `arc2_opus46_summary.json` hint is consistent with the official examples and was used as the starting hypothesis.

The `arc2_sonnet45_summary.jsonl` hint was rejected. Its reported counts are wrong on the official examples, and its dimension mapping is too vague:

- Train 1 actually has 5 cells of color 6 and 10 cells of color 8.
- Train 2 actually has 7 cells of color 4 and 5 cells of color 5.
- The output rectangle dimensions are exactly `min(non-bg counts)` by `max(non-bg counts)`, not approximate.

Correct rule:

- Ignore input positions and only count the two non-7 colors.
- Create a fresh `16x16` output filled with 7.
- In the bottom-left corner, draw a `height x width` rectangle of 2s where `height = min(counts)` and `width = max(counts)`.
- Over that rectangle, draw symmetric 4-diagonals row by row from the bottom corners inward; once they meet, they stay mirrored around the center.
