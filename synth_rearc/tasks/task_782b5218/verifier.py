from synth_rearc.core import *


def verify_782b5218(I: Grid) -> Grid:
    x0 = ofcolor(I, TWO)
    x1 = palette(I)
    x2 = remove(TWO, x1)
    x3 = other(x2, ZERO)
    x4 = width(I)
    x5 = height(I)
    x6 = tuple(
        max(i for i, j in x0 if j == k) if any(j == k for _, j in x0) else None
        for k in range(x4)
    )
    x7 = frozenset(
        (i, j)
        for j, x8 in enumerate(x6)
        if x8 is not None
        for i in range(x8 + ONE, x5)
    )
    x8 = canvas(ZERO, shape(I))
    x9 = fill(x8, x3, x7)
    x10 = fill(x9, TWO, x0)
    return x10
