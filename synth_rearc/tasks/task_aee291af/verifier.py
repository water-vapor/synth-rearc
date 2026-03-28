from synth_rearc.core import *


def verify_aee291af(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = []
    x3 = frozenset({EIGHT})
    x4 = frozenset({TWO, EIGHT})
    for x5 in range(THREE, min(x0, x1) + ONE):
        for x6 in range(subtract(x0, x5) + ONE):
            for x7 in range(subtract(x1, x5) + ONE):
                x8 = crop(I, (x6, x7), (x5, x5))
                x9 = asindices(x8)
                x10 = box(x9)
                x11 = toobject(x10, x8)
                x12 = palette(x11)
                if x12 != x3:
                    continue
                x13 = difference(x9, x10)
                x14 = toobject(x13, x8)
                x15 = palette(x14)
                x16 = difference(x15, x4)
                x17 = equality(x16, frozenset())
                x18 = contained(TWO, x15)
                x19 = both(x17, x18)
                if x19:
                    x2.append(x8)
    x20 = tuple(x2)
    x21 = leastcommon(x20)
    return x21
