from synth_rearc.core import *


def verify_e57337a4(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = vsplit(I, THREE)
    x2 = tuple(hsplit(x3, THREE) for x3 in x1)
    x3 = tuple(
        tuple(branch(greater(colorcount(x4, ZERO), ZERO), ZERO, x0) for x4 in x5)
        for x5 in x2
    )
    return x3
