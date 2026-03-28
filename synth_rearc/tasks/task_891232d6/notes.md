`arc2_opus46_summary.json` was directionally correct and I used it as the working hint.

`arc2_sonnet45_summary.jsonl` needed one correction from the official examples:

- The beam does not branch from both ends of a struck `7` run. A successful hit only continues from the run's right edge.
- The bounce only succeeds when the entire elbow corridor on the row below the hit, including the cell just past the run's right end, is empty.
- Otherwise the beam stops with a terminal `6` in the cell below the obstacle; top exits also terminate with `6`.
