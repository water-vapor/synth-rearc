from synth_rearc.core import *


def verify_2697da3f(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = fgpartition(I)
    x2 = first(x1)
    x3 = crop(I, ulcorner(x2), shape(x2))
    x4 = height(x3)
    x5 = width(x3)
    x6 = canvas(x0, (x5, x5))
    x7 = rot90(x3)
    x8 = hconcat(x6, x7)
    x9 = hconcat(x8, x6)
    x10 = canvas(x0, (x4, x4))
    x11 = vmirror(x3)
    x12 = hconcat(x3, x10)
    x13 = hconcat(x12, x11)
    x14 = rot270(x3)
    x15 = hconcat(x6, x14)
    x16 = hconcat(x15, x6)
    x17 = vconcat(x9, x13)
    x18 = vconcat(x17, x16)
    return x18
