`arc2_opus46_summary.json` was directionally correct and I used it as the initial hypothesis.

`arc2_sonnet45_summary.jsonl` was too loose to trust as written: it treats the legend as generic “markers” and suggests patterned/solid blocks interact pairwise. On the official examples the mapping is actually global: each legend color owns one normalized shape, patterned 5x5 blocks decode by that shape up to rotation/reflection, and solid blocks re-encode back to the legend’s displayed orientation.
