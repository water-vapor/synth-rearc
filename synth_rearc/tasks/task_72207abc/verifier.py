from synth_rearc.core import *


def verify_72207abc(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = order(x0, leftmost)
    x2 = apply(color, x1)
    x3 = size(x1)
    x4 = apply(leftmost, x1)
    x5 = last(x4)
    x6 = x3
    x7 = halve(height(I))
    x8 = decrement(width(I))
    x9 = I
    x10 = ZERO
    while True:
        x5 = add(x5, x6)
        if greater(x5, x8):
            break
        x11 = astuple(x7, x5)
        x12 = initset(x11)
        x13 = x2[x10 % x3]
        x9 = fill(x9, x13, x12)
        x6 = increment(x6)
        x10 = increment(x10)
    return x9
