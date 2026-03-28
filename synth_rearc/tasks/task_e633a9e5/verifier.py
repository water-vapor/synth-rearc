from synth_rearc.core import *


def verify_e633a9e5(I: Grid) -> Grid:
    x0 = tophalf(I)
    x1 = crop(I, DOWN, astuple(ONE, THREE))
    x2 = bottomhalf(I)
    x3 = vconcat(x0, x0)
    x4 = vconcat(x3, x1)
    x5 = vconcat(x4, x2)
    x6 = vconcat(x5, x2)
    x7 = lefthalf(x6)
    x8 = crop(x6, RIGHT, astuple(FIVE, ONE))
    x9 = righthalf(x6)
    x10 = hconcat(x7, x7)
    x11 = hconcat(x10, x8)
    x12 = hconcat(x11, x9)
    x13 = hconcat(x12, x9)
    return x13
