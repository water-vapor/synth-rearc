`arc2_opus46_summary.json` was used as the starting hint.

`arc2_sonnet45_summary.jsonl` was discarded because it misread several square frames as `5x6`, `7x8`, and `9x10` rectangles. The official examples consistently show odd-sized `2`-colored square frames (`5x5`, `7x7`, `9x9`) with a single preserved red center cell, and the output fills only the remaining interior background with size-dependent colors: `5 -> 8`, `7 -> 4`, `9 -> 3`.
