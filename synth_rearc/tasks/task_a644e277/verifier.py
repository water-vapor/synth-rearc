from synth_rearc.core import *


def verify_a644e277(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = leastcolor(I)
    x2 = palette(I)
    x3 = remove(x0, x2)
    x4 = other(x3, x1)
    x5 = width(I)
    x6 = tuple(x7.count(x4) for x7 in I)
    x7 = tuple(x8 for x8, x9 in enumerate(x6) if x9 > x5 // TWO)
    x8 = dmirror(I)
    x9 = tuple(x10.count(x4) for x10 in x8)
    x10 = height(I)
    x11 = tuple(x12 for x12, x13 in enumerate(x9) if x13 > x10 // TWO)
    x12 = tuple(x13 for x13 in x7 if any(I[x13][x14] != x4 for x14 in x11))
    x13 = tuple(x14 for x14 in x11 if any(I[x15][x14] != x4 for x15 in x7))
    x14 = first(x12)
    x15 = first(x13)
    x16 = last(x12)
    x17 = last(x13)
    x18 = astuple(x14, x15)
    x19 = increment(subtract(x16, x14))
    x20 = increment(subtract(x17, x15))
    x21 = astuple(x19, x20)
    x22 = crop(I, x18, x21)
    return x22
