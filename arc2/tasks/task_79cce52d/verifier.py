from arc2.core import *


def verify_79cce52d(I: Grid) -> Grid:
    x0 = ofcolor(I, TWO)
    x1 = extract(x0, matcher(first, ZERO))
    x2 = extract(x0, matcher(last, ZERO))
    x3 = last(x1)
    x4 = first(x2)
    x5 = crop(I, UNITY, (SIX, SIX))
    x6 = subtract(SEVEN, x4)
    x7 = subtract(SIX, x6)
    x8 = crop(x5, (x6, ZERO), (x7, SIX))
    x9 = crop(x5, ORIGIN, (x6, SIX))
    x10 = vconcat(x8, x9)
    x11 = subtract(SEVEN, x3)
    x12 = subtract(SIX, x11)
    x13 = crop(x10, (ZERO, x11), (SIX, x12))
    x14 = crop(x10, ORIGIN, (SIX, x11))
    x15 = hconcat(x13, x14)
    return x15
