from arc2.core import *


def verify_182e5d0f(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, THREE)
    x2 = colorfilter(x0, FIVE)
    x3 = I
    for x4 in x1:
        x5 = toindices(x4)
        x6 = tuple(
            x7 for x7 in x5 if equality(size(intersection(dneighbors(x7), x5)), ONE)
        )
        x8 = []
        for x9 in x6:
            x10 = first(intersection(dneighbors(x9), x5))
            x11 = subtract(x10, x9)
            if equality(x11[0], ZERO):
                x12 = toivec(ONE)
            else:
                x12 = tojvec(ONE)
            x13 = add(x9, x12)
            x14 = subtract(x9, x12)
            x15 = both(equality(index(I, x13), ZERO), equality(index(I, x14), ZERO))
            if x15:
                x8.append((x9, x10))
        x16 = tuple(x17 for x17 in x2 if adjacent(x4, x17))
        if len(x8) == ONE and positive(size(x16)):
            x18, x19 = x8[ZERO]
            x3 = cover(x3, x4)
            for x20 in x16:
                x3 = cover(x3, x20)
            x3 = fill(x3, THREE, initset(x18))
            x3 = fill(x3, FIVE, initset(x19))
    return x3
