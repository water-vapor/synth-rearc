from synth_rearc.core import *


def verify_42a15761(I: Grid) -> Grid:
    x0 = width(I)
    x1 = increment(divide(x0, FOUR))
    x2 = hsplit(I, x1)
    x3 = rbind(colorcount, ZERO)
    x4 = order(x2, x3)
    x5 = height(I)
    x6 = crop(I, astuple(ZERO, THREE), astuple(x5, ONE))
    x7 = first(x4)
    for x8 in x4[ONE:]:
        x7 = hconcat(x7, x6)
        x7 = hconcat(x7, x8)
    return x7
