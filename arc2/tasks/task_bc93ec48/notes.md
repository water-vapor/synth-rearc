`arc2_opus46_summary.json` matched the official examples: corner-anchored objects are copied clockwise to the next corner while the rest of the grid stays unchanged.

`arc2_sonnet45_summary.jsonl` was only directionally useful. Its "corner regions rotate clockwise" framing is misleading because the source objects are not removed or swapped out; the output is produced by overlaying the copied corner objects onto the original grid.
