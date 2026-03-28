from synth_rearc.core import *


def verify_639f5a19(
    I: Grid,
) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, EIGHT)
    x2 = I
    for x3 in x1:
        x4 = uppermost(x3)
        x5 = lowermost(x3)
        x6 = leftmost(x3)
        x7 = rightmost(x3)
        x8 = add(x4, halve(height(x3)))
        x9 = add(x6, halve(width(x3)))
        x10 = interval(x4, x8, ONE)
        x11 = interval(x8, increment(x5), ONE)
        x12 = interval(x6, x9, ONE)
        x13 = interval(x9, increment(x7), ONE)
        x14 = product(x10, x12)
        x15 = product(x10, x13)
        x16 = product(x11, x12)
        x17 = product(x11, x13)
        x18 = interval(add(x4, TWO), subtract(x5, ONE), ONE)
        x19 = interval(add(x6, TWO), subtract(x7, ONE), ONE)
        x20 = product(x18, x19)
        x21 = fill(x2, SIX, x14)
        x22 = fill(x21, ONE, x15)
        x23 = fill(x22, TWO, x16)
        x24 = fill(x23, THREE, x17)
        x2 = fill(x24, FOUR, x20)
    return x2
