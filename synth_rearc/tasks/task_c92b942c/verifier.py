from synth_rearc.core import *


def verify_c92b942c(
    I: Grid,
) -> Grid:
    x0 = hconcat(I, I)
    x1 = hconcat(x0, I)
    x2 = vconcat(x1, x1)
    x3 = vconcat(x2, x1)
    x4 = ofcolor(x3, ZERO)
    x5 = difference(asindices(x3), x4)
    x6 = mapply(hfrontier, x5)
    x7 = underfill(x3, ONE, x6)
    x8 = shift(x5, NEG_UNITY)
    x9 = shift(x5, UNITY)
    x10 = combine(x8, x9)
    x11 = difference(x10, x5)
    x12 = fill(x7, THREE, x11)
    return x12
