# 470c91de Notes

- `arc2_opus46_summary.json` was consistent with the official examples and was used as the starting hypothesis.
- `arc2_sonnet45_summary.jsonl` was discarded. It notices the `8` markers, but its claim that the rectangles are globally reorganized for better separation is incorrect.
- The actual rule is local: each non-background colored object is a filled rectangle with one corner replaced by `8`, and the completed rectangle shifts one cell diagonally outward in the direction of that marked corner.
- A useful verifier detail is that multicolor connected components are misleading here, because an `8` can also touch a different rectangle. The stable unit is each non-`8` univalued component whose `delta` is exactly the marked corner cell.
