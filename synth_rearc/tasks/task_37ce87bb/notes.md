`arc2_opus46_summary.json` matches the official examples: the output adds a bottom-anchored `5` column at `w - 2`, and its height is `count(8) - count(2)`.

`arc2_sonnet45_summary.jsonl` overfits the examples as an overlap/growth interaction between the `8` and `2` columns. The official pairs do not require row-wise overlap logic; the net cell-count difference alone explains all examples.
