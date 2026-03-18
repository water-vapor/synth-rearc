from arc2.core import *


def verify_03560426(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = order(x0, leftmost)
    x2 = mostcolor(I)
    x3 = shape(I)
    x4 = canvas(x2, x3)
    x5 = (ZERO, ZERO)
    x6 = x4
    for x7 in x1:
        x8 = shift(normalize(x7), x5)
        x6 = paint(x6, x8)
        x5 = lrcorner(x8)
    return x6
