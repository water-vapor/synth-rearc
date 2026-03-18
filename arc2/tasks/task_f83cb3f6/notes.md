Used `arc2_opus46_summary.json` as the starting hypothesis and discarded the conflicting `arc2_sonnet45_summary.jsonl` hint.

- The `sonnet45` summary claims some cells outside the `8` frontier can remain unchanged. That is false for the official task: in train example 0, the bottom row contains foreground cells in the input and is cleared completely in the output.
- The `opus46` summary matches the official examples: the `8` cells define a single horizontal or vertical axis, and foreground cells collapse onto the cells immediately adjacent to that axis while preserving row or column identity.

Confirmed rule:

- If the `8` cells lie on one row, then each active `8` column checks whether there is any foreground cell above and/or below it. The output places one foreground cell directly above and/or below the `8` row in that same column.
- If the `8` cells lie on one column, then each active `8` row checks whether there is any foreground cell to its left and/or right. The output places one foreground cell directly left and/or right of the `8` column in that same row.
- All non-`8` cells not represented by that collapse disappear.
