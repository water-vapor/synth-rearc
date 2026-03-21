from arc2.core import *


def verify_aaecdb9a(I: Grid) -> Grid:
    x0 = objects(I, T, T, T)
    x1 = size(colorfilter(x0, FIVE))
    x2 = size(colorfilter(x0, TWO))
    x3 = size(colorfilter(x0, EIGHT))
    x4 = size(colorfilter(x0, NINE))
    x5 = size(colorfilter(x0, SIX))
    x6 = (x1, x2, x3, x4, x5)
    x7 = maximum(x6)
    x8 = canvas(SEVEN, astuple(x7, FIVE))
    x9 = interval(subtract(x7, x1), x7, ONE)
    x10 = product(x9, initset(ZERO))
    x11 = fill(x8, FIVE, x10)
    x12 = interval(subtract(x7, x2), x7, ONE)
    x13 = product(x12, initset(ONE))
    x14 = fill(x11, TWO, x13)
    x15 = interval(subtract(x7, x3), x7, ONE)
    x16 = product(x15, initset(TWO))
    x17 = fill(x14, EIGHT, x16)
    x18 = interval(subtract(x7, x4), x7, ONE)
    x19 = product(x18, initset(THREE))
    x20 = fill(x17, NINE, x19)
    x21 = interval(subtract(x7, x5), x7, ONE)
    x22 = product(x21, initset(FOUR))
    x23 = fill(x20, SIX, x22)
    return x23
