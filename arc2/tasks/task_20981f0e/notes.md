`arc2_opus46_summary.json` was consistent with the official examples and I used it as the working hypothesis.

`arc2_sonnet45_summary.jsonl` was too vague and partially misleading: it described a generic within-band "compaction" into middle rows, but the actual rule depends on both the red marker rows and the red marker columns. The `1`-shape in each 4x4 compartment is preserved exactly and translated so that its 2x2 bounding box is centered inside that compartment; nothing is re-packed or re-shaped.
