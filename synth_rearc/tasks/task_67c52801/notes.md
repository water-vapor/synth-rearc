`arc2_opus46_summary.json` was used as the starting hint.

`arc2_sonnet45_summary.jsonl` was discarded because it treats the second-to-last row as a marker pattern for columnwise falling. The official examples instead show that this row is a floor row with zero gaps, and the upper rectangles are reassigned to those gaps by matching one rectangle dimension to each gap width, rotating when needed.
