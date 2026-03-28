from synth_rearc.core import *


def verify_20fb2937(
    I: Grid,
) -> Grid:
    x0 = crop(I, ORIGIN, (THREE, THREE))
    x1 = crop(I, (ZERO, FOUR), (THREE, THREE))
    x2 = crop(I, (ZERO, EIGHT), (THREE, THREE))
    x3 = mostcolor(x0)
    x4 = mostcolor(x1)
    x5 = mostcolor(x2)
    x6 = index(I, (FOUR, ONE))
    x7 = index(I, (FOUR, FIVE))
    x8 = index(I, (FOUR, NINE))
    x9 = height(I)
    x10 = width(I)
    x11 = subtract(x9, SEVEN)
    x12 = crop(I, (SEVEN, ZERO), (x11, x10))
    x13 = canvas(SEVEN, shape(x12))
    x14 = ofcolor(x12, x6)
    x15 = ofcolor(x12, x7)
    x16 = ofcolor(x12, x8)
    x17 = fork(combine, initset, neighbors)
    x18 = mapply(x17, x14)
    x19 = fill(x13, x3, x18)
    x20 = mapply(x17, x15)
    x21 = fill(x19, x4, x20)
    x22 = mapply(x17, x16)
    x23 = fill(x21, x5, x22)
    return x23
