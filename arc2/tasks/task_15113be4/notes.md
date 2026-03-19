`arc2_opus46_summary.json` was consistent with the official examples and I used it as the starting hypothesis.

`arc2_sonnet45_summary.jsonl` was misleading. It reduces the rule to copying marked columns, but the special-color region actually encodes a full `3x3` mask via a `2x` upscaled shape. A tile changes only when all mask positions are `1`, and only those mask positions are recolored.
