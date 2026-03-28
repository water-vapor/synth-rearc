from synth_rearc.core import *


def verify_516b51b7(I: Grid) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = colorfilter(x0, ONE)
    x2 = compose(minimum, shape)
    x3 = chain(halve, decrement, x2)
    x4 = compose(increment, x3)
    x5 = lbind(interval, ONE)
    x6 = rbind(x5, ONE)
    x7 = compose(x6, x4)
    x8 = lbind(power, inbox)
    x9 = lbind(apply, x8)
    x10 = compose(x9, x7)
    x11 = fork(rapply, x10, identity)
    x12 = lbind(add, TWO)
    x13 = compose(x12, even)
    x14 = lbind(apply, x13)
    x15 = compose(x14, x7)
    x16 = lbind(mpapply, recolor)
    x17 = fork(x16, x15, x11)
    x18 = mapply(x17, x1)
    x19 = paint(I, x18)
    return x19
