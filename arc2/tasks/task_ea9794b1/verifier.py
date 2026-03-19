from arc2.core import *


def verify_ea9794b1(I: Grid) -> Grid:
    x0 = tophalf(I)
    x1 = bottomhalf(I)
    x2 = lefthalf(x0)
    x3 = righthalf(x0)
    x4 = lefthalf(x1)
    x5 = righthalf(x1)
    x6 = canvas(ZERO, (FIVE, FIVE))
    x7 = ofcolor(x2, FOUR)
    x8 = fill(x6, FOUR, x7)
    x9 = ofcolor(x5, EIGHT)
    x10 = fill(x8, EIGHT, x9)
    x11 = ofcolor(x4, NINE)
    x12 = fill(x10, NINE, x11)
    x13 = ofcolor(x3, THREE)
    x14 = fill(x12, THREE, x13)
    return x14
