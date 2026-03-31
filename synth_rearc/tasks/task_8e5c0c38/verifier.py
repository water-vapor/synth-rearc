from synth_rearc.core import *

from .helpers import best_vertical_subset_8e5c0c38


def verify_8e5c0c38(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = fgpartition(I)
    x2 = canvas(x0, shape(I))
    for x3 in x1:
        x4 = color(x3)
        x5, _ = best_vertical_subset_8e5c0c38(x3)
        x6 = recolor(x4, x5)
        x2 = paint(x2, x6)
    return x2
