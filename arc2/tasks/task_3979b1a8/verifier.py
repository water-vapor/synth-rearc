from arc2.core import *


def verify_3979b1a8(I: Grid) -> Grid:
    x0 = leastcolor(I)
    x1 = center(asindices(I))
    x2 = index(I, x1)
    x3 = mostcolor(I)
    x4 = (x0, x2, x3)
    x5 = height(I)
    x6 = width(I)
    x7 = tuple(x4[x8 % THREE] for x8 in range(x6))
    x8 = repeat(x7, x5)
    x9 = tuple(x4[x10 % THREE] for x10 in range(x5))
    x10 = rbind(repeat, x6)
    x11 = apply(x10, x9)
    x12 = tuple(
        tuple(x4[(max(x13, x14) + (x13 == x14)) % THREE] for x14 in range(x6))
        for x13 in range(x5)
    )
    x13 = hconcat(I, x8)
    x14 = hconcat(x11, x12)
    x15 = vconcat(x13, x14)
    return x15
