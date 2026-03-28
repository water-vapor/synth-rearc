from synth_rearc.core import *


def verify_712bf12e(
    I: Grid,
) -> Grid:
    x0 = tuple(sorted(ofcolor(I, TWO), key=lambda x: x[1]))
    x1 = width(I)
    x2 = set(x0)
    for x3 in x0:
        x4, x5 = x3
        while x4 > ZERO:
            x6 = decrement(x4)
            x7 = (x6, x5)
            x8 = index(I, x7)
            if x8 == ZERO:
                x4 = x6
                x2.add((x4, x5))
                continue
            x9 = increment(x5)
            x10 = x9 < x1
            x11 = branch(x10, index(I, (x4, x9)), NEG_ONE)
            if both(x10, equality(x11, ZERO)):
                x5 = x9
                x2.add((x4, x5))
                continue
            break
    x12 = fill(I, TWO, frozenset(x2))
    return x12
