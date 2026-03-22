from arc2.core import *


def verify_73c3b0d8(I: Grid) -> Grid:
    x0 = ofcolor(I, FOUR)
    x1 = shift(x0, DOWN)
    x2 = ofcolor(I, TWO)
    x3 = uppermost(x2)
    x4 = decrement(x3)
    x5 = matcher(first, x4)
    x6 = sfilter(x1, x5)
    x7 = mapply(rbind(shoot, NEG_UNITY), x6)
    x8 = mapply(rbind(shoot, UP_RIGHT), x6)
    x9 = combine(x7, x8)
    x10 = combine(x1, x9)
    x11 = canvas(ZERO, shape(I))
    x12 = fill(x11, TWO, x2)
    x13 = fill(x12, FOUR, x10)
    return x13
