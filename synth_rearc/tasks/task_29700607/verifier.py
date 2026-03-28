from synth_rearc.core import *


def verify_29700607(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = sfilter(x1, matcher(uppermost, ZERO))
    x3 = order(x2, leftmost)
    x4 = decrement(height(I))
    x5 = canvas(x0, shape(I))
    for x6 in x3:
        x7 = color(x6)
        x8 = first(toindices(x6))
        x9 = remove(x8, ofcolor(I, x7))
        if equality(size(x9), ZERO):
            x10 = astuple(x4, last(x8))
        else:
            x10 = first(x9)
        x11 = astuple(first(x10), last(x8))
        x12 = connect(x8, x11)
        x13 = connect(x11, x10)
        x14 = combine(x12, x13)
        x15 = recolor(x7, x14)
        x5 = paint(x5, x15)
    return x5
