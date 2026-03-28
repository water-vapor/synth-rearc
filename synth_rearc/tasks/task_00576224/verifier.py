from synth_rearc.core import *


def verify_00576224(I: Grid) -> Grid:
    x0 = hconcat(I, I)
    x1 = hconcat(x0, I)
    x2 = vmirror(x1)
    x3 = vconcat(x1, x2)
    x4 = vconcat(x3, x1)
    return x4
