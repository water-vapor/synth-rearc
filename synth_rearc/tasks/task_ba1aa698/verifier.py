from synth_rearc.core import *

from .helpers import (
    blank_panel_ba1aa698,
    motif_object_ba1aa698,
    paint_motif_at_top_ba1aa698,
    predict_next_top_ba1aa698,
    split_panels_ba1aa698,
)


def verify_ba1aa698(
    I: Grid,
) -> Grid:
    x0 = split_panels_ba1aa698(I)
    x1 = tuple(motif_object_ba1aa698(x2) for x2 in x0)
    x2 = first(x1)
    x3 = tuple(uppermost(x4) for x4 in x1)
    x4 = predict_next_top_ba1aa698(x3, x2, I[ZERO][ZERO])
    x5 = blank_panel_ba1aa698(first(x0))
    x6 = paint_motif_at_top_ba1aa698(x5, x2, x4)
    return x6
