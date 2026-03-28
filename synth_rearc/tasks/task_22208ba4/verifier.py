from synth_rearc.core import *


def verify_22208ba4(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = tuple(x1)
    x3 = tuple(color(x4) for x4 in x2)
    x4 = canvas(x0, shape(I))
    x5 = []
    for x6 in x2:
        x7 = color(x6)
        x8 = x3.count(x7)
        x9 = height(x6)
        x10 = width(x6)
        x11 = uppermost(x6)
        x12 = leftmost(x6)
        x13 = branch(equality(x11, ZERO), x9, invert(x9))
        x14 = branch(equality(x12, ZERO), x10, invert(x10))
        x15 = astuple(x13, x14)
        x16 = branch(greater(x8, ONE), shift(x6, x15), x6)
        x5.append(x16)
    x17 = merge(tuple(x5))
    x18 = paint(x4, x17)
    return x18
