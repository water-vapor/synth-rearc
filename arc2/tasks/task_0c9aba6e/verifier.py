from arc2.core import *


def verify_0c9aba6e(I: Grid) -> Grid:
    x0 = tophalf(I)
    x1 = bottomhalf(I)
    x2 = cellwise(x0, x1, ONE)
    x3 = replace(x2, ZERO, EIGHT)
    x4 = replace(x3, ONE, ZERO)
    return x4
