from arc2.core import *


def verify_8618d23e(I: Grid) -> Grid:
    x0 = vsplit(I, TWO)
    x1 = first(x0)
    x2 = last(x0)
    x3 = height(x1)
    x4 = width(x1)
    x5 = canvas(NINE, astuple(x3, ONE))
    x6 = hconcat(x1, x5)
    x7 = hconcat(x5, x2)
    x8 = canvas(NINE, astuple(ONE, increment(x4)))
    x9 = vconcat(x6, x8)
    x10 = vconcat(x9, x7)
    return x10
