from arc2.core import *


def verify_e7b06bea(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = colorfilter(x0, FIVE)
    x2 = first(x1)
    x3 = remove(x2, x0)
    x4 = order(x3, leftmost)
    x5 = cover(I, merge(x3))
    x6 = size(x2)
    x7 = decrement(leftmost(first(x4)))
    x8 = x5
    for x9 in range(height(I)):
        x10 = divide(x9, x6)
        x11 = x10 % size(x4)
        x12 = color(x4[x11])
        x13 = astuple(x9, x7)
        x8 = fill(x8, x12, initset(x13))
    return x8
