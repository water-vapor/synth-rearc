from synth_rearc.core import *


def verify_7c8af763(I: Grid) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = colorfilter(x0, ZERO)
    x2 = ofcolor(I, ONE)
    x3 = ofcolor(I, TWO)
    x4 = I
    for x5 in x1:
        x6 = toindices(x5)
        x7 = mapply(dneighbors, x6)
        x8 = intersection(x7, x2)
        x9 = intersection(x7, x3)
        x10 = size(x8)
        x11 = size(x9)
        x12 = greater(x10, x11)
        x13 = branch(x12, ONE, TWO)
        x4 = fill(x4, x13, x5)
    return x4
