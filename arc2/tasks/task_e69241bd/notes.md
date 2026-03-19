`arc2_opus46_summary.json` matched the official examples closely enough to use as the working hypothesis.

`arc2_sonnet45_summary.jsonl` was not reliable for this task. Its diagonal wedge / opposite-corner spreading story does not fit the official examples. The actual rule is orthogonal region filling: every 0-component bordered by exactly one non-`0`, non-`5` seed color gets recolored to that seed color, while `5` cells remain walls and untouched components stay `0`.
