Both summary hints were discarded.

`arc2_sonnet45_summary.jsonl` is incorrect because the task is not a column-wise gravity sort. `arc2_opus46_summary.json` is closer, but it still explains the lower color in terms of per-column filling instead of preserving whole 8-connected motifs.

The rule supported by the official examples is:
- find the 8-connected components of the top-row color inside the field of `7`s and translate each one upward until its topmost cell reaches row `1`
- find the 8-connected components of the bottom-row color and translate each one downward until its bottommost cell reaches row `h - 2`
- leave the solid top and bottom border rows unchanged and set everything else to `7`

There is one dataset quirk in training example `0`: the right-edge bottom-color vertical segment is extended upward by two extra cells in the official output. The verifier matches that official output, but the generator follows the clean motif-translation family and avoids that specific edge case.
