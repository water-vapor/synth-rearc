from arc2.core import *


def verify_9ddd00f0(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = other(x0, ZERO)
    x2 = height(I)
    x3 = ZERO
    for x4 in range(TWO, SIX):
        if x4 * x4 + x4 - ONE == x2:
            x3 = x4
            break
    if x3 == ZERO:
        return I
    x4 = canvas(ZERO, shape(I))
    x5 = increment(x3)
    for x6 in range(x3):
        x7 = multiply(x6, x5)
        x8 = interval(x7, add(x7, x3), ONE)
        for x9 in range(x3):
            x10 = multiply(x9, x5)
            x11 = interval(x10, add(x10, x3), ONE)
            x12 = product(x8, x11)
            x4 = fill(x4, x1, x12)
            x13 = initset(astuple(add(x7, x6), add(x10, x9)))
            x4 = fill(x4, ZERO, x13)
    return x4
