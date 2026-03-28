`arc2_opus46_summary.json` was usable as a starting hint: the left guide columns define the recoloring order, and the guide is erased in the output.

`arc2_sonnet45_summary.jsonl` was misleading and was discarded. The task is not a row-wise lane propagation rule. The right side is a left-to-right sequence of solid 8-rectangles, and touching rectangles can merge into a single connected 8-component. The correct decomposition is by consecutive columns with the same occupied-row profile, then recolor those rectangles in guide order.
