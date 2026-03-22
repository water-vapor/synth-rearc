from arc2.core import *


def verify_80214e03(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = tuple(
        (color(x2), uppermost(x2), lowermost(x2), leftmost(x2), rightmost(x2), size(x2))
        for x2 in x0
    )
    x3 = []
    for x4 in x1:
        x5, x6, x7, x8, x9, x10 = x4
        x11 = F
        for x12 in x1:
            x13, x14, x15, x16, x17, x18 = x12
            if x12 == x4 or x13 != x5:
                continue
            x19 = x14 <= x6 and x7 <= x15 and x16 <= x8 and x9 <= x17
            x20 = (x14, x15, x16, x17) != (x6, x7, x8, x9)
            x21 = (x14, x15, x16, x17) == (x6, x7, x8, x9) and x18 > x10
            if x19 and (x20 or x21):
                x11 = T
                break
        if not x11:
            x3.append(x4)
    x22 = tuple(sorted({x23[1] for x23 in x3} | {x23[2] + ONE for x23 in x3}))
    x24 = tuple(sorted({x25[3] for x25 in x3} | {x25[4] + ONE for x25 in x3}))
    x26 = len(x22) - ONE
    x27 = len(x24) - ONE
    x28 = [list(x29) for x29 in canvas(ZERO, (x26, x27))]
    for x30 in range(x26):
        x31 = x22[x30]
        x32 = x22[x30 + ONE] - ONE
        for x33 in range(x27):
            x34 = x24[x33]
            x35 = x24[x33 + ONE] - ONE
            x36 = tuple(
                I[x37][x38]
                for x37 in range(x31, x32 + ONE)
                for x38 in range(x34, x35 + ONE)
                if I[x37][x38] != ZERO
            )
            if len(x36) == ZERO:
                continue
            x39 = mostcommon(x36)
            x28[x30][x27 - x33 - ONE] = x39
    return tuple(tuple(x40) for x40 in x28)
