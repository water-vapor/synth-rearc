`eee78d87` treats the 3x3 colored motif as a compressed lattice stencil.

- Corners map to cell interiors.
- Top and bottom middles map to vertical segments.
- Left and right middles map to horizontal segments.
- The center maps to intersections.

The output paints the selected stencil features in `9` inside the centered window, and paints the complement of those feature types across the full 16x16 lattice in the background color `7`.
