from synth_rearc.core import *


def verify_45a5af55(I: Grid) -> Grid:
    x0 = height(I)
    x1 = decrement(x0)
    x2 = double(x1)
    x3 = canvas(ZERO, astuple(x2, x2))
    for x4 in interval(ZERO, x1, ONE):
        x5 = index(I, astuple(x4, ZERO))
        x6 = decrement(subtract(x2, x4))
        x7 = box(frozenset({astuple(x4, x4), astuple(x6, x6)}))
        x3 = fill(x3, x5, x7)
    return x3
