`arc2_opus46_summary.json` matched the official rule closely enough to use.

The `arc2_sonnet45_summary.jsonl` hint was discarded. Its main mismatch is the claim that outside markers create full row fills across the rectangle. In the official examples, only markers already aligned with the rectangle's row or column bands extend, and they extend outward away from the rectangle until the grid edge or the next blocker on that same line.
