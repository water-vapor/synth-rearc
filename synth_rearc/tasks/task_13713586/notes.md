`arc2_opus46_summary.json` was consistent with the official examples and I used it as a starting hint.

I discarded one detail from `arc2_sonnet45_summary.jsonl`: it says overlapping propagated regions "coexist" and do not overwrite each other. The official training pairs show the opposite behavior. When two filled rectangles overlap, the rectangle seeded by the segment closer to the gray border remains visible in the overlap.
