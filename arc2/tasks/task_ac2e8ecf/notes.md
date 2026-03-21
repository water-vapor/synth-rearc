`arc2_opus46_summary.json` is consistent with the official examples and was used as the working hypothesis.

`arc2_sonnet45_summary.jsonl` was discarded. It claims the split is based on whether an object starts in the upper or lower half of the input, but that does not match the official examples: in `ac2e8ecf`, hollow rectangular frames move upward and all other row-and-column cross/T shapes move downward, regardless of their starting half.
