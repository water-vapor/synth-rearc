`arc2_opus46_summary.json` was consistent with the official examples and I used it as the starting hint.

I discarded `arc2_sonnet45_summary.jsonl` for the output rule. It correctly notices that the inputs contain horizontal bars of colors `3` and `2`, but its explanation of the leftover output cells is wrong. The official pairs are simpler: count connected components of `3`, then connected components of `2`, write that many `3`s and `2`s into a fixed 6-cell row-major buffer, and leave the remaining cells `0`.
