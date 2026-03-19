Rejected the Sonnet hint. It treats the gray `5` cells as the mechanism that decides which objects move or reflect, but the official examples instead show a simpler anchor-copy rule: every multi-cell motif has one unique least-frequent anchor color, and each isolated singleton of that same color is a destination where the entire motif is restamped with the anchor cell aligned to the singleton.

The Opus hint was the useful starting point, but I generalized it slightly in code: the body of a motif does not need to be color `1`, only the anchor must be the uniquely rare color inside the motif.
