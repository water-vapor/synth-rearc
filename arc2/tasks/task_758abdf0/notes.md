`arc2_opus46_summary.json` matches the official task closely enough to use as a starting hint.

`arc2_sonnet45_summary.jsonl` overfits the unseen test case and invents an "approximate reflection" / special-case shift. The real rule is lane-local and exact: each lane is read perpendicular to the all-zero border, a single `8` adjacent to that border becomes a 2-cell `8` bar extending inward, and an existing 2-cell `8` bar disappears and becomes a 2-cell `0` bar on the opposite edge in the same lane.
