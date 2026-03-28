`arc2_sonnet45_summary.jsonl` is wrong for this task. It describes drawing rectangles from markers to lines, but the official outputs instead add a single one-cell-wide orthogonal wire.

`arc2_opus46_summary.json` is broadly correct and was used as the starting point, with one correction: the 3-cell bars are visited in order across the family of parallel lines, so vertical-bar tasks are ordered left-to-right and horizontal-bar tasks are ordered top-to-bottom.
