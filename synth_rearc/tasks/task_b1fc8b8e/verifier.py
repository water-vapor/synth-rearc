from synth_rearc.core import *


def verify_b1fc8b8e(I: Grid) -> Grid:
    x0 = ofcolor(I, EIGHT)
    x1 = size(x0)
    x2 = double(double(FOUR))
    x3 = equality(x1, x2)
    x4 = connect(ORIGIN, RIGHT)
    x5 = shift(x4, DOWN)
    x6 = combine(x4, x5)
    x7 = connect(RIGHT, UNITY)
    x8 = connect(DOWN, UNITY)
    x9 = combine(x7, x8)
    x10 = branch(x3, x6, x9)
    x11 = shift(x10, astuple(ZERO, THREE))
    x12 = shift(x10, astuple(THREE, ZERO))
    x13 = shift(x10, THREE_BY_THREE)
    x14 = combine(x10, x11)
    x15 = combine(x12, x13)
    x16 = combine(x14, x15)
    x17 = canvas(ZERO, (FIVE, FIVE))
    x18 = fill(x17, EIGHT, x16)
    return x18
