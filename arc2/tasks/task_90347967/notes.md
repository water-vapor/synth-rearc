`arc2_sonnet45_summary.jsonl` is wrong for this task: it claims a full-grid `rot180`, but in the larger official examples the singleton `5` stays fixed instead of moving to the opposite corner.

`arc2_opus46_summary.json` matches the training pairs. The correct rule is a point reflection around the unique `5`: every other nonzero cell keeps its color and moves to the location with the opposite row/column offset from that `5`, while all remaining cells become `0`.
