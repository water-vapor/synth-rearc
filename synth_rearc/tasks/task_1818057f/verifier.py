from synth_rearc.core import *


def verify_1818057f(I: Grid) -> Grid:
    x0 = ofcolor(I, FOUR)
    x1 = rbind(intersection, x0)
    x2 = compose(x1, dneighbors)
    x3 = matcher(size, FOUR)
    x4 = compose(x3, x2)
    x5 = sfilter(x0, x4)
    x6 = mapply(dneighbors, x5)
    x7 = combine(x5, x6)
    x8 = fill(I, EIGHT, x7)
    return x8
