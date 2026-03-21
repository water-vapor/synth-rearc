`arc2_opus46_summary.json` matched the official examples closely, so I used it as the starting hypothesis.

`arc2_sonnet45_summary.jsonl` was misleading here. The task is not a checkerboard-dependent color swap. The stable rule in the official examples is:

- identify the background color and the three non-background colors
- order the three non-background colors by the left-to-right span of their occupied columns
- extend each color's occupied column span vertically across the full grid height
- recolor only the original background cells inside each span to the next span's color cyclically
- leave all originally non-background cells unchanged
