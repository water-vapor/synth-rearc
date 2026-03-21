`arc2_opus46_summary.json` matched the official examples closely enough to use as the working hypothesis.

`arc2_sonnet45_summary.jsonl` was rejected. It invents divider bands and a reflection story that do not match the training pairs. The actual input is just a left-to-right sequence of top-anchored solid rectangles separated by background columns.

Corrected rule:
- extract the foreground rectangles in left-to-right order;
- for each rectangle with height `h` and width `w`, let `a = min(h, w)` and `b = max(h, w)`;
- lay `a x b` rectangles across the top of a 10-row output, separated by one background column;
- independently lay `b x a` rectangles across the bottom of the same output, also separated by one background column.
