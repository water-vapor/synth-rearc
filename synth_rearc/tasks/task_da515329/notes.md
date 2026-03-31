`da515329` is the clipped infinite-spiral family.

- The `8` input marks four clockwise spiral arms around a missing center cell.
- Let `k` be the arm length in the input cross.
- Each arm starts from the adjacent center cell, keeps going outward for `k-1` cells, then follows the same clockwise `4, 8, 12, ...` spiral scaffold.
- For `k >= 3`, every scaffold leg is split into: `leg - 2`, then a clockwise jog of `k - 2`, then a final stretch of `k`.
- The output is the union of the four infinite arms clipped to the finite grid.
