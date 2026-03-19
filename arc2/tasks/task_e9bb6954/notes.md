`arc2_opus46_summary.json` was used as the starting hint.

`arc2_sonnet45_summary.jsonl` was discarded because it misread the source objects as larger `3x4` blocks and described a vague intersection-priority rule. The official examples consistently use isolated solid `3x3` squares as the only generators, and every crossing between different-colored projected rows and columns is cleared back to `0`.
