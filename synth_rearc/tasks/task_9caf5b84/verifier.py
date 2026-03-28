from synth_rearc.core import *


def verify_9caf5b84(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = lbind(colorcount, I)
    x2 = order(x0, x1)
    x3 = last(x2)
    x4 = remove(x3, x2)
    x5 = last(x4)
    x6 = remove(x3, x0)
    x7 = remove(x5, x6)
    x8 = lbind(ofcolor, I)
    x9 = mapply(x8, x7)
    x10 = fill(I, SEVEN, x9)
    return x10
