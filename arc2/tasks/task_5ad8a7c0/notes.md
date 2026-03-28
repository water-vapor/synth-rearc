`arc2_opus46_summary.json` and `arc2_sonnet45_summary.jsonl` were both discarded for this task.

The corrected rule is: each non-empty row contains exactly one symmetric pair of red cells, and the output fills the row segment for the row or rows whose two red cells are closest together. This explains examples 2 and 4: the shortest pair is already the adjacent `002200` row, so the selected segment is already complete and the output stays unchanged.

The summary hints instead try to anchor the rule to repeated rows, outer rows, or the global extreme columns. Example 2 breaks those readings immediately because it contains a `200002` row at the global extremes, yet that row is not the one that changes.
