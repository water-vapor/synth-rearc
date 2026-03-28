from synth_rearc.core import *


def verify_ce039d91(I: Grid) -> Grid:
    x0 = vmirror(I)
    x1 = cellwise(I, x0, ZERO)
    x2 = ofcolor(x1, FIVE)
    x3 = fill(I, ONE, x2)
    return x3
