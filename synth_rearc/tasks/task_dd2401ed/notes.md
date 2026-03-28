# Notes

`arc2_sonnet45_summary.jsonl` was discarded. It describes the gray bar shift correctly only vaguely and claims the in-between red cells always turn blue, which is contradicted by official example 3: the bar moves from column 3 to column 7, but the red cells at columns 5 and 6 stay red.

`arc2_opus46_summary.json` was used as the working hint. Its all-or-nothing recolor condition matches the official examples: collect the blue offsets to the left of the gray bar, move the bar one column beyond the farthest mirrored extent, and recolor the red cells in the gap only when every blue offset is represented by at least one red cell on the right side before the new bar.
