from synth_rearc.core import *


def verify_33b52de3(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = argmax(x0, numcolors)
    x2 = remove(x1, x0)
    x3 = subgrid(x1, I)
    x4 = asobject(x3)
    x5 = order(x4, last)
    x6 = apply(first, x5)
    x7 = order(x2, ulcorner)
    x8 = pair(x6, x7)
    x9 = fork(recolor, first, last)
    x10 = apply(x9, x8)
    x11 = merge(x2)
    x12 = fill(I, ZERO, x11)
    x13 = merge(x10)
    x14 = paint(x12, x13)
    return x14
