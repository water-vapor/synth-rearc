`arc2_opus46_summary.json` was a useful starting point here, but I discarded the `arc2_sonnet45_summary.jsonl` hint.

The Sonnet summary claims the task recolors "standalone regular geometric shapes". That does not fit the official examples: several clean, isolated shapes stay blue, while some larger stretched shapes turn red. The actual rule is stricter and depends on the top-left red template.

Corrected rule:
- Take the top-left red object as the reference template.
- For every blue connected component, crop its bounding box and collapse only consecutive duplicate rows and consecutive duplicate columns.
- If that reduced binary shape matches the red template under rotation and mirror symmetry, recolor the whole blue object red.
- Otherwise leave it blue.
