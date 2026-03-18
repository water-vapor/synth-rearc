## Summary hint check

- `arc2_opus46_summary.json` matched the official examples and was used as the starting hypothesis.
- `arc2_sonnet45_summary.jsonl` was discarded. It describes marker growth along rectangular borders, but the official outputs instead recolor every strictly interior cell of each nonzero blob.

## Correct rule

1. Treat each 4-connected nonzero region as one object, even though it contains both `1` cells and a single non-`1` seed cell.
2. Keep the region's outer one-cell-thick shell unchanged.
3. Find the cells in that region whose full 8-neighborhood also stays inside the same region.
4. Recolor all of those interior cells to the seed color already present in that region.
