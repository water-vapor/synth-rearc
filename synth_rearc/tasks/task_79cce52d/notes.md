`arc2_opus46_summary.json` was accepted. It correctly identifies the task as a toroidal shift of the 6x6 interior, with the top-frame `2` giving the horizontal shift and the left-frame `2` giving the vertical shift.

`arc2_sonnet45_summary.jsonl` was rejected. It claims the interior is anti-diagonally transposed after border removal, but training example 2 disproves that immediately: the output is a wraparound row/column shift of the interior, not a rotation or transpose.
