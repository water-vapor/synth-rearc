from synth_rearc.core import *


def verify_3d6c6e23(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = canvas(ZERO, (x0, x1))
    for x3 in range(x1):
        x4 = tuple((x5, I[x5][x3]) for x5 in range(x0) if I[x5][x3] != ZERO)
        if len(x4) == ZERO:
            continue
        x6 = []
        for _, x7 in x4:
            if x7 not in x6:
                x6.append(x7)
        x8 = tuple(x6)
        x9 = tuple(sum(ONE for _, x10 in x4 if x10 == x11) for x11 in x8)
        x12 = ZERO
        x13 = ONE
        x14 = []
        while x12 < len(x4):
            x14.append(x13)
            x12 += x13
            x13 += TWO
        x15 = len(x14)
        x16 = x0 - x15
        x17 = ZERO
        for x18, x19 in zip(x8, x9):
            x20 = x19
            while x20 > ZERO:
                x21 = x14[x17]
                x22 = x16 + x17
                x23 = connect((x22, x3 - x17), (x22, x3 + x17))
                x2 = fill(x2, x18, x23)
                x20 -= x21
                x17 += ONE
    return x2
