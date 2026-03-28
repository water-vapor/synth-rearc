`arc2_opus46_summary.json` was directionally correct: the task is about corner-marker quartets framing a payload, and the output is the payload whose color matches the framing corners.

`arc2_sonnet45_summary.jsonl` was rejected. The official examples do not show a "unique pattern among duplicates" rule; instead they show several framed payloads, with exactly one frame whose marker color also appears in the enclosed payload. The solver therefore looks for local TL/TR/BL/BR marker quartets and extracts the smallest enclosed same-color payload.
