from arc2.core import *


def verify_cf133acc(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = {}
    for x3 in range(x0):
        for x4 in range(ONE, subtract(x1, ONE)):
            x5 = index(I, (x3, x4))
            if flip(equality(x5, ZERO)):
                continue
            x6 = index(I, (x3, decrement(x4)))
            x7 = index(I, (x3, increment(x4)))
            x8 = both(flip(equality(x6, ZERO)), equality(x6, x7))
            if x8:
                x2.setdefault(x4, []).append((x3, x6))
    x9 = I
    for x10, x11 in x2.items():
        x12 = tuple(sorted(x11))
        x13 = ZERO
        for x14, x15 in x12:
            x16 = connect((x13, x10), (x14, x10))
            x9 = fill(x9, x15, x16)
            x13 = increment(x14)
        x17 = tuple(
            index(I, (x18, x10))
            for x18 in range(x13, x0)
            if flip(equality(index(I, (x18, x10)), ZERO))
        )
        x19 = x12[-ONE][ONE] if equality(len(x17), ZERO) else first(x17)
        x20 = connect((x13, x10), (decrement(x0), x10))
        x9 = fill(x9, x19, x20)
    return x9
