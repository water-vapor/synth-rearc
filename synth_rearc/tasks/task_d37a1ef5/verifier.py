from synth_rearc.core import *


def verify_d37a1ef5(
    I: Grid,
) -> Grid:
    x0 = ofcolor(I, TWO)
    x1 = backdrop(x0)
    x2 = ofcolor(I, FIVE)
    x3 = backdrop(x2)
    x4 = difference(x1, x3)
    x5 = fill(I, TWO, x4)
    return x5
