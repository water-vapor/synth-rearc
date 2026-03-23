from arc2.core import *


def verify_281123b4(I: Grid) -> Grid:
    x0 = hsplit(I, FOUR)
    x1 = x0[0]
    x2 = x0[1]
    x3 = x0[2]
    x4 = x0[3]
    x5 = canvas(ZERO, shape(x1))
    x6 = ofcolor(x2, FIVE)
    x7 = fill(x5, FIVE, x6)
    x8 = ofcolor(x1, EIGHT)
    x9 = fill(x7, EIGHT, x8)
    x10 = ofcolor(x4, FOUR)
    x11 = fill(x9, FOUR, x10)
    x12 = ofcolor(x3, NINE)
    x13 = fill(x11, NINE, x12)
    return x13
