from synth_rearc.core import *


def verify_52364a65(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = frozenset()
    for x3 in x1:
        x4 = uppermost(x3)
        x5 = lowermost(x3)
        x6 = leftmost(x3)
        x7 = increment(x6)
        x8 = frozenset({(x4, x6), (x5, x7)})
        x9 = backdrop(x8)
        x10 = toindices(x3)
        x11 = intersection(x10, x9)
        x2 = combine(x2, x11)
    x12 = fill(I, x0, x2)
    return x12
