from synth_rearc.core import *


def verify_37ce87bb(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = ofcolor(I, x0)
    x2 = asindices(I)
    x3 = difference(x2, x1)
    x4 = rightmost(x3)
    x5 = add(x4, TWO)
    x6 = colorcount(I, EIGHT)
    x7 = colorcount(I, TWO)
    x8 = subtract(x6, x7)
    x9 = height(I)
    x10 = subtract(x9, x8)
    x11 = interval(x10, x9, ONE)
    x12 = product(x11, initset(x5))
    x13 = fill(I, FIVE, x12)
    return x13
