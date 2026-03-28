from synth_rearc.core import *


def verify_103eff5b(I: Grid) -> Grid:
    x0 = objects(I, F, T, T)
    x1 = argmin(x0, size)
    x2 = subgrid(x1, I)
    x3 = rot90(x2)
    x4 = ofcolor(I, EIGHT)
    x5 = divide(height(x4), height(x3))
    x6 = asobject(x3)
    x7 = sfilter(x6, lambda x: x[0] != ZERO)
    x8 = upscale(x7, x5)
    x9 = shift(x8, ulcorner(x4))
    x10 = cover(I, x4)
    x11 = paint(x10, x9)
    return x11
