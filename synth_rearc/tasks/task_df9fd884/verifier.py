from synth_rearc.core import *


def verify_df9fd884(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, FOUR)
    x2 = argmin(x1, uppermost)
    x3 = first(difference(x0, x1))
    x4 = delta(x2)
    x5 = leftmost(x4)
    x6 = height(I)
    x7 = height(x3)
    x8 = subtract(x6, x7)
    x9 = astuple(x8, x5)
    x10 = normalize(x3)
    x11 = shift(x10, x9)
    x12 = cover(I, x3)
    x13 = paint(x12, x11)
    return x13
