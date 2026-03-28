from synth_rearc.core import *


def verify_d4b1c2b1(I: Grid) -> Grid:
    x0 = numcolors(I)
    x1 = upscale(I, x0)
    return x1
