from synth_rearc.core import *


def verify_9473c6fb(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = ofcolor(I, x0)
    x2 = difference(asindices(I), x1)
    x3 = size(x2)
    x4 = apply(first, x2)
    x5 = size(x4)
    x6 = equality(x5, x3)
    x7 = order(x2, identity)
    x8 = order(x2, last)
    x9 = branch(x6, x7, x8)
    x10 = interval(ZERO, x3, THREE)
    x11 = interval(ONE, x3, THREE)
    x12 = interval(TWO, x3, THREE)
    x13 = frozenset(x9[x14] for x14 in x10)
    x15 = frozenset(x9[x16] for x16 in x11)
    x17 = frozenset(x9[x18] for x18 in x12)
    x19 = fill(I, TWO, x13)
    x20 = fill(x19, EIGHT, x15)
    x21 = fill(x20, FIVE, x17)
    return x21
