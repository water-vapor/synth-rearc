from arc2.core import *


def verify_dd2401ed(I: Grid) -> Grid:
    x0 = ofcolor(I, FIVE)
    x1 = leftmost(x0)
    x2 = ofcolor(I, ONE)
    x3 = sfilter(x2, lambda x4: x4[1] < x1)
    x4 = compose(lbind(subtract, x1), last)
    x5 = apply(x4, x3)
    x6 = maximum(x5)
    x7 = increment(x6)
    x8 = add(x1, x7)
    x9 = shift(x0, tojvec(x7))
    x10 = ofcolor(I, TWO)
    x11 = sfilter(x10, lambda x12: x1 < x12[1] < x8)
    x12 = compose(rbind(subtract, x1), last)
    x13 = apply(x12, x11)
    x14 = difference(x5, x13)
    x15 = equality(size(x14), ZERO)
    x16 = branch(x15, x11, frozenset())
    x17 = cover(I, x0)
    x18 = fill(x17, ONE, x16)
    x19 = fill(x18, FIVE, x9)
    return x19
