`arc2_opus46_summary.json` matched the corrected official examples and was used as the working hint.

`arc2_sonnet45_summary.jsonl` was discarded. Its ascending-order branch depends on the numeric identities of the colors, which is not permutation-invariant and does not survive the upstream fix to training example 1. The corrected task is uniform: split the grid into dominant-color vertical strips, preserve each strip internally, and cyclically shift the strips left by one.
