from synth_rearc.core import *


def verify_f3cdc58f(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = canvas(ZERO, astuple(x0, x1))
    x3 = colorcount(I, ONE)
    x4 = colorcount(I, TWO)
    x5 = colorcount(I, THREE)
    x6 = colorcount(I, FOUR)
    x7 = interval(subtract(x0, x3), x0, ONE)
    x8 = interval(subtract(x0, x4), x0, ONE)
    x9 = interval(subtract(x0, x5), x0, ONE)
    x10 = interval(subtract(x0, x6), x0, ONE)
    x11 = product(x7, (ZERO,))
    x12 = product(x8, (ONE,))
    x13 = product(x9, (TWO,))
    x14 = product(x10, (THREE,))
    x15 = fill(x2, ONE, x11)
    x16 = fill(x15, TWO, x12)
    x17 = fill(x16, THREE, x13)
    x18 = fill(x17, FOUR, x14)
    return x18
