from arc2.core import *


def verify_a406ac07(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = last(I)
    x3 = decrement(x1)
    x4 = interval(ZERO, x1, ONE)
    x5 = I
    for x6 in interval(ZERO, decrement(x0), ONE):
        x7 = I[x6][x3]
        x8 = frozenset((x6, x9) for x9 in x4 if x2[x9] == x7)
        x5 = fill(x5, x7, x8)
    return x5
