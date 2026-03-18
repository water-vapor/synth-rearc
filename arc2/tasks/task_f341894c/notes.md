`arc2_sonnet45_summary.jsonl` was discarded, and `arc2_opus46_summary.json` was only used as a partial hint.

- The Sonnet summary claims the task is about vertical mirror symmetry. That does not match the official examples: the changes are local `1`/`6` swaps, not a whole-grid reflection constraint.
- The Opus summary correctly identifies the role of same-line `7` markers and local `1`/`6` swaps, but it states the swap condition backwards.

Correct rule:

- Each active object is a horizontal or vertical adjacent `1`/`6` domino.
- A singleton `7` lies somewhere else on that same row or column and determines the direction for that domino.
- In the output, the domino is oriented so that the `6` is the cell nearest the nearest same-line `7`, and the `1` is the cell farther from that marker.
- Background `8` cells and all `7` markers stay unchanged.
