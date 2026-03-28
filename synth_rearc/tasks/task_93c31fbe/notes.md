`arc2_opus46_summary.json` was accurate enough to use as the starting hypothesis, but I discarded the `arc2_sonnet45_summary.jsonl` hint.

The Sonnet hint describes the task as generic reorganization or movement of scattered `1`s around rectangular frames. The official examples are more specific: the non-`1` color is not a full frame at all, but four 3-cell L-corners defining the corners of an implicit rectangle.

The actual rule is box-local reflection. For each implicit rectangle, keep the corner markers fixed, keep only the `1`s whose cells lie inside that rectangle, and add their mirror image across the rectangle's longer central axis. Any `1`s outside all such rectangles are deleted.
