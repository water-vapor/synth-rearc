from synth_rearc.core import *


def verify_917bccba(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = fork(equality, box, toindices)
    x2 = extract(x0, x1)
    x3 = other(x0, x2)
    x4 = mostcolor(I)
    x5 = shape(I)
    x6 = canvas(x4, x5)
    x7 = color(x3)
    x8 = urcorner(x2)
    x9 = hfrontier(x8)
    x10 = fill(x6, x7, x9)
    x11 = vfrontier(x8)
    x12 = fill(x10, x7, x11)
    x13 = paint(x12, x2)
    return x13
