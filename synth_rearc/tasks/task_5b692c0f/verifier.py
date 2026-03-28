from synth_rearc.core import *


def _complete_object_5b692c0f(
    obj: Object,
) -> Object:
    x0 = sfilter(obj, matcher(first, FOUR))
    if len(x0) == ZERO:
        return obj
    x1 = tuple(i for _, (i, _) in x0)
    x2 = tuple(j for _, (_, j) in x0)
    x3 = mostcommon(x1)
    x4 = x1.count(x3)
    x5 = mostcommon(x2)
    x6 = x2.count(x5)
    if greater(x6, x4):
        x7 = frozenset((value, loc) for value, loc in x0 if loc[1] == x5)
        x8 = frozenset(cell for cell in obj if cell not in x7)
        x9 = frozenset(cell for cell in x8 if cell[1][1] < x5)
        x10 = frozenset(cell for cell in x8 if cell[1][1] > x5)
        x11 = branch(greater(size(x9), size(x10)), x9, x10)
        x12 = frozenset((value, (i, subtract(multiply(TWO, x5), j))) for value, (i, j) in x11)
        return combine(x7, combine(x11, x12))
    x7 = frozenset((value, loc) for value, loc in x0 if loc[0] == x3)
    x8 = frozenset(cell for cell in obj if cell not in x7)
    x9 = frozenset(cell for cell in x8 if cell[1][0] < x3)
    x10 = frozenset(cell for cell in x8 if cell[1][0] > x3)
    x11 = branch(greater(size(x9), size(x10)), x9, x10)
    x12 = frozenset((value, (subtract(multiply(TWO, x3), i), j)) for value, (i, j) in x11)
    return combine(x7, combine(x11, x12))


def verify_5b692c0f(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = canvas(mostcolor(I), shape(I))
    for x2 in x0:
        x3 = _complete_object_5b692c0f(x2)
        x1 = paint(x1, x3)
    return x1
