`arc2_opus46_summary.json` matched the official examples and was used as the working hint.

`arc2_sonnet45_summary.jsonl` was discarded. It describes the `3x3` output as if it were sampled from fixed input subwindows, but the official examples instead depend on each nonzero object's enclosed zero-cell count. Those counts are rendered as left-justified color runs in consecutive output rows, ordered by the objects' left-to-right positions.
