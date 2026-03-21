`arc2_opus46_summary.json` was directionally useful but needed one correction: the color-7 marker is not always a single connected component in the official examples. The reliable rule is to take the full color-7 partition, form its bounding rectangle, and extract the unique 3x3 ring whose own bounding box lies inside that rectangle.

`arc2_sonnet45_summary.jsonl` was discarded. The 7-cells do not select the answer via a line intersection or nearest-block heuristic; the decisive feature is strict containment inside the color-7 bounding box.
