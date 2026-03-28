from synth_rearc.core import *


def verify_6d1d5c90(I: Grid) -> Grid:
    x0 = height(I)
    x1 = crop(I, ORIGIN, astuple(x0, ONE))
    x2 = ofcolor(x1, TWO)
    x3 = uppermost(x2)
    x4 = astuple(x0, decrement(width(I)))
    x5 = crop(I, RIGHT, x4)
    x6 = vsplit(x5, x0)
    x7 = interval(ZERO, x0, ONE)
    x8 = pair(x7, x6)
    x9 = lambda x: (first(x) + x3) % x0
    x10 = order(x8, x9)
    x11 = apply(last, x10)
    x12 = merge(x11)
    return x12
