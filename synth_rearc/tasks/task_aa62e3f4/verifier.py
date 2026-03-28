from synth_rearc.core import *


def verify_aa62e3f4(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = asindices(I)
    x2 = ofcolor(I, x0)
    x3 = difference(x1, x2)
    x4 = toobject(x3, I)
    x5 = leastcolor(x4)
    x6 = mapply(dneighbors, x3)
    x7 = difference(x6, x3)
    x8 = canvas(x0, shape(I))
    x9 = fill(x8, x5, x7)
    return x9
