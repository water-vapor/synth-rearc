from synth_rearc.core import *


def verify_7e0986d6(I: Grid) -> Grid:
    x0 = shape(I)
    x1, x2 = x0
    x3 = mostcolor(I)
    x4 = palette(I)
    x5 = remove(x3, x4)
    x6 = argmax(x5, lbind(colorcount, I))
    x7 = ofcolor(I, x3)
    x8 = difference(asindices(I), x7)
    x9 = tuple(
        tuple(ONE if (i, j) in x8 else ZERO for j in range(x2))
        for i in range(x1)
    )
    x10 = [[ZERO] * (x2 + ONE) for _ in range(x1 + ONE)]
    for i in range(x1):
        x11 = ZERO
        for j in range(x2):
            x11 += x9[i][j]
            x10[i + ONE][j + ONE] = x10[i][j + ONE] + x11
    x12 = []
    for i0 in range(x1):
        for j0 in range(x2):
            if x9[i0][j0] == ZERO:
                continue
            for i1 in range(i0 + ONE, x1):
                for j1 in range(j0 + ONE, x2):
                    x13 = x10[i1 + ONE][j1 + ONE] - x10[i0][j1 + ONE] - x10[i1 + ONE][j0] + x10[i0][j0]
                    x14 = (i1 - i0 + ONE) * (j1 - j0 + ONE)
                    if x13 == x14:
                        x12.append((i0, j0, i1, j1, x14))
    x15 = order(x12, lambda x: -last(x))
    x16 = []
    for i0, j0, i1, j1, x17 in x15:
        x18 = any(
            i0 >= a and j0 >= b and i1 <= c and j1 <= d
            for a, b, c, d, _ in x16
        )
        if x18:
            continue
        x16.append((i0, j0, i1, j1, x17))
    x19 = canvas(x3, x0)
    for i0, j0, i1, j1, _ in x16:
        x20 = backdrop(frozenset({(i0, j0), (i1, j1)}))
        x19 = fill(x19, x6, x20)
    return x19
