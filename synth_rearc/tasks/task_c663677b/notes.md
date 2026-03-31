The official `arc1/evaluation/c663677b` examples are all `27x27` periodic wallpapers with exact `8x8` row/column period. The input deletes several axis-aligned regions by replacing them with `0`, and the output restores the full wallpaper.

The verifier follows that directly:
- infer the smallest vertical and horizontal periods while treating `0` as unknown,
- recover one base tile by residue-class voting over the visible cells, and
- retile the full `27x27` canvas.

For generation, I matched the observed family rather than a single exact algebra:
- build a symmetric `8x8` tile,
- keep one or two all-`1` frontier rows/columns in the same positions seen in the official set (`7`, optionally `4` or `1`),
- repeat that tile to `27x27`, and
- remove several rectangles while protecting one intact `8x8` period so every residue class remains observable.
