from synth_rearc.core import *


def verify_e84fef15(I: Grid) -> Grid:
    x0 = compress(I)
    x1 = vsplit(x0, FIVE)
    x2 = rbind(hsplit, FIVE)
    x3 = apply(x2, x1)
    x4 = merge(x3)
    x5 = mostcommon(x4)
    x6 = leastcommon(x4)
    x7 = cellwise(x5, x6, ONE)
    return x7
