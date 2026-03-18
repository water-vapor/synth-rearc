from arc2.core import *


def verify_12eac192(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = sizefilter(x0, ONE)
    x2 = sizefilter(x0, TWO)
    x3 = combine(x1, x2)
    x4 = lbind(recolor, THREE)
    x5 = mapply(x4, x3)
    x6 = paint(I, x5)
    return x6
