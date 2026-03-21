`arc2_opus46_summary.json` was a useful starting hint and matches the official examples.

`arc2_sonnet45_summary.jsonl` was discarded. Its rotation hypothesis is wrong: the task does not rotate the input. The actual rule keeps the same orientation, swaps the outer and inner L-borders between the two non-8 colors, places `8` at the outer and inner corner junctions, and fills the remaining interior with `8` except for a same-direction diagonal of the interior color extending away from the original L-corner.
