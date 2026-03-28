from synth_rearc.core import *


def verify_27f8ce4f(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = ofcolor(I, x0)
    x2 = shape(I)
    x3 = multiply(x2, x2)
    x4 = canvas(ZERO, x3)
    x5 = asobject(I)
    x6 = lbind(shift, x5)
    x7 = rbind(multiply, x2)
    x8 = apply(x7, x1)
    x9 = mapply(x6, x8)
    x10 = paint(x4, x9)
    return x10
