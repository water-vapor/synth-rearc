`arc2_opus46_summary.json` was used as the starting hint.

`arc2_sonnet45_summary.jsonl` was discarded. It describes copying patterns between horizontal bands only, but the official examples are partitioned by both full rows and full columns into subcells. The real rule is local to each occupied `2x2` cell block: three same-colored cells are given, diagonally opposite cells are related by `180`-degree rotation, and the output fills the missing fourth cell with the `180`-rotated copy of its diagonal opposite.
