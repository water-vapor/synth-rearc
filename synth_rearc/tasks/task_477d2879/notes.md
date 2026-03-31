Rule sketch:
- White `1` cells form the thin line-objects.
- Non-`0/1` markers either replace a white line cell or sit in a zero-region.
- Markers with at least two orthogonal white neighbors belong to a white object.
- All other markers belong to a zero-region.
- The output fills every white object / zero-region with the color of the marker placed in it.

Generator sketch:
- Build 1-3 white objects as unions of overlapping rectangle perimeters on a fixed `13x13` canvas.
- Compute the induced zero-regions.
- Assign one unique color to each white object and zero-region, with an occasional duplicate marker in a larger zero-region.
