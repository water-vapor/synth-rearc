from arc2.core import *


def verify_456873bc(I: Grid) -> Grid:
    x0 = tuple(x1 for x1, x2 in enumerate(I) if set(x2) == {THREE})
    x1 = tuple(x2 for x2 in interval(ZERO, width(I), ONE) if {x3[x2] for x3 in I} == {THREE})
    x2 = size(x0) if size(x0) > ZERO else size(x1)
    x3 = increment(x2)
    x4 = interval(ZERO, height(I), x3)
    x5 = []
    for x6 in x4:
        for x7 in x4:
            x8 = crop(I, (x6, x7), (x2, x2))
            x9 = palette(x8)
            if THREE in x9 or colorcount(x8, TWO) == ZERO:
                continue
            x5.append(x8)
    x10 = first(tuple(x5))
    x11 = ofcolor(x10, TWO)
    x12 = canvas(ZERO, shape(I))
    for x13 in x11:
        x14 = multiply(x13, x3)
        x15 = shift(x11, x14)
        x12 = fill(x12, TWO, x15)
        x16 = add(x13, x14)
        x12 = fill(x12, EIGHT, initset(x16))
    return x12
