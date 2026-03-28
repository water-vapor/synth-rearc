Used `arc2_opus46_summary.json` as the working hypothesis and rejected the `arc2_sonnet45_summary.jsonl` explanation after checking the official examples.

- The `sonnet45` hint incorrectly claims that marker rows trigger full-width horizontal fills and that non-rectangle rows get an alternating stripe pattern inside the square.
- The official examples show a stricter blocker rule instead: each row of the 2-square extends left and/or right only when that whole side segment is empty, and each column extends up and/or down only when that whole side segment is empty.
- The non-2 singleton pixels are blockers that stay unchanged; they do not encode a separate stripe pattern.
