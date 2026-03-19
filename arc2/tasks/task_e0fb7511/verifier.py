from arc2.core import *


def verify_e0fb7511(I: Grid) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = colorfilter(x0, ZERO)
    x2 = sizefilter(x1, ONE)
    x3 = merge(x2)
    x4 = toindices(x3)
    x5 = ofcolor(I, ZERO)
    x6 = difference(x5, x4)
    x7 = fill(I, EIGHT, x6)
    return x7
