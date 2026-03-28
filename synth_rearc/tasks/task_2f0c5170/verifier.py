from synth_rearc.core import *


def verify_2f0c5170(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = rbind(colorcount, ZERO)
    x2 = fork(subtract, size, x1)
    x3 = matcher(x2, ONE)
    x4 = extract(x0, x3)
    x5 = other(x0, x4)
    x6 = leastcolor(x4)
    x7 = matcher(first, x6)
    x8 = sfilter(x4, x7)
    x9 = sfilter(x5, x7)
    x10 = compose(flip, matcher(first, ZERO))
    x11 = sfilter(x5, x10)
    x12 = subtract(ulcorner(x8), ulcorner(x9))
    x13 = shift(x11, x12)
    x14 = shift(x13, invert(ulcorner(x4)))
    x15 = canvas(ZERO, shape(x4))
    x16 = paint(x15, x14)
    return x16
