`arc2_sonnet45_summary.jsonl` was discarded. It proposes moving 3x3 blocks around the
whole 7x7 grid, but the official examples keep every block fixed in place.

`arc2_opus46_summary.json` was also discarded. It describes an anti-diagonal reflection,
but the examples instead apply a different ring permutation around each center-7 cell:
the four corner values rotate one quarter-turn in one direction, while the four
orthogonally adjacent values rotate one quarter-turn in the opposite direction.
