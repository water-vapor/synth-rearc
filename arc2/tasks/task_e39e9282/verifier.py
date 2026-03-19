from arc2.core import *


def verify_e39e9282(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = colorfilter(x1, FIVE)
    x3 = colorfilter(x1, SIX)
    x4 = combine(x2, x3)
    x5 = sizefilter(x4, NINE)
    x6 = sfilter(x5, square)
    x7 = ofcolor(I, NINE)
    x8 = fill(I, x0, x7)
    x9 = fill(x8, x0, merge(x2))
    x10 = x9
    for x11 in x6:
        x12 = outbox(x11)
        x13 = difference(x12, corners(x12))
        x14 = intersection(x7, x13)
        x15 = uppermost(x11)
        x16 = lowermost(x11)
        x17 = leftmost(x11)
        x18 = rightmost(x11)
        x19 = color(x11)
        x20 = branch(equality(x19, FIVE), ONE, TWO)
        for x21 in x14:
            x22, x23 = x21
            if equality(x19, FIVE):
                x10 = fill(x10, NINE, initset(x21))
            if x22 == x15 - ONE:
                x24 = add(x22, x20)
                x25 = (x24, x23)
            elif x22 == x16 + ONE:
                x24 = subtract(x22, x20)
                x25 = (x24, x23)
            elif x23 == x17 - ONE:
                x24 = add(x23, x20)
                x25 = (x22, x24)
            elif x23 == x18 + ONE:
                x24 = subtract(x23, x20)
                x25 = (x22, x24)
            else:
                continue
            x10 = fill(x10, NINE, initset(x25))
    return x10
