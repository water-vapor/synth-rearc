`arc2_opus46_summary.json` was directionally useful; `arc2_sonnet45_summary.jsonl` was discarded.

The Sonnet hint describes the task as a broad color swap based on overlapping column spans. That does not match the official examples. Each connected `{5,7}` component actually contains a solid rectangular `7` block and a same-row or same-column run of exterior `5` cells. The output clears those exterior `5`s back to `4` and moves the same `5` area into the `7` rectangle as an interior strip attached to the matching edge row or column.
