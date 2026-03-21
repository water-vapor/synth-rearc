from arc2.core import *


def verify_9caba7c3(I: Grid) -> Grid:
    x0 = interval(ZERO, THREE, ONE)
    x1 = frozenset(product(x0, x0))
    x2 = []
    x3 = len(I)
    x4 = len(I[0])
    for i in range(x3 - TWO):
        for j in range(x4 - TWO):
            x5 = crop(I, (i, j), THREE_BY_THREE)
            x6 = tuple(x5[a][b] for a in x0 for b in x0)
            if not all(v in (TWO, FIVE) for v in x6):
                continue
            if x5[ONE][ONE] != FIVE:
                continue
            x7 = frozenset((i + a, j + b) for a, b in x1 if I[i + a][j + b] == TWO)
            if len(x7) == ZERO:
                continue
            x2.append(((i, j), x7))
    x8 = tuple(loc for loc, reds in x2 if not any(reds < reds2 for _, reds2 in x2))
    x9 = I
    for i, j in x8:
        x10 = shift(x1, (i, j))
        x11 = frozenset((i + a, j + b) for a, b in x1 if I[i + a][j + b] == TWO)
        x12 = fill(x9, SEVEN, x10)
        x13 = fill(x12, TWO, x11)
        x9 = fill(x13, FOUR, frozenset({(i + ONE, j + ONE)}))
    return x9
