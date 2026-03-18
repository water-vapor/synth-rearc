`arc2_sonnet45_summary.jsonl` was discarded for this task. Its main claim is that the hollow frames are filled with a generic diagonal-stripe pattern, but the official `f21745ec` examples show a different rule: one pre-patterned rectangle provides the exact interior occupancy mask.

The usable hypothesis came from `arc2_opus46_summary.json` and matches the examples. Every rectangle whose outer dimensions match the patterned template keeps or receives that same mask in its own color, while differently sized rectangles are erased from the output.
