from synth_rearc.core import *


def verify_7e02026e(I: Grid) -> Grid:
    x0 = ofcolor(I, ZERO)
    x1 = rbind(intersection, x0)
    x2 = chain(size, x1, dneighbors)
    x3 = matcher(x2, FOUR)
    x4 = sfilter(x0, x3)
    x5 = fork(combine, initset, dneighbors)
    x6 = mapply(x5, x4)
    x7 = fill(I, THREE, x6)
    return x7
