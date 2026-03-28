from synth_rearc.core import *


def verify_52fd389e(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = order(x0, ulcorner)
    x2 = I
    for x3 in x1:
        x4 = other(palette(x3), FOUR)
        x5 = colorcount(x3, x4)
        x6 = astuple(x5, x5)
        x7 = subtract(ulcorner(x3), x6)
        x8 = add(lrcorner(x3), x6)
        x9 = backdrop(frozenset({x7, x8}))
        x2 = fill(x2, x4, x9)
        x2 = paint(x2, x3)
    return x2
