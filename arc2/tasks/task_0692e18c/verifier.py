from arc2.core import *


def verify_0692e18c(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = other(x0, ZERO)
    x2 = switch(I, ZERO, x1)
    x3 = shape(I)
    x4 = multiply(x3, x3)
    x5 = canvas(ZERO, x4)
    x6 = asobject(x2)
    x7 = ofcolor(I, x1)
    x8 = rbind(multiply, x3)
    x9 = apply(x8, x7)
    x10 = lbind(shift, x6)
    x11 = mapply(x10, x9)
    x12 = paint(x5, x11)
    return x12
