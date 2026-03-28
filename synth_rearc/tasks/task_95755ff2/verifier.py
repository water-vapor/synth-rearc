from synth_rearc.core import *


def verify_95755ff2(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = [list(x3) for x3 in I]
    x3 = tuple(tuple(x4 for x4, x5 in enumerate(x6) if x5 == TWO) for x6 in I)
    x4 = tuple((x5[ZERO], x5[-ONE]) for x5 in x3)
    x5 = tuple(tuple(x6 for x6 in range(x0) if I[x6][x7] == TWO) for x7 in range(x1))
    x6 = tuple((x7[ZERO], x7[-ONE]) for x7 in x5)
    x7 = I[ZERO]
    x8 = I[-ONE]
    for x9, x10 in enumerate(x7):
        if x10 not in (ZERO, TWO):
            x11, x12 = x6[x9]
            for x13 in range(x11 + ONE, x12):
                if x2[x13][x9] != ZERO:
                    break
                x2[x13][x9] = x10
    for x14, x15 in enumerate(x8):
        if x15 not in (ZERO, TWO):
            x16, x17 = x6[x14]
            for x18 in range(x17 - ONE, x16, -ONE):
                if x2[x18][x14] != ZERO:
                    break
                x2[x18][x14] = x15
    for x19, x20 in enumerate(I):
        x21 = x20[ZERO]
        if x21 not in (ZERO, TWO):
            x22, x23 = x4[x19]
            for x24 in range(x22 + ONE, x23):
                if x2[x19][x24] != ZERO:
                    break
                x2[x19][x24] = x21
        x25 = x20[-ONE]
        if x25 not in (ZERO, TWO):
            x26, x27 = x4[x19]
            for x28 in range(x27 - ONE, x26, -ONE):
                if x2[x19][x28] != ZERO:
                    break
                x2[x19][x28] = x25
    return tuple(tuple(x29) for x29 in x2)
