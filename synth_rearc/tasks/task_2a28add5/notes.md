Summary hints corrected for `2a28add5`.

- The Sonnet summary is not usable. It invents cluster detection, bounding boxes, and singleton preservation, none of which match the official examples.
- The Opus summary is closer, but still wrong: it says to fill the span from the row's leftmost non-`7` to rightmost non-`7` whenever a row contains `6`.
- The actual rule is row-local and depends on the `6`'s ordinal position within that row's non-`7` cells.

Corrected rule:

- Start from a `7` background.
- For each row containing a `6`, count the non-`7` cells strictly to the left of that `6` and strictly to the right of it.
- Replace the whole row in the output by a contiguous run of `8`s on the same row, with the run extending that many cells left and right from the `6`'s column.
- Equivalently, the row's non-`7` cells are collapsed into one contiguous block while preserving the `6`'s rank among them.
