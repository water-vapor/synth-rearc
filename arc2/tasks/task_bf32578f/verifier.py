from arc2.core import *


def verify_bf32578f(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = other(x0, ZERO)
    x2 = ofcolor(I, x1)
    x3 = uppermost(x2)
    x4 = lowermost(x2)
    x5 = vmirror(x2)
    x6 = shift(x5, (ZERO, width(x2)))
    x7 = canvas(ZERO, shape(I))
    x8 = frozenset()
    for x9 in range(x3 + 1, x4):
        x10 = frozenset(x11 for x11 in x2 if x11[0] == x9)
        x12 = frozenset(x13 for x13 in x6 if x13[0] == x9)
        x14 = increment(rightmost(x10))
        x15 = decrement(leftmost(x12))
        x16 = connect((x9, x14), (x9, x15))
        x8 = combine(x8, x16)
    x17 = fill(x7, x1, x8)
    return x17
