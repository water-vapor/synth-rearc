`arc2_opus46_summary.json` was consistent with the official examples and I used it as a starting hint.

`arc2_sonnet45_summary.jsonl` was discarded. It treats the task as a switch between a "diagonal zigzag" case and a separate "rectangular frame" case based on a rough ratio threshold, but the official examples are better explained by one construction: a single thin tilted rectangle outline whose two blue cells are opposite corners. When one axis gap is larger, the same outline just picks up straight horizontal or vertical end stretches on that longer axis.
