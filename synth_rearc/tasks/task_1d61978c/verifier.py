from synth_rearc.core import *


def verify_1d61978c(I: Grid) -> Grid:
    x0 = ofcolor(I, FIVE)
    x1 = sfilter(
        x0,
        lambda x: either(contained(add(x, NEG_UNITY), x0), contained(add(x, UNITY), x0)),
    )
    x2 = sfilter(
        x0,
        lambda x: either(contained(add(x, UP_RIGHT), x0), contained(add(x, DOWN_LEFT), x0)),
    )
    x3 = intersection(x1, x2)
    x4 = difference(x1, x3)
    x5 = difference(x2, x3)
    x6 = size(x4)
    x7 = size(x5)
    x8 = greater(x7, x6)
    x9 = branch(x8, x4, x5)
    x10 = branch(x8, x5, x4)
    x11 = fill(I, SEVEN, x0)
    x12 = fill(x11, TWO, x9)
    x13 = fill(x12, EIGHT, x10)
    return x13
