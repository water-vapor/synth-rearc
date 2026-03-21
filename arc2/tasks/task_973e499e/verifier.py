from arc2.core import *


def verify_973e499e(I: Grid) -> Grid:
    x0 = shape(I)
    x1 = multiply(x0, x0)
    x2 = canvas(ZERO, x1)
    x3 = remove(ZERO, palette(I))
    x4 = x2
    for x5 in x3:
        x6 = ofcolor(I, x5)
        x7 = lbind(shift, x6)
        x8 = rbind(multiply, x0)
        x9 = apply(x8, x6)
        x10 = mapply(x7, x9)
        x4 = fill(x4, x5, x10)
    return x4
