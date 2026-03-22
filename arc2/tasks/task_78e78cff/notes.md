`arc2_sonnet45_summary.jsonl` has no entry for `78e78cff`.

I discarded the `arc2_opus46_summary.json` hint as incomplete. The useful part is that the special color fills row-wise gaps defined by the other foreground color, but the hint incorrectly says the area above and below the occupied band becomes a vertical stripe through the marker column.

That is not true in the official examples:
- training example 2 has a four-cell-wide top and bottom band
- the test example has a three-cell-wide top band and a one-cell-wide bottom band

The corrected rule is:
- on occupied rows, fill the background gap bounded by the nearest left-side and right-side shape cells; if a row only has left-side shape cells, fill from that cluster to the right edge
- on empty rows between the topmost and bottommost occupied rows, fill the whole row
- above the topmost occupied row and below the bottommost occupied row, repeat the fill pattern of the nearest occupied boundary row
