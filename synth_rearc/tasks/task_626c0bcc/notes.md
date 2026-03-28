`arc2_sonnet45_summary.jsonl` was rejected. Its quadrant-style recoloring story does not survive the official examples: the same row band can contain multiple different output colors, and the correct latent structure is not positional quadrants.

`arc2_opus46_summary.json` had the right core idea, but it needed one correction. The output really is an exact cover by four motif types inside `2x2` boxes:
- color `1`: full `2x2` square
- color `2`: `2x2` with the top-left corner missing
- color `3`: `2x2` with the bottom-left corner missing
- color `4`: `2x2` with the top-right corner missing

The subtlety is that the input is the binary union of those motifs after all nonzero colors have been collapsed to `8`, so a motif's "missing" corner in the output can be filled by a different neighboring motif in the input. The verifier therefore has to recover the unique exact cover of the sky cells rather than classify each visible `2x2` window independently.
