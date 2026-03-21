from arc2.core import *


def verify_d6542281(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, F, T, T)
    x2 = objects(I, T, T, T)
    x3 = tuple(x4 for x4 in x1 if greater(numcolors(x4), ONE))
    x4 = I
    for x5 in x3:
        x6 = tuple(palette(x5))
        x7 = {}
        x8 = tuple()
        for x9 in x6:
            x10 = sfilter(x5, matcher(first, x9))
            x11 = normalize(x10)
            x12 = tuple(
                x13 for x13 in x2
                if both(equality(color(x13), x9), equality(normalize(x13), x11))
            )
            x13 = tuple(x14 for x14 in x12 if toindices(x14) != toindices(x10))
            if len(x13) > ZERO:
                x7[x9] = x13
                x8 = combine(x8, (x10,))
        x9 = tuple(x7.keys())
        if len(x9) == ZERO:
            continue
        for x10 in x6:
            x11 = sfilter(x5, matcher(first, x10))
            if both(equality(size(x11), ONE), flip(contained(x10, x9))):
                x4 = fill(x4, x0, x11)
        for x10 in x8:
            x11 = ulcorner(x10)
            x12 = color(x10)
            x13 = x7[x12]
            for x14 in x13:
                x15 = subtract(ulcorner(x14), x11)
                x16 = shift(x5, x15)
                x4 = paint(x4, x16)
    return x4
