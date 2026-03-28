from synth_rearc.core import *


def verify_15113be4(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = difference(x0, frozenset({ZERO, ONE, FOUR}))
    x2 = first(x1)
    x3 = objects(I, T, T, F)
    x4 = colorfilter(x3, x2)
    x5 = merge(x4)
    x6 = subgrid(x5, I)
    x7 = downscale(x6, TWO)
    x8 = ofcolor(x7, x2)
    x9 = I
    for i in interval(ZERO, 23, FOUR):
        for j in interval(ZERO, 23, FOUR):
            x10 = crop(I, (i, j), THREE_BY_THREE)
            x11 = ofcolor(x10, ONE)
            if x8.issubset(x11):
                x12 = shift(x8, (i, j))
                x9 = fill(x9, x2, x12)
    return x9
