from arc2.core import *


def verify_fc754716(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = first(x0)
    x2 = color(x1)
    x3 = shape(I)
    x4 = canvas(ZERO, x3)
    x5 = asindices(x4)
    x6 = box(x5)
    x7 = fill(x4, x2, x6)
    return x7
