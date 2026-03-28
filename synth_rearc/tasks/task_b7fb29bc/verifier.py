from synth_rearc.core import *


def verify_b7fb29bc(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = first(x0)
    x2 = box(x1)
    x3 = difference(toindices(x1), x2)
    x4 = delta(x2)
    x5 = decrement(maximum(shape(x4)))
    x6 = interval(ONE, increment(x5), ONE)
    x7 = compose(flip, even)
    x8 = sfilter(x6, x7)
    x9 = sfilter(x6, even)
    x10 = lbind(power, outbox)
    x11 = apply(x10, x8)
    x12 = apply(x10, x9)
    x13 = rapply(x11, x3)
    x14 = rapply(x12, x3)
    x15 = rbind(intersection, x4)
    x16 = apply(x15, x13)
    x17 = apply(x15, x14)
    x18 = fill(I, FOUR, merge(x16))
    x19 = fill(x18, TWO, merge(x17))
    return x19
