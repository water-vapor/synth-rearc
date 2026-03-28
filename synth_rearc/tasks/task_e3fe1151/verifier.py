from synth_rearc.core import *


def verify_e3fe1151(I: Grid) -> Grid:
    x0 = remove(SEVEN, palette(I))
    x1 = tuple(x0)
    x2 = {x3: divide(add(colorcount(I, x3), THREE), FOUR) for x3 in x1}
    x3 = astuple(TWO, TWO)
    x4 = astuple(ZERO, THREE)
    x5 = astuple(THREE, ZERO)
    x6 = astuple(THREE, THREE)
    x7 = (
        (ORIGIN, crop(I, ORIGIN, x3)),
        (x4, crop(I, x4, x3)),
        (x5, crop(I, x5, x3)),
        (x6, crop(I, x6, x3)),
    )
    x8 = I
    for x9, x10 in x7:
        x11 = shift(ofcolor(x10, SEVEN), x9)
        x12 = next(x13 for x13 in x1 if colorcount(x10, x13) < x2[x13])
        x8 = fill(x8, x12, x11)
    return x8
