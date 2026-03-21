The `arc2_opus46_summary.json` hint was discarded.

Its incorrect detail is the overwrite condition: marked columns do not preserve unrelated colored blocks. For every non-background marker in the top row, rows below that marker are rewritten across the entire column, and only cells already equal to the marker color flip back to background. All other colors in that column are overwritten by the marker color.
