Legend rows in a narrow left strip encode `source -> target`.

- Left cell is always the source color.
- Right cell is the fill color when present.
- Missing right cells, background right cells, and explicit `0` right cells are treated as unmapped.

Main objects use one color per family. For mapped colors:

- Paired corner Ls complete their overall bounding box with the mapped color via `underfill`.
- Full 2x2 squares recolor to the mapped color via `fill`.

Boxes are applied from smaller to larger so nested regions behave like the official task.
