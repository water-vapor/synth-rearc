The summary hint was discarded.

The hint claimed the horizontal arm orientation depends on the marker column parity. The 5x5 official example disproves that: its marker is in column 2 (zero-based), but the output uses the top-right/bottom-left orientation instead of the top-left/bottom-right orientation predicted by parity.

The rule that matches all official examples is:
- draw a full blue vertical line through the unique non-background marker
- if the marker is in the exact center column, draw the top arm to the right edge and the bottom arm to the left edge
- otherwise, draw the top arm to the left edge and the bottom arm to the right edge
