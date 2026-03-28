from synth_rearc.core import *


def verify_21f83797(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = other(x0, ZERO)
    x2 = ofcolor(I, x1)
    x3 = ulcorner(x2)
    x4 = lrcorner(x2)
    x5 = hfrontier(x3)
    x6 = vfrontier(x3)
    x7 = hfrontier(x4)
    x8 = vfrontier(x4)
    x9 = combine(x5, x6)
    x10 = combine(x7, x8)
    x11 = combine(x9, x10)
    x12 = fill(I, x1, x11)
    x13 = backdrop(x2)
    x14 = box(x2)
    x15 = difference(x13, x14)
    x16 = fill(x12, ONE, x15)
    return x16
