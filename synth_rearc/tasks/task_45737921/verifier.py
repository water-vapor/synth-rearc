from synth_rearc.core import *


def verify_45737921(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = canvas(ZERO, shape(I))
    x2 = x1
    for x3 in x0:
        x4 = palette(x3)
        x5 = minimum(x4)
        x6 = other(x4, x5)
        x7 = frozenset((branch(equality(x8, x5), x6, x5), x9) for x8, x9 in x3)
        x2 = paint(x2, x7)
    return x2
