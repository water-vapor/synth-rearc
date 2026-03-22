from arc2.core import *


def verify_963c33f8(I: Grid) -> Grid:
    x0 = len(I)
    x1 = len(I[ZERO])
    x2 = next(
        j for j in range(x1 - 2)
        if all(I[i][j + k] == NINE for i in (ZERO, ONE) for k in range(3))
        and all(I[TWO][j + k] in (ONE, NINE) for k in range(3))
    )
    x3 = tuple(I[TWO][x2 + k] for k in range(3))
    x4 = fill(I, SEVEN, frozenset((i, j) for i in range(3) for j in range(x2, x2 + 3)))
    x5 = [list(row) for row in x4]
    x6 = []
    for x7, x8 in enumerate(range(x2, x2 + 3)):
        x9 = [NINE, NINE, x3[x7]]
        x10 = x8
        if x3[x7] == ONE:
            x11 = next((i for i in range(3, x0) if I[i][x8] == FIVE), None)
            x12 = x0 - 3 if x11 is None else x11 - 3
        else:
            if (
                x7 == TWO
                and x8 + ONE < x1
                and I[x0 - 3][x8 + ONE] == FIVE
                and I[x0 - 2][x8 + ONE] == FIVE
                and not (I[x0 - 3][x8] == FIVE and I[x0 - 2][x8] == FIVE)
            ):
                x10 = x8 + ONE
            if (
                x7 == ZERO
                and x8 - ONE >= ZERO
                and I[x0 - 3][x8 - ONE] == FIVE
                and I[x0 - 2][x8 - ONE] == FIVE
                and not (I[x0 - 3][x8] == FIVE and I[x0 - 2][x8] == FIVE)
            ):
                x10 = x8 - ONE
            x12 = x0 - 3
            x6.append(x10)
        for x13, x14 in enumerate(x9):
            x5[x12 + x13][x10] = x14
    x15 = x0 - ONE
    x16 = x0 - 3
    for x17 in x6:
        if x5[x16][x17] != NINE or I[x15][x17] != FIVE:
            continue
        x18 = x17
        while x18 - ONE >= ZERO and I[x15][x18 - ONE] == FIVE:
            x18 -= ONE
        x19 = x17
        while x19 + ONE < x1 and I[x15][x19 + ONE] == FIVE:
            x19 += ONE
        x20 = x19 - x18 + ONE
        if x17 == x18 and x20 >= FIVE and x17 - TWO in x6:
            for x21 in range(x17 + ONE, min(x17 + 3, x1)):
                if x5[x15][x21] == FIVE:
                    x5[x15][x21] = SEVEN
    return tuple(tuple(row) for row in x5)
