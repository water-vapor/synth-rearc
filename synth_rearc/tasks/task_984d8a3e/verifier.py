from synth_rearc.core import *


def verify_984d8a3e(I: Grid) -> Grid:
    x0 = tuple(first(x1) for x1 in I)
    x1 = mostcommon(x0)
    x2 = tuple(last(x3) for x3 in I)
    x3 = mostcommon(x2)
    x4 = tuple(x5 for x5 in palette(I) if x5 not in (x1, x3))
    x5 = first(x4)
    x6 = width(I)
    x7 = tuple(x8.count(x5) for x8 in I)
    x8 = tuple(x9.count(x3) for x9 in I)
    x9 = tuple(x6 - x10 - ONE for x10 in x8)
    x10 = minimum(x9)
    x11 = []
    for x12, x13, x14 in zip(I, x7, x8):
        x15 = x12.count(x1)
        x16 = max(ZERO, x10 - x13 + ONE)
        x17 = x15 - x16
        x18 = repeat(x1, x16)
        x19 = repeat(x5, x13)
        x20 = repeat(x1, x17)
        x21 = repeat(x3, x14)
        x11.append(x18 + x19 + x20 + x21)
    x22 = tuple(x11)
    return x22
