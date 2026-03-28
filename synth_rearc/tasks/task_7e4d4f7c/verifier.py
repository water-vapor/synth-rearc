from synth_rearc.core import *


def verify_7e4d4f7c(I: Grid) -> Grid:
    x0 = width(I)
    x1 = crop(I, ORIGIN, (ONE, x0))
    x2 = crop(I, DOWN, (ONE, x0))
    x3 = crop(x2, RIGHT, (ONE, subtract(x0, ONE)))
    x4 = first(palette(x3))
    x5 = other(palette(x1), x4)
    x6 = replace(x1, x5, SIX)
    x7 = vconcat(x1, x2)
    x8 = vconcat(x7, x6)
    return x8
