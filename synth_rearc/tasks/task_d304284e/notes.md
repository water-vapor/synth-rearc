## Summary hint check

- `arc2_opus46_summary.json` matched the official examples and was used as the working hint.
- I discarded the detailed `arc2_sonnet45_summary.jsonl` analysis. It misreads the second motif as 4 columns wide and overstates the spacing as a width-independent constant, while the official family uses a fixed 3-column motif copied with one blank column between copies.

## Correct rule

1. Read the single orange motif from the input.
2. Stamp that motif to the right with one blank column between copies, coloring the copies in a repeating `7, 7, 6` cycle.
3. For each `6` copy in that top row, stamp the same `6` motif downward with one blank row between copies.
4. Clip partial copies against the right and bottom borders.
