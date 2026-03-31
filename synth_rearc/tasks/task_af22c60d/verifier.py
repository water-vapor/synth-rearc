from synth_rearc.core import *


def _orbit_af22c60d(
    loc: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    i, j = loc
    x0 = {(i, j)}
    if i >= TWO:
        x0.add((31 - i, j))
    if j >= TWO:
        x0.add((i, 31 - j))
    if i >= TWO and j >= TWO:
        x0.add((31 - i, 31 - j))
    return tuple(sorted(x0))


def verify_af22c60d(
    I: Grid,
) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = [list(x3) for x3 in I]
    for x3 in range(x0):
        for x4 in range(x1):
            x5 = _orbit_af22c60d((x3, x4))
            x6 = tuple(index(I, x7) for x7 in x5)
            x7 = tuple(x8 for x8 in x6 if x8 != ZERO)
            if len(x7) == ZERO:
                continue
            x2[x3][x4] = x7[ZERO]
    return tuple(tuple(x3) for x3 in x2)
