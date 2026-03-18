from arc2.core import *


def verify_f45f5ca7(I: Grid) -> Grid:
    x0 = ofcolor(I, EIGHT)
    x1 = apply(first, x0)
    x2 = product(x1, initset(ONE))
    x3 = ofcolor(I, TWO)
    x4 = apply(first, x3)
    x5 = product(x4, initset(TWO))
    x6 = ofcolor(I, FOUR)
    x7 = apply(first, x6)
    x8 = product(x7, initset(THREE))
    x9 = ofcolor(I, THREE)
    x10 = apply(first, x9)
    x11 = product(x10, initset(FOUR))
    x12 = canvas(ZERO, shape(I))
    x13 = fill(x12, EIGHT, x2)
    x14 = fill(x13, TWO, x5)
    x15 = fill(x14, FOUR, x8)
    x16 = fill(x15, THREE, x11)
    return x16
