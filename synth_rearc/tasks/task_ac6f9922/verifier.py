from synth_rearc.core import *


def verify_ac6f9922(I: Grid) -> Grid:
    x0 = index(I, ORIGIN)
    x1 = objects(I, T, F, F)
    x2 = colorfilter(x1, x0)
    x3 = rbind(bordering, I)
    x4 = compose(flip, x3)
    x5 = sfilter(x2, x4)
    x6 = order(x5, fork(astuple, uppermost, leftmost))
    x7 = apply(uppermost, x6)
    x8 = dedupe(x7)
    x9 = apply(leftmost, x6)
    x10 = dedupe(x9)
    x11 = partition(I)
    x12 = colorfilter(x11, x0)
    x13 = first(x12)
    x14 = remove(x13, x11)
    x15 = argmax(x14, size)
    x16 = color(x15)
    x17 = canvas(x0, astuple(size(x8), size(x10)))
    x18 = x17
    for x19 in x6:
        x20 = x8.index(uppermost(x19))
        x21 = x10.index(leftmost(x19))
        x22 = delta(x19)
        x23 = toobject(x22, I)
        x24 = palette(x23)
        x25 = remove(x16, x24)
        if greater(size(x25), ZERO):
            x27 = first(x25)
        else:
            x27 = x0
        x28 = fill(x18, x27, initset(astuple(x20, x21)))
        x18 = x28
    return x18
