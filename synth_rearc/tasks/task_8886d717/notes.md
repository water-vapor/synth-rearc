`arc2_sonnet45_summary.jsonl` was discarded. It describes marker migration to region boundaries, but the official examples only apply a local rule: 8s touching a 2 orthogonally are absorbed into the 2-region, while the rest stay 8.

`arc2_opus46_summary.json` was partially useful but still corrected here. It gets the erase criterion right, but it says the surviving 8s grow away from the 9 frontier; the official examples show the opposite. Surviving 8s duplicate one step toward the full 9 border line.
