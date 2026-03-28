# 45737921 notes

- `arc2_opus46_summary.json` matched the official training examples: each disconnected nonzero object keeps its geometry and simply swaps its two colors.
- `arc2_sonnet45_summary.jsonl` was rejected. It claimed each object is also horizontally reflected, but the official examples do not show any reflection. For example, `585/585/888` becomes `858/858/555`, which is exactly a color swap and not a mirror operation.
- Generator choice: use multiple separated full `3x3` two-color blocks, because every official object is a fully occupied `3x3` component and the task acts independently on each block.
