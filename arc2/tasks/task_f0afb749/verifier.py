from arc2.core import *


def verify_f0afb749(I: Grid) -> Grid:
    x0 = upscale(I, TWO)
    x1 = ofcolor(I, ZERO)
    x2 = difference(asindices(I), x1)
    x3 = astuple(UNITY, NEG_UNITY)
    x4 = product(x2, x3)
    x5 = fork(shoot, first, last)
    x6 = mapply(x5, x4)
    x7 = intersection(x6, x1)
    x8 = apply(lbind(multiply, TWO), x7)
    x9 = shift(x8, UNITY)
    x10 = combine(x8, x9)
    x11 = fill(x0, ONE, x10)
    return x11
