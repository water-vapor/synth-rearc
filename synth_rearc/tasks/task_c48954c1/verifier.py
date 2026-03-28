from synth_rearc.core import *


def verify_c48954c1(I: Grid) -> Grid:
    x0 = vmirror(I)
    x1 = hconcat(x0, I)
    x2 = hconcat(x1, x0)
    x3 = hmirror(x2)
    x4 = vconcat(x3, x2)
    x5 = vconcat(x4, x3)
    return x5
