from arc2.core import *


def verify_87ab05b8(I: Grid) -> Grid:
    x0 = ulcorner(ofcolor(I, TWO))
    x1 = multiply(divide(x0, TWO), TWO)
    x2 = interval(x1[ZERO], x1[ZERO] + TWO, ONE)
    x3 = interval(x1[ONE], x1[ONE] + TWO, ONE)
    x4 = product(x2, x3)
    x5 = canvas(SIX, shape(I))
    x6 = fill(x5, TWO, x4)
    return x6
