from arc2.core import *


def verify_c074846d(I: Grid) -> Grid:
    x0 = ofcolor(I, FIVE)
    x1 = ofcolor(I, TWO)
    x2 = position(x0, x1)
    x3 = last(x2)
    x4 = first(x2)
    x5 = invert(x4)
    x6 = astuple(x3, x5)
    x7 = size(x1)
    x8 = interval(ONE, increment(x7), ONE)
    x9 = lbind(multiply, x6)
    x10 = apply(x9, x8)
    x11 = lbind(shift, x0)
    x12 = mapply(x11, x10)
    x13 = replace(I, TWO, THREE)
    x14 = fill(x13, TWO, x12)
    return x14
