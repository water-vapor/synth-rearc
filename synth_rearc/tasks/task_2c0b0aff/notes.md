## Summary Hint Notes

- `arc2_opus46_summary.json` is consistent with the official examples: the correct rule is to crop the nonzero rectangle containing the largest number of complete green (`3`) orthogonal pluses.
- `arc2_sonnet45_summary.jsonl` is misleading for this task. The training examples do not support a "most complete/self-contained rectangle" rule. Several distractor rectangles are fully enclosed and rectangular, but they lose because they contain fewer complete `3` pluses.
- Implementation detail: because color `8` is frequently the most common color in the whole input, the verifier cannot rely on `objects(..., without_bg=True)` directly. It first collapses `8 -> 3` to build a nonzero mask, extracts the dense rectangular components from that mask, and then scores each crop by the number of complete green pluses in the original grid.
