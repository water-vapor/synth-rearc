from synth_rearc.core import *


def verify_2ba387bc(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = multiply(THREE, FOUR)
    x2 = matcher(size, x1)
    x3 = sfilter(x0, x2)
    x4 = multiply(FOUR, FOUR)
    x5 = matcher(size, x4)
    x6 = sfilter(x0, x5)
    x7 = order(x3, ulcorner)
    x8 = order(x6, ulcorner)
    x9 = astuple(FOUR, FOUR)
    x10 = canvas(ZERO, x9)
    x11 = lbind(paint, x10)
    x12 = compose(x11, normalize)
    x13 = apply(x12, x7)
    x14 = apply(x12, x8)
    x15 = size(x13)
    x16 = size(x14)
    x17 = maximum(astuple(x15, x16))
    x18 = repeat(x10, subtract(x17, x15))
    x19 = repeat(x10, subtract(x17, x16))
    x20 = combine(x13, x18)
    x21 = combine(x14, x19)
    x22 = papply(hconcat, x20, x21)
    x23 = merge(x22)
    return x23
