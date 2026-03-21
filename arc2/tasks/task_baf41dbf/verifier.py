from arc2.core import *


def verify_baf41dbf(
    I: Grid,
) -> Grid:
    x0 = ofcolor(I, THREE)
    x1 = ulcorner(x0)
    x2 = lrcorner(x0)
    x3 = x1[ZERO]
    x4 = x1[ONE]
    x5 = x2[ZERO]
    x6 = x2[ONE]
    x7 = tuple(
        x8
        for x8 in range(x3, increment(x5))
        if all(I[x8][x9] == THREE for x9 in range(x4, increment(x6)))
    )
    x8 = tuple(
        x9
        for x9 in range(x4, increment(x6))
        if all(I[x10][x9] == THREE for x10 in range(x3, increment(x5)))
    )
    x9 = tuple(x10 for x10 in x7 if x10 != x3 and x10 != x5)
    x10 = tuple(x11 for x11 in x8 if x11 != x4 and x11 != x6)
    x11 = ofcolor(I, SIX)
    x12 = tuple(x13[ZERO] for x13 in x11 if x13[ZERO] < x3)
    x13 = tuple(x14[ZERO] for x14 in x11 if x14[ZERO] > x5)
    x14 = tuple(x15[ONE] for x15 in x11 if x15[ONE] < x4)
    x15 = tuple(x16[ONE] for x16 in x11 if x16[ONE] > x6)
    x16 = minimum(x12) + ONE if len(x12) > ZERO else x3
    x17 = maximum(x13) - ONE if len(x13) > ZERO else x5
    x18 = minimum(x14) + ONE if len(x14) > ZERO else x4
    x19 = maximum(x15) - ONE if len(x15) > ZERO else x6
    x20 = fill(I, ZERO, x0)
    x21 = (x16,) + x9 + (x17,)
    x22 = (x18,) + x10 + (x19,)
    x23 = x20
    for x24 in x21:
        x25 = connect((x24, x18), (x24, x19))
        x23 = fill(x23, THREE, x25)
    for x26 in x22:
        x27 = connect((x16, x26), (x17, x26))
        x23 = fill(x23, THREE, x27)
    return x23
