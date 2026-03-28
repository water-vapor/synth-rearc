`arc2_opus46_summary.json` was consistent with the official examples. The deciding feature is the largest 4-connected single-color component, and the output is a `3x3` square filled with that component's color.

`arc2_sonnet45_summary.jsonl` was misleading. It described the task as choosing the color with the largest solid rectangular region, but that fails on the first training example: colors `3` and `5` both admit a largest full rectangle of area `20`, while the correct output is color `3` because its connected component is larger overall (`28` cells versus `20`).
