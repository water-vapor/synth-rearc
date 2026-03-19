`arc2_opus46_summary.json` was used as the working hint. Its repeated-`3x3` description matches the official examples exactly.

`arc2_sonnet45_summary.jsonl` was discarded. It overfit the visible `5` row/rectangle effect and treated the placement as a vague empty-region search, but the stable invariant is simpler: the top-left `3x3` pattern is copied once elsewhere, and the output adds a full `5x5` border around that second copy.
