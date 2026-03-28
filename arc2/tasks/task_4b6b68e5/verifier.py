from arc2.core import *

from .helpers import enclosed_cells_4b6b68e5


def verify_4b6b68e5(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = shape(I)
    x2 = canvas(x0, x1)
    x3 = objects(I, T, F, T)
    x4 = compose(rbind(greater, ONE), size)
    x5 = sfilter(x3, x4)
    x6 = x2
    for x7 in x5:
        x6 = paint(x6, x7)
        x8 = enclosed_cells_4b6b68e5(x7)
        x9 = tuple(
            index(I, x10)
            for x10 in x8
            if index(I, x10) not in (x0, color(x7))
        )
        if len(x9) == ZERO:
            continue
        x11 = mostcommon(x9)
        x6 = fill(x6, x11, x8)
    return x6
