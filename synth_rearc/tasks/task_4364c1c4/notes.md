`arc2_opus46_summary.json` matches the official examples and was used as the working hypothesis.

`arc2_sonnet45_summary.jsonl` was rejected. It describes objects moving toward the nearest grid edge, but that fails on the third and test examples: the motion is determined by vertical touching pairs, not by edge proximity. In the official task, each upper object shifts one column left and each lower object shifts one column right while preserving the exact component shapes.
