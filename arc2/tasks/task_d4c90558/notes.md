# d4c90558 notes

- The two summary hints conflicted. The `arc2_opus46_summary.json` entry had the core rule right, but the `arc2_sonnet45_summary.jsonl` entry incorrectly described a proportional width-scaling rule and top-to-bottom ordering.
- The official examples show exact gray-cell counting instead: for each colored rectangular ring, count the gray `5` cells inside that ring's bounding box, emit one output row in the ring color with exactly that many filled cells, pad with black, and sort rows by ascending count.
- The generator therefore constructs off-center rectangular rings with sparse gray singleton noise inside their holes, then derives the output directly from those per-ring gray counts.
