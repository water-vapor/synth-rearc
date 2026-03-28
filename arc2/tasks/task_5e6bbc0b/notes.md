`arc2_opus46_summary.json` was consistent with the official examples and I used it as the working hint.

`arc2_sonnet45_summary.jsonl` was rejected. It describes a rough middle split into solid halves, but the official examples instead compress each row or column into a contiguous run whose length equals the count of nonzero checkerboard cells, and only the `8`-bearing row or column gets an adjacent opposite-side `9` run of length `count - 1`.
