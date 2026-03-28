from synth_rearc.core import *


def verify_9f27f097(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = ofcolor(I, ZERO)
    x2 = toobject(x1, I)
    x3 = other(x0, x2)
    x4 = subgrid(x3, I)
    x5 = vmirror(x4)
    x6 = asobject(x5)
    x7 = shift(x6, ulcorner(x2))
    return paint(I, x7)
