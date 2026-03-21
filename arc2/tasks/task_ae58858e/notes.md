`arc2_opus46_summary.json` matched the official examples and was used as the working hint:
recolor each orthogonally connected red component to `6` exactly when its size is greater
than `3`.

`arc2_sonnet45_summary.jsonl` was discarded. It claims the transformed cells are maximal
solid rectangles, but the first training example recolors the lower-left red L-tetromino,
which is a single size-4 component and not a rectangle.
