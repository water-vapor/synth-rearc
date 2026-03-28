from synth_rearc.core import *


def verify_95a58926(I: Grid) -> Grid:
    x0 = remove(ZERO, palette(I))
    x1 = other(x0, FIVE)
    x2 = height(I)
    x3 = width(I)
    x4 = tuple(i for i in range(x2) if ZERO not in I[i])
    x5 = tuple(j for j in range(x3) if all(I[i][j] != ZERO for i in range(x2)))
    x6 = canvas(ZERO, shape(I))
    x7 = x6
    for x8 in x4:
        x9 = product(initset(x8), interval(ZERO, x3, ONE))
        x7 = fill(x7, FIVE, x9)
    for x10 in x5:
        x11 = product(interval(ZERO, x2, ONE), initset(x10))
        x7 = fill(x7, FIVE, x11)
    x12 = product(x4, x5)
    x13 = fill(x7, x1, x12)
    return x13
