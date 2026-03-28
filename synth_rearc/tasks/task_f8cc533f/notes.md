`arc2_sonnet45_summary.jsonl` is incorrect for `f8cc533f`: the task is not per-object vertical reflection.

`arc2_opus46_summary.json` is also incomplete and misleading: each object is not repaired from its own local symmetries alone.

Correct rule:
- Each non-background color marks one damaged copy of the same latent square template.
- Normalize every colored object to its own upper-left corner, then union those normalized shapes to recover the shared template.
- Repaint that recovered template at every object's original upper-left corner, preserving each object's color.

This explains the one cropped 5x4 example as well: it is just a damaged top-left-aligned copy of the shared 5x5 template.
