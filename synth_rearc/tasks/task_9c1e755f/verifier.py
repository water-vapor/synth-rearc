from synth_rearc.core import *


def verify_9c1e755f(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, FIVE)
    x2 = tuple(x3 for x3 in x1 if either(hline(x3), vline(x3)))
    x3 = I
    if len(x2) == ZERO:
        return x3
    x4 = argmax(x2, size)
    if vline(x4):
        x5 = leftmost(x4)
        x6 = uppermost(x4)
        x7 = lowermost(x4)
        x8 = tuple(range(x6, increment(x7)))
        x9 = tuple(
            x10
            for x10 in x8
            if (
                (x5 > ZERO and I[x10][decrement(x5)] != ZERO)
                or (x5 < decrement(width(I)) and I[x10][increment(x5)] != ZERO)
            )
        )
        if len(x9) > ZERO:
            x10 = any(x5 > ZERO and I[x11][decrement(x5)] != ZERO for x11 in x9)
            x11 = len(x9)
            for x12, x13 in enumerate(x8):
                x14 = x9[x12 % x11]
                for x15, x16 in enumerate(I[x14]):
                    if x16 != ZERO:
                        x3 = fill(x3, x16, initset((x13, x15)))
            if x10:
                x17 = x5 + TWO
                x18 = decrement(width(I))
                for x19 in x8:
                    x20 = tuple(
                        (x21, x22)
                        for x21, x22 in enumerate(I[x19])
                        if both(greater(x22, ZERO), greater(x21, x5))
                    )
                    if len(x20) == ONE:
                        x23 = x20[ZERO][ONE]
                        x24 = connect((x19, x17), (x19, x18))
                        x3 = fill(x3, x23, x24)
            else:
                x17 = ZERO
                x18 = x5 - TWO
                for x19 in x8:
                    x20 = tuple(
                        (x21, x22)
                        for x21, x22 in enumerate(I[x19])
                        if both(greater(x22, ZERO), greater(x5, x21))
                    )
                    if len(x20) == ONE:
                        x23 = x20[ZERO][ONE]
                        x24 = connect((x19, x17), (x19, x18))
                        x3 = fill(x3, x23, x24)
    for x25 in x2:
        if not hline(x25):
            continue
        x26 = uppermost(x25)
        x27 = leftmost(x25)
        x28 = rightmost(x25)
        for x29 in range(height(I)):
            if x29 == x26:
                continue
            x30 = I[x29][x27]
            x31 = I[x29][x28]
            x32 = x30 if x30 != ZERO else x31 if x31 != ZERO else None
            if x32 is None:
                continue
            x33 = connect((x29, x27), (x29, x28))
            x3 = fill(x3, x32, x33)
    return x3
