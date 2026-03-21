`arc2_sonnet45_summary.jsonl` had no entry for this task.

`arc2_opus46_summary.json` was discarded as written. It only matches the dense full-row cases, but several official training inputs have `7` gaps in the seed row, so there is no contiguous non-background span and no evidence that the lower rows need both diagonal parents.

The official examples are explained by a simpler rule:

- Only the top row contains seed cells, using colors `2`, `5`, and sometimes `7` gaps.
- Let the active seed interval run from the leftmost non-`7` seed cell to the rightmost non-`7` seed cell.
- Each lower row is produced by shifting the previous active segment one cell down-right, swapping `2 <-> 5`, and leaving `7` unchanged.
- The active interval shrinks by one cell on each side per row, which creates the downward triangle seen in the outputs.
