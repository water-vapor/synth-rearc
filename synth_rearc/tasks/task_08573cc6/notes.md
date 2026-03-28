Rule summary for `08573cc6`:

- The input contains two nonzero color seeds at `(0, 0)` and `(0, 1)` plus a single `1`.
- Starting one cell left of the `1`, draw a clockwise orthogonal spiral.
- Horizontal segments use the first seed color.
- Vertical segments use the second seed color.
- Segment lengths grow as `2, 3, 4, ...`.
- Stop after the first segment that would leave the grid; that last segment is clipped by the border.
