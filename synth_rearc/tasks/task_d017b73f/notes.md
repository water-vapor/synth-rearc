`arc2_sonnet45_summary.jsonl` was discarded. It describes a 180-degree rotation plus cropping, which does not match any official example.

`arc2_opus46_summary.json` was directionally useful but incomplete. The more precise rule is: each nonzero connected component is a small 4-connected path piece; preserve the left-to-right order, then translate each later piece so its left endpoint sits exactly one cell to the right of the previous piece's right endpoint, producing a single horizontal path chain.
