from arc2.core import *


def verify_c61be7dc(I: Grid) -> Grid:
    x0 = ofcolor(I, FIVE)
    x1 = frontiers(I)
    x2 = sfilter(x1, matcher(color, ZERO))
    x3 = sfilter(x2, vline)
    x4 = size(x0)
    x5 = halve(decrement(x4))
    x6 = divide(height(I), TWO)
    x7 = divide(width(I), TWO)
    x8 = canvas(mostcolor(I), shape(I))
    x9 = decrement(height(I))
    x10 = decrement(width(I))
    if equality(size(x3), TWO):
        x11 = decrement(x7)
        x12 = increment(x7)
        x13 = connect((ZERO, x11), (x9, x11))
        x14 = connect((ZERO, x12), (x9, x12))
        x15 = connect((x6, ZERO), (x6, x10))
        x16 = subtract(x6, x5)
        x17 = add(x6, x5)
        x18 = connect((x16, x7), (x17, x7))
    else:
        x11 = decrement(x6)
        x12 = increment(x6)
        x13 = connect((x11, ZERO), (x11, x10))
        x14 = connect((x12, ZERO), (x12, x10))
        x15 = connect((ZERO, x7), (x9, x7))
        x16 = subtract(x7, x5)
        x17 = add(x7, x5)
        x18 = connect((x6, x16), (x6, x17))
    x19 = fill(x8, ZERO, x13)
    x20 = fill(x19, ZERO, x14)
    x21 = fill(x20, ZERO, x15)
    x22 = fill(x21, FIVE, x18)
    return x22
