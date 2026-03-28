from arc2.core import *


def verify_396d80d7(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = argmin(x0, compose(size, backdrop))
    x2 = color(x1)
    x3 = toindices(other(x0, x1))
    x4 = mapply(ineighbors, x3)
    x5 = mapply(dneighbors, x3)
    x6 = difference(x4, x5)
    x7 = difference(x6, x3)
    x8 = ofcolor(I, mostcolor(I))
    x9 = intersection(x7, x8)
    x10 = fill(I, x2, x9)
    return x10
