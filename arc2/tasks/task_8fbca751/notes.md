`arc2_opus46_summary.json` is consistent with the official examples: each connected sky-blue component is completed to its own bounding rectangle, and the missing cells inside that rectangle are filled red.

`arc2_sonnet45_summary.jsonl` was discarded. Its "largest solid block stays unchanged, other 8s get marked" hypothesis does not match the training pairs, where every component participates uniformly in the rectangle-completion rule.
