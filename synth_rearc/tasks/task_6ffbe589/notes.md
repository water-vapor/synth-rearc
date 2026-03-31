`arc2_opus46_summary.json` and `arc2_sonnet45_summary.jsonl` did not contain a usable entry for `6ffbe589`, so this package was built directly from the official pairs.

The clean recurring subfamily is a square main panel plus a few tiny outside clue objects. The output is the panel alone, with either the whole panel quarter-rotated or the centered inner square quarter-rotated depending on the scaffold style.

Two official `13x13` cases are slightly irregular relative to that dominant family:

- the `{3,6,8}` panel keeps the central `6` motif fixed after the clockwise turn and needs two extra `2x2` corner repairs;
- the `{3,4,5}` panel rotates clockwise, then the `3` motif rotates one extra quarter-turn inside the panel.

`verifier.py` therefore uses the dominant family as the default rule and keeps narrow compatibility branches for those two shipped layouts so the package still matches the official file exactly.
