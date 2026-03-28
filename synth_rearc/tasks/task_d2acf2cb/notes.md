`arc2_opus46_summary.json` was consistent with the official examples and I used it as the starting hypothesis.

I discarded the `arc2_sonnet45_summary.jsonl` hint. It invents broader "regions" between 4-marked boundaries and talks about recovering nearby patterns, but the official task is narrower: a `4` only matters when it appears at both border ends of the same row or the same column, and the cells strictly between those endpoints are recolored by the fixed involution `0 <-> 8` and `6 <-> 7`.
