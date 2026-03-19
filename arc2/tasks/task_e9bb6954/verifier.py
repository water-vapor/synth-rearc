from arc2.core import *


def verify_e9bb6954(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = sizefilter(x0, NINE)
    x2 = sfilter(x1, square)
    x3 = order(x2, ulcorner)
    x4 = apply(center, x3)
    x5 = apply(color, x3)
    x6 = apply(fork(combine, hfrontier, vfrontier), x4)
    x7 = I
    for x8, x9 in zip(x5, x6):
        x7 = fill(x7, x8, x9)
    x10 = frozenset()
    for x11, (x12, x13) in enumerate(zip(x5, x6)):
        for x14, x15 in zip(x5[x11 + ONE:], x6[x11 + ONE:]):
            if x12 != x14:
                x10 = combine(x10, intersection(x13, x15))
    x16 = fill(x7, ZERO, x10)
    return x16
