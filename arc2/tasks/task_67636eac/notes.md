`arc2_opus46_summary.json` was used as the starting hint.

`arc2_sonnet45_summary.jsonl` was corrected because it collapses the task to a single plus-shape extraction rule. The official examples contain two distinct 3x3 motif families: a solid plus and a hollow diamond, and the output preserves whichever motif appears in the input by cropping each disconnected colored object to its own bounding box and concatenating those crops along the dominant input layout axis.
