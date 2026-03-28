from synth_rearc.core import *


def verify_8ee62060(I: Grid) -> Grid:
    x0 = halve(height(I))
    x1 = vsplit(I, x0)
    x2 = interval(ZERO, x0, ONE)
    x3 = pair(x2, x1)
    x4 = compose(invert, first)
    x5 = order(x3, x4)
    x6 = apply(last, x5)
    x7 = merge(x6)
    return x7

