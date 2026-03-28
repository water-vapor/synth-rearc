Summary hints were discarded for this task.

- `arc2_opus46_summary.json` says the objects are repositioned to stack around the `5`, but the official examples do not support any pairwise packing rule.
- `arc2_sonnet45_summary.jsonl` describes a generic vertical compaction process, which also fails on the official examples.

Correct rule:

- Extract each non-background connected object independently.
- Move each object straight downward by exactly its own cell count.
- Keep the object's shape and column placement unchanged.
- Let normal clipping remove any cells that fall below the grid.
