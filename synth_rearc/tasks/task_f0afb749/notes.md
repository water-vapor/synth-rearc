`arc2_opus46_summary.json` matched the official examples: every nonzero seed expands to a solid `2x2` block, and every zero cell on that seed's NW-SE diagonal becomes a blue `[[1,0],[0,1]]` marker block.

`arc2_sonnet45_summary.jsonl` was rejected. It describes the blue markers as row/column-dependent "free positions" in an identity-like layout, but the official examples are explained exactly by diagonal closure on `j - i` offsets, with no row/column criterion.
