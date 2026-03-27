from arc2.core import *


def verify_32e9702f(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = other(x0, ZERO)
    x2 = ofcolor(I, x1)
    x3 = shift(x2, LEFT)
    x4 = canvas(FIVE, shape(I))
    x5 = fill(x4, x1, x3)
    return x5
