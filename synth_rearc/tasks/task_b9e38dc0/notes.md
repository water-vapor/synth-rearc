`b9e38dc0` is modeled as a directional beam puzzle.

- Normalize the task so the largest non-background color forms a horizontal projector bar near the top.
- Propagate the beam row by row below that bar.
- Existing non-background cells block the beam and split it into independently growing components.
- Narrow one-sided components created by single-cell splits only widen every other row, which is the key detail needed for the official examples.

The generator samples directly in this normalized downward-beam space, adds walls and later blockers, and then rotates the finished example back into one of the task-family orientations.
