from synth_rearc.core import *


def verify_759f3fd3(
    I: Grid,
) -> Grid:
    x0 = frontiers(I)
    x1 = extract(x0, hline)
    x2 = extract(x0, vline)
    x3 = intersection(toindices(x1), toindices(x2))
    x4 = first(x3)
    x5 = initset(x4)
    x6 = height(I)
    x7 = width(I)
    x8 = astuple(x6, x7)
    x9 = maximum(x8)
    x10 = increment(x9)
    x11 = interval(TWO, x10, TWO)
    x12 = lbind(power, outbox)
    x13 = apply(x12, x11)
    x14 = rapply(x13, x5)
    x15 = frozenset(merge(x14))
    x16 = underfill(I, FOUR, x15)
    return x16
