Used `arc2_opus46_summary.json` only as a loose starting hint and corrected it after checking the official examples.

- The hint is broadly right that the blue `8` columns continue downward and detour around one-row red `2` blockers.
- The incorrect part is the tie case: the training examples do not split a single centered stream to both sides of a blocker. When a stream is equally far from both exits of an odd-length blocker, the output takes the right-hand exit.

Confirmed rule:

- Read the top-row blue cells as the active stream columns.
- Extend each stream downward to the bottom of the grid.
- If a stream hits a horizontal red blocker, route it across the row just above the blocker to the nearest open column immediately outside that blocker, then continue downward from there.
- The red cells remain unchanged.
