from arc2.core import *


def verify_e7a25a18(I: Grid) -> Grid:
    x0 = ofcolor(I, TWO)
    x1 = subgrid(x0, I)
    x2 = ofcolor(x1, ZERO)
    x3 = ofcolor(x1, TWO)
    x4 = asindices(x1)
    x5 = difference(x4, x2)
    x6 = difference(x5, x3)
    x7 = subgrid(x6, x1)
    x8 = upscale(x7, TWO)
    x9 = canvas(TWO, shape(x1))
    x10 = astuple(ONE, ONE)
    x11 = asobject(x8)
    x12 = shift(x11, x10)
    x13 = paint(x9, x12)
    return x13
