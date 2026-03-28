from arc2.core import *


def verify_5ad8a7c0(I: Grid) -> Grid:
    x0 = []
    for x1, x2 in enumerate(I):
        x3 = tuple(x4 for x4, x5 in enumerate(x2) if equality(x5, TWO))
        if equality(len(x3), TWO):
            x0.append((x1, x3[ZERO], x3[ONE], subtract(x3[ONE], x3[ZERO])))
    x4 = tuple(x5[THREE] for x5 in x0)
    x5 = minimum(x4)
    x6 = I
    for x7, x8, x9, x10 in x0:
        if equality(x10, x5):
            x11 = connect((x7, x8), (x7, x9))
            x6 = fill(x6, TWO, x11)
    return x6
