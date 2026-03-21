`arc2_opus46_summary.json` was a useful starting hint about splitting the `4x9` input into left stencil, separator, and right candidate fill, but its "show the right half wherever the left has 0s" phrasing is incomplete.

`arc2_sonnet45_summary.jsonl` was rejected. Both summaries miss the key gate visible in the official examples: the right-hand colored mask is used only when its nonzero cells exactly match the zero-mask of the left `4x4`. Partial overlap is not enough. When the masks differ, the output is just the left stencil unchanged.
