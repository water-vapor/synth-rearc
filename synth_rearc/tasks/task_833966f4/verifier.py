from synth_rearc.core import *


def verify_833966f4(I: Grid) -> Grid:
    x0 = crop(I, ORIGIN, (TWO, ONE))
    x1 = rot180(x0)
    x2 = crop(I, (TWO, ZERO), UNITY)
    x3 = crop(I, (THREE, ZERO), (TWO, ONE))
    x4 = rot180(x3)
    x5 = vconcat(x1, x2)
    x6 = vconcat(x5, x4)
    return x6
