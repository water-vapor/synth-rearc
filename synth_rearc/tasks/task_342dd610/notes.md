Summary handling for `342dd610`:

- The `arc2_opus46_summary.json` hint matched the official examples and was used as the starting hypothesis.
- The `arc2_sonnet45_summary.jsonl` hint was discarded because it claims variable move distances for colors `1` and `2`.
- The official examples support fixed offsets instead: `1 -> (0, +1)`, `2 -> (0, -2)`, `7 -> (-2, 0)`, `9 -> (+2, 0)`.
