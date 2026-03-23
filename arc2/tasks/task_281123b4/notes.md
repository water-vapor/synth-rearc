`arc2_opus46_summary.json` was consistent with the official examples and was used as the starting hypothesis: the input is four `4x4` monochrome layers separated by full green columns, and the output is their overlay with precedence `5 -> 8 -> 4 -> 9`.

`arc2_sonnet45_summary.jsonl` was too incomplete to trust on its own. It correctly noticed that the green columns are structural, but it framed the task as generic marker filtering and column extraction rather than the fixed four-panel layer stack that the official examples actually show.
