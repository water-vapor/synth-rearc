from synth_rearc.core import *


def verify_252143c9(I: Grid) -> Grid:
    x0 = shape(I)
    x1 = canvas(SEVEN, x0)
    x2 = asindices(I)
    x3 = center(x2)
    x4 = index(I, x3)
    x5 = ofcolor(I, x4)
    x6 = centerofmass(x5)
    x7 = subtract(x6, x3)
    x8 = sign(x7)
    x9 = shoot(x3, x8)
    x10 = fill(x1, x4, x9)
    return x10
