## Summary hint check

- `arc2_opus46_summary.json` was close on the opposite-side reflection idea, but it is still wrong: the reflected copy keeps the tab, and only border clipping can hide that tab.
- `arc2_sonnet45_summary.jsonl` was discarded. It treats the task as vague object-pairing and misses the per-object mirror rule entirely.

## Correct rule

1. Each green object is a hollow rectangular frame with a single centered tab on exactly one side.
2. Mirror that whole object across the axis perpendicular to the tab side.
3. Place the mirrored copy on the opposite side of the original with a one-cell gap between the two bounding boxes.
4. Use color `1` for left/right-tab objects and color `8` for top/bottom-tab objects.
5. Leave the original green objects unchanged; any out-of-bounds part of a mirrored copy is simply clipped by the grid.
