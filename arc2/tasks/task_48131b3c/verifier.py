from arc2.core import *


def verify_48131b3c(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = other(x0, ZERO)
    x2 = switch(I, ZERO, x1)
    x3 = hconcat(x2, x2)
    x4 = vconcat(x3, x3)
    return x4
