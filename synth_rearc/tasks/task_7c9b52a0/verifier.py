from synth_rearc.core import *


def verify_7c9b52a0(
    I: Grid,
) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = first(x0)
    x2 = canvas(ZERO, shape(x1))
    x3 = order(x0, lambda x4: (uppermost(x4), leftmost(x4)))
    x4 = x2
    for x5 in x3:
        x6 = subgrid(x5, I)
        x7 = palette(x6)
        x8 = difference(x7, frozenset({ZERO}))
        x9 = first(x8)
        x10 = ofcolor(x6, x9)
        x4 = fill(x4, x9, x10)
    return x4
