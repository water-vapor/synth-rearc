from arc2.core import *

from .helpers import landing_to_anchor_f28a3cbb


def verify_f28a3cbb(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = sizefilter(x1, NINE)
    x3 = argmin(x2, uppermost)
    x4 = argmax(x2, lowermost)
    x5 = toindices(x3)
    x6 = toindices(x4)
    x7 = color(x3)
    x8 = color(x4)
    x9 = ofcolor(I, x7)
    x10 = ofcolor(I, x8)
    x11 = difference(x9, x5)
    x12 = difference(x10, x6)
    x13 = rbind(landing_to_anchor_f28a3cbb, x3)
    x14 = rbind(landing_to_anchor_f28a3cbb, x4)
    x15 = apply(x13, x11)
    x16 = apply(x14, x12)
    x17 = combine(x5, x15)
    x18 = combine(x6, x16)
    x19 = canvas(x0, shape(I))
    x20 = fill(x19, x7, x17)
    x21 = fill(x20, x8, x18)
    return x21
