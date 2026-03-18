from arc2.core import *


def verify_fc10701f(I: Grid) -> Grid:
    x0 = ofcolor(I, NINE)
    x1 = ofcolor(I, SEVEN)
    x2 = ofcolor(I, ZERO)
    x3 = replace(I, NINE, SEVEN)
    x4 = fill(x3, SIX, x1)
    x5 = apply(first, x0)
    x6 = apply(last, x0)
    x7 = apply(first, x2)
    x8 = apply(last, x2)
    x9 = vmatching(x0, x1)
    x10 = interval(increment(minimum((lowermost(x0), lowermost(x1)))), maximum((uppermost(x0), uppermost(x1))), ONE)
    x11 = sfilter(x7, rbind(contained, x10))
    x12 = product(x11, x6)
    x13 = interval(increment(minimum((rightmost(x0), rightmost(x1)))), maximum((leftmost(x0), leftmost(x1))), ONE)
    x14 = sfilter(x8, rbind(contained, x13))
    x15 = product(x5, x14)
    x16 = branch(x9, x12, x15)
    x17 = fill(x4, TWO, x16)
    return x17
