from synth_rearc.core import *


def verify_8597cfd7(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, FIVE)
    x2 = merge(x1)
    x3 = uppermost(x2)
    x4 = width(I)
    x5 = astuple(x3, x4)
    x6 = crop(I, ORIGIN, x5)
    x7 = increment(x3)
    x8 = height(I)
    x9 = subtract(x8, x7)
    x10 = astuple(x9, x4)
    x11 = astuple(x7, ZERO)
    x12 = crop(I, x11, x10)
    x13 = colorcount(x6, TWO)
    x14 = colorcount(x12, TWO)
    x15 = subtract(x14, x13)
    x16 = colorcount(x6, FOUR)
    x17 = colorcount(x12, FOUR)
    x18 = subtract(x17, x16)
    x19 = greater(x15, x18)
    x20 = branch(x19, TWO, FOUR)
    x21 = canvas(x20, TWO_BY_TWO)
    return x21
