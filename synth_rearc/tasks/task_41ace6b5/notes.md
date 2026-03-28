`arc2_opus46_summary.json` matched the examples closely and was used as the main hint.

The `arc2_sonnet45_summary.jsonl` entry was discarded as a literal rule description. Its "upward spreading wave" framing is only a loose narrative; the exact transformation is column-local on the even columns:

- each even column in the input is a bottom-aligned suffix of `8`s followed by `1`s
- the output keeps each column's `1` count
- the output uses the global maximum `8` count to fill the upper even-column band up to the `2` row
- all remaining lower even-column cells become `9`
