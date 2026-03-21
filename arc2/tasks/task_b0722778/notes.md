`arc2_opus46_summary.json` was used as the starting hint.

`arc2_sonnet45_summary.jsonl` was discarded because it incorrectly reframed the task as a marker-based extraction from fixed columns. In the official examples, each nonblank 2-row band contains three 2x2 blocks: the middle block is either a `vmirror`, `rot90`, or `rot270` transform of the left block, or a pure recoloring with the same shape. The output is the right block with that same per-band relation applied, while the zero separator rows are preserved.
