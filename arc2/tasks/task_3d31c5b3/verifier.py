from arc2.core import *


def verify_3d31c5b3(I: Grid) -> Grid:
    x0 = vsplit(I, FOUR)
    x1 = x0[ZERO]
    x2 = x0[ONE]
    x3 = x0[TWO]
    x4 = x0[THREE]
    x5 = ofcolor(x1, ZERO)
    x6 = ofcolor(x2, FOUR)
    x7 = intersection(x5, x6)
    x8 = fill(x1, FOUR, x7)
    x9 = ofcolor(x8, ZERO)
    x10 = ofcolor(x4, EIGHT)
    x11 = intersection(x9, x10)
    x12 = fill(x8, EIGHT, x11)
    x13 = ofcolor(x12, ZERO)
    x14 = ofcolor(x3, TWO)
    x15 = intersection(x13, x14)
    x16 = fill(x12, TWO, x15)
    return x16
