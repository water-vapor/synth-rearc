from arc2.core import *


def verify_f3e62deb(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = first(x0)
    x2 = color(x1)
    x3 = uppermost(x1)
    x4 = lowermost(x1)
    x5 = leftmost(x1)
    x6 = rightmost(x1)
    x7 = height(I)
    x8 = width(I)
    x9 = astuple(invert(x3), ZERO)
    x10 = astuple(ZERO, subtract(decrement(x8), x6))
    x11 = astuple(subtract(decrement(x7), x4), ZERO)
    x12 = astuple(ZERO, invert(x5))
    x13 = equality(x2, SIX)
    x14 = equality(x2, EIGHT)
    x15 = equality(x2, FOUR)
    x16 = branch(x15, x11, x12)
    x17 = branch(x14, x10, x16)
    x18 = branch(x13, x9, x17)
    x19 = shift(x1, x18)
    x20 = canvas(ZERO, shape(I))
    x21 = paint(x20, x19)
    return x21
