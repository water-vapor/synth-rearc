from arc2.core import *


def _move_patch_5034a0b5(
    patch: Indices,
    direction: IntegerTuple,
    interior: Indices,
) -> Indices:
    x0 = set()
    for x1 in patch:
        x2 = add(x1, direction)
        x3 = branch(contained(x2, interior), x2, x1)
        x0.add(x3)
    return frozenset(x0)


def verify_5034a0b5(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = index(I, ORIGIN)
    x3 = index(I, (ZERO, ONE))
    x4 = index(I, (ONE, ZERO))
    x5 = index(I, (ONE, subtract(x1, ONE)))
    x6 = index(I, (subtract(x0, ONE), ONE))
    x7 = interval(ONE, subtract(x0, ONE), ONE)
    x8 = interval(ONE, subtract(x1, ONE), ONE)
    x9 = product(x7, x8)
    x10 = intersection(ofcolor(I, x3), x9)
    x11 = intersection(ofcolor(I, x4), x9)
    x12 = intersection(ofcolor(I, x5), x9)
    x13 = intersection(ofcolor(I, x6), x9)
    x14 = I
    for x15 in (x10, x11, x12, x13):
        x14 = fill(x14, x2, x15)
    x15 = _move_patch_5034a0b5(x10, UP, x9)
    x16 = _move_patch_5034a0b5(x11, LEFT, x9)
    x17 = _move_patch_5034a0b5(x12, RIGHT, x9)
    x18 = _move_patch_5034a0b5(x13, DOWN, x9)
    x19 = fill(x14, x3, x15)
    x20 = fill(x19, x4, x16)
    x21 = fill(x20, x5, x17)
    x22 = fill(x21, x6, x18)
    return x22
