from synth_rearc.core import *


def verify_41ace6b5(I: Grid) -> Grid:
    x0 = ofcolor(I, TWO)
    x1 = uppermost(x0)
    x2 = height(I)
    x3 = width(I)
    x4 = interval(ONE, x3, TWO)
    x5 = tuple(sum(I[x6][x7] == EIGHT for x6 in range(x2)) for x7 in x4)
    x6 = maximum(x5)
    x7 = tuple(sum(I[x8][x9] == ONE for x8 in range(x2)) for x9 in x4)
    x8 = frozenset((x9, x10) for x9 in range(x2) for x10 in x4)
    x9 = fill(I, SEVEN, x8)
    x10 = interval(add(subtract(x1, x6), ONE), increment(x1), ONE)
    x11 = frozenset((x12, x13) for x12 in x10 for x13 in x4)
    x12 = fill(x9, EIGHT, x11)
    x13 = frozenset(
        (x14, x15)
        for x15, x16 in zip(x4, x7)
        for x14 in interval(increment(x1), add(increment(x1), x16), ONE)
    )
    x14 = fill(x12, ONE, x13)
    x15 = frozenset(
        (x16, x17)
        for x17, x18 in zip(x4, x7)
        for x16 in interval(add(increment(x1), x18), x2, ONE)
    )
    x16 = fill(x14, NINE, x15)
    return x16
