from synth_rearc.core import *


def verify_c658a4bd(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = compose(maximum, shape)
    x2 = valmax(x0, x1)
    x3 = astuple(x2, x2)
    x4 = canvas(ZERO, x3)
    x5 = compose(decrement, x1)
    x6 = fork(astuple, x5, x5)
    x7 = initset(ORIGIN)
    x8 = rbind(insert, x7)
    x9 = compose(x8, x6)
    x10 = compose(box, x9)
    x11 = lbind(subtract, x2)
    x12 = chain(halve, x11, x1)
    x13 = fork(astuple, x12, x12)
    x14 = fork(shift, x10, x13)
    x15 = fork(recolor, color, x14)
    x16 = apply(x15, x0)
    x17 = merge(x16)
    x18 = paint(x4, x17)
    return x18
