from arc2.core import *


def verify_50aad11f(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, SIX)
    x2 = matcher(color, SIX)
    x3 = compose(flip, x2)
    x4 = sfilter(x0, x3)
    x5 = sizefilter(x4, ONE)
    x6 = merge(x1)
    x7 = width(x6)
    x8 = height(x6)
    x9 = greater(x7, x8)
    x10 = branch(x9, leftmost, uppermost)
    x11 = order(x1, x10)
    x12 = lambda x: argmin(x5, lbind(manhattan, x))
    x13 = apply(x12, x11)
    x14 = apply(color, x13)
    x15 = lambda x16, x17: paint(canvas(ZERO, shape(x16)), normalize(recolor(x17, x16)))
    x16 = papply(x15, x11, x14)
    x17 = branch(x9, hconcat, vconcat)
    x18 = first(x16)
    for x19 in x16[1:]:
        x18 = x17(x18, x19)
    return x18
