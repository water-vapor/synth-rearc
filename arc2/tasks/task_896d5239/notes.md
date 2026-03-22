`arc2_sonnet45_summary.jsonl` was rejected for this task. It describes rectangle filling from clusters of `3`s, but the official examples instead show clipped right isosceles triangles with diagonal sides.

`arc2_opus46_summary.json` matched the examples closely and was used as the starting hypothesis. The only important refinement is that the triangles can be clipped by the grid border, so the fill is the in-bounds portion of the triangle while any visible green boundary markers remain `3`.
