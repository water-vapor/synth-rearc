from synth_rearc.core import *


def verify_1e81d6f9(I: Grid) -> Grid:
    x0 = index(I, UNITY)
    x1 = ofcolor(I, x0)
    x2 = remove(UNITY, x1)
    x3 = fill(I, ZERO, x2)
    return x3
