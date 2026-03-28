from synth_rearc.core import *


def verify_a680ac02(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = compose(square, backdrop)
    x2 = compose(rbind(greater, ZERO), compose(size, delta))
    x3 = fork(both, x1, x2)
    x4 = sfilter(x0, x3)
    x5 = merge(x4)
    x6 = height(x5)
    x7 = width(x5)
    x8 = greater(x6, x7)
    x9 = order(x4, uppermost)
    x10 = order(x4, leftmost)
    x11 = branch(x8, x9, x10)
    x12 = apply(rbind(subgrid, I), x11)
    x13 = branch(x8, vconcat, hconcat)
    x14 = first(x12)
    for x15 in x12[ONE:]:
        x14 = x13(x14, x15)
    return x14
