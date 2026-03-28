`arc2_opus46_summary.json` was directionally useful: the task does highlight a maximal diagonal run inside the black region, and the longer of the two diagonal orientations wins.

The official examples add one detail that the summaries do not spell out: when several parallel runs in the winning orientation have the same maximal length, the chosen run is the one closest to the center of the region's bounding box. Train example 2 is the clearest case; three down-left runs have equal length, and the output marks the centered one.
