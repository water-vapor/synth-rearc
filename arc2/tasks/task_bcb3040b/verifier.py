from arc2.core import *


def verify_bcb3040b(I: Grid) -> Grid:
    x0 = ofcolor(I, TWO)
    x1 = order(x0, identity)
    x2 = first(x1)
    x3 = last(x1)
    x4 = connect(x2, x3)
    x5 = ofcolor(I, ZERO)
    x6 = intersection(x4, x5)
    x7 = fill(I, TWO, x6)
    x8 = ofcolor(I, ONE)
    x9 = intersection(x4, x8)
    x10 = fill(x7, THREE, x9)
    return x10
