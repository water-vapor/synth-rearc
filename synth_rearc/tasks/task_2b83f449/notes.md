Rule summary:

- Odd rows contain one or more horizontal `7 7 7` bars on a black background.
- Every such bar becomes `8 6 8`, and the bar center is copied vertically onto the adjacent even rows as `6`.
- The even rows start as `8` rows with border `3`s and occasional internal `0` holes.
- On even rows, the remaining `3` markers are not preserved directly. They are re-derived from how the leftmost and rightmost bar centers change between the odd row above and the odd row below, with holes splitting the row into separate segments.

Generator choices:

- Keep the observed alternating-row layout exactly.
- Sample 1 to 3 non-overlapping bar centers per active odd row, with gradual row-to-row mutations to preserve the staircase-like official distribution.
- Allow sparse single-cell holes on even rows so the generated previews include the same broken-row cases that create internal `3` markers in the official examples.
