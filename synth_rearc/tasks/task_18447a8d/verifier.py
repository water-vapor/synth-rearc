from synth_rearc.core import *


def verify_18447a8d(I: Grid) -> Grid:
    x0 = height(I)
    x1 = interval(ONE, x0, ONE)
    x2 = lambda r: all(v == SEVEN for v in I[r])
    x3 = tuple(r for r in x1 if not x2(r))
    x4 = tuple(r for r in x3 if x2(decrement(r)))
    x6 = tuple(
        tuple(sum(I[add(r, k)][j] == EIGHT for j in range(FIVE)) for k in range(THREE))
        for r in x4
    )
    x7 = tuple(
        tuple(sum(I[add(r, k)][j] != SEVEN for j in range(SEVEN, 11)) for k in range(THREE))
        for r in x4
    )
    x8 = tuple(
        next(v for k in range(THREE) for v in I[add(r, k)] if v not in (SEVEN, EIGHT))
        for r in x4
    )
    x9 = dict(zip(x7, x8))
    x10 = ofcolor(I, EIGHT)
    x11 = fill(canvas(SEVEN, shape(I)), EIGHT, x10)
    x12 = tuple(tuple(subtract(FIVE, v) for v in x13) for x13 in x6)
    x13 = tuple(x9[x14] for x14 in x12)
    x14 = x11
    for x15, x16, x17 in zip(x4, x6, x13):
        for x18, x19 in enumerate(x16):
            x20 = frozenset((add(x15, x18), j) for j in range(x19, FIVE))
            x14 = fill(x14, x17, x20)
    return x14
