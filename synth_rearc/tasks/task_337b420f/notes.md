Summary hints rejected.

- The `arc2_opus46_summary.json` entry correctly recognized the three `5 x 5` panels separated by `0` columns, but it overstates the translation step: most official examples need no movement at all, and only overlap cases require a one-cell adjustment.
- The `arc2_sonnet45_summary.jsonl` entry also identified the panel structure, but its claim that the third panel is horizontally mirrored is incorrect.
- In the official task, each panel contains multiple same-color `4`-connected components on an `8` background. The output keeps the largest component from each panel, then overlays those three retained components into a single `5 x 5` grid, shifting a retained component by one cell only when its original position would overlap a larger already-placed component.
