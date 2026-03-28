`arc2_opus46_summary.json` had the main structure right: the interior is built from nested square boxes with the repeating color cycle `2, 5, 0, 5`. `arc2_sonnet45_summary.jsonl` was incomplete because it omitted the invisible `0` layer entirely.

There is one small official-example wrinkle: the `9x9` outer frame example (so a `7x7` interior) stops at the `3x3` zero box instead of adding the final singleton `5` that the naive cycle would predict. The verifier and generator preserve that observed `7x7`-interior edge case so the official examples match exactly.
