from arc2.core import *


def verify_84ba50d3(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, ONE)
    x2 = first(colorfilter(x0, TWO))
    x3 = uppermost(x2)
    x4 = mostcolor(I)
    x5 = decrement(height(I))
    x6 = fill(I, x4, merge(x1))
    for x7 in x1:
        x8 = {}
        x9 = set()
        for _, (x10, x11) in x7:
            x8[x10] = increment(x8.get(x10, ZERO))
            x9.add(x11)
        x12 = max(x8.values())
        if equality(x12, ONE):
            x13 = subtract(x5, lowermost(x7))
            x14 = frozenset((x3, x15) for x15 in x9)
            x6 = fill(x6, x4, x14)
        else:
            x13 = subtract(decrement(x3), max(x16 for x16, x17 in x8.items() if equality(x17, x12)))
        x18 = shift(x7, toivec(x13))
        x6 = paint(x6, x18)
    return x6
