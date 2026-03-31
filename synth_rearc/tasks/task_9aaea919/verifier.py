from synth_rearc.core import *


def verify_9aaea919(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = sfilter(x1, lambda x: both(hline(x), equality(size(x), FIVE)))
    x3 = sfilter(x1, lambda x: greater(size(x), FIVE))
    x4 = sfilter(x2, matcher(color, TWO))
    x5 = sfilter(x2, matcher(color, THREE))
    x6 = tuple(order(x3, lambda x: (leftmost(x), uppermost(x))))
    x7 = tuple(x8 for x8 in x6 if any(vmatching(x8, x9) for x9 in x4))
    x8 = tuple(x9 for x9 in x6 if any(vmatching(x9, x10) for x10 in x5))
    x9 = fill(I, x0, merge(x2))
    x10 = fill(x9, FIVE, merge(x7))
    x11 = size(x7)
    x12 = tuple(order(x5, leftmost))
    for x13 in x12:
        x14 = tuple(x15 for x15 in x8 if vmatching(x15, x13))
        if len(x14) == ZERO:
            continue
        x15 = argmin(x14, uppermost)
        for x16 in range(ONE, increment(x11)):
            x17 = multiply(FOUR, x16)
            x18 = shift(x15, (-x17, ZERO))
            x10 = paint(x10, x18)
    return x10
