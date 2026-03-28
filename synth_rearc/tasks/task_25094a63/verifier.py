from synth_rearc.core import *


def verify_25094a63(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = [[ZERO for _ in range(x1)] for _ in range(x0)]
    for x3 in range(x0):
        x2[x3][x1 - ONE] = ONE
        for x4 in range(x1 - TWO, -ONE, -ONE):
            x5 = equality(I[x3][x4], I[x3][x4 + ONE])
            x2[x3][x4] = increment(x2[x3][x4 + ONE]) if x5 else ONE
    x6 = [[ZERO for _ in range(x1 + ONE)] for _ in range(x0 + ONE)]
    for x7 in range(x0):
        for x8 in range(x1):
            x9 = x2[x7][x8]
            if not greater(x9, THREE):
                continue
            x10 = I[x7][x8]
            for x11 in range(x7, x0):
                if x10 != I[x11][x8]:
                    break
                x9 = min(x9, x2[x11][x8])
                if not greater(x9, THREE):
                    break
                x12 = x11 - x7 + ONE
                if greater(x12, THREE):
                    x6[x7][x8] += ONE
                    x6[x11 + ONE][x8] -= ONE
                    x6[x7][x8 + x9] -= ONE
                    x6[x11 + ONE][x8 + x9] += ONE
    x13 = set()
    for x14 in range(x0):
        for x15 in range(x1):
            x16 = x6[x14][x15]
            if x14 > ZERO:
                x16 += x6[x14 - ONE][x15]
            if x15 > ZERO:
                x16 += x6[x14][x15 - ONE]
            if x14 > ZERO and x15 > ZERO:
                x16 -= x6[x14 - ONE][x15 - ONE]
            x6[x14][x15] = x16
            if positive(x16):
                x13.add((x14, x15))
    x17 = fill(I, FOUR, frozenset(x13))
    return x17
