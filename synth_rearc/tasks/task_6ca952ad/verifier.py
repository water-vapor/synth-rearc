from synth_rearc.core import *


def verify_6ca952ad(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = rbind(greater, THREE)
    x2 = compose(x1, size)
    x3 = sfilter(x0, x2)
    x4 = mapply(toindices, x3)
    x5 = cover(I, x4)
    x6 = totuple(x3)
    x7 = height(I)
    x8 = decrement(x7)
    x9 = apply(lowermost, x6)
    x10 = repeat(x8, size(x6))
    x11 = papply(subtract, x10, x9)
    x12 = apply(toivec, x11)
    x13 = papply(shift, x6, x12)
    x14 = mapply(identity, x13)
    x15 = paint(x5, x14)
    return x15
