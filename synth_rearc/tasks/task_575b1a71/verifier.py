from synth_rearc.core import *


def verify_575b1a71(
    I: Grid,
) -> Grid:
    x0 = ofcolor(I, ZERO)
    x1 = apply(last, x0)
    x2 = order(x1, identity)
    x3 = interval(ONE, FIVE, ONE)
    x4 = canvas(FIVE, shape(I))
    for x5, x6 in zip(x2, x3):
        x7 = sfilter(x0, matcher(last, x5))
        x4 = fill(x4, x6, x7)
    return x4
