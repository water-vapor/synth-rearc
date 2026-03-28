from synth_rearc.core import *


def verify_007bbfb7(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = other(x0, ZERO)
    x2 = shape(I)
    x3 = multiply(x2, x2)
    x4 = canvas(ZERO, x3)
    x5 = ofcolor(I, x1)
    x6 = lbind(shift, x5)
    x7 = shape(I)
    x8 = rbind(multiply, x7)
    x9 = apply(x8, x5)
    x10 = mapply(x6, x9)
    x11 = fill(x4, x1, x10)
    return x11
