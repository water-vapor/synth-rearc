from arc2.core import *


def verify_e619ca6e(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = canvas(ZERO, shape(I))
    x2 = interval(ONE, increment(height(I)), ONE)
    x3 = x1
    for x4 in x0:
        x3 = paint(x3, x4)
        x5 = height(x4)
        x6 = width(x4)
        x7 = astuple(x5, invert(x6))
        x8 = astuple(x5, x6)
        for x9 in x2:
            x10 = multiply(x7, x9)
            x11 = multiply(x8, x9)
            x12 = shift(x4, x10)
            x13 = shift(x4, x11)
            x3 = paint(x3, x12)
            x3 = paint(x3, x13)
    return x3
