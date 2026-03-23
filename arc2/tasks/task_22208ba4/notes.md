`arc2_opus46_summary.json` was used as the starting hint.

`arc2_sonnet45_summary.jsonl` was discarded because it introduced spurious corner-specific exceptions. The official examples follow a simpler rule: any corner block whose color appears in more than one corner moves diagonally inward by its own height and width, while colors that appear only once stay at the corner.
