`arc2_opus46_summary.json` was used as the working hint. Its checkerboard-phase description matches all official examples.

`arc2_sonnet45_summary.jsonl` was rejected. It reduces the rule to "fill alternating rows in the main zero rectangle", but the official outputs also recolor matching-parity black cells outside that rectangle, and within affected rows only one column parity is filled. The corrected rule is: find the lone non-`0/5` seed cell and recolor every black cell whose row parity and column parity both match the seed.
