from arc2.core import *


def verify_981add89(I: Grid) -> Grid:
    x0 = width(I)
    x1 = astuple(ONE, x0)
    x2 = crop(I, ORIGIN, x1)
    x3 = decrement(height(I))
    x4 = astuple(x3, x0)
    x5 = crop(I, DOWN, x4)
    x6 = mostcolor(I)
    x7 = asindices(x2)
    x8 = ofcolor(x2, x6)
    x9 = difference(x7, x8)
    x10 = x5
    for x11 in x9:
        x12 = index(x2, x11)
        x13 = last(x11)
        x14 = initset(x13)
        x15 = interval(ZERO, x3, ONE)
        x16 = product(x15, x14)
        x17 = ofcolor(x10, x12)
        x18 = intersection(x16, x17)
        x19 = fill(x10, x12, x16)
        x10 = fill(x19, x6, x18)
    x20 = vconcat(x2, x10)
    return x20
