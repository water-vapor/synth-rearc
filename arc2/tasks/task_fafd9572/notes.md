Both summary hints were discarded as incomplete for `fafd9572`.

- `arc2_opus46_summary.json` says to recolor each separate color-`1` object in scan order from the palette cells. That fails on the second training example: there are `12` four-connected color-`1` pieces but only `6` palette cells.
- `arc2_sonnet45_summary.jsonl` also stays at the level of local clusters/proximity and misses the actual self-similar correspondence.

Correct rule:

- The non-`1` cells form a small colored template shape.
- The color-`1` region is made of larger copies of that same support shape, using eight-connectivity for each copy.
- The upper-left corners of those large copies form a scaled-up copy of the small template shape.
- Read the palette cells in scan order and recolor the corresponding large copy uniformly with that cell's color.

In the second training example, each true target object is an eight-connected 6-cell shape made of two diagonal 3-cell corners, not the individual 3-cell corners themselves.
