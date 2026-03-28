`arc2_opus46_summary.json` was used as the working hint. Its description matches the official examples: only the `0` rows or columns that lie strictly in the gap between the `7` block and the `9` block are projected onto the `9` span.

`arc2_sonnet45_summary.jsonl` was discarded as too broad. It describes the new `2` cells as using all rows or columns that contain `0`, but the official examples contradict that: extra `0` markers outside the gap remain unprojected in the larger examples.
