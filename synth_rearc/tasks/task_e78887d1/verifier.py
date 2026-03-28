from synth_rearc.core import *


def verify_e78887d1(I: Grid) -> Grid:
    x0 = ofcolor(I, ZERO)
    x1 = difference(asindices(I), x0)
    x2 = decrement(decrement(lowermost(x1)))
    x3 = width(I)
    x4 = crop(I, astuple(x2, ZERO), astuple(THREE, x3))
    x5 = divide(increment(x3), FOUR)
    x6 = hsplit(x4, x5)
    x7 = interval(ZERO, x5, ONE)
    x8 = apply(lbind(multiply, FOUR), x7)
    x9 = last(x8)
    x10 = combine(repeat(x9, ONE), remove(x9, x8))
    x11 = rbind(ofcolor, ZERO)
    x12 = fork(difference, asindices, x11)
    x13 = apply(x12, x6)
    x14 = compose(rbind(other, ZERO), palette)
    x15 = apply(x14, x6)
    x16 = last(x15)
    x17 = combine(repeat(x16, ONE), remove(x16, x15))
    x18 = papply(recolor, x17, x13)
    x19 = apply(tojvec, x10)
    x20 = mpapply(shift, x18, x19)
    x21 = canvas(ZERO, astuple(THREE, x3))
    x22 = paint(x21, x20)
    return x22
