from synth_rearc.core import *


def verify_fbf15a0b(I: Grid) -> Grid:
    x0 = ofcolor(I, FIVE)
    x1 = leftmost(x0)
    x2 = rightmost(x0)
    x3 = equality(x1, x2)
    x4 = uppermost(x0)
    x5 = height(I)
    x6 = halve(x5)
    x7 = greater(x6, x4)
    x8 = tophalf(I)
    x9 = bottomhalf(I)
    x10 = branch(x7, x8, x9)
    x11 = width(I)
    x12 = halve(x11)
    x13 = greater(x12, x1)
    x14 = lefthalf(I)
    x15 = righthalf(I)
    x16 = branch(x13, x14, x15)
    x17 = branch(x3, x10, x16)
    x18 = replace(x17, FIVE, EIGHT)
    return x18
