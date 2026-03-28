`arc2_opus46_summary.json` and the matching `arc2_sonnet45_summary.jsonl` entry both describe this task as a Sierpinski-like corner fractal. That does not match the official examples.

The official rule is simpler: the input is a single-color corner-anchored `L` on a `6x6` background-7 grid, with leg length `n`. The output is a `16x16` background-7 grid containing a same-corner triangle outline of leg length `2n`, drawn in the same foreground color by doubling the two legs and adding one straight diagonal hypotenuse between their free endpoints.
