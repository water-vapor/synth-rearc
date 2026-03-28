from arc2.core import *


def verify_34b99a2b(I: Grid) -> Grid:
    x0 = ofcolor(I, FOUR)
    x1 = leftmost(x0)
    x2 = height(I)
    x3 = astuple(x2, x1)
    x4 = crop(I, ORIGIN, x3)
    x5 = astuple(ZERO, increment(x1))
    x6 = astuple(x2, subtract(width(I), increment(x1)))
    x7 = crop(I, x5, x6)
    x8 = difference(asindices(x4), ofcolor(x4, ZERO))
    x9 = difference(asindices(x7), ofcolor(x7, ZERO))
    x10 = difference(x8, x9)
    x11 = difference(x9, x8)
    x12 = combine(x10, x11)
    x13 = canvas(ZERO, shape(x4))
    x14 = fill(x13, TWO, x12)
    return x14
