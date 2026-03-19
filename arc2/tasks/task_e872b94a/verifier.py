from arc2.core import *


def verify_e872b94a(I: Grid) -> Grid:
    x0 = objects(I, T, T, F)
    x1 = colorfilter(x0, FIVE)
    x2 = size(x1)
    x3 = increment(x2)
    x4 = astuple(x3, ONE)
    x5 = canvas(ZERO, x4)
    return x5
