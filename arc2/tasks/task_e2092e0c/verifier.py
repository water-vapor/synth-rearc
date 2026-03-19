from arc2.core import *


def verify_e2092e0c(I: Grid) -> Grid:
    x0 = crop(I, ORIGIN, THREE_BY_THREE)
    x1 = asobject(x0)
    x2 = occurrences(I, x1)
    x3 = other(x2, ORIGIN)
    x4 = shift(x1, x3)
    x5 = outbox(x4)
    x6 = fill(I, FIVE, x5)
    return x6
