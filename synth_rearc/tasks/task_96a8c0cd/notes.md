# 96a8c0cd

`arc2_opus46_summary.json` matches the official examples closely enough to use: the single
`2` grows straight inward from the border, and each parallel bar reroutes that path to a
fixed side determined by the bar color.

`arc2_sonnet45_summary.jsonl` was discarded. It misreads the task as a generic rectilinear
Steiner-tree or framing problem, but the official examples instead show a single continuous
snake whose detour direction is encoded locally by bar color: `1` takes the
upper/left-counterclockwise bypass, and `3` takes the lower/right-clockwise bypass.
