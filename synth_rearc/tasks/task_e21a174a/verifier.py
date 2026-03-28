from synth_rearc.core import *


def verify_e21a174a(I: Grid) -> Grid:
    x0 = objects(I, T, T, T)
    x1 = order(x0, compose(invert, uppermost))
    x2 = merge(x0)
    x3 = uppermost(x2)
    x4 = lowermost(x2)
    x5 = height(I)
    x6 = subtract(subtract(x5, x4), ONE)
    x7 = width(I)
    x8 = rbind(astuple, x7)
    x9 = lbind(canvas, ZERO)
    x10 = chain(x9, x8, height)
    x11 = compose(tojvec, leftmost)
    x12 = fork(shift, normalize, x11)
    x13 = fork(paint, x10, x12)
    x14 = apply(x13, x1)
    x15 = merge(x14)
    x16 = canvas(ZERO, (x3, x7))
    x17 = canvas(ZERO, (x6, x7))
    x18 = combine(x16, x15)
    x19 = combine(x18, x17)
    return x19
