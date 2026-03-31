from synth_rearc.core import *


def verify_903d1b4a(
    I: Grid,
) -> Grid:
    x0 = astuple(identity, hmirror)
    x1 = astuple(vmirror, dmirror)
    x2 = astuple(cmirror, rot90)
    x3 = astuple(rot180, rot270)
    x4 = combine(x0, x1)
    x5 = combine(x2, x3)
    x6 = combine(x4, x5)
    x7 = rbind(rapply, I)
    x8 = x7(x6)
    x9 = shape(I)
    x10 = first(x9)
    x11 = last(x9)
    x12 = []
    for x13 in interval(ZERO, x10, ONE):
        x14 = []
        for x15 in interval(ZERO, x11, ONE):
            x16 = THREE
            x17 = astuple(x13, x15)
            for x18 in x8:
                x19 = index(x18, x17)
                x20 = equality(x19, THREE)
                if flip(x20):
                    x16 = x19
                    break
            x14.append(x16)
        x12.append(tuple(x14))
    return tuple(x12)
