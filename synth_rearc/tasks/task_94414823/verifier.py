from synth_rearc.core import *


def verify_94414823(I: Grid) -> Grid:
    x0 = ofcolor(I, FIVE)
    x1 = objects(I, T, F, T)
    x2 = sizefilter(x1, ONE)
    x3 = totuple(x2)
    x4 = first(x3)
    x5 = last(x3)
    x6 = outbox(x0)
    x7 = ulcorner(x6)
    x8 = lrcorner(x6)
    x9 = insert(x8, initset(x7))
    x10 = ulcorner(x4)
    x11 = contained(x10, x9)
    x12 = branch(x11, color(x4), color(x5))
    x13 = branch(x11, color(x5), color(x4))
    x14 = astuple(increment(uppermost(x0)), increment(leftmost(x0)))
    x15 = asindices(canvas(ZERO, TWO_BY_TWO))
    x16 = shift(x15, x14)
    x17 = shift(x16, ZERO_BY_TWO)
    x18 = shift(x16, TWO_BY_ZERO)
    x19 = shift(x17, TWO_BY_ZERO)
    x20 = fill(I, x12, x16)
    x21 = fill(x20, x13, x17)
    x22 = fill(x21, x13, x18)
    x23 = fill(x22, x12, x19)
    return x23
