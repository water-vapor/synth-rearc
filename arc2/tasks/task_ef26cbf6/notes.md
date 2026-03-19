`arc2_opus46_summary.json` was usable as the starting hypothesis. `arc2_sonnet45_summary.jsonl` was discarded.

The sonnet hint collapses the task to horizontal sections and "nearest marker" recoloring, which does not fit the official examples. The examples instead show a stricter paired-compartment rule:

- Divider lines of `4` split the grid into `3x3` compartments.
- One side of the layout contains exactly one colored sample cell per compartment.
- The opposite side contains a blue `1` motif in the paired compartment.
- Every `1` in that motif is recolored to the paired sample color, while background `0`, divider `4`, and the sample cell itself stay unchanged.
- The sample side is not fixed: the official examples use left, top, and right placements.
