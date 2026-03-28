from arc2.core import *


def verify_67636eac(I: Grid) -> Grid:
    x0 = objects(I, T, T, T)
    x1 = merge(x0)
    x2 = height(x1)
    x3 = width(x1)
    x4 = greater(x2, x3)
    x5 = order(x0, uppermost)
    x6 = order(x0, leftmost)
    x7 = branch(x4, x5, x6)
    x8 = apply(rbind(subgrid, I), x7)
    x9 = branch(x4, vconcat, hconcat)
    x10 = first(x8)
    for x11 in x8[ONE:]:
        x10 = x9(x10, x11)
    return x10
