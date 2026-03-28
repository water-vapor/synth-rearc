from synth_rearc.core import *


def verify_00dbd492(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = compose(square, backdrop)
    x2 = sfilter(x0, x1)
    x3 = matcher(height, ONE)
    x4 = compose(flip, x3)
    x5 = sfilter(x2, x4)
    x6 = fork(equality, toindices, box)
    x7 = sfilter(x5, x6)
    x8 = matcher(height, FIVE)
    x9 = sfilter(x7, x8)
    x10 = mapply(delta, x9)
    x11 = underfill(I, EIGHT, x10)
    x12 = matcher(height, SEVEN)
    x13 = sfilter(x7, x12)
    x14 = mapply(delta, x13)
    x15 = underfill(x11, FOUR, x14)
    x16 = matcher(height, NINE)
    x17 = sfilter(x7, x16)
    x18 = mapply(delta, x17)
    x19 = underfill(x15, THREE, x18)
    return x19
