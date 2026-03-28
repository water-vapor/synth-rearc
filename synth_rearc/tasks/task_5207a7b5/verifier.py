from synth_rearc.core import *


def verify_5207a7b5(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, FIVE)
    x2 = first(x1)
    x3 = height(x2)
    x4 = leftmost(x2)
    x5 = height(I)
    x6 = width(I)
    x7 = canvas(ZERO, shape(I))
    x8 = fill(x7, FIVE, x2)
    x9 = interval(ONE, increment(x4), ONE)
    for x10 in x9:
        x11 = subtract(x4, x10)
        x12 = min(x5, add(x3, multiply(TWO, x10)))
        x13 = frozenset((r, x11) for r in range(x12))
        x8 = fill(x8, EIGHT, x13)
    x14 = interval(ONE, subtract(x6, x4), ONE)
    for x15 in x14:
        x16 = subtract(x3, multiply(TWO, x15))
        if positive(x16):
            x17 = add(x4, x15)
            x18 = frozenset((r, x17) for r in range(x16))
            x8 = fill(x8, SIX, x18)
    return x8
