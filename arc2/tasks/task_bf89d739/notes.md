`arc2_opus46_summary.json` matched the official examples and was used as the working hint.

`arc2_sonnet45_summary.jsonl` was discarded. It describes a more generic minimal
Manhattan connection network, but the official task is more specific:

- Pick the farthest pair of red cells that already share a row or a column.
- Use that pair as the main straight spine, leaving the red endpoints unchanged.
- Connect every other red cell to that spine with exactly one perpendicular green
  segment.
