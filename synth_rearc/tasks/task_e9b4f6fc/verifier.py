from synth_rearc.core import *


def verify_e9b4f6fc(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = argmax(x0, size)
    x2 = subgrid(x1, I)
    x3 = remove(x1, x0)
    x4 = sizefilter(x3, TWO)
    x5 = order(x4, ulcorner)
    x6 = x2
    for x7 in x5:
        x8 = ulcorner(x7)
        x9 = lrcorner(x7)
        x10 = index(I, x8)
        x11 = index(I, x9)
        x6 = replace(x6, x11, x10)
    return x6
