The `arc2_opus46_summary.json` hint is only partially reliable for `1478ab18`.

It correctly says the output is a right triangle drawn from a pair of `5` markers plus the row/column-swapped missing corner, but it says to choose the farthest pair that share a row, column, or diagonal. That is not sufficient: in all three official training examples there are row or column pairs tied with the active pair, and those are not used.

The reliable rule is:
- Among the four `5` markers, find the unique longest diagonal pair.
- The other square corner on that diagonal is missing; the remaining visible square corner is just a distractor.
- Draw the hypotenuse between the longest diagonal pair and the two legs from the missing corner to those endpoints in color `8`, leaving every original `5` unchanged.

For generation, the fourth `5` is sampled inside the same square's bounding box with a strong bias toward the inactive diagonal, which matches the official examples.
