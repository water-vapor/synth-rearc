from synth_rearc.core import *


def verify_31d5ba1a(I: Grid) -> Grid:
    x0 = tophalf(I)
    x1 = bottomhalf(I)
    x2 = replace(x0, NINE, FOUR)
    x3 = cellwise(x2, x1, SIX)
    x4 = replace(x3, FOUR, ZERO)
    return x4
