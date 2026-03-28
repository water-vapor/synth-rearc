`arc2_sonnet45_summary.jsonl` was discarded for `5034a0b5`. Its vertical-flip explanation is contradicted by every official pair: the border stays fixed, but interior rows are not reversed.

`arc2_opus46_summary.json` was the useful starting hint, but it needed one correction. The border colors do act as directional labels for matching interior cells, and unrelated interior colors stay fixed, but there is no wraparound. When a labeled cell is already adjacent to its matching border, it stays in place instead of wrapping to the opposite side.
