`arc2_opus46_summary.json` matched the official examples and was used as the working hint.

`arc2_sonnet45_summary.jsonl` was discarded. Its ascending-order branch claims the grid is horizontally flipped cell-by-cell, but the first training example only matches if whole dominant-color strips are reordered while preserving each strip's internal noisy pixel pattern. In the ascending case the strip order is reversed; otherwise the strips are cyclically shifted left by one.
