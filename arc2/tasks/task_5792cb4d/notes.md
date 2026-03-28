`arc2_opus46_summary.json` was a useful starting hint: it correctly describes the task as reversing the color order along a fixed connected path.

`arc2_sonnet45_summary.jsonl` was rejected. Its anti-diagonal-reflection claim fails on the second training example, where the occupied cells stay in place and only the path's color sequence is reversed end-to-end.
