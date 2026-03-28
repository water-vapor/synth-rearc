`arc2_opus46_summary.json` was correct enough to use. The official examples do form a comparison table keyed by the nonzero colors in the rightmost column, and each `2x2` table entry is `2` exactly when the two corresponding shapes are the same up to rotation or reflection.

`arc2_sonnet45_summary.jsonl` was rejected. It claims the body is an order-dependent antisymmetric matrix with `2` and `5` determined by row/column order, but the official examples are symmetric instead: `2` appears only for pairs of congruent shapes, `5` for non-congruent pairs, and the diagonal stays blank.
