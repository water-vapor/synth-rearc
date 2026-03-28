`arc2_opus46_summary.json` was consistent with the official examples and I used it as the working hypothesis.

`arc2_sonnet45_summary.jsonl` was misleading in two ways:
- it describes the transformation as if it were evaluated within each 3-row block, but the actual rule is global across the full 4x6 slot lattice;
- it suggests a border/fill-style conversion, but the output simply recolors whole matching motifs to `8` and whole in-between motifs to `7`, preserving each slot's original occupied cells.

Corrected rule:
- split the grid into 24 `3x3` motif slots separated by zero gutters;
- find the single slot containing color `8` and use its occupied-cell pattern as the template;
- recolor every slot with the same occupied-cell pattern to `8`;
- for any non-template slot strictly between two template-matching slots in the same row or column of the slot lattice, recolor that slot to `7`.
