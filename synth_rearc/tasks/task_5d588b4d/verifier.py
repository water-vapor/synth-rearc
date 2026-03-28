from synth_rearc.core import *


def verify_5d588b4d(I: Grid) -> Grid:
    x0 = remove(ZERO, palette(I))
    x1 = first(x0)
    x2 = ofcolor(I, x1)
    x3 = size(x2)
    x4 = width(I)
    x5 = interval(ONE, increment(x3), ONE)
    x6 = interval(decrement(x3), ZERO, NEG_ONE)
    x7 = combine(x5, x6)
    x8 = tuple(combine(repeat(x1, x9), (ZERO,)) for x9 in x7)
    x9 = merge(x8)[:-1]
    x10 = add(divide(decrement(size(x9)), x4), ONE)
    x11 = canvas(ZERO, astuple(x10, x4))
    x12 = frozenset(
        astuple(divide(x13, x4), x13 % x4)
        for x13, x14 in enumerate(x9)
        if equality(x14, x1)
    )
    x15 = fill(x11, x1, x12)
    return x15
