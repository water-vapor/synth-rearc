from synth_rearc.core import *


def verify_668eec9a(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = order(x0, uppermost)
    x2 = apply(color, x1)
    x3 = size(x2)
    x4 = mostcolor(I)
    x5 = subtract(FIVE, x3)
    x6 = repeat(x4, x5)
    x7 = combine(x6, x2)
    x8 = rbind(repeat, THREE)
    x9 = apply(x8, x7)
    return x9
