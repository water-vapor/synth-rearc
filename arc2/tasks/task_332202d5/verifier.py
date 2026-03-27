from arc2.core import *


def verify_332202d5(I: Grid) -> Grid:
    x0 = leftmost(ofcolor(I, ONE))
    x1 = tuple(sorted(i for i, j in ofcolor(I, ONE) if j == x0))
    x2 = {x3: other(I[x3], ONE) for x3 in x1}
    x3 = height(I)
    x4 = width(I)
    x5 = []
    for x6 in range(x3):
        x7 = [ONE] * x4
        if contained(x6, x1):
            x7[x0] = EIGHT
            x5.append(tuple(x7))
            continue
        x8 = tuple(abs(x6 - x9) for x9 in x1)
        x9 = min(x8)
        x10 = tuple(x2[x11] for x11, x12 in zip(x1, x8) if x12 == x9)
        x11 = set(x10)
        if len(x11) == ONE:
            x12 = next(iter(x11))
            x7 = [x12] * x4
            x7[x0] = ONE
        x5.append(tuple(x7))
    x13 = tuple(x5)
    return x13
