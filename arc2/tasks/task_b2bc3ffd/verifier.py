from arc2.core import *


def verify_b2bc3ffd(I: Grid) -> Grid:
    x0 = canvas(SEVEN, shape(I))
    x1 = ofcolor(I, EIGHT)
    x2 = fill(x0, EIGHT, x1)
    x3 = objects(I, T, F, T)
    x4 = colorfilter(x3, EIGHT)
    x5 = difference(x3, x4)
    for x6 in x5:
        x7 = astuple(invert(size(x6)), ZERO)
        x8 = shift(x6, x7)
        x2 = paint(x2, x8)
    return x2
