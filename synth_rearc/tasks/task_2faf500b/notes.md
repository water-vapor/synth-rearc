`arc2_opus46_summary.json` was used as the starting hint.

`arc2_sonnet45_summary.jsonl` was discarded because its "reflection axis" description is too loose and does not match the row-by-row and column-by-column mechanics in the official examples. The exact rule is not a mirror or swap: each nonzero rectangle contains a zigzagging `6` divider in the two central columns or rows, and the output removes the `6`s while pushing the `9` runs away from that divider into two separate half-blocks.
