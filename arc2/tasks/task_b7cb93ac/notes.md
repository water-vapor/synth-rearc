`arc2_opus46_summary.json` was a useful starting hint: the task really is rigid packing of the non-background connected components into a filled `3x4` rectangle, with the unique largest component kept in its input orientation and the smaller components rotated as needed.

`arc2_sonnet45_summary.jsonl` was discarded. Its "template plus relative left/right filling" story does not explain the official examples. The decisive structure is exact tiling of the packed rectangle, not a cross-like template with heuristic side assignments.
