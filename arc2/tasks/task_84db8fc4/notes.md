`arc2_opus46_summary.json` matched the official examples, so I used it as the starting hypothesis.

`arc2_sonnet45_summary.jsonl` was rejected. Its size-threshold rule does not survive the official examples: enclosed zero-components of sizes `1` and `2` become `5`, while border-touching zero-components of sizes `4`, `5`, `7`, and `12` still become `2`. The stable rule is simply:

- extract the `0` connected-components with 4-connectivity
- recolor every component touching the outer border to `2`
- recolor every fully enclosed component to `5`
- leave all `1` and `3` cells unchanged
