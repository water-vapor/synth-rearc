from arc2.core import *


def _ray_137f0df0(
    I: Grid,
    start: IntegerTuple,
    direction: IntegerTuple,
) -> Indices:
    x0, x1 = direction
    x2, x3 = add(start, direction)
    x4 = set()
    while index(I, (x2, x3)) == ZERO:
        x4.add((x2, x3))
        x2 += x0
        x3 += x1
    return frozenset(x4)


def _blue_patch_137f0df0(
    I: Grid,
    reds: Indices,
) -> Indices:
    x0 = frozenset({})
    for x1 in reds:
        x2 = frozenset({})
        for x3 in (UP, DOWN, LEFT, RIGHT):
            x2 = combine(x2, _ray_137f0df0(I, x1, x3))
        x0 = combine(x0, x2)
    return x0


def verify_137f0df0(
    I: Grid,
) -> Grid:
    x0 = ofcolor(I, FIVE)
    x1 = delta(x0)
    x2 = fill(I, TWO, x1)
    x3 = _blue_patch_137f0df0(I, x1)
    x4 = frozenset(x5 for x5 in x3 if index(x2, x5) == ZERO)
    x5 = fill(x2, ONE, x4)
    return x5
