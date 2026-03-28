`arc2_opus46_summary.json` matched the official examples closely enough to use as the working hint.

`arc2_sonnet45_summary.jsonl` was discarded. It treats every `6` as an output marker, but the official pairs only keep the far endpoint of each straight lower-half `2 -> 6...6` segment.

The reliable rule is:

- keep the full-width `9` row as the horizontal mirror axis
- in the lower half, each red `2` is attached to one straight orthogonal ray of one or more magenta `6`s
- erase the anchor `2` and all intermediate `6`s, keeping only the far `6` endpoint as a red `2`
- place a gray `5` at the vertical mirror of that endpoint across the `9` row
- erase the original upper-half gray distractors back to background `7`
