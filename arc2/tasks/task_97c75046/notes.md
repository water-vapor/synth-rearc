# 97c75046

`arc2_opus46_summary.json` was useful as a starting hypothesis: the task really does move the
single `5` to a tip on the outer boundary of the `0` region after first approaching the region
from the original side of the marker.

`arc2_sonnet45_summary.jsonl` was discarded. Calling the target a generic "concave corner"
does not explain examples like the second and fourth official pairs, where the correct cell is
found by tracing the exposed staircase edge away from the initial approach point rather than by
looking for a single global indentation.

The rule used here is:
1. Move from the lone `5` straight toward the `0` component until the marker is just outside it.
2. If that contact point continues into a diagonal staircase edge, keep following that exposed
   edge away from the original `5`.
3. Place the `5` on the last reachable boundary cell of that traced edge and restore the old
   marker cell to background.
