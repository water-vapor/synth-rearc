`arc2_opus46_summary.json` was used as the starting hypothesis and it matches the official examples: cyan cells that overlap the top-bottom mirror of the input become `2`, while the remaining cyan cells become `5`.

The Sonnet summary was rejected. It proposes a coordinate-based checkerboard/modulo recoloring rule, but the training pairs are explained exactly by vertical self-overlap and contain many cells that contradict the claimed positional arithmetic.
