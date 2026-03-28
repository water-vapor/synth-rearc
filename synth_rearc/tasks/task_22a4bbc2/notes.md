`arc2_opus46_summary.json` matched the official examples and was used as the working hint.

`arc2_sonnet45_summary.jsonl` was discarded. It describes duplicated row patterns and special handling of first duplicate occurrences, but the official task is simpler and component-based: extract the nonzero 4-connected monochrome components, order them from top to bottom, and recolor every third component starting with the topmost one to `2`.
