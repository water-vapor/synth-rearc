from arc2.core import *


def verify_be03b35f(I: Grid) -> Grid:
    x0 = crop(I, astuple(THREE, ZERO), TWO_BY_TWO)
    x1 = rot90(x0)
    return x1
