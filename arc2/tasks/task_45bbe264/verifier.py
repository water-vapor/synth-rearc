from arc2.core import *


def verify_45bbe264(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = lambda x2: recolor(color(x2), hfrontier(ulcorner(x2)))
    x2 = lambda x3: recolor(color(x3), vfrontier(ulcorner(x3)))
    x3 = mapply(x1, x0)
    x4 = mapply(x2, x0)
    x5 = combine(x3, x4)
    x6 = apply(uppermost, x0)
    x7 = apply(leftmost, x0)
    x8 = mapply(toindices, x0)
    x9 = difference(product(x6, x7), x8)
    x10 = canvas(mostcolor(I), shape(I))
    x11 = paint(x10, x5)
    x12 = fill(x11, TWO, x9)
    x13 = paint(x12, merge(x0))
    return x13
