from arc2.core import *


def verify_9b30e358(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = ofcolor(I, x0)
    x2 = asindices(I)
    x3 = difference(x2, x1)
    x4 = uppermost(x3)
    x5 = astuple(x4, ZERO)
    x6 = astuple(subtract(height(I), x4), width(I))
    x7 = crop(I, x5, x6)
    x8 = height(x7)
    x9 = tophalf(x7)
    x10 = bottomhalf(x7)
    x11 = vconcat(x10, x9)
    x12 = branch(even(x8), x11, x7)
    x13 = height(I)
    x14 = divide(x13, x8)
    x15 = merge(repeat(x12, x14))
    x16 = subtract(x13, multiply(x14, x8))
    x17 = astuple(x16, width(I))
    x18 = crop(x12, ORIGIN, x17)
    x19 = vconcat(x15, x18)
    return x19
