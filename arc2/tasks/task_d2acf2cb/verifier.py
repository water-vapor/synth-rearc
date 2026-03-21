from arc2.core import *


def verify_d2acf2cb(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = decrement(x0)
    x3 = decrement(x1)
    x4 = interval(ZERO, x0, ONE)
    x5 = interval(ZERO, x1, ONE)
    x6 = tuple(
        x7 for x7 in x4
        if both(equality(I[x7][ZERO], FOUR), equality(I[x7][x3], FOUR))
    )
    x7 = tuple(
        x8 for x8 in x5
        if both(equality(I[ZERO][x8], FOUR), equality(I[x2][x8], FOUR))
    )
    x8 = I
    for x9 in x6:
        x10 = frozenset((x9, x11) for x11 in interval(ONE, x3, ONE))
        x12 = intersection(ofcolor(x8, ZERO), x10)
        x13 = intersection(ofcolor(x8, EIGHT), x10)
        x14 = intersection(ofcolor(x8, SIX), x10)
        x15 = intersection(ofcolor(x8, SEVEN), x10)
        x16 = fill(x8, EIGHT, x12)
        x17 = fill(x16, ZERO, x13)
        x18 = fill(x17, SEVEN, x14)
        x8 = fill(x18, SIX, x15)
    for x19 in x7:
        x20 = frozenset((x21, x19) for x21 in interval(ONE, x2, ONE))
        x22 = intersection(ofcolor(x8, ZERO), x20)
        x23 = intersection(ofcolor(x8, EIGHT), x20)
        x24 = intersection(ofcolor(x8, SIX), x20)
        x25 = intersection(ofcolor(x8, SEVEN), x20)
        x26 = fill(x8, EIGHT, x22)
        x27 = fill(x26, ZERO, x23)
        x28 = fill(x27, SEVEN, x24)
        x8 = fill(x28, SIX, x25)
    return x8
