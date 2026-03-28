from arc2.core import *


def verify_4a1cacc2(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = palette(I)
    x2 = other(x1, x0)
    x3 = ofcolor(I, x2)
    x4 = first(x3)
    x5 = initset(x4)
    x6 = asindices(I)
    x7 = corners(x6)
    x8 = compose(rbind(manhattan, x5), initset)
    x9 = argmin(x7, x8)
    x10 = insert(x9, x5)
    x11 = backdrop(x10)
    x12 = fill(I, x2, x11)
    return x12
