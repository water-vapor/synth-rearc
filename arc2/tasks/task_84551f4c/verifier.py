from arc2.core import *


def verify_84551f4c(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = tuple(j for j in range(x1) if any(I[i][j] != ZERO for i in range(x0)))
    x3 = tuple(next(I[i][j] for i in range(x0) if I[i][j] != ZERO) for j in x2)
    x4 = tuple(sum(I[i][j] != ZERO for i in range(x0)) for j in x2)
    x5 = dict(zip(x2, x3))
    x6 = dict(zip(x2, x4))
    x7 = set()
    for x8, x9 in zip(x2, x3):
        if x9 != ONE:
            continue
        x10 = x8
        while x10 in x5:
            x7.add(x10)
            x11 = add(x10, x6[x10])
            if x11 not in x5:
                break
            x10 = x11
    x12 = canvas(ZERO, (x0, x1))
    x13 = x12
    for x14 in x2:
        if x14 in x7:
            continue
        x15 = frozenset((i, x14) for i in range(subtract(x0, x6[x14]), x0))
        x13 = fill(x13, x5[x14], x15)
    x16 = decrement(x0)
    x17 = x13
    for x18 in x2:
        if x18 not in x7:
            continue
        x19 = frozenset((x16, j) for j in range(x18, add(x18, x6[x18])))
        x17 = fill(x17, x5[x18], x19)
    return x17
