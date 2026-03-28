from synth_rearc.core import *


def verify_d19f7514(I: Grid) -> Grid:
    x0 = tophalf(I)
    x1 = bottomhalf(I)
    x2 = replace(x0, THREE, FOUR)
    x3 = replace(x1, FIVE, FOUR)
    x4 = cellwise(x2, x3, FOUR)
    return x4
