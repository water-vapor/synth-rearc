`arc2_opus46_summary.json` was useful as a starting hypothesis: the task is a 4-way overlay of the quadrants formed by the central row/column of `4`s.

`arc2_sonnet45_summary.jsonl` gets the precedence wrong. It claims the top-right `9` quadrant outranks the top-left `7` quadrant, but the official examples show the opposite. For example, in training pair 2, cells with `(TL, TR, BL, BR) = (7, 9, 2, 0)` output `7`, not `9`.

The corrected rule is fixed priority `8 > 7 > 9 > 2 > 0` after removing the divider and aligning the four `5x4` quadrants.
