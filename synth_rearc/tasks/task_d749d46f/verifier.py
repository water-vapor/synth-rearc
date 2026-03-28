from synth_rearc.core import *


def verify_d749d46f(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = other(palette(I), x0)
    x2 = objects(I, T, F, T)
    x3 = order(x2, leftmost)
    x4 = apply(height, x3)
    x5 = apply(width, x3)
    x6 = papply(min, x4, x5)
    x7 = papply(max, x4, x5)
    x8 = decrement(add(sum(x7), size(x7)))
    x9 = canvas(x0, (TEN, x8))
    x10 = x9
    x11 = ZERO
    x12 = ZERO
    for x13, x14 in pair(x6, x7):
        x15 = interval(ZERO, x13, ONE)
        x16 = interval(ZERO, x14, ONE)
        x17 = product(x15, x16)
        x18 = shift(x17, (ZERO, x11))
        x10 = fill(x10, x1, x18)
        x19 = interval(subtract(TEN, x14), TEN, ONE)
        x20 = product(x19, x15)
        x21 = shift(x20, (ZERO, x12))
        x10 = fill(x10, x1, x21)
        x11 = add(x11, increment(x14))
        x12 = add(x12, increment(x13))
    return x10
