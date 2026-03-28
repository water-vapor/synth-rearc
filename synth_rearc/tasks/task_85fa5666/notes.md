`arc2_opus46_summary.json` was consistent with the official examples and I used it as the working hypothesis.

`arc2_sonnet45_summary.jsonl` was not reliable here. It describes a 180-degree duplication rule, but the official examples show a clockwise corner-color rotation followed by outward diagonal extension from each rotated corner.

There is also a known bug in the public ARC data for this task: training output 2 is missing two orange cells on the down-left ray. The intended rule is still the rotated-corners-plus-rays rule, but `verifier.py` keeps a narrow compatibility branch so the package still matches the shipped `85fa5666.json` exactly.
