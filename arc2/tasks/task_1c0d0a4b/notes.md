`arc2_opus46_summary.json` matched the official examples and was used as the working hint: the full-zero rows and columns are separators, and each `3x3` block is color-complemented from cyan-on-black to black-on-red.

`arc2_sonnet45_summary.jsonl` was rejected. It describes a column-wise XOR/parity rule inside each horizontal section, but the training examples are explained exactly by partitioning the grid with the zero frontiers and replacing every in-block `0` with `2` while erasing every in-block `8` to `0`.
