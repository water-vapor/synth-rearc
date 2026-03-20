from arc2.core import *


def verify_1c0d0a4b(I: Grid) -> Grid:
    x0 = frontiers(I)
    x1 = colorfilter(x0, ZERO)
    x2 = merge(x1)
    x3 = toindices(x2)
    x4 = asindices(I)
    x5 = difference(x4, x3)
    x6 = fill(I, TWO, x5)
    x7 = ofcolor(I, EIGHT)
    x8 = fill(x6, ZERO, x7)
    return x8
