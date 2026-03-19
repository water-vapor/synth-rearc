## Summary hint check

- `arc2_opus46_summary.json` matched the official examples and was used as the working hint.
- `arc2_sonnet45_summary.jsonl` was discarded. Its block-count-based color rotations do not fit the training pairs; the output colors are determined by profile matching instead.

## Correct rule

1. Split the grid into 3-row panels separated by full-width `7` rows.
2. In each panel, read the left `8` shape as three prefix lengths inside columns `0..4`.
3. Compute that panel's needed complement to width five, then find the panel whose right-aligned colored shape on columns `7..10` has exactly that three-row profile.
4. Keep the `8` cells fixed, fill the complement on the left with that matched panel's color, and erase the original right-side shape back to `7`.
