from synth_rearc.core import *


def verify_17b80ad2(I: Grid) -> Grid:
    x0 = width(I)
    x1 = hsplit(I, x0)
    x2 = []
    for x3 in x1:
        x4 = height(x3)
        x5 = subtract(x4, ONE)
        x6 = index(x3, (x5, ZERO))
        if x6 != FIVE:
            x2.append(x3)
            continue
        x7 = []
        x8 = FIVE
        for x9 in range(x5, NEG_ONE, NEG_ONE):
            x10 = index(x3, (x9, ZERO))
            if x10 != ZERO:
                x8 = x10
            x7.append((x8,))
        x11 = tuple(reversed(x7))
        x2.append(x11)
    x12 = x2[ZERO]
    for x13 in x2[ONE:]:
        x12 = hconcat(x12, x13)
    return x12
