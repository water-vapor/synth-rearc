from synth_rearc.core import *


def verify_458e3a53(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = tuple(i for i, row in enumerate(I) if len(set(row)) == ONE)
    x3 = I[x2[ZERO]][ZERO]
    x4 = (NEG_ONE,) + x2 + (x0,)
    x5 = tuple((a + ONE, b - ONE) for a, b in zip(x4, x4[ONE:]) if b - a > ONE)
    x6 = tuple(
        tuple(j for j in range(x1) if all(I[i][j] == x3 for i in range(r0, r1 + ONE)))
        for r0, r1 in x5
    )
    x7 = tuple((NEG_ONE,) + cols + (x1,) for cols in x6)
    x8 = tuple(
        tuple(
            frozenset(
                I[i][j]
                for i in range(r0, r1 + ONE)
                for j in range(c0 + ONE, c1)
            )
            for c0, c1 in zip(cuts, cuts[ONE:])
            if c1 - c0 > ONE
        )
        for (r0, r1), cuts in zip(x5, x7)
    )
    x9 = tuple(
        tuple(next(iter(palette0)) for palette0 in row if len(palette0) == ONE)
        for row in x8
    )
    x10 = tuple(row for row in x9 if len(row) > ZERO)
    return x10
