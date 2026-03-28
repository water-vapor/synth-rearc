from synth_rearc.core import *


def verify_69889d6e(I: Grid) -> Grid:
    x0 = ofcolor(I, TWO)
    x1 = first(x0)
    x2 = I
    x3 = x1
    x4 = RIGHT
    while True:
        x5 = UP if equality(x4, RIGHT) else RIGHT
        x6 = add(x3, x5)
        x7 = index(I, x6)
        if equality(x7, None):
            break
        if equality(x7, ONE):
            x8 = UP if equality(x5, RIGHT) else RIGHT
            x9 = add(x3, x8)
            x10 = index(I, x9)
            if either(equality(x10, None), equality(x10, ONE)):
                break
            x3 = x9
            x4 = x8
        else:
            x3 = x6
            x4 = x5
        x2 = fill(x2, TWO, initset(x3))
    return x2
