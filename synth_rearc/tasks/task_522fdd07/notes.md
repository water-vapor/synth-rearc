## Summary Hints

`arc2_opus46_summary.json` was consistent with the official examples and I used it as the working hypothesis.

`arc2_sonnet45_summary.jsonl` was discarded. It invents a special "seed" interpretation where a singleton drives the whole transformation, but the official first two training examples contain no singleton at all and are still explained perfectly by the simpler objectwise rule below.

## Corrected Rule

Each non-background object is handled independently on a fresh `7` canvas:

- A singleton expands to a centered `9x9` square of the same color, clipped by the grid boundary.
- Any larger monochrome object is replaced by the interior of its bounding box, which for the official data means removing the outer one-cell border from each filled odd square.
