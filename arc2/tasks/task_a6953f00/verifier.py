from arc2.core import *


def verify_a6953f00(I: Grid) -> Grid:
    x0 = width(I)
    x1 = subtract(x0, TWO)
    x2 = even(x0)
    x3 = branch(x2, astuple(ZERO, x1), ORIGIN)
    x4 = crop(I, x3, TWO_BY_TWO)
    return x4
