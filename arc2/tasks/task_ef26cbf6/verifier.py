from arc2.core import *


def verify_ef26cbf6(I: Grid) -> Grid:
    x0 = frontiers(I)
    x1 = colorfilter(x0, FOUR)
    x2 = sfilter(x1, hline)
    x3 = sfilter(x1, vline)
    x4 = equality(size(x3), ONE)
    x5 = rot90(I)
    x6 = branch(x4, I, x5)
    x7 = frontiers(x6)
    x8 = colorfilter(x7, FOUR)
    x9 = order(sfilter(x8, hline), uppermost)
    x10 = extract(sfilter(x8, vline), vline)
    x11 = leftmost(x10)
    x12 = astuple(height(x6), x11)
    x13 = crop(x6, ORIGIN, x12)
    x14 = equality(colorcount(x13, ONE), ZERO)
    x15 = increment(x11)
    x16 = subtract(width(x6), x15)
    x17 = branch(x14, x15, ZERO)
    x18 = branch(x14, ZERO, x15)
    x19 = branch(x14, x16, x11)
    x20 = branch(x14, x11, x16)
    x21 = height(x6)
    x22 = x6
    x23 = [ZERO]
    x24 = []
    for x25 in x9:
        x26 = uppermost(x25)
        x24.append(x26)
        x23.append(increment(x26))
    x24.append(x21)
    for x25, x26 in zip(x23, x24):
        x27 = subtract(x26, x25)
        x28 = crop(x6, (x25, x17), (x27, x19))
        x29 = crop(x6, (x25, x18), (x27, x20))
        x30 = other(palette(x29), ZERO)
        x31 = shift(ofcolor(x28, ONE), (x25, x17))
        x22 = fill(x22, x30, x31)
    x32 = rot270(x22)
    x33 = branch(x4, x22, x32)
    return x33
