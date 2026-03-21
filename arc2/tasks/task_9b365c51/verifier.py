from arc2.core import *


def verify_9b365c51(I: Grid) -> Grid:
    x0 = frontiers(I)
    x1 = sfilter(x0, vline)
    x2 = palette(I)
    x3 = remove(ZERO, x2)
    x4 = remove(EIGHT, x3)
    x5 = rbind(contained, x4)
    x6 = compose(x5, color)
    x7 = sfilter(x1, x6)
    x8 = order(x7, leftmost)
    x9 = apply(color, x8)
    x10 = height(I)
    x11 = width(I)
    x12 = canvas(ZERO, shape(I))
    x13 = tuple(tuple(i for i in range(x10) if I[i][j] == EIGHT) for j in range(x11))
    x14 = x12
    x15 = ZERO
    x16 = ZERO
    while x15 < x11:
        x17 = x13[x15]
        if len(x17) == ZERO:
            x15 = increment(x15)
            continue
        x18 = increment(x15)
        while x18 < x11 and x13[x18] == x17:
            x18 = increment(x18)
        x19 = product(x17, interval(x15, x18, ONE))
        x20 = x9[x16]
        x14 = fill(x14, x20, x19)
        x15 = x18
        x16 = increment(x16)
    return x14
