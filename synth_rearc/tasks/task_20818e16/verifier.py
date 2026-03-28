from synth_rearc.core import *


def verify_20818e16(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = tuple((color(x2), backdrop(x2)) for x2 in x0)
    x2 = order(x1, lambda x3: (size(last(x3)), height(last(x3)), width(last(x3)), first(x3)))
    x3 = last(x2)
    x4 = canvas(first(x3), shape(last(x3)))
    x5 = x4
    for x6, x7 in x2[-2::-1]:
        x8 = recolor(x6, normalize(x7))
        x5 = paint(x5, x8)
    return x5
