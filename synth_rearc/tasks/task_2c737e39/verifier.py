from synth_rearc.core import *


def verify_2c737e39(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = argmax(x0, size)
    x2 = ofcolor(I, FIVE)
    x3 = sfilter(x1, matcher(first, FIVE))
    x4 = equality(size(x3), ZERO)
    x5 = compose(rbind(adjacent, x1), initset)
    x6 = sfilter(x2, x5)
    x7 = branch(x4, x6, toindices(x3))
    x8 = first(x7)
    x9 = other(x2, x8)
    x10 = subtract(x9, x8)
    x11 = difference(x1, x3)
    x12 = shift(x11, x10)
    x13 = fill(I, ZERO, initset(x9))
    x14 = paint(x13, x12)
    return x14
