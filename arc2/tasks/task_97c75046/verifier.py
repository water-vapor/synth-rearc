from arc2.core import *


def verify_97c75046(I: Grid) -> Grid:
    x0 = ofcolor(I, ZERO)
    x1 = first(ofcolor(I, FIVE))
    x2 = initset(x1)
    x3 = gravitate(x2, x0)
    x4 = shift(x2, x3)
    x5 = first(x4)
    x6 = (NEG_UNITY, UP_RIGHT, DOWN_LEFT, UNITY)
    x7 = manhattan(x4, x2)
    x8 = x5
    for x9 in x6:
        x10 = add(x5, x9)
        x11 = index(I, x10)
        x12 = x11 is not None and x11 != ZERO
        x13 = adjacent(initset(x10), x0) if x12 else F
        x14 = manhattan(initset(x10), x2) if x12 else ZERO
        x15 = both(x13, greater(x14, x7))
        if x15:
            x16 = x5
            x17 = x7
            while True:
                x18 = add(x16, x9)
                x19 = index(I, x18)
                x20 = x19 is not None and x19 != ZERO
                x21 = adjacent(initset(x18), x0) if x20 else F
                x22 = manhattan(initset(x18), x2) if x20 else ZERO
                x23 = both(x21, greater(x22, x17))
                if flip(x23):
                    break
                x16 = x18
                x17 = x22
            x8 = x16
            break
    x24 = mostcolor(I)
    x25 = fill(I, x24, x2)
    x26 = fill(x25, FIVE, initset(x8))
    return x26
