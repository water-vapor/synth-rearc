`arc2_opus46_summary.json` was used as the initial hint and matched the official examples closely.

`arc2_sonnet45_summary.jsonl` was discarded. It says the output marks only the "outermost" `4` cells with `3` and frames the transformation as depending on already aligned `2` fragments. In the official examples, every original `4` cell is recolored to `3`, and the activated rows or columns are determined by the support of the `4` objects; the `2` side only contributes the per-line count that gets packed against the far border.
