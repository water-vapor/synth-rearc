`arc2_opus46_summary.json` was used as the starting hint.

Its main reconstruction rule was correct: the non-legend occurrences of each legend row's left color define a sparse parity marker for a larger rectangle, and the output fills the one-cell-expanded rectangle with the row's two colors.

One detail was wrong in the hint: the overwrite order is not top-to-bottom legend order. The official examples only match when the legend rows are painted in reverse order, so the top legend row has the highest priority in overlaps.
