from arc2.core import *


def verify_8e2edd66(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = other(x0, ZERO)
    x2 = ofcolor(I, ZERO)
    x3 = lbind(shift, x2)
    x4 = shape(I)
    x5 = rbind(multiply, x4)
    x6 = apply(x5, x2)
    x7 = mapply(x3, x6)
    x8 = multiply(x4, x4)
    x9 = canvas(ZERO, x8)
    x10 = fill(x9, x1, x7)
    return x10
