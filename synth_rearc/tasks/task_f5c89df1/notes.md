`arc2_opus46_summary.json` was used as the working hint. Its description matches the official examples: the blue `8` pattern is interpreted relative to the single green `3` anchor, then translated so each red `2` anchor takes over the green anchor's role.

`arc2_sonnet45_summary.jsonl` was discarded. It describes the task as reflection, but the official examples contradict that: every output is a pure translation copy of the original blue offsets, with no mirrored or flipped cells.
