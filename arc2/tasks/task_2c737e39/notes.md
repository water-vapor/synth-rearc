`arc2_opus46_summary.json` was rejected because it assumes the source anchor gray cell is always contained inside the copied shape. The official task family includes an adjacent-anchor case where the source gray sits next to the motif and is not part of the copied component.

The corrected rule is: find the largest non-background object, use the gray cell that is either inside that object or directly adjacent to it as the source anchor, then copy only the non-gray motif so that this source anchor aligns with the other gray cell. The target gray is cleared in the output.
