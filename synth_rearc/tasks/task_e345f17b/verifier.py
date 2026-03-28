from synth_rearc.core import *


def verify_e345f17b(I: Grid) -> Grid:
    x0 = lefthalf(I)
    x1 = righthalf(I)
    x2 = ofcolor(x0, ZERO)
    x3 = ofcolor(x1, ZERO)
    x4 = intersection(x2, x3)
    x5 = canvas(ZERO, shape(x0))
    x6 = fill(x5, FOUR, x4)
    return x6
