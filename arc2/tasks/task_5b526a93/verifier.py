from arc2.core import *


def verify_5b526a93(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = apply(ulcorner, x0)
    x2 = apply(first, x1)
    x3 = apply(last, x1)
    x4 = product(x2, x3)
    x5 = difference(x4, x1)
    x6 = first(x0)
    x7 = normalize(x6)
    x8 = recolor(EIGHT, x7)
    x9 = lbind(shift, x8)
    x10 = mapply(x9, x5)
    x11 = paint(I, x10)
    return x11
