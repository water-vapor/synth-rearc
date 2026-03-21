`arc2_opus46_summary.json` and `arc2_sonnet45_summary.jsonl` were useful only as rough hints for the spatial compression rule.

Both summaries were discarded as generation guidance because the official examples do not show nine independently chosen nonzero cells. They consistently use five distinct latent colors arranged in mirrored pairs:

- the main-diagonal corners match
- the anti-diagonal corners match
- the inner main-diagonal cells match
- the inner anti-diagonal cells match
- the center is a fifth distinct color

The verifier still follows the same compression rule described by the hints: read the nine occupied diagonal positions from the fixed `5x5` layout and pack them into the corresponding `3x3` diamond.
