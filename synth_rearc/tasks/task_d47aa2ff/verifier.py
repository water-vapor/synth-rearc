from synth_rearc.core import *


def verify_d47aa2ff(I: Grid) -> Grid:
    x0 = lefthalf(I)
    x1 = righthalf(I)
    x2 = cellwise(x0, x1, ZERO)
    x3 = shape(x0)
    x4 = canvas(ZERO, x3)
    x5 = cellwise(x0, x4, ONE)
    x6 = cellwise(x1, x4, ONE)
    x7 = ofcolor(x5, ZERO)
    x8 = ofcolor(x6, ZERO)
    x9 = difference(x7, x8)
    x10 = difference(x8, x7)
    x11 = fill(x2, ONE, x9)
    x12 = fill(x11, TWO, x10)
    return x12
