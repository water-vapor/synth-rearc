from synth_rearc.core import *


def verify_770cc55f(
    I: Grid,
) -> Grid:
    x0 = palette(I)
    x1 = remove(ZERO, x0)
    x2 = other(x1, TWO)
    x3 = ofcolor(I, x2)
    x4 = uppermost(x3)
    x5 = lowermost(x3)
    x6 = matcher(first, x4)
    x7 = sfilter(x3, x6)
    x8 = matcher(first, x5)
    x9 = sfilter(x3, x8)
    x10 = subtract(x5, x4)
    x11 = astuple(x10, ZERO)
    x12 = shift(x7, x11)
    x13 = intersection(x12, x9)
    x14 = mapply(vfrontier, x13)
    x15 = size(x7)
    x16 = size(x9)
    x17 = ofcolor(I, TWO)
    x18 = uppermost(x17)
    x19 = width(I)
    x20 = interval(ZERO, x19, ONE)
    x21 = increment(x4)
    x22 = interval(x21, x18, ONE)
    x23 = product(x22, x20)
    x24 = intersection(x14, x23)
    x25 = increment(x18)
    x26 = interval(x25, x5, ONE)
    x27 = product(x26, x20)
    x28 = intersection(x14, x27)
    x29 = greater(x15, x16)
    x30 = branch(x29, x24, x28)
    x31 = fill(I, FOUR, x30)
    return x31
