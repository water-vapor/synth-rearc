from synth_rearc.core import *

from .helpers import (
    best_generic_companion_35ab12c3,
    infer_outlines_35ab12c3,
    paint_cells_35ab12c3,
    points_by_color_35ab12c3,
    special_pentagon_companion_35ab12c3,
    special_rectangle_companion_35ab12c3,
)


def verify_35ab12c3(I: Grid) -> Grid:
    x0 = points_by_color_35ab12c3(I)
    x1 = infer_outlines_35ab12c3(x0)
    x2 = I
    x3 = frozenset()
    for x4, x5 in x1.items():
        x2 = paint_cells_35ab12c3(x2, x4, x5["cells"])
        x3 = x3 | x5["cells"]
    for x6, x7 in x0.items():
        if x6 in x1:
            continue
        x8 = special_rectangle_companion_35ab12c3(x7, x1, x3)
        if x8 is None:
            x8 = special_pentagon_companion_35ab12c3(x7, x1, x3)
        if x8 is None:
            x8 = best_generic_companion_35ab12c3(x7, x1, x3)
        if x8 is None:
            continue
        x2 = paint_cells_35ab12c3(x2, x6, x8)
        x3 = x3 | x8
    return x2
