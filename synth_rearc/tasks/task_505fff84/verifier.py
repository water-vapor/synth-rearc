from synth_rearc.core import *


def verify_505fff84(I: Grid) -> Grid:
    x0 = ofcolor(I, ONE)
    x1 = order(x0, identity)
    x2 = ofcolor(I, EIGHT)
    x3 = order(x2, identity)
    x4 = apply(first, x1)
    x5 = apply(last, x1)
    x6 = apply(last, x3)
    x7 = apply(increment, x5)
    x8 = papply(astuple, x4, x7)
    x9 = papply(subtract, x6, x7)
    x10 = apply(lbind(astuple, ONE), x9)
    x11 = papply(lbind(crop, I), x8, x10)
    x12 = apply(first, x11)
    return x12
