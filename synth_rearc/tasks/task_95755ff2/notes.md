`arc2_opus46_summary.json` matched the official examples closely and was used as the starting hypothesis.

`arc2_sonnet45_summary.jsonl` was discarded. It describes the pattern as diagonal projection from corner sequences, but the official pairs show a simpler orthogonal rule:

- top-border colors fill straight downward within their columns
- bottom-border colors fill straight upward within their columns
- left-border colors fill straight rightward within their rows
- right-border colors fill straight leftward within their rows

Each fill starts just inside the 2-diamond, writes only through zeros, and stops at the first existing nonzero blocker.
