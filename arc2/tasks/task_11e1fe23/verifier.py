from arc2.core import *


def verify_11e1fe23(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = mapply(toindices, x0)
    x2 = center(x1)
    x3 = initset(x2)
    x4 = totuple(x0)
    x5 = lbind(position, x3)
    x6 = apply(x5, x4)
    x7 = apply(normalize, x4)
    x8 = lbind(add, x2)
    x9 = apply(x8, x6)
    x10 = papply(shift, x7, x9)
    x11 = merge(x10)
    x12 = paint(I, x11)
    x13 = fill(x12, FIVE, x3)
    return x13
