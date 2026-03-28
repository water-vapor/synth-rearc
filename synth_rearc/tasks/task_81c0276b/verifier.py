from synth_rearc.core import *


def verify_81c0276b(I: Grid) -> Grid:
    x0 = frontiers(I)
    x1 = color(first(x0))
    x2 = replace(I, x1, ZERO)
    x3 = partition(x2)
    x4 = sfilter(x3, lambda x5: color(x5) != ZERO)
    x5 = order(x4, lambda x6: (size(x6), color(x6)))
    x6 = divide(size(x5[-ONE]), FOUR)
    x7 = canvas(ZERO, (size(x5), x6))
    x8 = x7
    for x9, x10 in zip(interval(ZERO, size(x5), ONE), x5):
        x11 = divide(size(x10), FOUR)
        x12 = connect((x9, ZERO), (x9, x11 - ONE))
        x8 = fill(x8, color(x10), x12)
    return x8
