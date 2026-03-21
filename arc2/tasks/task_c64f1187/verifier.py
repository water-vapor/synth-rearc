from arc2.core import *


def verify_c64f1187(I: Grid) -> Grid:
    x0 = order(objects(I, F, F, T), lambda x: (uppermost(x), leftmost(x)))
    x1 = sfilter(x0, lambda x: contained(FIVE, palette(x)))
    x2 = minimum(apply(uppermost, x1))
    x3 = minimum(apply(leftmost, x1))
    x4 = maximum(apply(lowermost, x1))
    x5 = maximum(apply(rightmost, x1))
    x6 = astuple(x2, x3)
    x7 = astuple(x4 - x2 + ONE, x5 - x3 + ONE)
    x8 = canvas(ZERO, x7)
    x9 = colorfilter(objects(I, T, F, T), ONE)
    x10 = {}
    for x11 in x9:
        x12 = index(I, subtract(ulcorner(x11), UNITY))
        x13 = subgrid(x11, I)
        x10[x12] = x13
    x14 = x8
    for x15 in x1:
        x16 = palette(x15)
        if size(x16) == ONE:
            continue
        x17 = other(x16, FIVE)
        x18 = replace(x10[x17], ONE, x17)
        x19 = shift(asobject(x18), subtract(ulcorner(x15), x6))
        x14 = paint(x14, x19)
    return x14
