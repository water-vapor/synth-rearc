from synth_rearc.core import *


def verify_332efdb3(I: Grid) -> Grid:
    x0 = shape(I)
    x1 = canvas(ONE, x0)
    x2 = height(I)
    x3 = width(I)
    x4 = interval(ONE, x2, TWO)
    x5 = interval(ONE, x3, TWO)
    x6 = product(x4, x5)
    x7 = fill(x1, ZERO, x6)
    return x7
