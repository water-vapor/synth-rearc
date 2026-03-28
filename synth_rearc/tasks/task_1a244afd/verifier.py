from synth_rearc.core import *


def verify_1a244afd(I: Grid) -> Grid:
    x0 = ofcolor(I, ONE)
    x1 = ofcolor(I, SIX)
    x2 = canvas(EIGHT, shape(I))
    x3 = fill(x2, ONE, x0)
    x4 = frozenset({})
    x5 = order(x0, identity)
    for x6 in x5:
        x7 = tuple(x8 for x8 in x1 if x8[0] == x6[0] or x8[1] == x6[1])
        if len(x7) == ZERO:
            continue
        x8 = argmin(
            x7,
            lambda x9: (
                abs(x9[0] - x6[0]) + abs(x9[1] - x6[1]),
                ZERO if x9[1] == x6[1] else ONE,
                x9[0],
                x9[1],
            ),
        )
        x9 = subtract(x8, x6)
        x10 = astuple(-x9[1], x9[0])
        x11 = add(x6, x10)
        x4 = insert(x11, x4)
    x12 = underfill(x3, SEVEN, x4)
    return x12
