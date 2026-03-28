`arc2_opus46_summary.json` is correct for this task and was used as the working hypothesis.

`arc2_sonnet45_summary.jsonl` is misleading here. It claims the rule is to take the bounding box of all colored cells, rotate it 90 degrees counterclockwise, and place that rotated crop at the top-left. That does not match the official examples: the outputs preserve each rectangle as its own object, keep the left-to-right object order, and overlap consecutive rectangles on exactly one corner cell.
