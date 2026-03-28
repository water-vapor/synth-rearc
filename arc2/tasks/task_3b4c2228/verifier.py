from arc2.core import *


def verify_3b4c2228(I: Grid) -> Grid:
    x0 = canvas(THREE, (TWO, TWO))
    x1 = asobject(x0)
    x2 = occurrences(I, x1)
    x3 = size(x2)
    x4 = interval(ZERO, x3, ONE)
    x5 = pair(x4, x4)
    x6 = canvas(ZERO, (THREE, THREE))
    x7 = fill(x6, ONE, x5)
    return x7
