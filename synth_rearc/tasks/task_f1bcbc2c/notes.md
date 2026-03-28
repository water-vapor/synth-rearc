`arc2_opus46_summary.json` was a useful starting hint, but it needed one correction: when the `9` sits on a corner, it is not part of the filled corridor. In those cases the filled `8` path is only the upper corridor branch adjacent to that marker, and the `9` remains unchanged.

`arc2_sonnet45_summary.jsonl` was discarded. It describes the task as a vertical "tube filling" process, but the official examples clearly show a one-cell-wide corridor that can turn horizontally, and the corner-marker cases split a larger candidate component into a target branch and a distractor branch.
