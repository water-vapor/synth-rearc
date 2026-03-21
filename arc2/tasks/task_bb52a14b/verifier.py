from arc2.core import *


def verify_bb52a14b(I: Grid) -> Grid:
    x0 = ofcolor(I, FOUR)
    x1 = subgrid(x0, I)
    x2 = replace(x1, FOUR, ZERO)
    x3 = asobject(x2)
    x4 = occurrences(I, x3)
    x5 = ofcolor(x1, FOUR)
    x6 = lbind(shift, x5)
    x7 = mapply(x6, x4)
    x8 = fill(I, FOUR, x7)
    return x8
