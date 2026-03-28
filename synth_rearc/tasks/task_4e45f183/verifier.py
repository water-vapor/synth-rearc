from synth_rearc.core import *


def verify_4e45f183(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = remove(ZERO, palette(I))
    x2 = other(x1, x0)
    x3 = replace(I, x2, x0)
    x4 = x3
    for x5 in range(THREE):
        for x6 in range(THREE):
            x7 = add(ONE, multiply(SIX, x5))
            x8 = add(ONE, multiply(SIX, x6))
            x9 = crop(I, (x7, x8), (FIVE, FIVE))
            x10 = ofcolor(x9, x2)
            x11 = centerofmass(x10)
            x12 = add(ONE, sign(subtract(x11, TWO)))
            x13 = add(ONE, multiply(SIX, x12))
            x14 = shift(recolor(x2, x10), x13)
            x4 = paint(x4, x14)
    return x4
