# 6d1d5c90

- `arc2_sonnet45_summary.jsonl` was usable after simplification. Its modular arithmetic description reduces to a plain cyclic downward row shift by the marker row index.
- `arc2_opus46_summary.json` was rejected. It says the row containing `2` should move to the top after removing column 0, but train example 1 has the marker on row 2 and the output order is rows `4,5,0,1,2,3`, not `2,3,4,5,0,1`.
- Correct rule: remove the first column, find the row of the lone `2` in that column, then rotate the remaining six rows downward by that row index.
