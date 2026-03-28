from synth_rearc.core import *


def verify_7953d61e(I: Grid) -> Grid:
    x0 = rot270(I)
    x1 = rot180(I)
    x2 = rot90(I)
    x3 = hconcat(I, x0)
    x4 = hconcat(x1, x2)
    x5 = vconcat(x3, x4)
    return x5
