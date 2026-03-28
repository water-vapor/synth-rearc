# 9ba4a9aa Notes

`arc2_opus46_summary.json` was directionally useful: the task really does use a unique checkerboard 3x3 marker and a dotted connector network to pick one 3x3 ring block.

`arc2_sonnet45_summary.jsonl` was discarded. The "bottom-right quadrant" heuristic is wrong on the official examples.

Corrected rule:

- Find the unique 3x3 checkerboard block.
- Look at the single non-background cell directly adjacent to that checkerboard; its color identifies the relevant dotted path.
- Follow the connected component of that color using step-2 orthogonal moves between dotted cells.
- The output is the 3x3 ring block touched by that component.

So the important correction is that the selector is not a spatial quadrant heuristic. It is the specific same-color dotted component attached to the checkerboard marker.
