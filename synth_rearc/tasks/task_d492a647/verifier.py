from synth_rearc.core import *


def verify_d492a647(
    I: Grid,
) -> Grid:
    x0 = palette(I)
    x1 = difference(x0, frozenset({ZERO, FIVE}))
    x2 = first(x1)
    x3 = ofcolor(I, x2)
    x4 = first(x3)
    x5 = first(x4)
    x6 = last(x4)
    x7 = branch(even(x5), ZERO, ONE)
    x8 = branch(even(x6), ZERO, ONE)
    x9 = height(I)
    x10 = width(I)
    x11 = interval(x7, x9, TWO)
    x12 = interval(x8, x10, TWO)
    x13 = product(x11, x12)
    x14 = ofcolor(I, ZERO)
    x15 = intersection(x13, x14)
    x16 = fill(I, x2, x15)
    return x16
