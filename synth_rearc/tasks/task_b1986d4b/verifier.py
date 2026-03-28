from synth_rearc.core import *


def verify_b1986d4b(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, F)
    x2 = sfilter(x1, lambda x: both(color(x) != x0, square(x)))
    x3 = sizefilter(x2, FOUR)
    x4 = sizefilter(x2, NINE)
    x5 = sizefilter(x2, 16)
    x6 = valmax(x4, uppermost)
    x7 = sfilter(x3, lambda x: uppermost(x) <= x6)
    x8 = color(first(x7))
    x9 = color(first(x4))
    x10 = color(first(x5))
    x11 = size(x7)
    x12 = size(x4)
    x13 = size(x5)
    x14 = maximum((x11, x12, x13))
    x15 = []
    x16 = interval(ZERO, TWO, ONE)
    x17 = interval(ZERO, THREE, ONE)
    x18 = interval(ZERO, FOUR, ONE)
    x19 = canvas(x0, (FIVE, ONE))
    for x20 in interval(ZERO, x14, ONE):
        x21 = ZERO
        if x11 > x20:
            x21 = TWO
        if x12 > x20:
            x21 = THREE
        if x13 > x20:
            x21 = FOUR
        x22 = canvas(x0, (FIVE, x21))
        if x13 > x20:
            x22 = fill(x22, x10, product(x18, x18))
        if x12 > x20:
            x22 = fill(x22, x9, product(x17, x17))
        if x11 > x20:
            x22 = fill(x22, x8, product(x16, x16))
        x15.append(hconcat(x22, x19))
    x23 = x15[ZERO]
    for x24 in x15[ONE:]:
        x23 = hconcat(x23, x24)
    return x23
