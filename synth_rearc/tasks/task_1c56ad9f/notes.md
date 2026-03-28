`arc2_opus46_summary.json` was directionally useful, but `arc2_sonnet45_summary.jsonl` describes the alternation as if it starts from the top of the figure. The official examples do not support that.

The correct anchor is the bottom of the foreground figure's bounding box:
- shifted rows are exactly the rows whose distance from the bottom row is odd
- the first shifted row just above the bottom moves left
- higher shifted rows alternate right, left, right, ...

The input family is a single-color orthogonal lattice inside a rectangular bounding box, formed by the union of selected horizontal bar rows and selected vertical bar columns.
