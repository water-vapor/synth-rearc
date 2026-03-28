from synth_rearc.core import *


def verify_414297c0(I: Grid) -> Grid:
    x0 = objects(I, F, T, T)
    x1 = argmax(x0, size)
    x2 = subgrid(x1, I)
    x3 = mostcolor(x2)
    x4 = difference(palette(x2), initset(x3))
    x5 = difference(x0, initset(x1))
    x6 = x2
    for x7 in x5:
        x8 = difference(palette(x7), initset(TWO))
        x9 = intersection(x8, x4)
        if len(x9) != ONE:
            continue
        x10 = first(x9)
        x11 = sfilter(x7, matcher(first, x10))
        x12 = toindices(x11)
        if len(x12) != ONE:
            continue
        x13 = first(x12)
        x14 = sfilter(x7, matcher(first, TWO))
        x15 = toindices(x14)
        x16 = shift(x15, invert(x13))
        x17 = ofcolor(x2, x10)
        for x18 in x17:
            x19 = shift(x16, x18)
            x6 = fill(x6, TWO, x19)
    return x6
