from arc2.core import *


def verify_1c02dbbe(I: Grid) -> Grid:
    x0 = ofcolor(I, FIVE)
    x1 = backdrop(x0)
    x2 = partition(I)
    x3 = matcher(color, ZERO)
    x4 = compose(flip, x3)
    x5 = sfilter(x2, x4)
    x6 = matcher(color, FIVE)
    x7 = compose(flip, x6)
    x8 = sfilter(x5, x7)
    x9 = lbind(intersection, x1)
    x10 = compose(x9, backdrop)
    x11 = fork(recolor, color, x10)
    x12 = mapply(x11, x8)
    x13 = canvas(ZERO, shape(I))
    x14 = fill(x13, FIVE, x1)
    x15 = paint(x14, x12)
    return x15
