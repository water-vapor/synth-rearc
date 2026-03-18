from arc2.core import *


def verify_f0df5ff0(I: Grid) -> Grid:
    x0 = ofcolor(I, ONE)
    x1 = mapply(neighbors, x0)
    x2 = underfill(I, ONE, x1)
    return x2
