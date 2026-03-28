from synth_rearc.core import *


def verify_54db823b(I: Grid) -> Grid:
    x0 = asindices(I)
    x1 = ofcolor(I, ZERO)
    x2 = difference(x0, x1)
    x3 = canvas(ZERO, shape(I))
    x4 = fill(x3, ONE, x2)
    x5 = objects(x4, T, F, F)
    x6 = colorfilter(x5, ONE)
    x7 = rbind(toobject, I)
    x8 = compose(rbind(colorcount, NINE), x7)
    x9 = argmin(x6, x8)
    x10 = fill(I, ZERO, x9)
    return x10
