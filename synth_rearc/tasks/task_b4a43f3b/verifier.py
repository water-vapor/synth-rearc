from synth_rearc.core import *


def verify_b4a43f3b(I: Grid) -> Grid:
    x0 = crop(I, ORIGIN, (SIX, SIX))
    x1 = downscale(x0, TWO)
    x2 = crop(I, (SEVEN, ZERO), (SIX, SIX))
    x3 = ofcolor(x2, TWO)
    x4 = apply(rbind(multiply, THREE), x3)
    x5 = shape(x2)
    x6 = multiply(x5, THREE)
    x7 = canvas(ZERO, x6)
    x8 = difference(palette(x1), initset(ZERO))
    for x9 in x8:
        x10 = ofcolor(x1, x9)
        x11 = lbind(shift, x10)
        x12 = mapply(x11, x4)
        x7 = fill(x7, x9, x12)
    return x7
