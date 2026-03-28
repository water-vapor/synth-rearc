from synth_rearc.core import *


def verify_1da012fc(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = argmax(x0, size)
    x2 = matcher(first, FIVE)
    x3 = rbind(sfilter, x2)
    x4 = x3(x1)
    x5 = difference(x1, x4)
    x6 = order(x5, last)
    x7 = apply(first, x6)
    x8 = cover(I, x1)
    x9 = objects(x8, T, T, T)
    x10 = order(x9, ulcorner)
    x11 = papply(recolor, x7, x10)
    x12 = merge(x11)
    x13 = paint(I, x12)
    return x13
