`arc2_opus46_summary.json` was accurate enough to use as the starting hypothesis, but I discarded the `arc2_sonnet45_summary.jsonl` hint.

The Sonnet hint describes a mirror/reflection task with boundary marking. The official examples do not support that: the repeated `2`-patterns are not reflected, and the `8`s always appear at the same internal coordinate as the block's row/column address in the larger block lattice.

The actual rule is self-stamping. A single visible `n x n` template block of `2`s defines an `n x n` array of block positions. Every `2` in the template places a full copy of that template in the corresponding block position of the big grid, and in each placed copy the triggering template cell is recolored from `2` to `8`. The solid `3` bar simply hides one whole template row or column in the input and is erased in the output.
