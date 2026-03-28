from synth_rearc.core import *


TARGET_SETS_494EF9D7 = (
    frozenset({FOUR, SEVEN}),
    frozenset({ONE, EIGHT}),
)


def _compact_row_494ef9d7(I: Grid) -> Grid:
    x0 = difference(asindices(I), ofcolor(I, ZERO))
    x1 = remove(ZERO, palette(I))
    x2 = contained(x1, TARGET_SETS_494EF9D7)
    x3 = equality(size(x0), TWO)
    if not both(x2, x3):
        return I
    x4 = leftmost(x0)
    x5 = rightmost(x0)
    if equality(increment(x4), x5):
        return I
    x6 = astuple(ZERO, x5)
    x7 = astuple(ZERO, increment(x4))
    x8 = index(I, x6)
    x9 = fill(I, ZERO, initset(x6))
    x10 = fill(x9, x8, initset(x7))
    return x10


def verify_494ef9d7(I: Grid) -> Grid:
    x0 = height(I)
    x1 = vsplit(I, x0)
    x2 = apply(_compact_row_494ef9d7, x1)
    x3 = merge(x2)
    return x3
