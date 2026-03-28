from synth_rearc.core import *


def verify_bc4146bd(I: Grid) -> Grid:
    x0 = vmirror(I)
    x1 = hconcat(I, x0)
    x2 = hconcat(x1, I)
    x3 = hconcat(x2, x0)
    x4 = hconcat(x3, I)
    return x4
