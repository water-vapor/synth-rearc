from synth_rearc.core import *


def verify_5783df64(I: Grid) -> Grid:
    x0 = vsplit(I, THREE)
    x1 = rbind(hsplit, THREE)
    x2 = apply(x1, x0)
    x3 = lbind(apply, leastcolor)
    x4 = apply(x3, x2)
    return x4
