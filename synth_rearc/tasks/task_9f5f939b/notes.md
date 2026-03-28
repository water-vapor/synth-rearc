`arc2_sonnet45_summary.jsonl` was discarded for this task. It tries to explain the output as a generic row/column intersection pattern, but that interpretation already breaks down on training pair 3 and misses the actual object-level constraint.

The reliable rule is object-based: the input contains only isolated `1x2` dominoes on an `8` background, and a cell becomes `4` only when it is simultaneously centered between two horizontal `1x2` dominoes in its row and two vertical `1x2` dominoes in its column. Equivalently, the output marks the center of a dashed plus made from four separate `1x2` bars.

`arc2_opus46_summary.json` was consistent with the official examples and was used as the starting hypothesis.
