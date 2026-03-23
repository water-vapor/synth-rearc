`arc2_opus46_summary.json` was used as the starting hint.

`arc2_sonnet45_summary.jsonl` was discarded because it describes a generic top-left highlight / bottom-right shadow bevel effect. The official examples are stricter: every non-background object is a `2x2` L triomino, each `5` triomino produces a shifted `4` copy in the direction of its missing corner, and each `2` triomino produces a shifted `3` copy in the opposite diagonal direction. Generated `3` cells may overwrite generated `4` cells, but neither generated color overwrites the original `2` or `5` cells.
