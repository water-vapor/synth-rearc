from arc2.core import *


def verify_ad7e01d0(I: Grid) -> Grid:
    x0 = shape(I)
    x1 = multiply(x0, x0)
    x2 = canvas(ZERO, x1)
    x3 = ofcolor(I, FIVE)
    x4 = asobject(I)
    x5 = rbind(multiply, x0)
    x6 = apply(x5, x3)
    x7 = lbind(shift, x4)
    x8 = apply(x7, x6)
    x9 = merge(x8)
    x10 = paint(x2, x9)
    return x10
