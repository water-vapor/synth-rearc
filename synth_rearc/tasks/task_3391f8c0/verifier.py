from synth_rearc.core import *


def verify_3391f8c0(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, T, T)
    x2 = remove(x0, palette(I))
    x3 = first(x2)
    x4 = other(x2, x3)
    x5 = colorfilter(x1, x3)
    x6 = colorfilter(x1, x4)
    x7 = normalize(first(x5))
    x8 = normalize(first(x6))
    x9 = lambda x: shift(x8, ulcorner(x))
    x10 = lambda x: shift(x7, ulcorner(x))
    x11 = mapply(x9, x5)
    x12 = mapply(x10, x6)
    x13 = combine(x11, x12)
    x14 = canvas(x0, shape(I))
    x15 = paint(x14, x13)
    return x15
