from synth_rearc.core import *


def verify_140c817e(I: Grid) -> Grid:
    x0 = ofcolor(I, ONE)
    x1 = fork(combine, hfrontier, vfrontier)
    x2 = mapply(x1, x0)
    x3 = fill(I, ONE, x2)
    x4 = mapply(ineighbors, x0)
    x5 = fill(x3, THREE, x4)
    x6 = fill(x5, TWO, x0)
    return x6
