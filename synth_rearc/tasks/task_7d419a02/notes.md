`arc2_sonnet45_summary.jsonl` was discarded for this task. It describes the puzzle as horizontal sections with edge outlining, but the official examples do not transform whole sections or generic borders.

The corrected rule is a butterfly/hourglass recolor around the unique 2x2 `6` block. After rotating wide instances into the tall orientation, the `6` block sits on a 2-row body band inside a grid whose occupied rows come in 2-row bands separated by zero rows. For an `8` cell outside the body, compute its vertical band distance from the `6` rows and its horizontal pair distance from the `6` columns; recolor the cell to `4` exactly when the band distance is less than or equal to the pair distance. Rotating back yields the wide cases.

The Opus hint was useful as a starting point because the butterfly interpretation and the preserved body axis are correct, but it still needed the exact wedge geometry above to match all official examples.
