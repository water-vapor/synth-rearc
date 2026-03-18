`arc2_opus46_summary.json` was used as the working hint. Its anchor-and-pull description matches the official examples.

`arc2_sonnet45_summary.jsonl` was discarded. It framed the task as generic denoising into rectangles and missed the exact motion invariant visible in the official pairs: each non-anchor cell of a color moves along a fixed `(-1, 0, 1)` step vector toward its own 3x3 anchor block and stops at the first edge-adjacent cell. That distinction matters because some outliers approach diagonally, and some inputs contain short fragments rather than only isolated singletons.
