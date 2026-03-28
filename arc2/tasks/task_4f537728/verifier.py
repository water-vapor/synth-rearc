from arc2.core import *


def verify_4f537728(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = remove(ZERO, x0)
    x2 = other(x1, ONE)
    x3 = objects(I, T, F, T)
    x4 = colorfilter(x3, x2)
    x5 = first(x4)
    x6 = toindices(x5)
    x7 = mapply(hfrontier, x6)
    x8 = mapply(vfrontier, x6)
    x9 = combine(x7, x8)
    x10 = ofcolor(I, ONE)
    x11 = intersection(x9, x10)
    x12 = fill(I, x2, x11)
    return x12
