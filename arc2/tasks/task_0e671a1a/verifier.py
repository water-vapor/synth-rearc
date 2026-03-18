from arc2.core import *


def verify_0e671a1a(I: Grid) -> Grid:
    x0 = ofcolor(I, THREE)
    x1 = ofcolor(I, FOUR)
    x2 = ofcolor(I, TWO)
    x3 = first(x0)
    x4 = first(x1)
    x5 = first(x2)
    x6 = astuple(first(x4), last(x3))
    x7 = astuple(first(x5), last(x4))
    x8 = connect(x3, x6)
    x9 = connect(x6, x4)
    x10 = connect(x4, x7)
    x11 = connect(x7, x5)
    x12 = combine(x8, x9)
    x13 = combine(x10, x11)
    x14 = combine(x12, x13)
    x15 = combine(x0, x1)
    x16 = combine(x15, x2)
    x17 = difference(x14, x16)
    x18 = fill(I, FIVE, x17)
    return x18
