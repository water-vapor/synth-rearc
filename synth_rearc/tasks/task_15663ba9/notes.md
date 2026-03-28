`arc2_opus46_summary.json` was used as the working hint, and `arc2_sonnet45_summary.jsonl` was discarded.

The sonnet summary overfit the task to hollow rectangles plus fixed adjacent edge marks, which does not match the official examples. The actual rule is local to any orthogonal 1-cell-wide cycle: every bend cell is recolored, with `4` for bends whose open-side diagonal leads to the exterior background and `2` for bends whose open-side diagonal faces an enclosed pocket.
