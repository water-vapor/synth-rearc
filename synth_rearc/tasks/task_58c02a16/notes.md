Discarded the summary hints as exact guidance.

- The sonnet summary describes the task as inserting separator 7s between motif copies; that does not match the official examples.
- The opus summary is closer, but it treats the entire top-left motif as the repeated template and reverses the recoloring direction.

Correct rule:

- The actual seed is the upper-left subgrid before the solid secondary-color border row and border column.
- The seed contains only the primary color and background 7.
- Each primary-color seed cell selects an unrecolored seed copy; each 7 seed cell selects the same seed with the primary color recolored to the secondary border color.
- That self-similar macro-tile is then repeated periodically and cropped to the full grid size.
