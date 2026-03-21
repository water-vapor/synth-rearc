`arc2_opus46_summary.json` was useful as a starting point, but one detail had to be corrected: the output does not preserve the matched solid rectangle intact.

The repeated `3x3` motif is stamped all the way to the nearest aligned edge cell of the matching rectangle, so the nearest `3`-cell strip of that rectangle is partially overwritten by the seed's outer color, with the seed-center color kept only on every third center cell.
