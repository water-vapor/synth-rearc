The summary hints were only partially usable.

- `arc2_opus46_summary.json` is close on the geometry of the transformed black object, but it overgeneralizes the selector as "the non-singleton colored object" with overlap/tie-breaking logic.
- In the official task family, the stable anchor is the gray `5` staircase. The transformed black object is the 14-cell wedge whose vertical span overlaps that gray object most.
- `arc2_sonnet45_summary.jsonl` also overfits the training pairs by talking about arbitrary overlapping colored regions and misses that the black wedge is reduced to its contact edge plus the untouched rectangular body while the two-cell tail is erased.
