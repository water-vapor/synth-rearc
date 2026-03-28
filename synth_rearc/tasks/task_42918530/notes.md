## Summary hint check

- `arc2_opus46_summary.json` matched the official examples and was used as the working hint.
- `arc2_sonnet45_summary.jsonl` was discarded. Its leftmost-block-per-row rule fails on the training pairs where the copied pattern comes from a same-colored frame in a different row.

## Correct rule

1. Split the grid into a rectangular lattice of `5x5` single-color square frames separated by `0` rows and columns.
2. For each nonzero color, inspect every frame of that color and extract its `3x3` interior.
3. If one frame of that color contains a non-empty interior pattern, treat that interior shape as the template for the color.
4. Copy that shape into every same-colored frame whose interior is completely blank, using the target frame's own color.
5. Leave frames of colors with no non-empty exemplar unchanged.
