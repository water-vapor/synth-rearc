`arc2_opus46_summary.json` was useful as a starting hypothesis, but it still needed correction. It correctly identified the 3x3 hollow squares, the edge marker, and the compact one-cell-per-ring map.

`arc2_sonnet45_summary.jsonl` was rejected as incomplete. It stops at the raw ring extraction and misses the last transformation step that actually produces the training outputs.

Corrected rule:
- detect all same-color 3x3 rings with zero centers;
- shrink each ring to one cell at its lattice position to form a compact map;
- use the all-`1` outer edge to choose a gravity direction on that compact map:
  - top edge: pack each row to the right;
  - bottom edge: pack each row to the left;
  - left edge: pack each column upward;
  - right edge: pack each column downward.
