from arc2.core import *

from .helpers import project_panel_object_9841fdad


def verify_9841fdad(I: Grid) -> Grid:
    x0 = frontiers(I)
    x1 = sfilter(x0, vline)
    x2 = matcher(leftmost, ZERO)
    x3 = width(I)
    x4 = decrement(x3)
    x5 = matcher(rightmost, x4)
    x6 = fork(either, x2, x5)
    x7 = compose(flip, x6)
    x8 = extract(x1, x7)
    x9 = leftmost(x8)
    x10 = height(I)
    x11 = subtract(x10, TWO)
    x12 = subtract(x9, ONE)
    x13 = subtract(subtract(x3, x9), TWO)
    x14 = astuple(ONE, ONE)
    x15 = astuple(x11, x12)
    x16 = crop(I, x14, x15)
    x17 = objects(x16, T, F, T)
    x18 = lbind(project_panel_object_9841fdad, x12)
    x19 = lbind(x18, x13)
    x20 = mapply(x19, x17)
    x21 = astuple(ONE, increment(x9))
    x22 = shift(x20, x21)
    x23 = paint(I, x22)
    return x23
