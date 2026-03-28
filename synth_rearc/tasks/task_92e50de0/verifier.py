from synth_rearc.core import *


def verify_92e50de0(I: Grid) -> Grid:
    x0 = leastcolor(I)
    x1 = ofcolor(I, x0)
    x2 = uppermost(x1)
    x3 = divide(x2, FOUR)
    x4 = multiply(x3, FOUR)
    x5 = leftmost(x1)
    x6 = divide(x5, FOUR)
    x7 = multiply(x6, FOUR)
    x8 = astuple(x4, x7)
    x9 = invert(x8)
    x10 = shift(x1, x9)
    x11 = even(x3)
    x12 = branch(x11, ZERO, FOUR)
    x13 = even(x6)
    x14 = branch(x13, ZERO, FOUR)
    x15 = height(I)
    x16 = interval(x12, x15, EIGHT)
    x17 = width(I)
    x18 = interval(x14, x17, EIGHT)
    x19 = product(x16, x18)
    x20 = lbind(shift, x10)
    x21 = mapply(x20, x19)
    x22 = fill(I, x0, x21)
    return x22
