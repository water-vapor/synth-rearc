from arc2.core import *


def verify_99caaf76(I: Grid) -> Grid:
    x0 = order(objects(I, F, T, T), ulcorner)
    x1 = canvas(EIGHT, shape(I))
    x2 = height(I)
    x3 = width(I)
    x4 = x1
    for x5 in x0:
        x6 = sfilter(x5, matcher(first, ONE))
        x7 = difference(x5, x6)
        x8 = rot180(subgrid(x7, I))
        x9 = shift(first(objects(x8, F, T, T)), ulcorner(x7))
        x10 = combine(x6, x9)
        x11 = position(x6, x7)
        if x11 == RIGHT:
            x12 = (ZERO, subtract(subtract(x3, ONE), rightmost(x10)))
        elif x11 == LEFT:
            x12 = (ZERO, invert(leftmost(x10)))
        elif x11 == DOWN:
            x12 = (subtract(subtract(x2, ONE), lowermost(x10)), ZERO)
        else:
            x12 = (invert(uppermost(x10)), ZERO)
        x13 = shift(x10, x12)
        x4 = paint(x4, x13)
    return x4
