from arc2.core import *


def verify_f5aa3634(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = totuple(x0)
    x2 = rbind(subgrid, I)
    x3 = apply(x2, x1)
    x4 = mostcommon(x3)
    return x4
