`arc2_sonnet45_summary.jsonl` was discarded for this task. Its "diagonal swap" story does not match any official example once the full-line separators are examined.

`arc2_opus46_summary.json` was useful as a starting point, but it needed one correction: the recursive partition is driven by the non-4 full-line separator color at the current level, while a single full row or column of color 4 inside a 9x9 base panel is not another recursive partition. That color-4 line is the mirror axis for the whole base panel.

The actual family is:
- 9x9 base panels with four 3x3 solid blocks and either a zero cross or a single color-4 mirror axis.
- Leaf base panels use color 1 as a placeholder and replace it with the panel's only other nonzero color.
- Larger examples tile those 9x9 panels with full separator rows and/or columns in color 5, 7, or 9, then solve each child panel recursively.
