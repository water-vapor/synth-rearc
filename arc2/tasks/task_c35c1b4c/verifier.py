from arc2.core import *


def verify_c35c1b4c(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = ofcolor(I, x0)
    x2 = width(I)
    x3 = decrement(x2)
    x4 = lbind(subtract, x3)
    x5 = compose(x4, last)
    x6 = fork(astuple, first, x5)
    x7 = apply(x6, x1)
    x8 = fill(I, x0, x7)
    return x8
