from arc2.core import *


def verify_e45ef808(I: Grid) -> Grid:
    x0 = ofcolor(I, SIX)
    x1 = ofcolor(I, ONE)
    x2 = uppermost(x0)
    x3 = lowermost(x1)
    x4 = sfilter(x0, matcher(first, x2))
    x5 = sfilter(x1, matcher(first, x3))
    x6 = rightmost(x4)
    x7 = rightmost(x5)
    x8 = sfilter(x1, matcher(last, x6))
    x9 = sfilter(x1, matcher(last, x7))
    x10 = fill(I, FOUR, x8)
    x11 = fill(x10, NINE, x9)
    return x11
