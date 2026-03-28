from synth_rearc.core import *


def verify_dce56571(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = leastcolor(I)
    x2 = ofcolor(I, x1)
    x3 = size(x2)
    x4 = width(I)
    x5 = height(I)
    x6 = divide(x5, TWO)
    x7 = subtract(x4, x3)
    x8 = divide(x7, TWO)
    x9 = add(x8, x3)
    x10 = decrement(x9)
    x11 = astuple(x6, x8)
    x12 = astuple(x6, x10)
    x13 = connect(x11, x12)
    x14 = shape(I)
    x15 = canvas(x0, x14)
    x16 = fill(x15, x1, x13)
    return x16
