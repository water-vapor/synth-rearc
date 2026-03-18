from arc2.core import *


def verify_12422b43(I: Grid) -> Grid:
    x0 = matcher(first, FIVE)
    x1 = sfilter(I, x0)
    x2 = replace(x1, FIVE, ZERO)
    x3 = asindices(I)
    x4 = ofcolor(I, ZERO)
    x5 = difference(x3, x4)
    x6 = lowermost(x5)
    x7 = increment(x6)
    x8 = height(I)
    x9 = subtract(x8, x7)
    x10 = height(x2)
    x11 = tuple(x2[x12 % x10] for x12 in range(x9))
    x12 = width(I)
    x13 = astuple(x7, x12)
    x14 = crop(I, ORIGIN, x13)
    x15 = vconcat(x14, x11)
    return x15
