from synth_rearc.core import *


def verify_3ad05f52(I: Grid) -> Grid:
    x0 = ofcolor(I, EIGHT)
    x1 = uppermost(x0)
    x2 = lowermost(x0)
    x3 = leftmost(x0)
    x4 = rightmost(x0)
    x5 = other(remove(EIGHT, palette(I)), ZERO)
    x6 = [list(row) for row in I]

    def bounded_h(i: Integer, j: Integer) -> Boolean:
        x7 = any(I[i][k] == EIGHT for k in range(x3, j))
        x8 = any(I[i][k] == EIGHT for k in range(j + ONE, x4 + ONE))
        return x7 and x8

    def bounded_v(i: Integer, j: Integer) -> Boolean:
        x7 = any(I[k][j] == EIGHT for k in range(x1, i))
        x8 = any(I[k][j] == EIGHT for k in range(i + ONE, x2 + ONE))
        return x7 and x8

    x7 = True
    while x7:
        x7 = False

        for x8 in range(x1, x2 + ONE):
            x9 = [x10 for x10 in range(x3, x4 + ONE) if x6[x8][x10] == x5]
            for x10, x11 in zip(x9, x9[ONE:]):
                if all(I[x8][x12] != EIGHT for x12 in range(x10, x11 + ONE)):
                    for x12 in range(x10, x11 + ONE):
                        if x6[x8][x12] != x5:
                            x6[x8][x12] = x5
                            x7 = True

        for x8 in range(x3, x4 + ONE):
            x9 = [x10 for x10 in range(x1, x2 + ONE) if x6[x10][x8] == x5]
            for x10, x11 in zip(x9, x9[ONE:]):
                if all(I[x12][x8] != EIGHT for x12 in range(x10, x11 + ONE)):
                    for x12 in range(x10, x11 + ONE):
                        if x6[x12][x8] != x5:
                            x6[x12][x8] = x5
                            x7 = True

        x8 = [
            (i, j)
            for i in range(x1, x2 + ONE)
            for j in range(x3, x4 + ONE)
            if x6[i][j] == x5
        ]
        for x9, x10 in x8:
            if x9 in (x1, x2) and bounded_h(x9, x10):
                x11 = x9 - ONE
                while x11 >= x1 and I[x11][x10] != EIGHT and bounded_h(x11, x10):
                    if x6[x11][x10] != x5:
                        x6[x11][x10] = x5
                        x7 = True
                    x11 -= ONE
                x11 = x9 + ONE
                while x11 <= x2 and I[x11][x10] != EIGHT and bounded_h(x11, x10):
                    if x6[x11][x10] != x5:
                        x6[x11][x10] = x5
                        x7 = True
                    x11 += ONE

            if x10 in (x3, x4) and bounded_v(x9, x10):
                x11 = x10 - ONE
                while x11 >= x3 and I[x9][x11] != EIGHT and bounded_v(x9, x11):
                    if x6[x9][x11] != x5:
                        x6[x9][x11] = x5
                        x7 = True
                    x11 -= ONE
                x11 = x10 + ONE
                while x11 <= x4 and I[x9][x11] != EIGHT and bounded_v(x9, x11):
                    if x6[x9][x11] != x5:
                        x6[x9][x11] = x5
                        x7 = True
                    x11 += ONE

        for x8 in range(x1, x2 + ONE):
            for x9 in range(x3 + ONE, x4):
                if (
                    I[x8][x9] == ZERO
                    and I[x8][x9 - ONE] == EIGHT
                    and I[x8][x9 + ONE] == EIGHT
                    and (
                        (x8 > x1 and x6[x8 - ONE][x9] == x5)
                        or (x8 < x2 and x6[x8 + ONE][x9] == x5)
                    )
                ):
                    if x6[x8][x9] != x5:
                        x6[x8][x9] = x5
                        x7 = True

        for x8 in range(x1 + ONE, x2):
            for x9 in range(x3, x4 + ONE):
                if (
                    I[x8][x9] == ZERO
                    and I[x8 - ONE][x9] == EIGHT
                    and I[x8 + ONE][x9] == EIGHT
                    and (
                        (x9 > x3 and x6[x8][x9 - ONE] == x5)
                        or (x9 < x4 and x6[x8][x9 + ONE] == x5)
                    )
                ):
                    if x6[x8][x9] != x5:
                        x6[x8][x9] = x5
                        x7 = True

        for x8 in range(x1, x2 + ONE):
            x9 = [x10 for x10 in range(x3, x4 + ONE) if I[x8][x10] == EIGHT]
            for x10, x11 in zip(x9, x9[ONE:]):
                if x11 - x10 <= ONE:
                    continue
                if any(x6[x8][x12] == x5 for x12 in range(x10 + ONE, x11)):
                    for x12 in range(x10 + ONE, x11):
                        if x6[x8][x12] != x5:
                            x6[x8][x12] = x5
                            x7 = True

        for x8 in range(x3, x4 + ONE):
            x9 = [x10 for x10 in range(x1, x2 + ONE) if I[x10][x8] == EIGHT]
            for x10, x11 in zip(x9, x9[ONE:]):
                if x11 - x10 <= ONE:
                    continue
                if any(x6[x12][x8] == x5 for x12 in range(x10 + ONE, x11)):
                    for x12 in range(x10 + ONE, x11):
                        if x6[x12][x8] != x5:
                            x6[x12][x8] = x5
                            x7 = True

        for x8, x9 in ((x1, x1 + ONE), (x2, x2 - ONE)):
            x10 = [x11 for x11 in range(x3, x4 + ONE) if I[x8][x11] == EIGHT]
            for x11, x12 in zip(x10, x10[ONE:]):
                if x12 - x11 <= ONE:
                    continue
                if all(x6[x9][x13] == x5 for x13 in range(x11 + ONE, x12)):
                    for x13 in range(x11 + ONE, x12):
                        if I[x8][x13] != EIGHT and x6[x8][x13] != x5:
                            x6[x8][x13] = x5
                            x7 = True

        for x8, x9 in ((x3, x3 + ONE), (x4, x4 - ONE)):
            x10 = [x11 for x11 in range(x1, x2 + ONE) if I[x11][x8] == EIGHT]
            for x11, x12 in zip(x10, x10[ONE:]):
                if x12 - x11 <= ONE:
                    continue
                if all(x6[x13][x9] == x5 for x13 in range(x11 + ONE, x12)):
                    for x13 in range(x11 + ONE, x12):
                        if I[x13][x8] != EIGHT and x6[x13][x8] != x5:
                            x6[x13][x8] = x5
                            x7 = True

    return tuple(tuple(row) for row in x6)
