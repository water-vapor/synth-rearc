`88bcf3b4` is a local rerouting task.

Each active motif contains:
- a straight horizontal or vertical anchor line,
- a non-line path object attached to that line by one 4-neighbor cell,
- a nearby target object.

The output preserves the anchor and target. The attached path is erased and redrawn from the same anchor cell so that it heads toward the target, traces the target's distance-1 contour on the side determined by the anchor/target geometry, then continues straight once that contour stops moving farther from the anchor cell.

The generator samples one or two such motifs on a shared background and explicitly constructs both the input path and the rerouted output path from the same latent anchor/target specification.
