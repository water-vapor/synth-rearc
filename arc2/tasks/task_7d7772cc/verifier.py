from arc2.core import *


def _column_7d7772cc(x0: Grid, x1: Integer) -> tuple[int, ...]:
    return tuple(x2[x1] for x2 in x0)


def verify_7d7772cc(I: Grid) -> Grid:
    x0 = tuple(frontiers(I))
    x1 = tuple(color(x2) for x2 in x0)
    x2 = next(x3 for x3 in x0 if x1.count(color(x3)) == ONE)
    x3 = color(x2)
    x4 = difference(ofcolor(I, x3), toindices(x2))
    x5 = hline(x2)
    x6 = uppermost(x2) if x5 else leftmost(x2)
    x7 = min(i for i, _ in x4) if x5 else min(j for _, j in x4)
    x8 = greater(x7, x6)
    if x5:
        x9 = increment(x6) if x8 else decrement(x6)
        x10 = decrement(x6) if x8 else increment(x6)
        x11 = ZERO if x8 else decrement(height(I))
        x12 = interval(ZERO, x6, ONE) if x8 else interval(increment(x6), height(I), ONE)
        x13 = next(x14 for x14 in x12 if len(set(I[x14])) > ONE)
        x14 = I[x11][ZERO]
        x15 = I
        for x16 in range(width(I)):
            x17 = I[x13][x16]
            if x17 == x14:
                continue
            x18 = x10 if x17 == I[x9][x16] else x11
            x15 = fill(x15, x14, frozenset({(x13, x16)}))
            x15 = fill(x15, x17, frozenset({(x18, x16)}))
        return x15
    x9 = increment(x6) if x8 else decrement(x6)
    x10 = decrement(x6) if x8 else increment(x6)
    x11 = ZERO if x8 else decrement(width(I))
    x12 = interval(ZERO, x6, ONE) if x8 else interval(increment(x6), width(I), ONE)
    x13 = next(x14 for x14 in x12 if len(set(_column_7d7772cc(I, x14))) > ONE)
    x14 = I[ZERO][x11]
    x15 = I
    for x16 in range(height(I)):
        x17 = I[x16][x13]
        if x17 == x14:
            continue
        x18 = x10 if x17 == I[x16][x9] else x11
        x15 = fill(x15, x14, frozenset({(x16, x13)}))
        x15 = fill(x15, x17, frozenset({(x16, x18)}))
    return x15
