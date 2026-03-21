from arc2.core import *


def verify_a04b2602(I: Grid) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = colorfilter(x0, THREE)
    x2 = apply(backdrop, x1)
    x3 = merge(x2)
    x4 = ofcolor(I, TWO)
    x5 = intersection(x3, x4)
    x6 = apply(neighbors, x5)
    x7 = merge(x6)
    x8 = difference(x7, x5)
    x9 = fill(I, ONE, x8)
    return x9
