`arc2_opus46_summary.json` was directionally correct and `arc2_sonnet45_summary.jsonl` was not.

The sonnet summary says the output height equals the number of gray components. On the official examples that is off by one: the correct rule is to count the gray connected components and output a black `n+1` by `1` grid.

I used the official puzzle plus the opus hint, and discarded the sonnet hint because it contradicts every training pair.
