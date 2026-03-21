# a934301b Notes

`arc2_opus46_summary.json` matched the official examples and was used as the starting hypothesis.

`arc2_sonnet45_summary.jsonl` was discarded. It claims the keep/remove decision depends on the position of a single `8` inside each rectangle, but that does not fit the training pairs:

- rectangles with no `8` are kept
- rectangles with a top-row `8` can still be removed
- kept rectangles are not restricted to a special `8` position

The actual rule is: treat each 4-connected nonzero object as one unit and erase it iff it contains more than one `8`.
