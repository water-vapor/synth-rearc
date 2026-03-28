from synth_rearc.core import *


def verify_18419cfa(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, EIGHT)
    x2 = I
    for x3 in x1:
        x4 = delta(x3)
        x5 = subgrid(x4, I)
        x6 = ofcolor(x5, TWO)
        x7 = ofcolor(vmirror(x5), TWO)
        x8 = ofcolor(hmirror(x5), TWO)
        x9 = ofcolor(hmirror(vmirror(x5)), TWO)
        x10 = combine(x6, x7)
        x11 = combine(x8, x9)
        x12 = combine(x10, x11)
        x13 = ulcorner(x4)
        x14 = shift(x12, x13)
        x2 = fill(x2, TWO, x14)
    return x2
