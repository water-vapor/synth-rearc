`arc2_opus46_summary.json` was used as the starting hint.

`arc2_sonnet45_summary.jsonl` was discarded because it invents rectangle-to-rectangle "connection" behavior and even describes a solid rectangle in the first example. The official examples are consistent with a simpler per-object rule: each color-1 object is a `4x4` rectangular frame missing exactly one non-corner border cell, the `2x2` interior is filled with color `2`, the missing border cell is restored as `2`, and that same line continues outward to the grid edge.
