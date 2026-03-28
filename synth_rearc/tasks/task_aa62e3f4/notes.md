`arc2_sonnet45_summary.jsonl` was rejected for this task. Its "mirror-symmetric outline" description does not match the official examples: the outputs are not reflections of the figure, they are the one-cell-thick orthogonal exterior border of the whole foreground shape.

`arc2_opus46_summary.json` matched the examples. The implemented rule is: find the rarest non-background color, erase the original figure, and draw that color on every background cell that is 4-neighbor adjacent to any cell of the full foreground component.
