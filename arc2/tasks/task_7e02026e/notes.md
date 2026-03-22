## Summary hint check

- `arc2_opus46_summary.json` matched the official examples and was used as the working hint.
- `arc2_sonnet45_summary.jsonl` was discarded. Its "rectangular holes" explanation does not fit the training pairs; the changed cells are exactly the union of orthogonal 5-cell pluses made of `0`.

## Correct rule

Find every `0` cell whose up, down, left, and right neighbors are also `0`. Recolor every cell belonging to any such 5-cell plus from `0` to `3`, and leave all other cells unchanged.
