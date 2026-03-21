from arc2.core import *


def verify_9f41bd9c(I: Grid) -> Grid:
    x0 = ofcolor(I, FIVE)
    x1 = ofcolor(I, SIX)
    x2 = fill(I, ONE, x0)
    x3 = uppermost(x0)
    x4 = uppermost(x1)
    x5 = add(x3, TWO)
    x6 = subtract(x4, x5)
    x7 = width(I)
    x8 = subtract(x7, FIVE)
    x9 = equality(leftmost(x0), ZERO)
    if x9:
        x10 = x2
        for x11 in range(x3, x5):
            x12 = frozenset((x11, x13) for x13 in range(x8, x7))
            x10 = fill(x10, FIVE, x12)
        for x11 in range(x6):
            x12 = add(x5, x11)
            x13 = subtract(x8, x11)
            x14 = frozenset((x12, x15) for x15 in range(x13, add(x13, FIVE), TWO))
            x10 = fill(x10, FIVE, x14)
        x15 = subtract(add(x8, FOUR), x6)
        x16 = frozenset((x4, x17) for x17 in range(add(x15, ONE)))
        x17 = fill(x10, NINE, x16)
        return x17
    x10 = x2
    for x11 in range(x3, x5):
        x12 = frozenset((x11, x13) for x13 in range(FIVE))
        x10 = fill(x10, FIVE, x12)
    for x11 in range(x6):
        x12 = add(x5, x11)
        x13 = frozenset((x12, x14) for x14 in range(x11, add(x11, FIVE), TWO))
        x10 = fill(x10, FIVE, x13)
    x14 = frozenset((x4, x15) for x15 in range(x6, x7))
    x15 = fill(x10, NINE, x14)
    return x15
