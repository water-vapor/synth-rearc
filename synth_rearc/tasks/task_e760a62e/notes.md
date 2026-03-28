`arc2_opus46_summary.json` matched the official examples closely enough to use as the working hypothesis.

`arc2_sonnet45_summary.jsonl` was not reliable for this task. Its main error is the claim that color `2` always expands vertically and color `3` always expands horizontally. In the official examples, both colors can connect across either shared block-rows or shared block-columns inside the blue `8` lattice, and any overlap between the two completed color regions becomes `6`.
