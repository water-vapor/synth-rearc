`arc2_opus46_summary.json` was used as the starting hint.

`arc2_sonnet45_summary.jsonl` was discarded. Its "irregular rectangles get cleaned up and separated" account misses the actual mechanism visible in every official example: each color is a solid rectangle, some colors have a one-cell-thick same-colored tail attached to one side, and that tail is a displacement instruction. The output repaints all stationary rectangles first, then repaints each tailed rectangle shifted by exactly the tail length in the tail direction, with the tail removed.
