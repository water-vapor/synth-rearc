`arc2_sonnet45_summary.jsonl` was discarded for this task. Its coordinate readout already disagrees with the official examples, and it hard-codes the wrong orientation-to-color mapping.

`arc2_opus46_summary.json` was useful only as a partial starting hint. It correctly identifies that the gray `5` cells separate into the two 45-degree diagonal families, but it omits the rule that decides which family becomes `2` and which becomes `8`.

Confirmed rule:

- Collect the `5` cells that belong to `\\`-oriented chains and the `5` cells that belong to `/`-oriented chains.
- Ignore any ambiguous intersection cells if they ever occur.
- Recolor the smaller family to red `2`.
- Recolor the larger family to azure `8`.
- Leave the `7` background unchanged.
