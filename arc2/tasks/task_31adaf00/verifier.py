from arc2.core import *


def verify_31adaf00(
    I: Grid,
) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = minimum((x0, x1))
    x3 = []
    for x4 in interval(TWO, increment(x2), ONE):
        x5 = multiply(x4, x4)
        x6 = increment(subtract(x0, x4))
        x7 = increment(subtract(x1, x4))
        for x8 in interval(ZERO, x6, ONE):
            for x9 in interval(ZERO, x7, ONE):
                x10 = product(interval(x8, add(x8, x4), ONE), interval(x9, add(x9, x4), ONE))
                x11 = crop(I, (x8, x9), (x4, x4))
                if equality(colorcount(x11, ZERO), x5):
                    x3.append((x5, x10))
    x12 = sorted(x3, key=lambda x: (-x[0], uppermost(x[1]), leftmost(x[1])))
    x13 = frozenset()
    for _, x14 in x12:
        if size(intersection(x13, x14)) != ZERO:
            continue
        x13 = combine(x13, x14)
    x15 = fill(I, ONE, x13)
    return x15
