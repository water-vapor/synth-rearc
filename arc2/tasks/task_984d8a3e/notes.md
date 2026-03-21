`arc2_opus46_summary.json` was correct enough to use, but the `arc2_sonnet45_summary.jsonl` hint was wrong and I discarded it.

The Sonnet hint claims the task is a selective diagonal reflection between two colors. The official examples do not support that at all: every row stays horizontally segmented into the same three color counts, and only the middle band is shifted left.

The actual rule is row-wise boundary alignment. Keep the rightmost color block fixed, preserve each row's three color counts, and move as much of the left block as possible to the far side of the middle block so the middle color's right boundary is as far left, and as aligned across rows, as the data allows.
