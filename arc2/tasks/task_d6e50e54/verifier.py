from arc2.core import *


def verify_d6e50e54(I: Grid) -> Grid:
    x0 = ofcolor(I, ONE)
    x1 = ulcorner(x0)
    x2 = lrcorner(x0)
    x3 = x1[ZERO]
    x4 = x1[ONE]
    x5 = x2[ZERO]
    x6 = x2[ONE]
    x7 = height(x0)
    x8 = width(x0)
    x9 = canvas(SEVEN, shape(I))
    x10 = fill(x9, TWO, x0)
    x11 = ofcolor(I, NINE)
    x12 = frozenset()
    for x13, x14 in x11:
        x15 = x3 <= x13 <= x5
        if x15:
            x16 = x14 < x4
            x17 = x4 - x14 if x16 else x14 - x6
            x18 = x4 if x16 else x6
            x19 = decrement(x4) if x16 else increment(x6)
            x20 = x18 if x17 < x8 else x19
            x21 = (x13, x20)
        else:
            x22 = x13 < x3
            x23 = x3 - x13 if x22 else x13 - x5
            x24 = x3 if x22 else x5
            x25 = decrement(x3) if x22 else increment(x5)
            x26 = x24 if x23 < x7 else x25
            x21 = (x26, x14)
        x12 = insert(x21, x12)
    x27 = fill(x10, NINE, x12)
    return x27
