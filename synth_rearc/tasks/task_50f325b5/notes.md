Both summary hints needed correction.

`arc2_sonnet45_summary.jsonl` was discarded. It treats the task as matching vague rectangular regions and even misreads some changed cells. That is not consistent with the official examples.

`arc2_opus46_summary.json` was the useful starting point. Its core "the `8` cells are the template, and matching `3` copies become `8`" description is correct.

The missing detail is overlap handling. The official task uses the full set of input `8` cells as the template, allows both rotations and reflections, then keeps the non-overlapping matches in reading order. That extra rule is needed for training example 2, where a later overlapping reflected candidate must be ignored.
