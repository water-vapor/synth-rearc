## Hint check

- The `arc2_opus46_summary.json` hint was essentially correct: the cross is redrawn so its hidden intersection lies at the frame's upper-right corner, with the frame color taking priority on overlaps.
- The `arc2_sonnet45_summary.jsonl` hint was a bit misleading because it describes the vertical line as simply "moved" and slightly misstates some frame extents. The cleaner rule is to redraw a full horizontal and vertical line through the frame's upper-right corner, then repaint the frame on top.
