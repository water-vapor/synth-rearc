`arc2_opus46_summary.json` was used as the working hint. Its Chebyshev-distance description matches the official examples.

`arc2_sonnet45_summary.jsonl` was discarded. It incorrectly described asymmetric rectangles, placed some `5` markers inside the painted region, and missed the simpler invariant visible in the official pairs: each `4` is the center of a filled square of `2`s, and the nearest `5` fixes the square radius as `distance - 1`.
