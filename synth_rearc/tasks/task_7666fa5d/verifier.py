from synth_rearc.core import *


def verify_7666fa5d(
    I: Grid,
) -> Grid:
    x0 = tuple(
        sorted(
            objects(I, T, T, T),
            key=lambda x1: (uppermost(x1), lowermost(x1), leftmost(x1)),
        )
    )
    x1 = []
    for x2 in x0:
        x3 = uppermost(x2)
        x4 = lowermost(x2)
        x5 = add(x3, rightmost(x2))
        x6 = subtract(x3, rightmost(x2))
        x7 = subtract(x4, leftmost(x2))
        x1.append((x3, x4, x5, x6, x7))
    x2 = []
    x3 = []
    x4 = NEG_ONE
    for x5 in x1:
        x6, x7, x8, x9, x10 = x5
        if both(len(x3) > ZERO, x6 > x4):
            x2.append(tuple(sorted(x3, key=lambda x11: x11[TWO])))
            x3 = []
        x3.append(x5)
        x4 = max(x4, x7)
    if len(x3) > ZERO:
        x2.append(tuple(sorted(x3, key=lambda x11: x11[TWO])))
    x5 = set()
    for x6 in x2:
        x7 = tuple(x8[THREE] for x8 in x6)
        x8 = tuple(x9[FOUR] for x9 in x6)
        x9 = []
        x10 = []
        x11 = 99
        x12 = -99
        for x13, x14 in zip(x7, x8):
            x11 = min(x11, x13)
            x12 = max(x12, x14)
            x9.append(x11)
            x10.append(x12)
        x13 = [99] * len(x6)
        x14 = [-99] * len(x6)
        x15 = 99
        x16 = -99
        for x17 in range(decrement(len(x6)), NEG_ONE, NEG_ONE):
            x18 = x7[x17]
            x19 = x8[x17]
            x15 = min(x15, x18)
            x16 = max(x16, x19)
            x13[x17] = x15
            x14[x17] = x16
        for x17 in range(decrement(len(x6))):
            x18 = x6[x17][TWO]
            x19 = x6[increment(x17)][TWO]
            x20 = max(x9[x17], x13[increment(x17)])
            x21 = min(x10[x17], x14[increment(x17)])
            if x20 > x21:
                continue
            for x22 in range(increment(x18), increment(x19)):
                for x23 in range(x20, increment(x21)):
                    if (x22 + x23) % TWO != ZERO:
                        continue
                    x24 = divide(add(x22, x23), TWO)
                    x25 = divide(subtract(x22, x23), TWO)
                    if 0 <= x24 < len(I) and 0 <= x25 < len(first(I)):
                        x5.add((x24, x25))
    return underfill(I, TWO, frozenset(x5))
