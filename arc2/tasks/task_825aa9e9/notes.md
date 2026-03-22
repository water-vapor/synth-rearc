# 825aa9e9 Notes

- `arc2_opus46_summary.json` was usable as a starting hint: the moving-color components do fall downward against a fixed support color.
- `arc2_sonnet45_summary.jsonl` was wrong. The official examples are not a vertical reflection or row reordering.
- The corrected rule is: identify the sparse moving color, keep the support color fixed, treat the support plus the row directly above it and the entire bottom row as blocked, then drop each moving connected component straight downward as a rigid object with stacking.
- Example 1 is the key counterexample to the reflection hypothesis: the two isolated `2` pixels in the right chamber stack vertically after falling, which is gravity behavior rather than mirroring.
