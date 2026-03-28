# b942fd60

`arc2_opus46_summary.json` matches the official examples: the red seed grows orthogonal
paths through zero cells, stops one cell before a nonzero obstacle, and branches
perpendicularly from that stopping point. The process repeats recursively and never
overwrites the original nonzero cells.

`arc2_sonnet45_summary.jsonl` was discarded. It misreads the outputs as fixed horizontal and
vertical framing lines chosen from rightmost colored cells, which fails on the recursive
turning behavior in examples like the first, second, and sixth training pairs.
