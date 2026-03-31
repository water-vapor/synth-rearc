`abc82100` is a legend-driven stamping task.

Rule summary:
- Each diagonal `8` component defines a stamp.
- The component's source-facing side center determines the anchor.
- One cell beyond that anchor is the target color marker.
- Two cells beyond it is the source color marker.
- Every other cell of the source color is replaced by a translated copy of the `8` component, recolored to the target color, with the anchor aligned to the source cell.
- Colors that are not source colors and are not part of any legend are preserved.
