from synth_rearc.core import *


def verify_99306f82(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, ONE)
    x2 = argmax(x1, size)
    x3 = order(difference(x0, x1), uppermost)
    x4 = tuple(color(x5) for x5 in x3)
    x6 = backdrop(inbox(x2))
    x7 = I
    for x8 in x4[:-ONE]:
        x9 = box(x6)
        x7 = fill(x7, x8, x9)
        x6 = backdrop(inbox(x6))
    x10 = last(x4)
    x11 = fill(x7, x10, x6)
    return x11
