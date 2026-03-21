`arc2_opus46_summary.json` was consistent with the official examples and matched the actual rule.

`arc2_sonnet45_summary.jsonl` was partially misleading. It described the output as if it were sampled from specific boundary positions around the divider. The official examples instead show a `3x3` compression of the whole layout: the middle row and middle column use the shared separator color, and the four corners are the dominant colors of the four quadrants defined by that separator row and separator column.
