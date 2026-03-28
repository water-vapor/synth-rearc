`arc2_opus46_summary.json` was directionally correct and I used it as the starting hypothesis.

I kept that core idea, but tightened the rule after checking the official examples:

- A naive flood fill over all non-`8` cells is too permissive and leaks around wall endpoints into exterior background.
- The filled area is the network of wall-bounded rooms, narrow connectors, and door openings inside the `8` framework.
- The seed color propagates through those rooms and door gaps, while unrelated exterior `0` background stays unchanged.
