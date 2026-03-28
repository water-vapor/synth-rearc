`arc2_opus46_summary.json` was directionally correct and useful as a starting hypothesis.

`arc2_sonnet45_summary.jsonl` was misleading in one important way: the task is not naturally "extract a 3x3 core and mirror it into a 6x6 block." The official examples are explained more directly by a fixed 6x6 hollow-diamond template for each signal color. Each visible signal fragment is a clipped and/or occluded subset of that template, and the output restores the full 6x6 diamonds and stacks them in signal-on-signal occlusion order.
