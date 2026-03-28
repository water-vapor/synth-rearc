from synth_rearc.core import *


def verify_b7256dcd(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = colorfilter(x1, SIX)
    x3 = difference(x1, x2)
    x4 = mapply(toindices, x3)
    x5 = fill(I, x0, x4)
    x6 = tuple(sfilter(x3, lbind(adjacent, x)) for x in x2)
    x7 = tuple(y if equality(size(x), ZERO) else recolor(color(first(x)), y) for x, y in zip(x6, x2))
    x8 = paint(x5, merge(x7))
    return x8
