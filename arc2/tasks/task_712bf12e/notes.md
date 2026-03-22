`arc2_sonnet45_summary.jsonl` had no entry for `712bf12e`.

`arc2_opus46_summary.json` was close but incomplete, so I treated it as a rejected/corrected hint rather than a source of truth. The missing details are:

- a path stops immediately when it reaches row `0`; it does not keep sliding right across the top row
- when the cell above is blocked, the path can shift right repeatedly on the same row as long as each next right cell is empty
- every move, both upward and rightward, is only into `0` cells

The implemented rule is the greedy trace seen in the official examples: from each bottom-row red seed, move up if possible, else move right if possible, else stop.
