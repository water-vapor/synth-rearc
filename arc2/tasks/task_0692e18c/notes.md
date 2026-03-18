## Summary hint check

- `arc2_opus46_summary.json` was consistent with the official examples and used as the starting hypothesis.
- `arc2_sonnet45_summary.jsonl` was rejected. It claims each occupied block contains a 90-degree counterclockwise rotation of the input, but the official examples instead contain the color-inverted input pattern.

## Correct rule

Let the input be a square grid with background `0` and one foreground color `c`.

1. Swap `0` and `c` inside the input to form an inverted `n x n` tile.
2. Create an `n^2 x n^2` output grid of zeros.
3. For every cell `(i, j)` in the input that contains `c`, place one copy of the inverted tile into output block `(i, j)`.
4. Leave blocks corresponding to background input cells empty.
