from synth_rearc.core import *


def verify_0c786b71(I: Grid) -> Grid:
    x0 = vmirror(I)
    x1 = hconcat(x0, I)
    x2 = hmirror(x1)
    x3 = vconcat(x2, x1)
    return x3
