from synth_rearc.core import *


def verify_c3202e5a(I: Grid) -> Grid:
    x0 = frontiers(I)
    x1 = sfilter(x0, hline)
    x2 = increment(size(x1))
    x3 = sfilter(x0, vline)
    x4 = increment(size(x3))
    x5 = compress(I)
    x6 = vsplit(x5, x2)
    x7 = rbind(hsplit, x4)
    x8 = apply(x7, x6)
    x9 = merge(x8)
    x10 = lbind(remove, ZERO)
    x11 = chain(size, x10, palette)
    x12 = matcher(x11, ONE)
    x13 = extract(x9, x12)
    return x13
