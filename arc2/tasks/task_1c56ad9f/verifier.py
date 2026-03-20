from arc2.core import *


def verify_1c56ad9f(I: Grid) -> Grid:
    x0 = leastcolor(I)
    x1 = ofcolor(I, x0)
    x2 = uppermost(x1)
    x3 = lowermost(x1)
    x4 = interval(decrement(x3), decrement(x2), NEG_TWO)
    x5 = rbind(astuple, ZERO)
    x6 = apply(x5, x4)
    x7 = apply(hfrontier, x6)
    x8 = lbind(intersection, x1)
    x9 = apply(x8, x7)
    x10 = interval(ZERO, size(x4), ONE)
    x11 = tuple(LEFT if even(k) else RIGHT for k in x10)
    x12 = mpapply(shift, x9, x11)
    x13 = merge(x9)
    x14 = difference(x1, x13)
    x15 = combine(x14, x12)
    x16 = canvas(mostcolor(I), shape(I))
    x17 = fill(x16, x0, x15)
    return x17
