from arc2.core import *


def verify_5ffb2104(I: Grid) -> Grid:
    x0 = list(objects(I, T, F, T))
    x1 = T
    x2 = astuple(ZERO, ONE)
    x3 = decrement(width(I))
    while x1:
        x1 = F
        x4 = frozenset()
        for x5 in x0:
            x4 = combine(x4, toindices(x5))
        x6 = []
        for x7 in x0:
            x8 = toindices(x7)
            x9 = difference(x4, x8)
            x10 = shift(x7, x2)
            x11 = toindices(x10)
            x12 = rightmost(x7) < x3
            x13 = intersection(difference(x11, x8), x9)
            x14 = both(x12, equality(size(x13), ZERO))
            if x14:
                x6.append(x10)
                x1 = T
            else:
                x6.append(x7)
        x0 = x6
    x15 = canvas(ZERO, shape(I))
    for x16 in x0:
        x15 = paint(x15, x16)
    return x15
