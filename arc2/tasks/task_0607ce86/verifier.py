from arc2.core import *


def verify_0607ce86(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = tuple(sum(v != ZERO for v in row) for row in I)
    x3 = tuple(i for i, x4 in enumerate(x2) if x4 > x1 // TWO)
    x4 = []
    x5 = x3[ZERO]
    x6 = x3[ZERO]
    for x7 in x3[ONE:]:
        if x7 == x6 + ONE:
            x6 = x7
        else:
            x4.append((x5, x6))
            x5 = x7
            x6 = x7
    x4.append((x5, x6))
    x8 = x4[ZERO][ONE] - x4[ZERO][ZERO] + ONE
    x9 = None
    x10 = None
    for x11 in (TWO, THREE, FOUR):
        x12 = x1 // x11
        for x13 in range(TWO, x12 + ONE):
            x14 = x11 * x13
            if x1 - x14 < TWO:
                continue
            x15 = ZERO
            x16 = ZERO
            x17 = ZERO
            x18 = []
            for x19 in range(x8):
                x20 = []
                for x21 in range(x13):
                    x22 = []
                    for x23, x24 in x4:
                        x25 = x23 + x19
                        for x26 in range(x11):
                            x27 = I[x25][x26 * x13 + x21]
                            x22.append(x27)
                    x22 = tuple(x22)
                    x28 = mostcommon(x22)
                    x29 = x22.count(x28)
                    x15 += x29
                    if x28 == ZERO:
                        x17 += ONE
                    else:
                        x16 += ONE
                    x20.append(x28)
                x18.append(tuple(x20))
            x30 = ZERO
            for x31, x32 in enumerate(I):
                for x33, x34 in enumerate(x32):
                    x35 = F
                    for x36, x37 in x4:
                        if x36 <= x31 < x36 + x8 and x33 < x14:
                            x35 = T
                            break
                    if (not x35) and x34 == ZERO:
                        x30 += ONE
            x38 = (x15, x16, -x17, x30, -x13)
            if x9 is None or x38 > x9:
                x9 = x38
                x10 = (x11, x13, tuple(x18))
    x39, x40, x41 = x10
    x42 = x41
    for _ in range(x39 - ONE):
        x42 = hconcat(x42, x41)
    x43 = canvas(ZERO, (x0, x1))
    x44 = asobject(x42)
    x45 = x43
    for x46, x47 in x4:
        x48 = shift(x44, (x46, ZERO))
        x45 = paint(x45, x48)
    return x45
