The summary hint is close but incomplete. Both `arc2_opus46_summary.json` and `arc2_sonnet45_summary.jsonl` describe the output size as `(# horizontal divider rows + 1) x (# vertical divider columns + 1)`, but training example 3 has a full separator column on the left border and the output width is still `3`, not `4`.

The corrected rule is to count contiguous non-separator row bands and contiguous non-separator column bands. Internal separator lines split one band into two, while a separator that sits on a border only trims the canvas edge and does not create an extra band.
