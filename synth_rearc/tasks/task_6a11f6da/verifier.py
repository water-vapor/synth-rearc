from synth_rearc.core import *


def verify_6a11f6da(I: Grid) -> Grid:
    x0 = width(I)
    x1 = astuple(FIVE, x0)
    x2 = crop(I, ORIGIN, x1)
    x3 = astuple(FIVE, ZERO)
    x4 = crop(I, x3, x1)
    x5 = astuple(TEN, ZERO)
    x6 = crop(I, x5, x1)
    x7 = canvas(ZERO, x1)
    x8 = ofcolor(x4, EIGHT)
    x9 = fill(x7, EIGHT, x8)
    x10 = ofcolor(x2, ONE)
    x11 = fill(x9, ONE, x10)
    x12 = ofcolor(x6, SIX)
    x13 = fill(x11, SIX, x12)
    return x13
