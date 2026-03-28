from synth_rearc.core import *


def verify_319f2597(I: Grid) -> Grid:
    x0 = ofcolor(I, ZERO)
    x1 = ulcorner(x0)
    x2 = lrcorner(x0)
    x3 = vfrontier(x1)
    x4 = vfrontier(x2)
    x5 = hfrontier(x1)
    x6 = hfrontier(x2)
    x7 = combine(x3, x4)
    x8 = combine(x5, x6)
    x9 = combine(x7, x8)
    x10 = fill(I, ZERO, x9)
    x11 = ofcolor(I, TWO)
    x12 = intersection(x9, x11)
    x13 = fill(x10, TWO, x12)
    return x13
