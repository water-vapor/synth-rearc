from arc2.core import *


def verify_6ea4a07e(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = other(x0, ZERO)
    x2 = equality(x1, THREE)
    x3 = branch(x2, ONE, FOUR)
    x4 = equality(x1, EIGHT)
    x5 = branch(x4, TWO, x3)
    x6 = replace(I, ZERO, x5)
    x7 = replace(x6, x1, ZERO)
    return x7
