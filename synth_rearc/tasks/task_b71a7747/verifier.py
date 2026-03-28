from synth_rearc.core import *


def verify_b71a7747(I: Grid) -> Grid:
    x0 = I
    while numcolors(x0) > TWO:
        x1 = palette((first(x0),))
        x2 = tuple(i for i, r in enumerate(x0) if not frozenset(r).issubset(x1))
        x3 = tuple(
            j
            for j in interval(ZERO, width(x0), ONE)
            if not frozenset(r[j] for r in x0).issubset(x1)
        )
        x4 = both(equality(len(x2), height(x0)), equality(len(x3), width(x0)))
        if x4:
            return x0
        x0 = tuple(tuple(x0[i][j] for j in x3) for i in x2)
    return x0
