from arc2.core import *


def verify_f5c89df1(I: Grid) -> Grid:
    x0 = ofcolor(I, EIGHT)
    x1 = ofcolor(I, THREE)
    x2 = ofcolor(I, TWO)
    x3 = first(x1)
    x4 = invert(x3)
    x5 = shift(x0, x4)
    x6 = lbind(shift, x5)
    x7 = apply(x6, x2)
    x8 = merge(x7)
    x9 = shape(I)
    x10 = canvas(ZERO, x9)
    x11 = fill(x10, EIGHT, x8)
    return x11
