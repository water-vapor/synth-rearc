from arc2.core import *


def verify_9f5f939b(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, ONE)
    x2 = sizefilter(x1, TWO)
    x3 = sfilter(x2, hline)
    x4 = sfilter(x2, vline)
    x5 = apply(lrcorner, x3)
    x6 = apply(rbind(add, (ZERO, TWO)), x5)
    x7 = apply(ulcorner, x3)
    x8 = apply(rbind(add, (ZERO, -TWO)), x7)
    x9 = intersection(x6, x8)
    x10 = apply(llcorner, x4)
    x11 = apply(rbind(add, (TWO, ZERO)), x10)
    x12 = apply(ulcorner, x4)
    x13 = apply(rbind(add, (-TWO, ZERO)), x12)
    x14 = intersection(x11, x13)
    x15 = intersection(x9, x14)
    x16 = intersection(x15, ofcolor(I, EIGHT))
    x17 = fill(I, FOUR, x16)
    return x17
