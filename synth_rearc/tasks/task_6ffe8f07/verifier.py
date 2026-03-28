from synth_rearc.core import *


def verify_6ffe8f07(I: Grid) -> Grid:
    x0 = ofcolor(I, EIGHT)
    x1 = ofcolor(I, ONE)
    x2 = uppermost(x0)
    x3 = lowermost(x0)
    x4 = leftmost(x0)
    x5 = rightmost(x0)
    x6 = interval(x2, increment(x3), ONE)
    x7 = interval(x4, increment(x5), ONE)
    x8 = width(I)
    x9 = height(I)
    x10 = set(x0)
    for x11 in x6:
        x12 = tuple(j for i, j in x1 if i == x11)
        x13 = tuple(j for j in x12 if j < x4)
        x14 = tuple(j for j in x12 if j > x5)
        x15 = branch(len(x13) == ZERO, ZERO, increment(maximum(x13)))
        x16 = branch(len(x14) == ZERO, decrement(x8), decrement(minimum(x14)))
        x17 = connect((x11, x15), (x11, x16))
        x10 |= set(x17)
    for x18 in x7:
        x19 = tuple(i for i, j in x1 if j == x18)
        x20 = tuple(i for i in x19 if i < x2)
        x21 = tuple(i for i in x19 if i > x3)
        x22 = branch(len(x20) == ZERO, ZERO, increment(maximum(x20)))
        x23 = branch(len(x21) == ZERO, decrement(x9), decrement(minimum(x21)))
        x24 = connect((x22, x18), (x23, x18))
        x10 |= set(x24)
    x25 = combine(x0, x1)
    x26 = difference(frozenset(x10), x25)
    x27 = fill(I, FOUR, x26)
    return x27
