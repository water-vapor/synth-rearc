The `arc2_opus46_summary.json` hint was close but incomplete. It described painting the full row span and full column span of the `8` rectangle across the whole grid while merely preserving `1` cells.

The official examples show a stricter rule: each horizontal or vertical arm extends outward from the `8` rectangle only until the nearest `1` blocker in that row or column. The `1` cells are preserved and also clip the arm, while `0` and `2` are repaintable to `4`.
