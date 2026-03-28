`arc2_opus46_summary.json` matched the official examples closely: the output is determined column by column by the lowest red `2`, with all non-red cells above it forced to `0` and all non-red cells below it forced to the third color.

`arc2_sonnet45_summary.jsonl` was too broad to use directly. It describes arbitrary region filling around a general boundary, but the official examples are simpler and more specific: only the lowest `2` in each column matters for the background/fill split, and columns with no `2` stay entirely `0` in the output.
