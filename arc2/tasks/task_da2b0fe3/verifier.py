from arc2.core import *


def verify_da2b0fe3(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = first(x0)
    x2 = other(x0, x1)
    x3 = hmatching(x1, x2)
    x4 = argmin(x0, leftmost)
    x5 = increment(rightmost(x4))
    x6 = height(I)
    x7 = decrement(x6)
    x8 = connect((ZERO, x5), (x7, x5))
    x9 = argmin(x0, uppermost)
    x10 = increment(lowermost(x9))
    x11 = width(I)
    x12 = decrement(x11)
    x13 = connect((x10, ZERO), (x10, x12))
    x14 = branch(x3, x8, x13)
    x15 = fill(I, THREE, x14)
    return x15
