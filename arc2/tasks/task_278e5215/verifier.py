from arc2.core import *


def verify_278e5215(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = matcher(numcolors, ONE)
    x2 = extract(x0, x1)
    x3 = other(x0, x2)
    x4 = subgrid(x2, I)
    x5 = subgrid(x3, I)
    x6 = tophalf(x5)
    x7 = height(x4)
    x8 = vupscale(x6, x7)
    x9 = bottomhalf(x5)
    x10 = mostcolor(x9)
    x11 = ofcolor(x4, ZERO)
    x12 = fill(x8, x10, x11)
    return x12
