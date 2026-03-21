from arc2.core import *


def verify_ca8de6ea(I: Grid) -> Grid:
    x0 = index(I, ORIGIN)
    x1 = index(I, UNITY)
    x2 = astuple(ZERO, FOUR)
    x3 = index(I, x2)
    x4 = astuple(ONE, THREE)
    x5 = index(I, x4)
    x6 = TWO_BY_TWO
    x7 = index(I, x6)
    x8 = astuple(THREE, ONE)
    x9 = index(I, x8)
    x10 = astuple(FOUR, ZERO)
    x11 = index(I, x10)
    x12 = astuple(THREE, THREE)
    x13 = index(I, x12)
    x14 = astuple(FOUR, FOUR)
    x15 = index(I, x14)
    x16 = (
        (x0, x1, x3),
        (x5, x7, x9),
        (x11, x13, x15),
    )
    return x16
