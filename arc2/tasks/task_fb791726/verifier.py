from arc2.core import *


def verify_fb791726(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = shape(I)
    x3 = canvas(ZERO, x2)
    x4 = hconcat(I, x3)
    x5 = hconcat(x3, I)
    x6 = vconcat(x4, x5)
    x7 = astuple(ONE, x1)
    x8 = interval(ZERO, subtract(x0, TWO), ONE)
    x9 = interval(ZERO, double(x1), ONE)
    x10 = x6
    for x11 in x8:
        x12 = crop(I, astuple(x11, ZERO), x7)
        x13 = increment(x11)
        x14 = crop(I, astuple(x13, ZERO), x7)
        x15 = increment(x13)
        x16 = crop(I, astuple(x15, ZERO), x7)
        x17 = equality(colorcount(x12, ZERO), x1)
        x18 = equality(colorcount(x14, ZERO), x1)
        x19 = equality(colorcount(x16, ZERO), x1)
        x20 = flip(x17)
        x21 = flip(x19)
        x22 = both(x20, both(x18, x21))
        if x22:
            x23 = product(initset(x13), x9)
            x24 = fill(x10, THREE, x23)
            x25 = add(x13, x0)
            x26 = product(initset(x25), x9)
            x10 = fill(x24, THREE, x26)
    return x10
