from arc2.core import *


def verify_c6141b15(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, T, T)
    x2 = tuple(x3 for x3 in palette(I) if x3 != x0)
    x3 = extract(x2, lambda x4: equality(size(colorfilter(x1, x4)), ONE))
    x4 = other(x2, x3)
    x5 = extract(x1, matcher(color, x3))
    x6 = colorfilter(x1, x4)
    x7 = toindices(x5)
    x8 = tuple(
        x9 for x9 in x7 if equality(size(intersection(neighbors(x9), x7)), ONE)
    )
    x9 = normalize(first(x6))
    x10 = centerofmass(x9)
    x11 = recolor(x4, x9)
    x12 = tuple(centerofmass(x13) for x13 in x6)
    x13 = frozenset()
    for x14 in x12:
        for x15 in x12:
            if x14 < x15:
                x13 = combine(x13, connect(x14, x15))
    x16 = canvas(x0, shape(I))
    x17 = fill(x16, x3, x13)
    for x18 in x8:
        x19 = shift(x11, subtract(x18, x10))
        x17 = paint(x17, x19)
    return x17
