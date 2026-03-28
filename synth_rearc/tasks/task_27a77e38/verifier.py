from synth_rearc.core import *


def verify_27a77e38(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = remove(FIVE, x0)
    x2 = remove(ZERO, x1)
    x3 = lbind(colorcount, I)
    x4 = argmax(x2, x3)
    x5 = height(I)
    x6 = decrement(x5)
    x7 = width(I)
    x8 = halve(x7)
    x9 = astuple(x6, x8)
    x10 = initset(x9)
    x11 = fill(I, x4, x10)
    return x11
