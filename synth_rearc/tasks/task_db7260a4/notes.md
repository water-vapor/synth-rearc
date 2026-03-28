`arc2_opus46_summary.json` was a useful starting point and matches the official rule closely.

`arc2_sonnet45_summary.jsonl` was too loose to use directly. It described a generic "drop into the structure" behavior, but the official examples are stricter: the red shape must contain a valid U-shaped basin with continuous side walls and a continuous bottom edge, and the selected basin is the first valid one whose span satisfies `left < marker_col <= right`. When no such basin exists, the fallback is a full blue bottom row.
