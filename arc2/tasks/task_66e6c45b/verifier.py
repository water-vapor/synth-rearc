from arc2.core import *


def verify_66e6c45b(I: Grid) -> Grid:
    x0 = asindices(I)
    x1 = ulcorner(x0)
    x2 = urcorner(x0)
    x3 = llcorner(x0)
    x4 = lrcorner(x0)
    x5 = crop(I, UNITY, TWO_BY_TWO)
    x6 = index(x5, ORIGIN)
    x7 = index(x5, RIGHT)
    x8 = index(x5, DOWN)
    x9 = index(x5, UNITY)
    x10 = canvas(ZERO, shape(I))
    x11 = fill(x10, x6, initset(x1))
    x12 = fill(x11, x7, initset(x2))
    x13 = fill(x12, x8, initset(x3))
    x14 = fill(x13, x9, initset(x4))
    return x14
