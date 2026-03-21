The summary hint was directionally useful but too high-level to use literally.

What is actually salient in `ac6f9922` is not a single board partitioned into rooms. The relevant objects are the non-border wall-colored rectangles laid out on a coarse row/column grid inside a shared background field. Each output cell corresponds to one such rectangle:
- solid wall rectangle -> output the wall color
- one-cell-thick wall frame with a colored interior fill -> output that interior color

That correction drove both the verifier and the generator.
