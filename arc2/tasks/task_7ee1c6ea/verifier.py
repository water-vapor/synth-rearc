from arc2.core import *


def verify_7ee1c6ea(I: Grid) -> Grid:
    x0 = ofcolor(I, FIVE)
    x1 = inbox(x0)
    x2 = backdrop(x1)
    x3 = ulcorner(x2)
    x4 = shape(x2)
    x5 = crop(I, x3, x4)
    x6 = palette(x5)
    x7 = remove(ZERO, x6)
    x8 = first(x7)
    x9 = other(x7, x8)
    x10 = switch(x5, x8, x9)
    x11 = asobject(x10)
    x12 = shift(x11, x3)
    x13 = paint(I, x12)
    return x13
