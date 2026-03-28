from synth_rearc.core import *


def verify_4364c1c4(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = mostcolor(I)
    x2 = shape(I)
    x3 = canvas(x1, x2)
    x4 = x3
    for x5 in x0:
        x6 = remove(x5, x0)
        x7 = ZERO
        for x8 in x6:
            x9 = adjacent(x5, x8)
            x10 = vmatching(x5, x8)
            x11 = both(x9, x10)
            if x11:
                x12 = uppermost(x5)
                x13 = uppermost(x8)
                x14 = subtract(x12, x13)
                x15 = sign(x14)
                x7 = add(x7, x15)
        x16 = sign(x7)
        x17 = tojvec(x16)
        x18 = shift(x5, x17)
        x4 = paint(x4, x18)
    return x4
