from synth_rearc.core import *


def verify_310f3251(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = difference(asindices(I), ofcolor(I, ZERO))
    x3 = frozenset((((x4 - ONE) % x0), ((x5 - ONE) % x1)) for x4, x5 in x2)
    x4 = recolor(TWO, x3)
    x5 = underpaint(I, x4)
    x6 = hconcat(hconcat(x5, x5), x5)
    x7 = vconcat(vconcat(x6, x6), x6)
    return x7
