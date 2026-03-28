from arc2.core import *


def verify_642d658d(I: Grid) -> Grid:
    x0 = totuple(ofcolor(I, FOUR))
    x1 = apply(dneighbors, x0)
    x2 = rbind(toobject, I)
    x3 = apply(x2, x1)
    x4 = tuple(x5 for x5 in x3 if size(x5) == FOUR)
    x5 = tuple(x6 for x6 in x4 if numcolors(x6) == ONE)
    x6 = tuple(x7 for x7 in apply(color, x5) if x7 != FOUR)
    x7 = mostcommon(x6)
    x8 = canvas(x7, UNITY)
    return x8
