from synth_rearc.core import *


def verify_f4081712(I: Grid) -> Grid:
    x0 = ofcolor(I, THREE)
    x1 = ulcorner(x0)
    x2 = shape(x0)
    x3 = height(I)
    x4 = subtract(subtract(x3, x1[ZERO]), x2[ZERO])
    x5 = astuple(x4, x1[ONE])
    x6 = crop(I, x5, x2)
    x7 = hmirror(x6)
    return x7
