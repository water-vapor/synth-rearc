from synth_rearc.core import *


def verify_25c199f5(I: Grid) -> Grid:
    x0 = hsplit(I, THREE)
    x1 = first(x0)
    x2 = crop(I, astuple(ZERO, SIX), astuple(FIVE, FIVE))
    x3 = last(x0)
    x4 = repeat(SEVEN, FIVE)
    x5 = matcher(identity, x4)
    x6 = compose(flip, x5)
    x7 = sfilter(x3, x6)
    x8 = sfilter(x2, x6)
    x9 = sfilter(x1, x6)
    x10 = vconcat(x7, x8)
    x11 = vconcat(x10, x9)
    x12 = height(x11)
    x13 = subtract(FIVE, x12)
    x14 = repeat(x4, x13)
    x15 = vconcat(x14, x11)
    return x15
