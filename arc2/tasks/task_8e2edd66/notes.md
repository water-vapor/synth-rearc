`arc2_opus46_summary.json` was correct enough to use. The official examples do form a `3x3` array of `3x3` blocks, and each filled block is the input's zero-mask recolored with the single foreground color.

`arc2_sonnet45_summary.jsonl` was rejected. It claims each filled block is a `90°` counter-clockwise rotation of the input, but the official examples contradict that: the block pattern is the color-inverted input, not a rotation.
