from synth_rearc.core import *


def verify_412b6263(I: Grid) -> Grid:
    x0 = rot270(I)
    x1 = height(x0)
    x2 = canvas(ONE, (x1, ONE))
    x3 = hconcat(x2, x0)
    x4 = hconcat(x3, x2)
    x5 = width(x4)
    x6 = canvas(ONE, (ONE, x5))
    x7 = fill(x6, SEVEN, initset(ORIGIN))
    x8 = decrement(x5)
    x9 = fill(x7, SEVEN, initset((ZERO, x8)))
    x10 = vconcat(x9, x4)
    x11 = vconcat(x10, x9)
    x12 = vconcat(x11, x4)
    x13 = vconcat(x12, x9)
    return x13
