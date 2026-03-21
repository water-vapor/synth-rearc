from arc2.core import *


def verify_ae58858e(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, TWO)
    x2 = sfilter(x1, lambda x3: greater(size(x3), THREE))
    x3 = mapply(toindices, x2)
    x4 = fill(I, SIX, x3)
    return x4
