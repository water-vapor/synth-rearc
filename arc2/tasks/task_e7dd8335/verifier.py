from arc2.core import *


def verify_e7dd8335(I: Grid) -> Grid:
    x0 = objects(I, T, T, F)
    x1 = colorfilter(x0, ONE)
    x2 = I
    for x3 in x1:
        x4 = uppermost(x3)
        x5 = lowermost(x3)
        x6 = leftmost(x3)
        x7 = rightmost(x3)
        x8 = (x4 + x5) // TWO
        x9 = interval(x8 + ONE, x5 + ONE, ONE)
        x10 = interval(x6, x7 + ONE, ONE)
        x11 = product(x9, x10)
        x12 = intersection(toindices(x3), x11)
        x13 = recolor(TWO, x12)
        x2 = paint(x2, x13)
    return x2
