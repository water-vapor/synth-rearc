from arc2.core import *


def verify_4852f2fa(I: Grid) -> Grid:
    x0 = ofcolor(I, EIGHT)
    x1 = subgrid(x0, I)
    x2 = ofcolor(x1, EIGHT)
    x3 = height(x1)
    x4 = width(x1)
    x5 = astuple(x3, x4)
    x6 = maximum(x5)
    x7 = subtract(x6, x3)
    x8 = subtract(x6, x4)
    x9 = astuple(x7, x8)
    x10 = shift(x2, x9)
    x11 = ofcolor(I, FOUR)
    x12 = size(x11)
    x13 = multiply(x6, x12)
    x14 = astuple(x6, x13)
    x15 = canvas(ZERO, x14)
    x16 = interval(ZERO, x13, x6)
    x17 = apply(tojvec, x16)
    x18 = lbind(shift, x10)
    x19 = mapply(x18, x17)
    x20 = fill(x15, EIGHT, x19)
    return x20
