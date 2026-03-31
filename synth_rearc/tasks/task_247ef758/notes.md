Rule summary for `247ef758`:

- The input has a left object bank, a solid separator column, and a bordered right playfield.
- Any diagonal-connected left object whose color appears on both the top border and the side border is moved.
- The object is erased from the left bank and stamped into the right interior at every row/column marker intersection for its color.
- The stamp uses bounding-box-center alignment.
- Unmatched left objects stay in place.
- Overlaps resolve bottom-to-top with respect to the source objects on the left, so higher source objects overwrite lower ones.

Generator choices:

- Uses a small library of official-style diagonal-connected motifs: pluses, diamonds, solid blocks, short bars, and diagonals.
- Samples 2-3 movable colors plus optional unmatched left decoys and optional border-only decoy colors.
- Keeps border markers on internal frame positions so stamps stay inside the bordered playfield.
