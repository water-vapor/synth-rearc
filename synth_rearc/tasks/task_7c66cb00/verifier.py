from synth_rearc.core import *


def verify_7c66cb00(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = subtract(width(I), ONE)
    x2 = objects(I, F, F, T)
    x3 = sfilter(x2, fork(both, matcher(leftmost, ZERO), matcher(rightmost, x1)))
    x4 = difference(x2, x3)
    x5 = I
    for x6 in x4:
        x5 = fill(x5, x0, x6)
    for x7 in x3:
        x8 = mostcolor(x7)
        x9 = leastcolor(x7)
        x10 = lowermost(x7)
        for x11 in x4:
            x12 = sfilter(x11, matcher(first, x8))
            if len(x12) == ZERO:
                continue
            x13 = subtract(x10, lowermost(x12))
            x14 = shift(x12, (x13, ZERO))
            x5 = fill(x5, x9, x14)
    return x5
