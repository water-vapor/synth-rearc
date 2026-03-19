from arc2.core import *


def verify_e133d23d(I: Grid) -> Grid:
    x0 = astuple(THREE, THREE)
    x1 = crop(I, ORIGIN, x0)
    x2 = crop(I, astuple(ZERO, FOUR), x0)
    x3 = replace(x1, SIX, TWO)
    x4 = replace(x2, EIGHT, TWO)
    x5 = cellwise(x3, x4, TWO)
    return x5
