`arc2_opus46_summary.json` was used as the starting hint.

`arc2_sonnet45_summary.jsonl` was discarded because it incorrectly described the task as a cellular automaton. The official examples instead encode the top-row run length `n` as a 1D sequence of same-color blocks with lengths `1,2,...,n,...,2,1`, separated by single zero cells and then wrapped row-by-row to the original input width.
