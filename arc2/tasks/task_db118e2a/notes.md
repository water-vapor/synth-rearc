`arc2_opus46_summary.json` was consistent with the official examples and was used as a starting hypothesis.

`arc2_sonnet45_summary.jsonl` was rejected. It claims the output contains a `5x9` pattern built by selecting only rows with non-`7` pixels, but the official outputs contain two identical `5x5` tiles. Each tile is formed from a centered `3x3` crop of the trimmed interior, wrapped with the input frame color on the non-corner border cells, then stamped onto a `15x15` background of `7`s.
