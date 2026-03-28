from arc2.core import *


def verify_42918530(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = interval(ZERO, x0, ONE)
    x3 = interval(ZERO, x1, ONE)
    x4 = lambda i: any(I[i][j] != ZERO for j in x3)
    x5 = lambda j: any(I[i][j] != ZERO for i in x2)
    x6 = tuple(i for i in x2 if x4(i) and (i == ZERO or not x4(decrement(i))))
    x7 = tuple(j for j in x3 if x5(j) and (j == ZERO or not x5(decrement(j))))
    x8 = {}
    for x9 in x6:
        for x10 in x7:
            x11 = crop(I, (x9, x10), (FIVE, FIVE))
            x12 = next(v for row in x11 for v in row if v != ZERO)
            x13 = frozenset(
                (i, j)
                for i in range(ONE, FOUR)
                for j in range(ONE, FOUR)
                if x11[i][j] != ZERO
            )
            if x13:
                x8[x12] = x13
    x14 = I
    for x15 in x6:
        for x16 in x7:
            x17 = crop(I, (x15, x16), (FIVE, FIVE))
            x18 = next(v for row in x17 for v in row if v != ZERO)
            x19 = frozenset(
                (i, j)
                for i in range(ONE, FOUR)
                for j in range(ONE, FOUR)
                if x17[i][j] != ZERO
            )
            if len(x19) == ZERO and x18 in x8:
                x20 = frozenset(add((x15, x16), x21) for x21 in x8[x18])
                x14 = fill(x14, x18, x20)
    return x14
