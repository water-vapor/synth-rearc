from synth_rearc.core import *


def verify_6e453dd6(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = canvas(x0, shape(I))
    x2 = first(colorfilter(partition(I), FIVE))
    x3 = leftmost(x2)
    x4 = colorfilter(objects(I, T, F, T), ZERO)
    x5 = tuple(shift(x6, (ZERO, x3 - rightmost(x6) - ONE)) for x6 in x4)
    x6 = paint(x1, x2)
    x7 = paint(x6, merge(x5))
    x8 = width(I)
    x9 = []
    for x10 in x5:
        x11 = rightmost(x10)
        x12 = {}
        for _, (x13, x14) in x10:
            x12.setdefault(x13, []).append(x14)
        for x13, x14 in x12.items():
            x15 = tuple(sorted(x14))
            x16 = size(x15)
            x17 = last(x15) - first(x15) + ONE
            if x11 != last(x15):
                continue
            if x16 == x17:
                continue
            x9.extend((x13, x18) for x18 in range(x3 + ONE, x8))
    x18 = frozenset(x9)
    x19 = fill(x7, TWO, x18)
    return x19
