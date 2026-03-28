from synth_rearc.core import *


def verify_470c91de(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = matcher(color, EIGHT)
    x3 = compose(flip, x2)
    x4 = sfilter(x1, x3)
    x5 = canvas(x0, shape(I))
    for x6 in x4:
        x7 = delta(x6)
        x8 = uppermost(x7)
        x9 = uppermost(x6)
        x10 = equality(x8, x9)
        x11 = branch(x10, NEG_ONE, ONE)
        x12 = leftmost(x7)
        x13 = leftmost(x6)
        x14 = equality(x12, x13)
        x15 = branch(x14, NEG_ONE, ONE)
        x16 = astuple(x11, x15)
        x17 = shift(backdrop(x6), x16)
        x18 = fill(x5, color(x6), x17)
        x5 = x18
    return x5
