from synth_rearc.core import *


def verify_292dd178(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, ONE)
    x2 = shape(I)
    x3 = I
    for x4 in x1:
        x5 = box(x4)
        x6 = toindices(x4)
        x7 = first(difference(x5, x6))
        x8, x9 = x7
        x10 = uppermost(x4)
        x11 = lowermost(x4)
        x12 = leftmost(x4)
        x13 = rightmost(x4)
        if x8 == x10:
            x14 = (ZERO, x9)
        elif x8 == x11:
            x14 = (decrement(x2[ZERO]), x9)
        elif x9 == x12:
            x14 = (x8, ZERO)
        else:
            x14 = (x8, decrement(x2[ONE]))
        x15 = connect(x7, x14)
        x16 = combine(delta(x4), x15)
        x3 = fill(x3, TWO, x16)
    return x3
