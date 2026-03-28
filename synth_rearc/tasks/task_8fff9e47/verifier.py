from synth_rearc.core import *


def verify_8fff9e47(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = tuple(I[i][j] for i in interval(ZERO, x0, TWO) for j in interval(ZERO, x1, TWO))
    x3 = tuple(I[i][j] for i in interval(ZERO, x0, TWO) for j in interval(ONE, x1, TWO))
    x4 = tuple(I[i][j] for i in interval(ONE, x0, TWO) for j in interval(ZERO, x1, TWO))
    x5 = tuple(I[i][j] for i in interval(ONE, x0, TWO) for j in interval(ONE, x1, TWO))
    x6 = tuple(reversed(x2))
    x7 = tuple(reversed(x3))
    x8 = tuple(reversed(x4))
    x9 = tuple(reversed(x5))
    x10 = len(x6)
    x11 = decrement(x10)
    x12 = interval(ZERO, x10, ONE)
    x13 = tuple(tuple(x6[min(i, j)] for j in x12) for i in x12)
    x14 = tuple(tuple(x7[min(i, subtract(x11, j))] for j in x12) for i in x12)
    x15 = tuple(tuple(x8[min(subtract(x11, i), j)] for j in x12) for i in x12)
    x16 = tuple(
        tuple(x9[min(subtract(x11, i), subtract(x11, j))] for j in x12)
        for i in x12
    )
    x17 = hconcat(x13, x14)
    x18 = hconcat(x15, x16)
    x19 = vconcat(x17, x18)
    return x19
