`arc2_sonnet45_summary.jsonl` had no entry for `a416fc5b`.

`arc2_opus46_summary.json` was directionally useful but inaccurate enough to require correction. It says a single `2` plus marks one board cell, but every official example has a fixed central `2` plus and one additional ring `2` plus. The corrected rule is:

- The input is a fixed `11x11` board with `6` separator lines and hollow `3x3` plus motifs.
- The central board cell always contains a `2` plus.
- A second `2` plus appears on one of the eight surrounding ring positions.
- In the normal case, the output adds an `8` plus three ring steps counterclockwise from that second `2` plus and a `5` plus three ring steps clockwise from it.
- If both `5` and `8` are already present in the input, the output is a solid `7` square whose side length equals the number of non-`6`, non-`7` cells in the input.

For ARC2 generation, the exact official family only gives `16` unique inputs (`8` ring positions times normal/special). The generator is now constrained to that exact support: every generated input is the fixed `11x11` board from the official task, and the shared builder caps this task at `16` examples instead of inventing larger off-distribution boards.
