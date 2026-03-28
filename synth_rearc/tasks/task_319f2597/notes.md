`arc2_opus46_summary.json` matched the official examples and was used as the starting hypothesis.

The `arc2_sonnet45_summary.jsonl` entry was incomplete: it correctly identified the marker `2x2` zero block and the two affected rows and columns, but it described the red `2` preservation only for the marker rows. In the official examples, red `2`s are protected everywhere on the resulting two-row/two-column cross, including cells outside the original marker rows.
