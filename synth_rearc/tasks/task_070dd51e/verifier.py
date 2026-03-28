from synth_rearc.core import *


def verify_070dd51e(I: Grid) -> Grid:
    x0 = remove(ZERO, palette(I))
    x1 = ()
    for x2 in x0:
        x3 = totuple(ofcolor(I, x2))
        x4 = first(x3)
        x5 = last(x3)
        x6 = connect(x4, x5)
        x1 = x1 + ((x2, x6),)
    x7 = canvas(ZERO, shape(I))
    for x8, x9 in x1:
        if hline(x9):
            x7 = fill(x7, x8, x9)
    for x10, x11 in x1:
        if vline(x11):
            x7 = fill(x7, x10, x11)
    return x7
