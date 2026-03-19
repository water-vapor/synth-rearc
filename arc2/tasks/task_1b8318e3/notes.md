The Sonnet and Opus summaries were useful as a starting point, but both were incomplete on the placement rule.

The summaries describe the non-`5` cells as moving to positions that are orthogonally adjacent to the nearest `5` block. That is not fully correct: the official outputs also use diagonal corner cells, and the placement is not just a nearest-cell clamp.

The implemented rule is:

1. Order the `5` anchors by proximity to each singleton.
2. For each singleton, take the nearest anchor first and compute its preferred halo cell from the singleton's offset to the `2x2` block:
   - equal row/column offsets go to the matching halo corner
   - otherwise the larger offset chooses whether the point lands on a row side or a column side
   - one left-corner case shifts inward when that side is already occupied
3. If that preferred halo cell is already occupied, try the next anchor.

That is why the summary hint was discarded rather than used directly.
