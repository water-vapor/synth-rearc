from arc2.core import *


def verify_bae5c565(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = shape(I)
    x2 = x1[0]
    x3 = x1[1]
    x4 = first(I)
    x5 = objects(I, T, F, T)
    x6 = colorfilter(x5, EIGHT)
    x7 = argmax(x6, height)
    x8 = uppermost(x7)
    x9 = leftmost(x7)
    x10 = tuple(EIGHT if equality(x11, x9) else x4[x11] for x11 in range(x3))
    x11 = canvas(x0, x1)
    x12 = frozenset()
    for x13 in range(x8, x2):
        x14 = subtract(x13, x8)
        x15 = max(ZERO, subtract(x9, x14))
        x16 = min(decrement(x3), add(x9, x14))
        x17 = frozenset((x10[x18], (x13, x18)) for x18 in range(x15, increment(x16)))
        x12 = combine(x12, x17)
    x19 = paint(x11, x12)
    return x19
