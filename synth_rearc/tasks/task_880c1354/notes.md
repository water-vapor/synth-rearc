`arc2_opus46_summary.json` was useful as a starting hint, but the sonnet summary overstates the structure as four corner regions in every case. The official examples show that the number of non-4/7 border components can collapse to 3 or 2 when adjacent corners stay connected around the fixed 4/7 scaffold.

The corrected rule is: keep the 4/7 scaffold unchanged, order the non-4/7 connected components by their first clockwise touchpoint on the outer border, and rotate their colors forward by one step around that border cycle.
