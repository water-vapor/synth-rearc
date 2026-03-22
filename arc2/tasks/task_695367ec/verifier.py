from arc2.core import *


def verify_695367ec(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = increment(x0)
    x3 = increment(x1)
    x4 = mostcolor(I)
    x5 = canvas(ZERO, (15, 15))
    x6 = interval(x0, 15, x2)
    x7 = interval(x1, 15, x3)
    x8 = interval(ZERO, 15, ONE)
    x9 = product(x6, x8)
    x10 = product(x8, x7)
    x11 = combine(x9, x10)
    x12 = fill(x5, x4, x11)
    return x12
