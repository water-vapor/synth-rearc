from arc2.core import *


def verify_20981f0e(I: Grid) -> Grid:
    x0 = ofcolor(I, TWO)
    x1 = apply(first, x0)
    x2 = order(x1, identity)
    x3 = apply(last, x0)
    x4 = order(x3, identity)
    x5 = height(I)
    x6 = width(I)
    x7 = canvas(ZERO, (x5, x6))
    x8 = fill(x7, TWO, x0)
    x9 = (-ONE,) + x2 + (x5,)
    x10 = (-ONE,) + x4 + (x6,)
    x11 = x8
    for x12, x13 in zip(x9, x9[ONE:]):
        x14 = x13 - x12 - ONE
        if x14 <= ZERO:
            continue
        for x15, x16 in zip(x10, x10[ONE:]):
            x17 = x16 - x15 - ONE
            if x17 <= ZERO:
                continue
            x18 = crop(I, (x12 + ONE, x15 + ONE), (x14, x17))
            x19 = ofcolor(x18, ONE)
            if size(x19) == ZERO:
                continue
            x20 = normalize(x19)
            x21 = shape(x20)
            x22 = halve(subtract((x14, x17), x21))
            x23 = add((x12 + ONE, x15 + ONE), x22)
            x24 = shift(x20, x23)
            x11 = fill(x11, ONE, x24)
    return x11
