from synth_rearc.core import *


def verify_48f8583b(I: Grid) -> Grid:
    x0 = leastcolor(I)
    x1 = ofcolor(I, x0)
    x2 = shape(I)
    x3 = asobject(I)
    x4 = rbind(multiply, x2)
    x5 = apply(x4, x1)
    x6 = lbind(shift, x3)
    x7 = mapply(x6, x5)
    x8 = multiply(x2, THREE)
    x9 = canvas(ZERO, x8)
    x10 = paint(x9, x7)
    return x10
