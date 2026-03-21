`arc2_opus46_summary.json` was directionally correct, but the `arc2_sonnet45_summary.jsonl` hint was too loose and partially misleading.

The real invariant is not “convert solid boundary rows/columns marked by 9s.” The output recolors the unique shortest path through the 8-maze that connects the terminal-adjacent 8 entry cells after removing every 8 that is orthogonally adjacent to a 7. In the official examples, those removed cells make the intended outer route unique.
