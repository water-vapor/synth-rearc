from synth_rearc.core import *


def verify_551d5bf1(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = I
    for x2 in x0:
        x3 = box(x2)
        x4 = difference(backdrop(x2), x3)
        x1 = fill(x1, EIGHT, x4)
        x5 = difference(x3, toindices(x2))
        x6 = uppermost(x2)
        x7 = lowermost(x2)
        x8 = leftmost(x2)
        x9 = rightmost(x2)
        for x10 in x5:
            x11, x12 = x10
            if x11 == x6:
                x13 = UP
            elif x11 == x7:
                x13 = DOWN
            elif x12 == x8:
                x13 = LEFT
            else:
                x13 = RIGHT
            x14 = shoot(x10, x13)
            x1 = fill(x1, EIGHT, x14)
    return x1
