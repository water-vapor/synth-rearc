`arc2_opus46_summary.json` was correct enough to use, but the `arc2_sonnet45_summary.jsonl` hint was wrong and I discarded it.

The Sonnet hint claims the task fills the whole bounding box between the two `2` markers. Train examples 2 and 5 falsify that immediately: both keep some `0` cells inside that bounding box unchanged.

The real rule is shortest-path based. Treat `1` as blocked, keep the two `2` endpoints fixed, and recolor exactly those `0` cells that lie on at least one shortest 4-connected path between the endpoints.
