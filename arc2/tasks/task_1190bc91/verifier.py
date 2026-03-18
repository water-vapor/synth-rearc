from arc2.core import *

from .helpers import (
    bar_mask_1190bc91,
    bar_mask_name_1190bc91,
    ordered_main_line_1190bc91,
    paint_main_line_1190bc91,
)


def verify_1190bc91(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = argmax(x0, size)
    x2 = ordered_main_line_1190bc91(x1)
    x3 = shape(I)
    x4 = paint_main_line_1190bc91(x3, x2)
    x5 = remove(x1, x0)
    x6 = matcher(size, TWO)
    x7 = sfilter(x5, x6)
    x8 = x4
    for x9 in x7:
        x10 = color(x9)
        x11 = bar_mask_name_1190bc91(x9, x2)
        x12 = bar_mask_1190bc91(x3, x2, x11)
        x8 = fill(x8, x10, x12)
    return x8
