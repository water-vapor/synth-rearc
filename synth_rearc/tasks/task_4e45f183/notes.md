Both summary hints were discarded.

`arc2_sonnet45_summary.jsonl` is incorrect: the official examples do not impose vertical mirror symmetry inside each 5x5 tile.

`arc2_opus46_summary.json` is closer because it identifies the nine center-of-mass buckets inside the tiles, but it still gets the action wrong. The motifs are not slid within their original tiles. Instead, each tile is moved to the output slot whose 3x3 position matches that tile's foreground center-of-mass bucket.
