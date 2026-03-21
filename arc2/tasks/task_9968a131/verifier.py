from arc2.core import *


def verify_9968a131(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = tuple(tuple(j for j, x2 in enumerate(x3) if x2 != x0) for x3 in I)
    x2 = tuple((i, x4) for i, x4 in enumerate(x1) if len(x4) == TWO)
    x3 = first(x2)
    x4 = x3[0]
    x5 = x3[1]
    x6 = tuple(I[x4][x7] for x7 in x5)
    x7 = x6[::-1]
    x8 = width(I)
    x9 = []
    for x10, x11 in enumerate(I):
        x12 = x1[x10]
        if len(x12) != TWO or x12 != x5:
            x9.append(x11)
            continue
        x13 = tuple(x11[x14] for x14 in x12)
        x14 = first(x12)
        x15 = increment(last(x12))
        if x13 == x7 and x15 < x8 and x11[x15] == x0:
            x16 = list(x11)
            x16[x14] = x0
            x16[increment(x14)] = x13[0]
            x16[x15] = x13[1]
            x9.append(tuple(x16))
        else:
            x9.append(x11)
    x17 = tuple(x9)
    return x17
