from arc2.core import *


def verify_5b6cbef5(I: Grid) -> Grid:
    x0 = asobject(I)
    x1 = ofcolor(I, ZERO)
    x2 = asindices(I)
    x3 = difference(x2, x1)
    x4 = rbind(multiply, FOUR)
    x5 = apply(x4, x3)
    x6 = lbind(shift, x0)
    x7 = mapply(x6, x5)
    x8 = shape(I)
    x9 = multiply(x8, FOUR)
    x10 = canvas(ZERO, x9)
    x11 = paint(x10, x7)
    return x11
