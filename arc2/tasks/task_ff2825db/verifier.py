from arc2.core import *


def verify_ff2825db(I: Grid) -> Grid:
    x0 = width(I)
    x1 = astuple(ONE, x0)
    x2 = crop(I, ORIGIN, x1)
    x3 = decrement(height(I))
    x4 = astuple(x3, x0)
    x5 = crop(I, DOWN, x4)
    x6 = index(x5, ORIGIN)
    x7 = palette(x5)
    x8 = remove(ZERO, x7)
    x9 = remove(x6, x8)
    x10 = lbind(colorcount, x5)
    x11 = argmax(x9, x10)
    x12 = ofcolor(x5, x11)
    x13 = box(x12)
    x14 = asindices(x5)
    x15 = box(x14)
    x16 = combine(x13, x15)
    x17 = canvas(ZERO, x4)
    x18 = fill(x17, x11, x16)
    x19 = vconcat(x2, x18)
    return x19
