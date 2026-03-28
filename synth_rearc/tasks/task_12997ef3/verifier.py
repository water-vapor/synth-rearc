from synth_rearc.core import *


def verify_12997ef3(I: Grid) -> Grid:
    x0 = ofcolor(I, ONE)
    x1 = crop(I, ulcorner(x0), shape(x0))
    x2 = mostcolor(I)
    x3 = ofcolor(I, x2)
    x4 = combine(x0, x3)
    x5 = difference(asindices(I), x4)
    x6 = equality(height(x5), ONE)
    x7 = branch(x6, last, first)
    x8 = order(x5, x7)
    x9 = tuple(replace(x1, ONE, index(I, x10)) for x10 in x8)
    x11 = first(x9)
    for x12 in x9[ONE:]:
        x11 = branch(x6, hconcat(x11, x12), vconcat(x11, x12))
    return x11
