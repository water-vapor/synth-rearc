`arc2_sonnet45_summary.jsonl` and `arc2_opus46_summary.json` both reverse the keep/discard rule.

Official examples show that the output keeps the half containing the two `5` markers, then turns those `5` cells back into background `8`.

The reliable rule is:
- if the `5`s share a column, keep the top or bottom half containing them
- if the `5`s share a row, keep the left or right half containing them
- replace `5` with `8` in the retained half
