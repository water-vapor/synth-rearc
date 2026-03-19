`arc2_opus46_summary.json` was directionally correct and I used it as the starting hypothesis.

`arc2_sonnet45_summary.jsonl` was not reliable for this task. It described row-wise sequence collapsing, but the official examples are governed by object geometry:

- Each green object is an orthogonal one-bend path.
- One endpoint is marked by a perpendicular `0-3-0` pattern.
- If that same green object also touches a `5`, the object collapses to the marked endpoint plus a new inward `5`.
- Unmarked green objects stay intact, and unrelated `5`s stay intact.
