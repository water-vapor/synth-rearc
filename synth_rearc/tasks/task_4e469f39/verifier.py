from synth_rearc.core import *


def verify_4e469f39(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, FIVE)
    x2 = width(I)
    x3 = I
    for x4 in x1:
        x5 = uppermost(x4)
        x6 = leftmost(x4)
        x7 = rightmost(x4)
        x8 = frozenset((x5, x9) for x9 in range(x6, x7 + ONE))
        x9 = difference(x8, toindices(x4))
        x10 = first(x9)
        x11 = subtract(x10[ONE], x6)
        x12 = subtract(x7, x10[ONE])
        x13 = delta(x4)
        if greater(x12, x11):
            x14 = frozenset((subtract(x5, ONE), x15) for x15 in range(x10[ONE], x2))
        else:
            x14 = frozenset((subtract(x5, ONE), x15) for x15 in range(x10[ONE] + ONE))
        x15 = combine(x13, x14)
        x3 = fill(x3, TWO, x15)
    return x3
