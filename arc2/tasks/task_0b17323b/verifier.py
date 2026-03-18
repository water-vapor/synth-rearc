from arc2.core import *


def verify_0b17323b(I: Grid) -> Grid:
    x0 = ofcolor(I, ONE)
    x1 = ulcorner(x0)
    x2 = lrcorner(x0)
    x3 = size(x0)
    x4 = decrement(x3)
    x5 = subtract(x2, x1)
    x6 = divide(x5, x4)
    x7 = shape(I)
    x8 = decrement(x7)
    x9 = subtract(x8, x2)
    x10 = divide(x9, x6)
    x11 = minimum(x10)
    x12 = interval(ONE, increment(x11), ONE)
    x13 = lbind(multiply, x6)
    x14 = apply(x13, x12)
    x15 = lbind(add, x2)
    x16 = apply(x15, x14)
    x17 = fill(I, TWO, x16)
    return x17
