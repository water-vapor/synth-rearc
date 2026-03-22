from arc2.core import *


def verify_90347967(I: Grid) -> Grid:
    x0 = ofcolor(I, FIVE)
    x1 = first(x0)
    x2 = sfilter(asobject(I), lambda x: x[ZERO] not in (ZERO, FIVE))
    x3 = double(x1)
    x4 = frozenset((x5, subtract(x3, x6)) for x5, x6 in x2)
    x5 = canvas(ZERO, shape(I))
    x6 = fill(x5, FIVE, x0)
    x7 = paint(x6, x4)
    return x7
